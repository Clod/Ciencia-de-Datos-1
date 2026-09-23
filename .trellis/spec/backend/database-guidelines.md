# Database Guidelines

> Database patterns and conventions for this project.

---

## Overview

This project has no database. The project has no ORM. The project has no migrations. The project has no transactions. The term "database" in this project means in-memory Python structures and file inputs read at cell startup.

## Query Patterns

There are no SQL queries. The equivalent lookup is the `vlookup` helper in `formula_simulation.py:20-30`:

```python
def vlookup(value, matrix, col_index, range_lookup=True):
    idx = col_index - 1
    best_row = None
    if value is None: return 0
    for row in matrix:
        try:
            if row[0] is None: continue
            if row[0] <= value: best_row = row
            else: break
        except: continue
    return best_row[idx] if best_row else 0
```

Usage with a matrix slice appears in `formula_simulation.py:420-425`:

```python
impuesto_anual = if_func(base_imponible>0,(vlookup(base_imponible,ESCALAS_MATRIX[18:27],3)),0)
```

Rules:

1. Slice `ESCALAS_MATRIX` before passing it. Never pass the full matrix when only rows `18:27` apply.
2. Convert `col_index` from 1-based to 0-based inside `vlookup`. Callers keep the spreadsheet 1-based index.
3. Return `0` when input is `None` or no row matches. Do not raise.

## Migrations

Not applicable. Schema changes mean editing `escalas_data.py` directly and re-running the marimo app.

## Naming Conventions

- Matrix constant: `ESCALAS_MATRIX` (`escalas_data.py:4`).
- Tax-bracket rows: plain lists with mixed types (`float`, `str 'en adelante'`, `None`). Example: `escalas_data.py:176-194`.
- Trace state: `trace` / `steps` lists of dicts with keys `line`, `i`, `j`, `nivel`, `msg`, `bottle_idx` (`loops_anidados_marimo.py:127-136`).

## Common Mistakes

- Treating `'23333.68'` as a number. The cell `escalas_data.py:223` stores `'23333.68'` as `str`, while neighbors store floats. Clean the value before arithmetic.
- Assuming rectangular data. Many rows are padded with `None` to width 19. Filter `None` before aggregation.
