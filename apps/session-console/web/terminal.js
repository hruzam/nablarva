import { Terminal } from '@xterm/xterm';
import { FitAddon } from '@xterm/addon-fit';
import '@xterm/xterm/css/xterm.css';
import { api } from './api.js';

const KEYS = Object.freeze({ Enter: '\r', Tab: '\t', ShiftTab: '\x1b[Z', Escape: '\x1b',
  ArrowUp: '\x1b[A', ArrowDown: '\x1b[B', ArrowRight: '\x1b[C', ArrowLeft: '\x1b[D',
  PageUp: '\x1b[5~', PageDown: '\x1b[6~', Home: '\x1b[H', End: '\x1b[F',
  Backspace: '\x7f', Delete: '\x1b[3~', CtrlC: '\x03', CtrlD: '\x04', CtrlZ: '\x1a' });

// Pinned DOM qualification glue: viewport and screen are siblings under .xterm.
function touchScroll(element) {
  const controller = new AbortController();
  const options = { capture: true, signal: controller.signal };
  let gesture = null;
  const reset = () => { gesture = null; };
  element.addEventListener('touchstart', event => {
    reset();
    if (event.touches.length !== 1) return;
    const terminal = event.target.closest?.('.xterm');
    const screen = terminal?.querySelector('.xterm-screen');
    if (!screen || !terminal.classList.contains('enable-mouse-events')) return;
    if (event.target.closest?.('textarea, input, a, button')) return;
    const touch = event.touches[0];
    const bounds = screen.getBoundingClientRect();
    if (touch.clientX < bounds.left || touch.clientX >= bounds.right ||
        touch.clientY < bounds.top || touch.clientY >= bounds.bottom) return;
    const measure = terminal.querySelector('.xterm-char-measure-element');
    const row = measure?.getBoundingClientRect().height || parseFloat(getComputedStyle(terminal).fontSize) * 1.3;
    gesture = { terminal, screen, id: touch.identifier, x: touch.clientX, y: touch.clientY,
      lastY: touch.clientY, row: Math.max(12, row || 18), pending: 0, active: false };
  }, { ...options, passive: true });
  element.addEventListener('touchmove', event => {
    const g = gesture;
    if (!g) return;
    if (event.touches.length !== 1 || !g.terminal.classList.contains('enable-mouse-events')) return reset();
    const touch = event.touches[0];
    if (touch.identifier !== g.id) return reset();
    if (!g.active) {
      const dx = touch.clientX - g.x, dy = touch.clientY - g.y;
      if (Math.max(Math.abs(dx), Math.abs(dy)) < 8) return;
      if (Math.abs(dx) >= Math.abs(dy)) return reset();
      g.active = true;
    }
    if (!event.cancelable) return reset();
    event.preventDefault();
    g.pending += g.lastY - touch.clientY;
    g.lastY = touch.clientY;
    const rows = Math.min(8, Math.floor(Math.abs(g.pending) / g.row));
    const direction = Math.sign(g.pending);
    for (let i = 0; i < rows; i++) g.screen.dispatchEvent(new WheelEvent('wheel', {
      bubbles: true, cancelable: true, deltaMode: WheelEvent.DOM_DELTA_LINE,
      deltaY: direction, clientX: g.x, clientY: g.y
    }));
    g.pending -= rows * direction * g.row;
  }, { ...options, passive: false });
  element.addEventListener('touchend', reset, { ...options, passive: true });
  element.addEventListener('touchcancel', reset, { ...options, passive: true });
  return () => controller.abort();
}

