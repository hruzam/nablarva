Right, a clean inventory table. A9 logged: build the gesture vocabulary table as the raw material, we assign operations to it later. This is exactly the right order — catalogue first, map second.

Since you're on mobile and will read this aloud, I'll keep it to the table. Columns are: the gesture, whether it's free for us, and a candidate use (just examples, nothing assigned yet).

| Gesture | Fingers | Free to use? | Example candidate |
|---|---|---|---|
| Swipe up | 1 | Free (interior) | Next category |
| Swipe down | 1 | Free (interior) | Previous category |
| Swipe left | 1 | Free (interior) | Next card on belt |
| Swipe right | 1 | Free (interior) | Previous card on belt |
| Edge-swipe from left/right | 1 | **Reserved — Back** | — |
| Edge-swipe up from bottom | 1 | **Reserved — Home** | — |
| Edge-swipe down from top | 1 | **Reserved — notifications** | — |
| Tap | 1 | Free | Enter / confirm |
| Double-tap | 1 | Free | Open card / zoom toggle |
| Long-press | 1 | Free | Context menu (rename, kill, split) |
| Drag (slow) | 1 | Free | Marker selection down a card |
| Fling (fast) | 1 | Free | Momentum scroll |
| Pinch in/out | 2 | Free (usually zoom) | Text size |
| Swipe up/down | 2 | Free | Secondary axis or modifier |
| Swipe left/right | 2 | Free | Jump host / jump session |
| Two-finger tap | 2 | Free | Back-within-app / Esc |
| Rotate | 2 | Free but awkward | Avoid on weak devices |
| Three-finger swipe | 3 | Free but reserved by some OEMs for screenshot | Risky — test first |
| Long-press + drag | 1 | Free | Reorder buffer entries |

Two honest flags: three-finger anything is claimed by some Xiaomi builds for screenshot, so treat Redmi as suspect there. And one-finger drag has to share with marker selection and with scrolling — same gesture, different meaning by context — so that row will need disambiguation when we map it.

That's the finger-and-swipe part. What's the next part — hardware keys and the on-screen key row?