# DECISIONS — Termbrana ADR Ledger

Append-only record of product-technical architecture decisions. Every entry cites the flag line or session brief that authorized it.

---

## ADR-0000 — Adoption record

**Date:** 2026-08-15  
**Authority:** nablarva flag L11 (majkee gavel 2026-08-15)  
**Session:** toolbox-termbrana-01-brief/brief.md  

### Adoption

Five founding files from `~/.remote/harvest/` adopted as substrate:

- `termbrana.project-definition.md` (Wave r0, role: founding canon)
- `termbrana.execution-plan.md` (Wave r0, role: founding canon)
- `termbrana.addendum-to-foil-theory.md` (Wave r0, role: founding canon)
- `foil_theory.md` (Nabla, role: research history)
- `foil_plugin.rs` (Nabla, role: research history)

### Host pins (M0)

Established at founding to freeze the host contract for all milestone work:

- **zellij:** 0.44.3
- **rustc:** 1.95.0
- **WASM target:** wasm32-wasip1
- **zellij-tile crate:** 0.44.3

### Decision: Independent core, Zellij-first observer

Termbrana is an independent semantic observation and navigation layer. NablaRava is one optional consumer of its neutral outputs, never a dependency.

The MVP delivers read-only navigation (no input injection or signal sending in the observer default). Semantic blocks, bookmarks, filters, search, and replay precede visual opacity.
