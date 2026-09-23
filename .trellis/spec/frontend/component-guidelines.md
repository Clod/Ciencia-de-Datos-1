# Component Guidelines

> How components are built in this project.

---

## Overview

Components are marimo cells, not React components. A cell is a Python function decorated with `@app.cell`. Cell parameters declare dependencies. Marimo re-executes dependent cells when state changes. There are no props, no JSX, no CSS modules.

## Component Structure

Standard cell shape (`formula_simulation.py:149-154`):

```python
@app.cell
def _(mo, sueldo_bruto):
    mo.md("### B30 - SAC Prorrateado\n**Formula:** `=(B27)/12`")
    sac_prorrateado = (sueldo_bruto)/12
    _fmt = f"${sac_prorrateado:,.2f}" if isinstance(sac_prorrateado, (int, float)) else sac_prorrateado
    mo.output.replace(mo.md(f"**El SAC prorrateado es:** `{_fmt}`"))
    return (sac_prorrateado,)
```

Rules:

1. Decorate every UI unit with `@app.cell`.
2. Name the function `_` and list marimo-provided values as parameters.
3. Call `mo.md(...)` first for the title plus source formula.
4. Compute one value per cell.
5. Render with `mo.output.replace(...)`.
6. Return the computed value when downstream cells need it.

## Props Conventions

Not applicable. Data flows through cell parameters. Example: `def _(mo, sueldo_bruto):` receives `sueldo_bruto` from an upstream cell. Declare each needed upstream name explicitly. Never rely on globals.

## Styling Patterns

Styles are inline HTML strings in `PLANTILLA_*` constants, filled with `.replace()`. Example (`loops_anidados_marimo.py:333-337`):

```python
PLANTILLA_LINEA_CODIGO = (
    "<div style='background: {bg}; border-left: 4px solid {color};"
    " padding: 2px 10px; opacity: {opacity}; white-space: pre;'>"
    "{idx}: {line}</div>"
)
```

Fill order matters: replace `{line}` last because line content can contain braces. The codebase documents this at `loops_anidados_marimo.py:517-523`. Never use `.format()` on these templates. `.format()` misinterprets braces inside didactic code such as `f'Botella {i}: {nivel}%'`.

Composition helper (`loops_anidados_marimo.py:599-607`):

```python
bottles = mo.Html(
    PLANTILLA_FILA_BOTELLAS.replace(
        "{botellas}",
        "".join([dibujar_botella(...) for i in range(CANT_BOTELLAS)])
    )
)
```

## Accessibility

No a11y standard is enforced. Keep `mo.ui.*` labels in Spanish matching the domain terms. Example: `mo.ui.number(value=3835388, label='Sueldo bruto')` (`formula_simulation.py:40`).

## Common Mistakes

- Using `.format()` on `PLANTILLA_*` strings. Use chained `.replace()` calls.
- Omitting `return` for a value used downstream. Marimo passes values only through returns.
- Calling `print()` for user output. Use `mo.output.replace(mo.md(...))` or `mo.Html(...)`.
