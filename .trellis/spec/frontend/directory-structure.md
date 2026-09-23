# Directory Structure

> How frontend code is organized in this project.

---

## Overview

This project has no `src/` frontend. This project has no component framework beyond marimo. The term "frontend" in this project means marimo cells that render UI (`mo.md`, `mo.ui.*`, `mo.Html`, `mo.vstack`, `mo.hstack`) inside root-level `.py` apps, plus static `.html` exports.

## Directory Layout

```
/
├── formula_simulation.py    # Marimo UI: inputs + result cells
├── loops_anidados_marimo.py # Marimo UI: controls + bottles + console
├── loops_anidados_marimo.md # Reference notes for the visualizer
├── maquina_de_cafe.html     # Static export example
├── loops_anidados.html      # Static export example
├── git.html
└── mp3/                     # Media assets
```

No `src/components/`, `src/hooks/`, or `src/assets/` directories exist.

## Module Organization

1. Keep UI construction inside the marimo app file. Do not extract a separate UI package.
2. Group HTML templates in one `hide_code=True` cell. Example: `loops_anidados_marimo.py:310-381` defines `PLANTILLA_LINEA_CODIGO`, `PLANTILLA_CAJA_CODIGO`, `PLANTILLA_BOTELLA`, `PLANTILLA_FILA_BOTELLAS`, `PLANTILLA_CONSOLA`.
3. Keep layout code (`mo.vstack`, `mo.hstack`) adjacent to the controls it arranges. Example: `formula_simulation.py:123-131` builds `layout` from `topes` and `others`.
4. Store reference prose in `.md` files next to the app. Example: `loops_anidados_marimo_referencia.md`.

## Naming Conventions

- Template constants: `PLANTILLA_<NOMBRE>` in UPPER_SNAKE_CASE. Example: `loops_anidados_marimo.py:333`.
- UI handles: snake_case ending in `_btn`, `controls`, `slider`, `layout`, `ui_dict`. Example: `loops_anidados_marimo.py:278-306`.
- Static exports: same basename as the app with `.html`. Example: `loops_anidados_marimo.py` renders `loops_anidados.html`.

## Examples

- Input dictionary: `formula_simulation.py:37-54` builds `mo.ui.dictionary({...})`.
- Control row: `loops_anidados_marimo.py:306` builds `controls = mo.hstack([prev_btn, next_btn, reset_btn, slider], justify="start")`.
- Page layout: `loops_anidados_marimo.py:637-650` composes two `mo.vstack` columns inside `mo.hstack`.
