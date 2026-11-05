/* Disposable ttyd 1.7.7/xterm 5.4 DOM adapter, injected through supported -I. */
(() => {
  let gesture = null;
  const reset = () => { gesture = null; };

  document.addEventListener('touchstart', event => {
    reset();
    if (event.touches.length !== 1) return;
    // Viewport and screen are siblings; Firefox may target the viewport overlay.
    const terminal = event.target.closest?.('.xterm');
    const screen = terminal?.querySelector('.xterm-screen');
    // Without mouse reporting, an alt-screen wheel can become shell arrow keys.
    if (!screen || !terminal.classList.contains('enable-mouse-events')) return;
    if (event.target.closest?.('textarea, input, a, button')) return;
    const touch = event.touches[0];
    const bounds = screen.getBoundingClientRect();
    if (touch.clientX < bounds.left || touch.clientX >= bounds.right ||
        touch.clientY < bounds.top || touch.clientY >= bounds.bottom) return;
    const measure = terminal.querySelector('.xterm-char-measure-element');
    const row = measure?.getBoundingClientRect().height ||
      parseFloat(getComputedStyle(terminal).fontSize) * 1.3;
    gesture = { screen, terminal, id: touch.identifier,
      x: touch.clientX, y: touch.clientY, lastY: touch.clientY,
      row: Math.max(12, row || 18), pending: 0, active: false };
  }, { capture: true, passive: true });

  document.addEventListener('touchmove', event => {
    const g = gesture;
    if (!g) return;
    if (event.touches.length !== 1 ||
        !g.terminal.classList.contains('enable-mouse-events')) return reset();
    const touch = event.touches[0];
    if (touch.identifier !== g.id) return reset();
    if (!g.active) {
      const dx = touch.clientX - g.x;
      const dy = touch.clientY - g.y;
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
    for (let i = 0; i < rows; i++) {
      g.screen.dispatchEvent(new WheelEvent('wheel', {
        bubbles: true, cancelable: true, deltaMode: WheelEvent.DOM_DELTA_LINE,
        deltaY: direction, clientX: g.x, clientY: g.y
      }));
    }
    g.pending -= rows * direction * g.row;
  }, { capture: true, passive: false });

  document.addEventListener('touchend', reset, { capture: true, passive: true });
  document.addEventListener('touchcancel', reset, { capture: true, passive: true });
})();
