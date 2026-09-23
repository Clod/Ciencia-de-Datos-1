# Error Handling

> How errors are handled in this project.

---

## Overview

This project defines no custom error classes. This project has no API error responses. Errors are handled with local guards inside marimo cells. Failures surface as marimo cell outputs, not as HTTP responses.

## Error Types

None defined. Use built-in Python behavior plus these sentinels:

- `None` means missing cell value. Example: `formula_simulation.py:23` returns `0` when `value is None`.
- `-1` in `bottle_idx` means no active bottle. Example: `loops_anidados_marimo.py:153-160` uses `"bottle_idx": -1` for init snapshots.
- `-1` in `line` means execution finished. Example: `loops_anidados_marimo.py:195` uses `"line": -1`.

## Error Handling Patterns

1. Guard `None` inputs at function entry and return `0`:

```python
if value is None: return 0
```

Source: `formula_simulation.py:23`.

2. Skip non-comparable matrix rows with `try/except: continue`:

```python
for row in matrix:
    try:
        if row[0] is None: continue
        if row[0] <= value: best_row = row
        else: break
    except: continue
```

Source: `formula_simulation.py:24-29`.

3. Guard display formatting with `isinstance`:

```python
_fmt = f"${sac_prorrateado:,.2f}" if isinstance(sac_prorrateado, (int, float)) else sac_prorrateado
```

Source: `formula_simulation.py:152`.

4. Guard optional UI values with `in` checks plus defaults:

```python
bono = ui_dict.value['bono'] if 'bono' in ui_dict.value else 0
```

Source: `formula_simulation.py:60`.

## API Error Responses

Not applicable. No backend endpoints exist.

## Common Mistakes

- Widening the bare `except: continue` in `vlookup` to silence real bugs. Keep the `except` body as `continue` only for row comparison, never for the whole cell.
- Raising instead of returning `0` from `vlookup`. Downstream tax cells expect a number and add it directly.
