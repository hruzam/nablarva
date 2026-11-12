#!/usr/bin/env python3
"""Run synthetic read/selection checks against an explicit disposable profile."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import subprocess
import sys
import time
from urllib.request import Request, urlopen
import uuid

ROOT=Path(__file__).resolve().parents[1]

def main():
 p=argparse.ArgumentParser();p.add_argument('--trial-root',type=Path,required=True);p.add_argument('--instance',required=True);p.add_argument('--window',required=True,type=int);p.add_argument('--port',required=True,type=int);args=p.parse_args()
 root=args.trial_root.resolve()
 if not str(root).startswith('/tmp/nablarva-observer-'):raise SystemExit('disposable trial root required')
 token=(root/'token').read_text()
 base=[sys.executable,'-I','-S','-B',str(ROOT/'observer.py'),'--runtime',str(root/'runtime')]
 def call(*parts,ok=True):
  r=subprocess.run(base+list(parts),capture_output=True,text=True,timeout=7)
  if (r.returncode==0)!=ok: raise RuntimeError('unexpected CLI exit: '+r.stderr)
  return json.loads(r.stdout if ok else r.stderr)
 def post(route,body):
  q=Request('http://127.0.0.1:%d/%s'%(args.port,route),headers={'Authorization':'Bearer '+token,'Content-Type':'application/json'},data=json.dumps(body).encode())
  with urlopen(q,timeout=5) as response:result=json.loads(response.read())
  if not result.get('ok'):raise RuntimeError(str(result))
  return result
 name='checks-'+uuid.uuid4().hex+'.md'; path=root/name
 text='Unicode α😀\nsecond line\n'; path.write_text(text)
 post('open_file',{'path':str(path)})
 tabs=call('tabs','--instance',args.instance,'--window',str(args.window))['views']
 matches=[(i,v) for i,v in enumerate(tabs) if v['path']==str(path)]
 if len(matches)!=1:raise RuntimeError('test view ambiguous')
 index,view=matches[0];vid=str(view['view']); common=['--instance',args.instance,'--window',str(args.window),'--view',vid]
 before=call('state',*common); part=call('read',*common,'--lines','1:1'); truncated=call('read',*common,'--max-chars','3')
 assert part['text']=='Unicode α😀\n' and part['returned_through_line']==1
 assert truncated['truncated'] is True
 post('send_to_view',{'index':index,'text':'UNSAVED\n'})
 revised=call('read',*common); conflict=call('read',*common,'--expected-revision',str(before['revision']),ok=False)
 assert revised['dirty'] and 'UNSAVED' in revised['text'] and path.read_text()==text
 assert conflict['error']['code']=='revision_conflict'
 with ThreadPoolExecutor(max_workers=8) as pool:
  captures=list(pool.map(lambda _:call('state',*common),range(20)))
 assert len({v['request_id'] for v in captures})==20 and all(v['view']==int(vid) for v in captures)
 prior=call('windows','--instance',args.instance);state1=call('state',*common);call('read',*common);state2=call('state',*common);after=call('windows','--instance',args.instance)
 assert prior['active_window']==after['active_window'] and state1['selections']==state2['selections'] and state1['viewport_position']==state2['viewport_position']
 invalid=call('read','--instance',args.instance,'--window',str(args.window),'--view','99999999',ok=False)
 assert invalid['error']['code']=='invalid_view'
 response_bytes=len(json.dumps(revised,ensure_ascii=False).encode())
 print(json.dumps({'view':int(vid),'unicode_range':'pass','explicit_truncation':'pass','unsaved_vs_disk':'pass','revision_conflict':'pass','concurrent_requests':len(captures),'focus_selection_scroll':'unchanged','invalid_view':'pass','sample_response_bytes':response_bytes},indent=2))

if __name__=='__main__':main()
