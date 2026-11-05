The first isolated browser runner stopped at its exact-string detached assertion.
The terminal emits detached plus last-target/uncertainty details, so exact equality
was not a valid assertion. Updated the runner to startsWith detached and unique
marker files, then all checks passed. No production behavior changed for this.
