// IndexedDB completion, not request success, is the durability acknowledgement.
const DB_NAME = 'session-console-storage';
let database;

function openDatabase() {
  if (!database) {
    database = new Promise((resolve, reject) => {
      const request = indexedDB.open(DB_NAME, 1);
      request.onupgradeneeded = () => {
        request.result.createObjectStore('drafts');
        request.result.createObjectStore('tray', { keyPath: 'id' });
      };
      request.onsuccess = () => {
        const db = request.result;
        db.onversionchange = () => { db.close(); database = undefined; };
        resolve(db);
      };
      request.onerror = () => reject(request.error);
      request.onblocked = () => reject(new Error('Storage upgrade blocked'));
    }).catch(error => { database = undefined; throw error; });
  }
  return database;
}

async function transact(storeName, mode, action) {
  const db = await openDatabase();
  return new Promise((resolve, reject) => {
    const tx = db.transaction(storeName, mode);
    let result;
    tx.oncomplete = () => resolve(result);
    tx.onabort = () => reject(tx.error || new Error('Storage transaction aborted'));
    tx.onerror = () => {}; // The abort event reports the failure once.
    try {
      action(tx.objectStore(storeName), value => { result = value; });
    } catch (error) {
      tx.abort();
      reject(error);
    }
  });
}

export const draftStore = {
  load(key) {
    return transact('drafts', 'readonly', (store, done) => {
      const request = store.get(key);
      request.onsuccess = () => done(request.result);
    });
  },
  save(key, text) {
    return transact('drafts', 'readwrite', store => { store.put(text, key); });
  },
  remove(key) {
    return transact('drafts', 'readwrite', store => { store.delete(key); });
  },
};

export const trayStore = {
  list() {
    return transact('tray', 'readwrite', (store, done) => {
      const items = [];
      const now = Date.now();
      const request = store.openCursor();
      request.onsuccess = () => {
        const cursor = request.result;
        if (!cursor) { done(items); return; }
        if (cursor.value.expiresAt <= now) cursor.delete();
        else items.push(cursor.value);
        cursor.continue();
      };
    });
  },
  add(text) {
    const item = { id: crypto.randomUUID(), text, expiresAt: Date.now() + 30 * 60 * 1000 };
    return transact('tray', 'readwrite', (store, done) => { store.add(item); done(item); });
  },
  remove(id) {
    return transact('tray', 'readwrite', store => { store.delete(id); });
  },
  clear() {
    return transact('tray', 'readwrite', store => { store.clear(); });
  },
};

export async function requestPersistence() {
  try {
    return Boolean(await navigator.storage?.persist?.());
  } catch {
    return false;
  }
}