export function createTerminal({ container, onState = () => {} }) {
  const terminal = new Terminal({ fontSize: 12, fontFamily: 'monospace', scrollback: 10000,
    cursorBlink: true, disableStdin: true, theme: { background: '#181c24', foreground: '#e5e9ef' } });
  const fitAddon = new FitAddon();
  terminal.loadAddon(fitAddon);
  terminal.open(container);
  const stopTouch = touchScroll(terminal.element);
  const encoder = new TextEncoder();
  let socket = null, view = null, state = 'detached', uncertainInput = false;
  let inputSent = false, historyRequested = false, pendingOutput = 0, paused = false;
  let disposed = false;
  let attaching = false, navigation = 0, cancelAttach = null;
  function emit(next, message) {
    state = next;
    terminal.options.disableStdin = next !== 'connected';
    onState({ state, targetId: view?.target.id, generation: view?.target.generation,
      uncertainInput, ...(message ? { message } : {}) });
  }
  function requireConnection() {
    if (state !== 'connected' || socket?.readyState !== WebSocket.OPEN) {
      throw new Error('Terminal is disconnected. Select the target explicitly; input was not queued.');
    }
  }
  function sendInput(data) {
    requireConnection();
    const bytes = encoder.encode(data);
    if (bytes.length > 256 * 1024 - 1) throw new Error('Terminal input is too large.');
    socket.send(encoder.encode('0' + data));
    inputSent = true;
  }
  const input = terminal.onData(data => {
    try { sendInput(data); } catch (error) { emit(state, error.message); }
  });
  const resize = terminal.onResize(({ cols, rows }) => {
    if (state === 'connected' && socket?.readyState === WebSocket.OPEN) {
      socket.send(encoder.encode('1' + JSON.stringify({ columns: cols, rows })));
    }
  });
  function fit() {
    if (!disposed && container.clientWidth > 0 && container.clientHeight > 0) fitAddon.fit();
  }
  const observer = new ResizeObserver(fit);
  observer.observe(container);

  async function clearAttachment() {
    if (cancelAttach) { cancelAttach(); cancelAttach = null; }
    const previous = view, previousSocket = socket;
    socket = null;
    if (inputSent) uncertainInput = true;
    inputSent = false;
    historyRequested = false;
    if (previousSocket) {
      previousSocket.onclose = null;
      previousSocket.onmessage = null;
      previousSocket.onerror = null;
      previousSocket.close(1000, 'Explicit detach');
    }
    // Drain already accepted writes before a new target resets the display.
    await new Promise(resolve => terminal.write('', resolve));
    emit('detached');
    view = null;
    if (previous) await api(`/api/views/${previous.viewId}`, { method: 'DELETE' });
  }

  async function detach() {
    navigation++;
    await clearAttachment();
  }

  async function attach(nextView) {
    if (disposed) throw new Error('Terminal was disposed.');
    if (attaching) throw new Error('A target attachment is already in progress.');
    attaching = true;
    const ticket = ++navigation;
    try {
    await clearAttachment();
    if (ticket !== navigation) throw new Error('Attachment cancelled by explicit detach.');
    view = nextView;
    pendingOutput = 0;
    paused = false;
    terminal.reset();
    fit();
    emit('connecting');
    const url = new URL(view.wsPath, location.origin);
    if (url.origin !== location.origin) throw new Error('Cross-origin terminal URL refused.');
    url.protocol = location.protocol === 'https:' ? 'wss:' : 'ws:';
    const current = new WebSocket(url, 'tty');
    socket = current;
    current.binaryType = 'arraybuffer';
    return await new Promise((resolve, reject) => {
      let ready = false;
      const timeout = setTimeout(() => {
        if (!ready) { cancelAttach = null; current.close(); reject(new Error('Terminal did not initialize.')); }
      }, 10000);
      cancelAttach = () => { clearTimeout(timeout); reject(new Error('Attachment cancelled.')); };
      current.onopen = () => current.send(JSON.stringify({ binding: nextView.binding,
        columns: terminal.cols, rows: terminal.rows }));
      current.onmessage = event => {
        if (socket !== current) return;
        const data = new Uint8Array(event.data);
        if (data[0] !== 48) return; // Own preferences; ignore ttyd title/preferences frames.
        if (!ready) {
          ready = true;
          cancelAttach = null;
          clearTimeout(timeout);
          emit('connected');
          resolve();
        }
        pendingOutput += data.length;
        if (!paused && pendingOutput > 100000) { paused = true; current.send(encoder.encode('2')); }
        terminal.write(data.subarray(1), () => {
          if (socket !== current) return;
          pendingOutput -= data.length;
          if (paused && pendingOutput < 20000 && current.readyState === WebSocket.OPEN) {
            paused = false;
            current.send(encoder.encode('3'));
          }
        });
      };
      current.onclose = event => {
        clearTimeout(timeout);
        cancelAttach = null;
        if (socket !== current) return;
        if (inputSent) uncertainInput = true;
        socket = null;
        emit(event.code === 4009 ? 'stale' : 'disconnected', event.reason || 'Select the target again to reconnect.');
        if (!ready) reject(new Error(event.reason || 'Terminal connection closed.'));
      };
      current.onerror = () => {
        clearTimeout(timeout);
        cancelAttach = null;
        if (!ready) reject(new Error('Terminal connection failed.'));
      };
    });
    } finally { attaching = false; }
  }

  async function history(action) {
    requireConnection();
    if (!['enter', 'leave', 'pageUp', 'pageDown'].includes(action)) throw new Error('Unsupported history action.');
    const attached = view;
    async function control(step) {
      if (view !== attached) throw new Error('Attachment changed during history navigation.');
      requireConnection();
      await api(`/api/views/${attached.viewId}/history`, {
        method: 'POST', body: { action: step, binding: attached.binding }
      });
      if (view !== attached) throw new Error('Attachment changed during history navigation.');
    }
    // Always establish copy mode: native keys/swipes may have left it since the last tap.
    if (action === 'pageUp' || action === 'pageDown') await control('enter');
    await control(action);
    historyRequested = action !== 'leave';
  }

  async function key(name) {
    requireConnection();
    if (name === 'History' || name === 'Live' ||
        (historyRequested && (name === 'PageUp' || name === 'PageDown'))) {
      const action = { History: 'enter', Live: 'leave', PageUp: 'pageUp', PageDown: 'pageDown' }[name];
      return history(action);
    }
    if (!Object.hasOwn(KEYS, name)) throw new Error('Unsupported terminal key.');
    sendInput(KEYS[name]);
  }

  function paste(text) {
    requireConnection();
    if (typeof text !== 'string') throw new Error('Paste requires text.');
    if (/[\r\n]/.test(text) && (!terminal.modes.bracketedPasteMode || !view.target.multilinePasteQualified)) {
      throw new Error('Multiline paste is not yet qualified for this target. Keep the draft; paste one line at a time.');
    }
    if (/[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]/.test(text)) {
      throw new Error('Control characters require an explicit terminal key action.');
    }
    terminal.paste(text);
  }

  async function dispose() {
    if (disposed) return;
    disposed = true;
    try { await detach(); } finally {
      observer.disconnect(); stopTouch(); input.dispose(); resize.dispose(); terminal.dispose();
    }
  }
  emit('detached');
  return { attach, detach, focus: () => terminal.focus(), paste, key, history, fit, dispose };
}
