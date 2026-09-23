# Logging Guidelines

> How logging is done in this project.

---

## Overview

This project uses no logging library. This project emits no structured logs. The term "logging" in this project means user-visible marimo outputs (`mo.md`, `mo.Html`, `mo.output.replace`) plus message strings stored in trace dicts.

## Log Levels

Not applicable. No `debug/info/warn/error` levels exist. Use these display equivalents:

1. Explanatory text: `mo.md(...)` with the formula shown. Example: `formula_simulation.py:150` shows `"### B30 - SAC Prorrateado\n**Formula:** \`=(B27)/12\`"`.
2. Computed result: `mo.output.replace(mo.md(f"**...:** \`{_fmt}\`"))`. Example: `formula_simulation.py:153`.
3. Simulated console: `console_msgs` list joined with `'<br>> '` inside `PLANTILLA_CONSOLA`. Example: `loops_anidados_marimo.py:614-626`.

## Structured Logging

Not applicable. Trace steps use this fixed dict shape (`loops_anidados_marimo.py:127-136`):

```python
{
    "line": 8,
    "i": 1,
    "j": 2,
    "nivel": 50.0,
    "msg": "Calculando nivel: 50.0%",
    "bottle_idx": 1
}
```

Keep all six keys on every appended step. Consumers read `st['bottle_idx']` and `st['line']` without guards (`loops_anidados_marimo.py:537-540`).

## What to Log

- Each computed variable with its source formula in the `mo.md` header. Example: `formula_simulation.py:177` shows `**Formula:** \`=-B5*11%\``.
- Each trace transition with `msg` text. Example: `loops_anidados_marimo.py:189` stores `f"Calculando nivel: {nivel:.1f}%"`.

## What NOT to Log

- No secrets exist in this project. No PII beyond salary inputs entered in local UI controls. Do not persist `ui_dict` values to disk. Do not add print-based logging that bypasses marimo cell outputs.
