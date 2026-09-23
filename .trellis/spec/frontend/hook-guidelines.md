# Hook Guidelines

> How hooks are used in this project.

---

## Overview

This project has no React hooks. The reactive primitives are `mo.state` and `mo.ui.*` elements with `on_click` / `on_change` callbacks. Cell re-execution replaces hook re-rendering.

## Custom Hook Patterns

Not applicable. Do not create `use*` functions. Put stateful logic in cells:

1. Create state with `mo.state`:

```python
get_step, set_step = mo.state(0, allow_self_loops=True)
```

Source: `loops_anidados_marimo.py:216`.

2. Read state by calling the getter as the first line of a dependent cell:

```python
current_idx = get_step()
```

Source: `loops_anidados_marimo.py:439`.

3. Write state from UI callbacks:

```python
set_step(lambda v: v + 1 if v < len(steps) - 1 else v)
```

Source: `loops_anidados_marimo.py:246`.

Controllers in this project (`loops_anidados_marimo.py:228-273`):

- `increment(_)`: advances one step, clamps at `len(steps) - 1`.
- `decrement(_)`: retreats one step, clamps at `0`.
- `reset(_)`: sets state to `0`.
- The `_` parameter names the unused click event.

## Data Fetching

No fetching library exists. No `React Query` / `SWR` equivalent exists. Data comes from:

- Local constants (`ESCALAS_MATRIX`).
- Trace lists built once per session (`steps = get_trace()` at `loops_anidados_marimo.py:200`).
- UI inputs (`mo.ui.dictionary`, `mo.ui.number`, `mo.ui.slider`, `mo.ui.button`).

## Naming Conventions

- State pair: `get_<name>, set_<name>`. Example: `get_step, set_step`.
- UI dictionary: `ui_dict` (`formula_simulation.py:37`).
- Buttons: `prev_btn`, `next_btn`, `reset_btn` (`loops_anidados_marimo.py:278-297`).
- Unused callback argument: `_`.

## Common Mistakes

- Forgetting `allow_self_loops=True` when a setter callback reads current state.
- Reading state without calling the getter. `get_step` without `()` passes the function, not the value.
- Letting the slider or buttons move the index outside `0..len(steps)-1`. Clamp in every controller.
