# Type Safety

> Type safety patterns in this project.

---

## Overview

No static type system is enforced. No `mypy` configuration exists. No runtime validation library (`Zod`, `Yup`) exists. Safety comes from `isinstance` guards, `None` checks, and fixed trace-dict shapes.

## Type Organization

Types are implicit:

- Money values: `int` or `float`. Formatted only after an `isinstance(x, (int, float))` check. Example: `formula_simulation.py:152`.
- Matrix cells: `float`, `str` (`'en adelante'`, `'23333.68'`), or `None`. Example: `escalas_data.py:176-194` and `escalas_data.py:223`.
- Trace steps: dicts with fixed keys `line`, `i`, `j`, `nivel`, `msg`, `bottle_idx`. Example: `loops_anidados_marimo.py:127-136`.
- Nullable loop indices: `i` / `j` are `None` outside loops, `int` inside loops.

## Validation

Validate at the boundary of each helper:

1. `vlookup` rejects `None` input with `return 0` (`formula_simulation.py:23`).
2. `vlookup` skips rows whose first cell is `None` (`formula_simulation.py:26`).
3. Display code falls back to the raw value when formatting does not apply:

```python
_fmt = f"${obra_social:,.2f}" if isinstance(obra_social, (int, float)) else obra_social
```

Source: `formula_simulation.py:197`.

## Common Patterns

- Sentinel `-1` for inactive position: `"bottle_idx": -1` (`loops_anidados_marimo.py:160`), `"line": -1` for termination (`loops_anidados_marimo.py:195`).
- 1-based spreadsheet columns converted once: `idx = col_index - 1` (`formula_simulation.py:21`).
- Decimal percentages stored both ways: `5` / `0.05` appear in different matrix blocks. Normalize before arithmetic.

## Forbidden Patterns

- Unchecked arithmetic on matrix cells. Matrix cells can be `str` or `None`. Check before computing.
- `any`-style untyped passthrough of `ui_dict.value` entries. Read each key with an explicit default.
- `.format()` on HTML templates containing code braces. Use chained `.replace()`.
