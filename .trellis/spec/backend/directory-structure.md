# Directory Structure

> How backend code is organized in this project.

---

## Overview

This project has no `src/` backend. The project is a flat data-science workspace. Python logic lives in root-level `.py` modules next to `.ipynb` lessons and `.xlsx` inputs. The term "backend" in this project means pure Python computation modules imported by marimo cells.

## Directory Layout

```
/
├── escalas_data.py          # Static data matrix (ESCALAS_MATRIX)
├── formula_simulation.py    # Marimo app: salary/tax simulation logic
├── loops_anidados_marimo.py # Marimo app: educational trace simulation
├── clase_01.ipynb           # Lesson notebooks
├── clase02.ipynb
├── AMBROSIS 2026 02 V3.xlsx # Source spreadsheet input
├── analysis_012026.md       # Analysis notes
├── __marimo__/              # Marimo session artifacts
├── .trellis/spec/           # Project guidelines
├── .venv/                   # Local virtualenv (not committed)
└── mp3/                     # Media assets
```

No `src/routes/`, `src/services/`, or `src/utils/` directories exist.

## Module Organization

1. Put shared static data in a root-level `<name>_data.py` module. Example: `escalas_data.py` exposes `ESCALAS_MATRIX`.
2. Put simulation logic in a root-level marimo app `<name>.py` with `app = marimo.App(width="full")`.
3. Keep helper functions (`if_func`, `vlookup`) in an early `@app.cell` so later cells receive them as parameters.
4. Keep lesson content in `.ipynb` files. Do not move lesson logic into separate packages.

## Naming Conventions

- Data modules: snake_case with `_data` suffix. Example: `escalas_data.py`.
- Marimo apps: snake_case describing the simulation. Example: `formula_simulation.py`.
- Exported constants: UPPER_SNAKE_CASE. Example: `ESCALAS_MATRIX` in `escalas_data.py:4`.
- Cell functions: anonymous `def _():` or `def _(<deps>):`. Example: `formula_simulation.py:8`, `formula_simulation.py:149`.

## Examples

- Data module: `escalas_data.py:4` defines `ESCALAS_MATRIX = [...]`.
- Computation cell: `formula_simulation.py:20-30` defines `vlookup(value, matrix, col_index, range_lookup=True)`.
- Import cell: `formula_simulation.py:7-13` imports `ESCALAS_MATRIX` and `datetime` and returns them for downstream cells.
