// Event-routing checks only: this cannot qualify Android touch or tmux rendering.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const listeners = new Map();
const emitted = [];
let mouse = true;
const terminal = {
  classList: { contains: () => mouse },
  querySelector: selector => selector === '.xterm-screen' ? screen :
    ({ getBoundingClientRect: () => ({ height: 14 }) })
};
const screen = { dispatchEvent: event => emitted.push(event),
  getBoundingClientRect: () => ({ left: 0, top: 0, right: 200, bottom: 500 }) };
const target = { closest: selector => selector === '.xterm' ? terminal : null };
class Wheel {
  static DOM_DELTA_LINE = 1;
  constructor(type, properties) { this.type = type; Object.assign(this, properties); }
}
vm.runInNewContext(fs.readFileSync(__dirname + '/trial/touch_scroll.js', 'utf8'), {
  document: { addEventListener: (name, fn, options) => listeners.set(name, { fn, options }) },
  getComputedStyle: () => ({ fontSize: '12px' }), WheelEvent: Wheel
});
const touch = (x, y, id = 1) => ({ clientX: x, clientY: y, identifier: id });
function event(name, touches, overrides = {}) {
  let prevented = false;
  const value = { target, touches, cancelable: true,
    preventDefault: () => { prevented = true; }, ...overrides };
  listeners.get(name).fn(value);
  return prevented;
}
const start = () => { emitted.length = 0; event('touchstart', [touch(40, 100)]); };

assert.equal(listeners.get('touchmove').options.passive, false);
assert.equal(listeners.get('touchstart').options.passive, true);
start();
assert.equal(event('touchmove', [touch(41, 105)]), false, 'tap jitter untouched');
event('touchend', []);
assert.equal(emitted.length, 0);
start();
assert.equal(event('touchmove', [touch(40, 142)]), true);
assert.equal(emitted.length, 3, 'one event per row crossed');
assert(emitted.every(e => e.deltaY === -1 && e.deltaMode === 1 &&
  e.clientX === 40 && e.clientY === 100 && e.bubbles && e.cancelable));
start();
event('touchmove', [touch(40, 72)]);
assert.equal(emitted.length, 2);
assert(emitted.every(e => e.deltaY === 1), 'upward finger motion is positive wheel');
start();
assert.equal(event('touchmove', [touch(65, 103)]), false, 'horizontal gesture untouched');
event('touchmove', [touch(65, 180)]);
assert.equal(emitted.length, 0, 'horizontal gesture stays ignored');
start();
assert.equal(event('touchmove', [touch(40, 140), touch(60, 140, 2)]), false);
event('touchmove', [touch(40, 160)]);
assert.equal(emitted.length, 0, 'pinch resets entire gesture');
start();
mouse = false;
assert.equal(event('touchmove', [touch(40, 160)]), false);
assert.equal(emitted.length, 0, 'mouse reporting loss sends no shell arrows');
mouse = true;
start();
event('touchcancel', []);
event('touchmove', [touch(40, 160)]);
assert.equal(emitted.length, 0);
start();
event('touchmove', [touch(40, 300)]);
assert.equal(emitted.length, 8, 'bounded wheel count per move');
event('touchend', []);
emitted.length = 0;
event('touchstart', [touch(40, 100)], { target: { closest: selector =>
  selector === '.xterm' ? terminal : {} } });
event('touchmove', [touch(40, 160)]);
assert.equal(emitted.length, 0, 'input/link controls untouched');
start();
event('touchmove', [touch(40, 142)]);
assert.equal(emitted.length, 3, 'viewport sibling target resolves through common xterm parent');
event('touchend', []);
emitted.length = 0;
event('touchstart', [touch(210, 100)]);
event('touchmove', [touch(210, 142)]);
assert.equal(emitted.length, 0, 'scrollbar gutter outside screen remains untouched');
console.log('PASS: threshold/taps, directions, row quantization, coordinates, horizontal, pinch, reporting loss, cancel, cap, input exclusion, viewport sibling, gutter');
