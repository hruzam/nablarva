const {chromium}=require('playwright');const fs=require('fs');const cp=require('child_process');
(async()=>{
const setup=JSON.parse(fs.readFileSync('/tmp/phone-console-browser/live-check.json'));
const config=JSON.parse(fs.readFileSync(setup.config));const [username,password]=JSON.parse(fs.readFileSync(config.credential_file)).credential.split(':');
function tmux(...args){return cp.execFileSync('tmux',['-L',setup.socket,...args],{encoding:'utf8'}).trim()}
const panesBefore=tmux('list-panes','-s','-t','=browser-check','-F','#{pane_id}:#{pane_pid}');
const desktopBefore=tmux('display-message','-p','-t','=browser-check--left:','#{window_id}');
const browser=await chromium.launch({headless:true});
try{
const context=await browser.newContext({viewport:{width:360,height:800},httpCredentials:{username,password}});
const p=await context.newPage();p.setDefaultTimeout(15000);const errors=[];p.on('pageerror',e=>errors.push(e.message));
await p.goto(config.public_origin);await p.waitForFunction(()=>document.querySelector('#mode').textContent==='LIVE');
const state=await p.evaluate(async()=>await(await fetch('/api/state')).json());
const first=state.targets.find(t=>t.label.includes('/ first')),second=state.targets.find(t=>t.label.includes('/ second'));
if(!first||!second)throw Error('Missing fixture targets');
if(await p.locator('#fixture-create').isVisible()||await p.locator('#end').isVisible())throw Error('Live destructive/create controls visible');
async function interact(target,filename){
 await p.selectOption('#target',target.id);await p.click('#attach');
 await p.waitForFunction(()=>document.querySelector('#connection').textContent.startsWith('connected'));
 const file=setup.root+'/'+Date.now()+'-'+filename;
 await p.fill('#draft',`printf %s "$TMUX_PANE" > '${file}'`);
 await p.click('#paste');await p.waitForTimeout(100);
 if(fs.existsSync(file))throw Error('Paste submitted without Enter');
 await p.click('#enter');
 const deadline=Date.now()+10000;while(!fs.existsSync(file)&&Date.now()<deadline)await p.waitForTimeout(50);
 if(fs.readFileSync(file,'utf8')!==target.paneId)throw Error('Input reached wrong pane');
 const horizontal=await p.evaluate(()=>({viewport:innerWidth,document:document.documentElement.scrollWidth}));
 if(horizontal.document>horizontal.viewport)throw Error('Phone page horizontal overflow '+JSON.stringify(horizontal));
 return horizontal;
}
const geometry=await interact(second,'second.txt');
await p.selectOption('#target',first.id);
if(await p.locator('#target').inputValue()!==second.id)throw Error('Target changed while still attached');
await p.click('#detach');await p.waitForFunction(()=>document.querySelector('#connection').textContent.startsWith('detached'));
p.on('dialog',d=>d.accept());
await interact(first,'first.txt');await p.click('#detach');
await p.waitForFunction(()=>document.querySelector('#connection').textContent.startsWith('detached'));
if(tmux('display-message','-p','-t','=browser-check--left:','#{window_id}')!==desktopBefore)throw Error('Desktop selected window changed');
if(tmux('list-panes','-s','-t','=browser-check','-F','#{pane_id}:#{pane_pid}')!==panesBefore)throw Error('Owner pane lifetime changed');
if(errors.length)throw Error(errors.join('\n'));
const result={at:new Date().toISOString(),isolatedOwnerSocket:setup.socket,twoSelectedPanesReceiveExactInput:true,pasteDoesNotSubmit:true,changingTargetRequiresDetach:true,desktopSelectionUnchanged:true,panePidsPreserved:true,liveCreateEndHidden:true,geometry,pageErrors:errors};
fs.writeFileSync('/home/hruzam/unikuklatrix/nablarva/.dev/session/phone-console-01-browser/raw/live-adapter/browser-isolated.2026-10-30.json',JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result));
}finally{await browser.close()}
})().catch(e=>{console.error(e);process.exit(1)});
