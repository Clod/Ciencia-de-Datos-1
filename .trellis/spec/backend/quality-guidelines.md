# Quality Guidelines

> Code quality standards for backend development.

---

## Overview

No linter configuration exists. No type checker configuration exists. No test suite exists. Quality is enforced by Scope Lock (modify only the requested cells) plus manual marimo runs (`marimo edit` / `marimo run`). Permission-First applies: no terminal modifications or file creation without explicit approval (`CLAUDE.md:8`, `GEMINI.md:8`).

## Forbidden Patterns

- New dependencies outside the declared marimo header. `loops_anidados_marimo.py:1-6` declares `requires-python = ">=3.11"` and `marimo>=0.24.2`. Do not import undeclared packages.
- Bare `except` beyond row-comparison loops. The only accepted bare `except` is `formula_simulation.py:29` (`except: continue`).
- Modifying code outside the active request scope. Scope Lock forbids it (`GEMINI.md:11`).
- Committing `.venv/`, `__pycache__/`, or `__marimo__/` artifacts. These directories exist locally and stay uncommitted.

## Required Patterns

1. Marimo app scaffold in every runnable `.py` app:

```python
import marimo
__generated_with = "0.21.1"
app = marimo.App(width="full")
```

Source: `formula_simulation.py:1-4`.

2. Cell decorator on every cell function: `@app.cell`. Optional `hide_code=True` only for explanatory markdown cells. Example: `formula_simulation.py:135`.
3. Explicit `return` of values consumed downstream. Example: `formula_simulation.py:13` returns `ESCALAS_MATRIX, datetime, mo`.
4. Executable entry point:

```python
if __name__ == "__main__":
    app.run()
```

Source: `formula_simulation.py:491-492`.

## Testing Requirements

No automated tests exist. Before marking work done:

1. Run `marimo run <file>.py` for a smoke load.
2. Change one UI input and confirm dependent cells recompute.
3. Confirm no new files were created without approval.

## Code Review Checklist

- [ ] Only requested cells or files changed.
- [ ] `vlookup` still returns `0` on `None` input.
- [ ] Display formatting still guards with `isinstance(x, (int, float))`.
- [ ] No secrets or absolute local paths added.
