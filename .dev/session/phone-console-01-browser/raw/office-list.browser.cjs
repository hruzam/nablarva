const {chromium}=require('playwright');
const fs=require('fs');
(async()=>{
 const [username,password]=JSON.parse(fs.readFileSync('/tmp/pc-trial-j6j1id09/state.json')).credential.split(':');
 const browser=await chromium.launch({headless:true});
 try {
  const context=await browser.newContext({viewport:{width:360,height:800},httpCredentials:{username,password}});
  const page=await context.newPage();const errors=[];page.on('pageerror',e=>errors.push(e.message));
  await page.goto('http://127.0.0.1:18790');
  await page.waitForFunction(()=>document.querySelector('#target').options.length>1);
  const before=await page.locator('#target').inputValue();
  await page.getByRole('button',{name:'List office workbenches',exact:true}).click();
  await page.waitForFunction(()=>document.querySelector('#office-output').textContent.includes('phone-console-01-browser'));
  const output=await page.locator('#office-output').textContent();
  const widths=[];
  for(const width of [360,412]){
   await page.setViewportSize({width,height:800});
   widths.push(await page.locator('#office-output').evaluate(el=>({viewport:innerWidth,client:el.clientWidth,scroll:el.scrollWidth,wrapped:el.scrollWidth<=el.clientWidth,scrollable:el.scrollHeight>el.clientHeight})));
  }
  if(widths.some(x=>!x.wrapped||!x.scrollable))throw Error('List did not wrap/scroll at phone widths');
  if(await page.locator('#target').inputValue()!==before)throw Error('Listing changed selected fixture');
  await page.route('**/api/office-workbenches',route=>route.fulfill({status:504,contentType:'application/json',body:JSON.stringify({error:{code:'office_timeout',message:'Office workbench listing timed out. Try again.'}})}));
  await page.getByRole('button',{name:'List office workbenches',exact:true}).click();
  await page.waitForFunction(()=>document.querySelector('#office-output').textContent.includes('Could not load'));
  if(await page.locator('#office-list').isDisabled())throw Error('Retry button left disabled');
  await page.unroute('**/api/office-workbenches');
  await page.getByRole('button',{name:'List office workbenches',exact:true}).click();
  await page.waitForFunction(()=>document.querySelector('#office-output').textContent.includes('phone-console-01-browser'));
  if(errors.length)throw Error(errors.join('\n'));
  const result={at:new Date().toISOString(),liveReadOnlyListing:true,lineCount:output.split('\n').length,widths,fixtureSelectionUnchanged:true,timeoutRetryPassed:true,pageErrors:errors};
  fs.writeFileSync('/home/hruzam/unikuklatrix/nablarva/.dev/session/phone-console-01-browser/raw/office-list.browser.2026-10-30.json',JSON.stringify(result,null,2)+'\n');
  console.log(JSON.stringify(result));
 }finally{await browser.close()}
})().catch(e=>{console.error(e);process.exit(1)});
