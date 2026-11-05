const {chromium}=require('playwright');const fs=require('fs');
(async()=>{
 const setup=JSON.parse(fs.readFileSync('/tmp/phone-console-browser/history-check.json'));
 const config=JSON.parse(fs.readFileSync(setup.config));const [username,password]=JSON.parse(fs.readFileSync(config.credential_file)).credential.split(':');
 const browser=await chromium.launch({headless:true});
 try{
 const p=await browser.newPage({viewport:{width:360,height:800},httpCredentials:{username,password}});p.setDefaultTimeout(15000);
 const errors=[];let inputFrames=0;const actions=[];
 p.on('pageerror',e=>errors.push(e.message));p.on('websocket',ws=>ws.on('framesent',e=>{if(Buffer.from(e.payload)[0]===48)inputFrames++}));
 p.on('request',r=>{if(r.url().endsWith('/history'))actions.push(JSON.parse(r.postData()).action)});
 await p.goto(config.public_origin);await p.waitForFunction(()=>document.querySelector('#mode').textContent==='LIVE');
 const state=await p.evaluate(async()=>await(await fetch('/api/state')).json());await p.selectOption('#target',state.targets[0].id);await p.click('#attach');
 await p.waitForFunction(()=>document.querySelector('#connection').textContent.startsWith('connected'));
 async function lastLine(){return await p.locator('.xterm-rows').evaluate(el=>Math.max(0,...[...el.textContent.matchAll(/HISTORY-LINE-(\d+)/g)].map(m=>Number(m[1]))))}
 async function waitLine(predicate){const deadline=Date.now()+5000;while(Date.now()<deadline){const n=await lastLine();if(predicate(n))return n;await p.waitForTimeout(50)}throw Error('History display did not move: '+await lastLine())}
 const live=await waitLine(n=>n===300);const inputsBefore=inputFrames;
 await p.click('#history-older');const older=await waitLine(n=>n>0&&n<live);
 await p.click('#history-older');const oldest=await waitLine(n=>n>0&&n<older);
 await p.click('#history-newer');const newer=await waitLine(n=>n>oldest);
 await p.click('#history-live');const returned=await waitLine(n=>n===300);
 if(inputFrames!==inputsBefore)throw Error('History buttons sent PTY input');
 const shortHeight=await p.locator('#terminal').evaluate(e=>e.clientHeight);
 await p.click('#expand-terminal');await p.waitForFunction(()=>document.querySelector('#terminal').clientHeight>500);
 const expandedHeight=await p.locator('#terminal').evaluate(e=>e.clientHeight);
 const geometry=await p.evaluate(()=>({width:innerWidth,scrollWidth:document.documentElement.scrollWidth}));
 if(geometry.scrollWidth>geometry.width)throw Error('Expanded view overflows width');
 await p.click('#expand-terminal');const shrinkHeight=await p.locator('#terminal').evaluate(e=>e.clientHeight);
 if(shrinkHeight!==shortHeight)throw Error('Shrink failed');
 // A pending Older request must never spill its next action into another attachment.
 let release,blocked;const gate=new Promise(r=>release=r);const entered=new Promise(r=>blocked=r);
 await p.route('**/api/views/*/history',async route=>{if(JSON.parse(route.request().postData()).action==='enter'){blocked();await gate}await route.continue()});
 const actionIndex=actions.length;
 await p.click('#history-older');await entered;await p.click('#detach');
 await p.waitForFunction(()=>document.querySelector('#connection').textContent.startsWith('detached')&&!document.querySelector('#detach').disabled);
 release();await p.waitForFunction(()=>!document.querySelector('#history-older').disabled);
 if(actions.slice(actionIndex).includes('pageUp'))throw Error('Detached history request continued scrolling');
 if(errors.length)throw Error(errors.join('\n'));
 const result={at:new Date().toISOString(),lines:{live,older,oldest,newer,returned},noHistoryPtyInput:true,detachCancelsPendingScroll:true,heights:{shortHeight,expandedHeight,shrinkHeight},geometry,actions,pageErrors:errors};
 fs.writeFileSync('/home/hruzam/unikuklatrix/nablarva/.dev/session/phone-console-01-browser/raw/history-controls/browser.json',JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result));
 }finally{await browser.close()}
})().catch(e=>{console.error(e);process.exit(1)});
