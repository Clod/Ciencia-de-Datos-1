# Quality Guidelines

> Code quality standards for frontend development.

---

## Overview

No frontend linter exists. No test runner exists. No accessibility checker exists. Quality means cells render in `marimo edit` and `marimo run`, Scope Lock holds (only requested cells change), and Spanish educational comments stay accurate.

## Forbidden Patterns

- `print()` for user output. Use `mo.output.replace(mo.md(...))` or `mo.Html(...)`.
- `.format()` on `PLANTILLA_*` HTML. Use chained `.replace()` with `{line}` last.
- Hard-coded bottle count `3` in rendering. Use `CANT_BOTELLAS` (`loops_anidados_marimo.py:100`, `loops_anidados_marimo.py:604`).
- New global CSS or external assets without approval. Styles are inline in templates.
- Editing template constants when the task targets simulation logic (Scope Lock).

## Required Patterns

1. Educational docstrings on simulation cells. Example: `loops_anidados_marimo.py:103-147` documents `get_trace()`, the trace format, and the `-1` sentinel.
2. Formula shown in every calculation header. Example: `formula_simulation.py:185` shows `"### B40 - Ley 19032\n**Formula:** \`=-B5*3%\`"`.
3. Money formatting through the `_fmt` guard:

```python
_fmt = f"${total_descuentos:,.2f}" if isinstance(total_descuentos, (int, float)) else total_descuentos
```

Source: `formula_simulation.py:206`.

4. Disabled states on boundary navigation:

```python
prev_btn = mo.ui.button(..., disabled=get_step() == 0, ...)
next_btn = mo.ui.button(..., disabled=get_step() == len(steps) - 1, ...)
```

Source: `loops_anidados_marimo.py:278-293`.

## Testing Requirements

No automated tests exist. Before marking work done:

1. Load the app with `marimo run <file>.py`.
2. Click through Anterior / Siguiente / Reiniciar or move the slider end to end.
3. Confirm code highlight, bottle levels, and console stay consistent at the first step, a middle step, and the final `"--- Ejecución terminada ---"` step.

## Code Review Checklist

- [ ] Every changed cell keeps `@app.cell` and explicit parameters.
- [ ] Templates still use `.replace()`, never `.format()`.
- [ ] Buttons clamp the index and disable at boundaries.
- [ ] Labels keep domain Spanish terms (`Sueldo bruto`, `Topes Cargas Sociales`).
