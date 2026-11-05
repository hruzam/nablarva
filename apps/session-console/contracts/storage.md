# Storage interface — experimental browser pilot

Cartan implementation contract, 2026-10-30; no architectural lock. Authentication,
exact Origin and CSRF validation belong to the host server middleware, on ALL routes.
Host calls `install_vault(app, root: Path)` from host/vault.py. It installs only:

- GET /api/vault -> {items:[{id,kind,name,revision,size,sha256,path?}]}
- GET /api/vault/{id} -> {id,kind,name,revision,text?,size,sha256,path?}
- PUT /api/vault/{id} JSON {kind:'prompt'|'shortcut',name,text,expectedRevision:int}:
  create at revision0 expectation, update only exact revision; response item. ID is
  UUID supplied by browser; kind immutable. Conflict409 with current revision.
- DELETE /api/vault/{id} JSON {expectedRevision:int} -> {deleted:true} or409.
- POST /api/files raw bytes; headers X-File-Name URL-encoded original name,
  X-Content-SHA256 lowercase64 hex. Max20MiB per file. Server hashes streamed bytes,
  verifies advertised digest, atomically persists and reads back digest, returns
  {id,kind:'file',name,revision:1,size,sha256,path,verified:true}. Reject mismatch422.
  No original filename enters filesystem paths; generated IDs only. Idempotency
  X-Upload-ID UUID required: retry same content+name returns original receipt; conflict409
  for reuse with different content. Failed writes leave no acknowledged item.
- GET /api/files/{id} -> attachment bytes, Content-Disposition attachment, nosniff.

Dedicated absolute root only, no arbitrary paths. SQLite metadata with transaction
revision checking acceptable; blobs in generated-ID files with fsync/atomic replace.
Never expose or read outside root; reject traversal/symlink escapes. Store file bytes
unchanged including EXIF; user chooses which photos to upload. No image processing.

Browser web/storage.js exports:
`draftStore.load(key)`, `draftStore.save(key,text)` -> Promise (ack only after IndexedDB
transaction completion), `draftStore.remove(key)`, `trayStore.list()`,
`trayStore.add(text)` (expires at wall-clock now+30min), `trayStore.remove(id)`,
`trayStore.clear()`, `requestPersistence()` -> Promise<boolean>. Unsent drafts do not
expire. Expired tray records filtered/deleted on access. Persistence denial must not
break writes; storage error is visible and draft remains in textarea. No localStorage
fallback pretending durable acknowledgement. Browser module has no UI/HTTP responsibilities.

Phone originals cannot be erased via browser file picker. Only AFTER per-file verified
receipt and browser digest equality may UI offer manual Gallery cleanup checklist.
Batch partial failures remain selected; never announce whole-batch success incorrectly.
