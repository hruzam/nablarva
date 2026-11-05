import './styles.css';
import {createTerminal} from './terminal.js';
import {draftStore, trayStore, requestPersistence} from './storage.js';
import {api} from './api.js';

const $ = id => document.getElementById(id);
const errorBox = $('error');
const showError = error => { errorBox.textContent = error?.message || String(error); errorBox.hidden = false; };
const run = fn => async () => { errorBox.hidden = true; try { await fn(); } catch (error) { showError(error); } };
let state, view, vaultItem, files = [], saving = Promise.resolve(), draftVersion = 0, uploading = false, lifecycleBusy = false;
const terminal = createTerminal({container: $('terminal'), onState: event => {
  $('connection').textContent = event.state + (event.targetId ? ` · ${view?.target?.label || event.targetId}` : '') + (event.uncertainInput ? ' · input may not have arrived' : '');
  if (event.message) showError(event.message);
}});
const fit = () => { try { terminal.fit(); } catch (error) { showError(error); } };
new ResizeObserver(fit).observe($('terminal'));
window.visualViewport?.addEventListener('resize', fit);
window.addEventListener('resize', fit);
function selectedTarget() { return state?.targets.find(t => t.id === $('target').value); }
function targetLabel(target) {
  return `${target.label || target.bed} · window ${target.tab ?? target.windowId ?? '?'} / pane ${target.paneId ?? '?'} / ${target.program ?? target.cmd ?? 'unknown program'}`;
}
function blockedTarget(target) {
  if (!target) return 'Choose a workbench, then tap Attach and Keyboard to interact with its terminal.';
  if (target.dead) return 'This pane has ended and cannot be attached.';
  if (target.singlePane === false || (state.mode === 'live' && target.singlePane !== true)) return 'Only single-pane windows can be attached.';
  return '';
}
async function refresh() {
  const previous = $('target').value;
  const next = await api('/api/state');
  if (!['fixture', 'live'].includes(next.mode)) throw new Error('Unsupported workbench mode.');
  if (view && !next.targets.some(t => t.id === view.target.id && t.generation === view.target.generation && !t.dead && t.singlePane !== false && (next.mode !== 'live' || t.singlePane === true))) await detach();
  state = next;
  $('mode').textContent = state.mode.toUpperCase();
  document.title = `Session console · ${state.mode}`;
  $('mode-notice').textContent = (state.mode === 'fixture' ? 'Synthetic workbenches only. ' : 'Live office workbenches. ') + 'Resizing the terminal may also resize the shared workstation view.';
  $('fixture-create').hidden = state.capabilities?.createFixture !== true;
  $('end').hidden = state.capabilities?.endFixture !== true;
  $('target').replaceChildren();
  const groups = new Map();
  for (const target of state.targets) {
    const bed = target.bed || 'Workbenches';
    if (!groups.has(bed)) { const group = document.createElement('optgroup'); group.label = bed; groups.set(bed, group); $('target').append(group); }
    const option = document.createElement('option'); option.value = target.id;
    option.textContent = targetLabel(target) + (target.dead ? ' · ended' : target.singlePane === false ? ' · multiple panes' : target.busy ? ' · running' : '');
    groups.get(bed).append(option);
  }
  if (previous && state.targets.some(t => t.id === previous)) $('target').value = previous;
  else { const missing = document.createElement('option'); missing.value = ''; missing.textContent = previous ? 'Previous workbench unavailable — choose another' : 'Choose a workbench'; $('target').prepend(missing); $('target').value = ''; }
  updateTarget();
}
function updateTarget() {
  const target = selectedTarget(), reason = blockedTarget(target);
  $('attach').disabled = lifecycleBusy || Boolean(reason);
  $('end').disabled = lifecycleBusy || !target || target.busy || target.canEnd !== true || state?.capabilities?.endFixture !== true;
  $('target-detail').textContent = reason || `Selected: ${targetLabel(target)}. ${view ? `Attached: ${targetLabel(view.target)}.` : 'Not attached. Tap Attach, then Keyboard.'}`;
}
async function lifecycle(fn) {
  if (lifecycleBusy) return;
  lifecycleBusy = true;
  for (const id of ['target', 'refresh', 'detach', 'create', 'fixture-name']) $(id).disabled = true;
  updateTarget();
  try { return await fn(); } finally {
    lifecycleBusy = false;
    for (const id of ['target', 'refresh', 'detach', 'create', 'fixture-name']) $(id).disabled = false;
    updateTarget();
  }
}
async function detach() {
  try { await terminal.detach(); } finally { view = undefined; }
}
$('refresh').onclick = run(() => lifecycle(refresh));
$('office-list').onclick = run(async () => {
  const button = $('office-list'), output = $('office-output');
  button.disabled = true;
  $('office-results').hidden = false;
  output.textContent = 'Loading office workbenches…';
  try {
    const result = await api('/api/office-workbenches');
    output.textContent = result.output || 'No office workbenches found.';
  } catch (error) {
    output.textContent = 'Could not load the list. Tap List office workbenches to retry.';
    throw error;
  } finally { button.disabled = false; }
});
$('target').onchange = updateTarget;
$('attach').onclick = run(() => lifecycle(async () => {
  const target = selectedTarget(); const reason = blockedTarget(target); if (reason) throw new Error(reason);
  if (view) await detach();
  view = await api('/api/views', {method:'POST', body:{targetId:target.id, generation:target.generation}});
  try { await terminal.attach(view); fit(); } catch (error) { await detach().catch(showError); throw error; }
}));
$('detach').onclick = run(() => lifecycle(detach));
$('create').onclick = run(() => lifecycle(async () => { const name = $('fixture-name').value.trim(); if (!name) throw new Error('Enter a workbench name.'); await api('/api/fixtures', {method:'POST',body:{name}}); $('fixture-name').value = ''; await refresh(); }));
$('end').onclick = run(() => lifecycle(async () => { const target = selectedTarget(); if (!target || target.busy || target.canEnd !== true) throw new Error('Choose an idle fixture that can be ended.'); if (!confirm(`End idle fixture “${target.label}”? This closes its workbench.`)) return; await api(`/api/fixtures/${encodeURIComponent(target.id)}`, {method:'DELETE',body:{generation:target.generation,confirm:true}}); if (view?.target?.id === target.id) await detach(); await refresh(); }));
$('focus').onclick = run(() => terminal.focus());
$('expand-terminal').onclick = () => {
  const section = $('terminal').closest('section');
  const expanded = section.classList.toggle('expanded');
  $('expand-terminal').textContent = expanded ? 'Shrink' : 'Expand';
  $('expand-terminal').setAttribute('aria-pressed', String(expanded));
  requestAnimationFrame(() => { fit(); section.scrollIntoView({block:'start', behavior:'smooth'}); });
};
let historyBusy = false;
for (const [id, action] of [['history-older','pageUp'], ['history-newer','pageDown'], ['history-live','leave']]) {
  $(id).onclick = run(async () => {
    checkAttachedTarget();
    if (historyBusy) return;
    historyBusy = true;
    const buttons = ['history-older','history-newer','history-live'].map($);
    buttons.forEach(button => { button.disabled = true; });
    try {
      await terminal.history(action);
      $('history-status').textContent = action === 'leave' ? 'Live terminal. Older opens earlier output.' : 'Browsing earlier output. Back to live returns to the current screen.';
    } finally {
      historyBusy = false;
      buttons.forEach(button => { button.disabled = false; });
    }
  });
}
const primary = [['Esc','Escape'],['Tab','Tab'],['↑','ArrowUp'],['↓','ArrowDown'],['Enter','Enter'],['Ctrl-C','CtrlC']];
const more = [['←','ArrowLeft'],['→','ArrowRight'],['Shift-Tab','ShiftTab'],['Page up','PageUp'],['Page down','PageDown'],['Home','Home'],['End','End'],['Backspace','Backspace'],['Delete','Delete'],['Ctrl-D','CtrlD'],['Ctrl-Z','CtrlZ']];
function keys(parent, list) { for (const [label, key] of list) { const button = document.createElement('button'); button.textContent = label; button.onclick = run(async () => { checkAttachedTarget(); if (key === 'CtrlD' && !confirm('Ctrl-D may end the shell. Send it?')) return; await terminal.key(key); }); parent.append(button); } }
keys($('primary-keys'), primary); keys($('more-keys'), more);
function saveDraft() {
  const text = $('draft').value, version = ++draftVersion;
  $('draft-status').textContent = 'Saving…';
  saving = saving.catch(() => {}).then(() => draftStore.save('composer', text)).then(() => { if (version === draftVersion) $('draft-status').textContent = 'Saved on this browser'; }, error => { $('draft-status').textContent = 'Save failed'; showError(error); throw error; });
  return saving;
}
let timer;
$('draft').addEventListener('input', () => { draftVersion++; clearTimeout(timer); $('draft-status').textContent = 'Unsaved'; timer = setTimeout(() => saveDraft().catch(() => {}), 400); });
$('save-draft').onclick = run(() => { clearTimeout(timer); return saveDraft(); });
$('clear-draft').onclick = run(async () => { if (!confirm('Clear this draft?')) return; $('draft').value = ''; clearTimeout(timer); await saveDraft(); });
function checkAttachedTarget() { if (lifecycleBusy) throw new Error('Wait for the workbench operation to finish.'); if (!view || view.target?.id !== $('target').value) throw new Error('Attach the selected workbench before sending.'); }
$('paste').onclick = run(() => { checkAttachedTarget(); return terminal.paste($('draft').value); });
$('enter').onclick = run(() => { checkAttachedTarget(); return terminal.key('Enter'); });
let trayTimer, trayRenderVersion = 0;
async function renderTray() {
  const version = ++trayRenderVersion;
  clearTimeout(trayTimer);
  const items = await trayStore.list();
  if (version !== trayRenderVersion) return;
  $('tray').replaceChildren();
  for (const item of items) {
    const div = document.createElement('div'); div.className = 'item';
    const p = document.createElement('p'); p.textContent = item.text;
    const expiry = document.createElement('span'); expiry.className = 'hint'; expiry.textContent = `Expires ${new Date(item.expiresAt).toLocaleTimeString()}`;
    const load = document.createElement('button'); load.textContent = 'Copy to draft';
    load.onclick = run(async () => {
      const current = (await trayStore.list()).find(entry => entry.id === item.id && entry.expiresAt > Date.now());
      if (!current) { await renderTray(); throw new Error('This tray item has expired or was removed.'); }
      $('draft').value = current.text; await saveDraft();
    });
    const remove = document.createElement('button'); remove.textContent = 'Remove'; remove.onclick = run(async () => { await trayStore.remove(item.id); await renderTray(); });
    div.append(p, expiry, document.createElement('br'), load, remove); $('tray').append(div);
  }
  if (items.length) {
    const nextExpiry = Math.min(...items.map(item => item.expiresAt));
    trayTimer = setTimeout(() => renderTray().catch(showError), Math.max(100, nextExpiry - Date.now() + 50));
  }
}
document.addEventListener('visibilitychange', () => { if (!document.hidden) renderTray().catch(showError); });
window.addEventListener('focus', () => renderTray().catch(showError));
$('tray-add').onclick = run(async () => { if (!$('draft').value) throw new Error('The draft is empty.'); await trayStore.add($('draft').value); await renderTray(); });
$('tray-clear').onclick = run(async () => { if (!confirm('Clear all tray items?')) return; await trayStore.clear(); await renderTray(); });
async function refreshVault() {
  const selected = $('vault-list').value; const result = await api('/api/vault'); $('vault-list').replaceChildren();
  for (const item of result.items.filter(i => i.kind === 'prompt' || i.kind === 'shortcut')) { const option = document.createElement('option'); option.value = item.id; option.textContent = `${item.name} · ${item.kind} · rev ${item.revision}`; $('vault-list').append(option); }
  if ([...$('vault-list').options].some(o => o.value === selected)) $('vault-list').value = selected;
  $('saved-files').replaceChildren();
  for (const item of result.items.filter(i => i.kind === 'file')) {
    const div = document.createElement('div'); div.className = 'item';
    const name = document.createElement('strong'); name.textContent = item.name;
    const info = document.createElement('p'); info.textContent = `${item.size} bytes · revision ${item.revision}\nSHA-256: ${item.sha256}\nWorkstation: ${item.path || 'Unavailable'}`;
    const link = document.createElement('a'); link.href = item.downloadUrl || `/api/files/${encodeURIComponent(item.id)}`; link.textContent = 'Download saved file';
    div.append(name, info, link); $('saved-files').append(div);
  }

}
$('vault-refresh').onclick = run(refreshVault);
$('files-refresh').onclick = run(refreshVault);
$('vault-load').onclick = run(async () => { if (!$('vault-list').value) throw new Error('Choose a saved item.'); vaultItem = await api(`/api/vault/${encodeURIComponent($('vault-list').value)}`); $('vault-kind').value = vaultItem.kind; $('vault-kind').disabled = true; $('vault-name').value = vaultItem.name; $('vault-text').value = vaultItem.text; $('vault-status').textContent = `Loaded revision ${vaultItem.revision}.`; });
$('vault-new').onclick = () => { vaultItem = undefined; $('vault-kind').disabled = false; $('vault-name').value = ''; $('vault-text').value = ''; $('vault-status').textContent = 'New item'; };
$('vault-save').onclick = run(async () => { const name = $('vault-name').value.trim(); if (!name) throw new Error('Enter a name for the saved item.'); const id = vaultItem?.id || crypto.randomUUID(); try { vaultItem = await api(`/api/vault/${id}`, {method:'PUT', body:{kind:$('vault-kind').value,name,text:$('vault-text').value,expectedRevision:vaultItem?.revision ?? 0}}); $('vault-kind').disabled = true; $('vault-status').textContent = `Saved revision ${vaultItem.revision}.`; await refreshVault(); $('vault-list').value = id; } catch (error) { if (error.status === 409) { const rev = error.detail?.currentRevision ?? error.detail?.error?.currentRevision ?? 'unknown'; $('vault-status').textContent = `Conflict: saved revision is ${rev}. Your text is unchanged; copy it before loading the current item.`; } throw error; } });
$('vault-draft').onclick = run(async () => { $('draft').value = $('vault-text').value; await saveDraft(); });
let reviewingOriginals = false;
function renderFiles() {
  $('file-list').replaceChildren();
  for (const entry of files) {
    const div = document.createElement('div'); div.className = 'item file-item';
    if (entry.file.type.startsWith('image/')) { const img = document.createElement('img'); img.className = 'preview'; img.alt = ''; img.src = entry.preview; div.append(img); }
    const name = document.createElement('strong'); name.textContent = entry.file.name; div.append(name);
    const description = document.createElement('p'); description.textContent = entry.receipt ? `Verified · ${entry.receipt.size} bytes\nWorkstation: ${entry.receipt.path}` : entry.error || `${entry.file.size} bytes · ready`; div.append(description);
    if (entry.receipt) { const link = document.createElement('a'); link.href = entry.receipt.downloadUrl || `/api/files/${encodeURIComponent(entry.receipt.id)}`; link.textContent = 'Download saved file'; div.append(link); }
    const remove = document.createElement('button'); remove.textContent = 'Remove from list'; remove.disabled = uploading; remove.onclick = () => { URL.revokeObjectURL(entry.preview); files = files.filter(f => f !== entry); renderFiles(); }; div.append(remove);
    $('file-list').append(div);
  }
  const verified = files.filter(entry => entry.receipt);
  $('review-originals').hidden = !verified.length;
  if (!verified.length) reviewingOriginals = false;
  $('cleanup').hidden = !reviewingOriginals || !verified.length;
  $('cleanup-files').replaceChildren();
  if (reviewingOriginals) for (const entry of verified) {
    const div = document.createElement('div'); div.className = 'item';
    const name = document.createElement('strong'); name.textContent = entry.file.name;
    const path = document.createElement('p'); path.textContent = `Workstation: ${entry.receipt.path}`;
    const label = document.createElement('label'); const check = document.createElement('input');
    check.type = 'checkbox'; check.checked = Boolean(entry.checkedCopy);
    check.onchange = () => { entry.checkedCopy = check.checked; };
    label.append(check, ' Checked saved copy'); div.append(name, path, label); $('cleanup-files').append(div);
  }
}
$('review-originals').onclick = () => { reviewingOriginals = true; renderFiles(); };
function addFiles(input) {
  const incoming = [...input.files]; input.value = '';
  if (files.length + incoming.length > 20) { showError(new Error('Choose at most 20 files in a batch.')); return; }
  for (const file of incoming) {
    if (file.size > 20 * 1024 * 1024) { showError(new Error(`${file.name} is larger than 20 MiB.`)); continue; }
    files.push({file, id:crypto.randomUUID(), preview:URL.createObjectURL(file)});
  }
  renderFiles();
}
$('files').onchange = event => addFiles(event.target);
$('camera').onchange = event => addFiles(event.target);
$('upload').onclick = run(async () => {
  if (!files.some(f => !f.receipt)) throw new Error('Choose files to upload.');
  uploading = true; $('upload').disabled = true; $('files').disabled = true; $('camera').disabled = true; renderFiles();
  try {
    for (const entry of files.filter(f => !f.receipt)) {
      try {
        entry.error = 'Uploading…'; renderFiles();
        const digest = await crypto.subtle.digest('SHA-256', await entry.file.arrayBuffer());
        const hash = [...new Uint8Array(digest)].map(n => n.toString(16).padStart(2,'0')).join('');
        const receipt = await api('/api/files', {method:'POST', body:entry.file, headers:{'X-File-Name':encodeURIComponent(entry.file.name),'X-Content-SHA256':hash,'X-Upload-ID':entry.id}});
        if (receipt.verified !== true || receipt.sha256 !== hash || receipt.size !== entry.file.size || !receipt.id || !receipt.path) throw new Error('Receipt verification failed. Retry this file.');
        entry.receipt = receipt; entry.error = '';
      } catch (error) { entry.error = `Failed: ${error.message}. Retry this file.`; }
      renderFiles();
    }
    await refreshVault();
  } finally { uploading = false; $('upload').disabled = false; $('files').disabled = false; $('camera').disabled = false; renderFiles(); }
});
let selectedId = '';
$('target').addEventListener('change', () => {
  if (view && $('target').value !== view.target.id) { $('target').value = view.target.id; showError('Detach the current workbench before choosing another.'); }
  else if (selectedId && $('target').value !== selectedId && $('draft').value && !confirm('The draft is still in the composer. Change the selected workbench? Check the target before pasting.')) $('target').value = selectedId;
  else selectedId = $('target').value;
  updateTarget();
});
(async () => {
  try { const initial = await draftStore.load('composer'); if (draftVersion === 0 && !$('draft').value) { $('draft').value = initial ?? ''; $('draft-status').textContent = initial === undefined ? 'No saved draft' : 'Draft loaded'; } } catch (error) { $('draft-status').textContent = 'Load failed'; showError(error); }
  requestPersistence().then(granted => { if (!granted) { const note = document.createElement('p'); note.className = 'hint'; note.textContent = 'Persistent storage was not granted. The browser may remove saved drafts under storage pressure.'; $('draft').after(note); } });
  await Promise.allSettled([lifecycle(refresh).then(() => { selectedId = $('target').value; }), renderTray(), refreshVault()]).then(results => { for (const result of results) if (result.status === 'rejected') showError(result.reason); });
})();
