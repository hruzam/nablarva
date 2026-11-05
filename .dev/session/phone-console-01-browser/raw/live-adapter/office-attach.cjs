const {chromium}=require('playwright');const fs=require('fs');const cp=require('child_process');
(async()=>{
const [username,password]=JSON.parse(fs.readFileSync('/tmp/pc-trial-j6j1id09/state.json')).credential.split(':');
const baseline=JSON.parse(fs.readFileSync('/home/hruzam/unikuklatrix/nablarva/.dev/session/phone-console-01-browser/raw/live-adapter/office-before.json'));
function tmux(...args){return cp.execFileSync('tmux',['-L','default',...args],{encoding:'utf8'}).trim()}
const browser=await chromium.launch({headless:true});
try{
 const p=await browser.newPage({viewport:{width:360,height:800},httpCredentials:{username,password}});p.setDefaultTimeout(30000);
 let outputBytes=0,inputFrames=0;const terminalReplies=[];const errors=[];p.on('pageerror',e=>errors.push(e.message));
 p.on('websocket',ws=>{ws.on('framereceived',e=>{const b=Buffer.from(e.payload);if(b[0]===48)outputBytes+=b.length-1});ws.on('framesent',e=>{const b=Buffer.from(e.payload);if(b[0]===48){inputFrames++;terminalReplies.push(b.subarray(1).toString('hex'))}})});
 await p.goto('http://127.0.0.1:18790');await p.waitForFunction(()=>document.querySelector('#mode').textContent==='LIVE');
 const state=await p.evaluate(async()=>await(await fetch('/api/state')).json());
 const target=state.targets.find(t=>t.bed===baseline.base&&t.program==='codex'&&t.singlePane&&!t.dead);
 if(!target)throw Error('Expected existing Codex target absent');
 await p.selectOption('#target',target.id);await p.click('#attach');
 await p.waitForFunction(()=>document.querySelector('#connection').textContent.startsWith('connected'));
 const deadline=Date.now()+10000;while(outputBytes===0&&Date.now()<deadline)await p.waitForTimeout(100);
 if(!outputBytes)throw Error('No real terminal output received');
 const attachedSize=tmux('display-message','-p','-t','=phone-console-01-browser:','#{window_width}x#{window_height}');
 const geometry=await p.evaluate(()=>({viewport:innerWidth,document:document.documentElement.scrollWidth}));
 if(geometry.document>geometry.viewport)throw Error('Mobile horizontal overflow '+JSON.stringify(geometry));
 await p.click('#detach');await p.waitForFunction(()=>document.querySelector('#connection').textContent.startsWith('detached')&&!document.querySelector('#detach').disabled);
 const after={panes:tmux('list-panes','-s','-t','=phone-console-01-browser','-F','#{window_id}:#{pane_id}:#{pane_pid}'),desktopWindow:tmux('display-message','-p','-t','=phone-console-01-browser--left:','#{window_id}'),windowSize:tmux('display-message','-p','-t','=phone-console-01-browser:','#{window_width}x#{window_height}')};
 if(after.panes!==baseline.panes||after.desktopWindow!==baseline.desktopWindow)throw Error('Office preservation/input check failed');
 if(errors.length)throw Error(errors.join('\n'));
 const result={at:new Date().toISOString(),mode:state.mode,listedTargets:state.targets.length,target:{bed:target.bed,windowId:target.windowId,paneId:target.paneId,program:target.program},realOutputBytes:outputBytes,inputFrames,terminalReplies,deliberateKeystrokes:0,desktopSelectionUnchanged:true,panePidsPreserved:true,geometry,dimensions:{before:baseline.windowSize,attached:attachedSize,after:after.windowSize},pageErrors:errors};
 fs.writeFileSync('/home/hruzam/unikuklatrix/nablarva/.dev/session/phone-console-01-browser/raw/live-adapter/office-attach.2026-10-30.json',JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result));
}finally{await browser.close()}
})().catch(e=>{console.error(e);process.exit(1)});
