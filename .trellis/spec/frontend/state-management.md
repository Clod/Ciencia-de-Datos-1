# State Management

> How state is managed in this project.

---

## Overview

State lives in two places: `mo.state` scalars for navigation position, and `mo.ui.dictionary` values for user inputs. Derived state is recomputed by marimo cell re-execution. No global store exists. No server cache exists.

## State Categories

1. Navigation state: `get_step, set_step = mo.state(0, allow_self_loops=True)` (`loops_anidados_marimo.py:216`). Holds the current trace index.
2. Input state: `ui_dict = mo.ui.dictionary({...})` (`formula_simulation.py:37-54`). Holds `mo.ui.number` controls for `bono`, `plus_vacaciones`, `sueldo_bruto`, and twelve monthly `tope_cargas_sociales_*` values.
3. Precomputed state: `steps = get_trace()` (`loops_anidados_marimo.py:200`). A list of snapshot dicts replayed forward and backward.
4. Derived state: `current = steps[current_idx]` (`loops_anidados_marimo.py:442`), `levels` recomputed by replaying steps (`loops_anidados_marimo.py:537-540`), `console_msgs` filtered by printable lines (`loops_anidados_marimo.py:614`).

Read inputs defensively with defaults (`formula_simulation.py:60`):

```python
bono = ui_dict.value['bono'] if 'bono' in ui_dict.value else 0
```

## When to Use Global State

Never promote state to a module global. Keep state inside cells and pass it through parameters and returns. The visualizer cell declares all dependencies explicitly (`loops_anidados_marimo.py:385-397`):

```python
def _(
    CANT_BOTELLAS,
    PLANTILLA_BOTELLA,
    ...
    controls,
    get_step,
    mo,
    pasos_llenado,
    steps,
):
```

## Server State

Not applicable. No backend calls exist. No caching layer exists. Rebuild `steps` by re-running `get_trace()` when simulation constants change.

## Common Mistakes

- Mutating `steps` in place during rendering. Rendering reads `steps[current_idx]` and replays prior entries. Mutation breaks backward navigation.
- Storing formatted strings as state. Store numbers (`nivel` as float) and format at render time with `f"${x:,.2f}"` guarded by `isinstance`.
- Splitting one input dictionary across cells. Keep a single `ui_dict` per app so `ui_dict.value` stays consistent.
