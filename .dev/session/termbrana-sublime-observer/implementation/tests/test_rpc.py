import importlib.util
import json
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from concurrent.futures import ThreadPoolExecutor

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('observer_client_test',ROOT/'observer.py')
client=importlib.util.module_from_spec(spec);spec.loader.exec_module(client)

class FakeServer:
 def __init__(self,root,reply):
  self.root=Path(root)/'sublime-observer';self.root.mkdir(mode=0o700)
  self.instance='a'*32;self.path=self.root/(self.instance+'.sock');self.reply=reply
  self.sock=socket.socket(socket.AF_UNIX,socket.SOCK_STREAM);self.sock.bind(str(self.path));self.sock.listen(32);self.sock.settimeout(.1)
  self.stop=threading.Event();self.threads=[]
  (self.root/(self.instance+'.json')).write_text(json.dumps({'instance':self.instance,'socket':str(self.path),'pid':123,'version':1}))
  self.thread=threading.Thread(target=self.serve,daemon=True);self.thread.start()
 def serve(self):
  while not self.stop.is_set():
   try:c,_=self.sock.accept()
   except socket.timeout:continue
   except OSError:break
   t=threading.Thread(target=self.handle,args=(c,),daemon=True);self.threads.append(t);t.start()
 def handle(self,c):
  with c:
   try:
    data=bytearray()
    while b'\n' not in data:
     chunk=c.recv(4096)
     if not chunk:return
     data.extend(chunk)
    q=json.loads(bytes(data).split(b'\n')[0]);r=self.reply(q);c.sendall((json.dumps(r)+'\n').encode())
   except OSError:pass
 def close(self):
  self.stop.set();self.sock.close();self.thread.join(1)
  for t in self.threads:t.join(1)

class RpcTests(unittest.TestCase):
 def setUp(self):self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
 def server(self,reply):
  s=FakeServer(self.temp.name,reply);self.addCleanup(s.close);return s
 def test_concurrent_responses_keep_request_identity(self):
  s=self.server(lambda q:{'ok':True,'request_id':q['request_id'],'instance':'a'*32,'view':q['view']})
  info=client.instances(s.root)[0]
  with ThreadPoolExecutor(max_workers=8) as pool:
   results=list(pool.map(lambda n:client.request(info,{'operation':'state','view':n},2),range(20)))
  self.assertEqual([x['view'] for x in results],list(range(20)))
  self.assertEqual(len({x['request_id'] for x in results}),20)
 def test_response_request_id_mismatch_fails(self):
  s=self.server(lambda q:{'ok':True,'request_id':'other'})
  with self.assertRaisesRegex(ValueError,'request ID mismatch'):client.request(client.instances(s.root)[0],{'operation':'windows'},2)
 def test_slow_response_cannot_extend_request_deadline(self):
  path=str(Path(self.temp.name)/'slow.sock')
  server=socket.socket(socket.AF_UNIX,socket.SOCK_STREAM);server.bind(path);server.listen(1)
  self.addCleanup(server.close)
  def drip():
   connection,_=server.accept()
   with connection:
    connection.recv(4096)
    try:
     for _ in range(30):connection.sendall(b' ');time.sleep(.02)
    except OSError:pass
  thread=threading.Thread(target=drip,daemon=True);thread.start()
  start=time.monotonic()
  with self.assertRaises(TimeoutError):client.request({'socket':path,'instance':'a'*32},{'operation':'windows'},.08)
  self.assertLess(time.monotonic()-start,.25)
  thread.join(1)
 def test_wait_rejects_stale_run_markers(self):
  s=self.server(lambda q:{'ok':True,'request_id':q['request_id'],'instance':'a'*32,'text':'RUN:old:BEGIN\nRUN:old:END','truncated':False})
  run='b'*32;(s.root/('run-'+run+'.token')).write_text(json.dumps({'instance':s.instance,'window':1,'issued_at':time.time()}))
  command=[sys.executable,'-I','-S','-B',str(ROOT/'observer.py'),'--runtime',self.temp.name,'--timeout','.3','wait','--instance',s.instance,'--window','1','--view','2','--run-id',run]
  r=subprocess.run(command,text=True,capture_output=True,timeout=3)
  self.assertNotEqual(r.returncode,0);self.assertIn('deadline expired',json.loads(r.stderr)['error']['message'])
 def test_wait_rejects_truncated_content_even_if_markers_present(self):
  run='b'*32
  s=self.server(lambda q:{'ok':True,'request_id':q['request_id'],'instance':'a'*32,'text':'RUN:'+run+':BEGIN\nRUN:'+run+':END','truncated':True})
  (s.root/('run-'+run+'.token')).write_text(json.dumps({'instance':s.instance,'window':1,'issued_at':time.time()}))
  command=[sys.executable,'-I','-S','-B',str(ROOT/'observer.py'),'--runtime',self.temp.name,'--timeout','1','wait','--instance',s.instance,'--window','1','--view','2','--run-id',run]
  r=subprocess.run(command,text=True,capture_output=True,timeout=3)
  self.assertNotEqual(r.returncode,0);self.assertIn('truncated',json.loads(r.stderr)['error']['message'])
 def test_abandoned_socket_is_marked_unreachable(self):
  s=self.server(lambda q:{'ok':True,'request_id':q['request_id']});root=s.root;s.close()
  self.assertFalse(client.instances(root)[0]['reachable'])
 def test_run_token_is_bound_to_window_and_consumed_once(self):
  current={'run':None}
  def reply(q):
   base={'ok':True,'request_id':q['request_id'],'instance':'a'*32}
   if q['operation']=='windows':base['windows']=[{'id':1}]
   else:base.update({'text':'RUN:'+current['run']+':BEGIN\nRUN:'+current['run']+':END','truncated':False})
   return base
  s=self.server(reply);base=[sys.executable,'-I','-S','-B',str(ROOT/'observer.py'),'--runtime',self.temp.name]
  issued=subprocess.run(base+['new-run','--instance',s.instance,'--window','1'],text=True,capture_output=True,check=True)
  current['run']=json.loads(issued.stdout)['run_id']
  wrong=subprocess.run(base+['wait','--instance',s.instance,'--window','2','--view','3','--run-id',current['run']],text=True,capture_output=True)
  self.assertNotEqual(wrong.returncode,0)
  command=base+['wait','--instance',s.instance,'--window','1','--view','3','--run-id',current['run']]
  self.assertEqual(subprocess.run(command,text=True,capture_output=True).returncode,0)
  self.assertNotEqual(subprocess.run(command,text=True,capture_output=True).returncode,0)

if __name__=='__main__':unittest.main()
