# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo",
# ]
# ///

import marimo

__generated_with = "0.23.0"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    # 🧪 Visualizador de Bucles Reactivo
    Explora cómo funcionan los bucles anidados paso a paso con la reactividad de **marimo**.
    """)
    return


@app.cell
def _():
    def get_trace():
        botellas = 3
        pasos_llenado = 3
        trace = []

        # Snapshot inicial
        trace.append({"line": 1, "i": None, "j": None, "nivel": 0, "msg": "Inicializando...", "bottle_idx": -1})
        trace.append({"line": 2, "i": None, "j": None, "nivel": 0, "msg": "Configurando pasos...", "bottle_idx": -1})

        for i in range(botellas):
            trace.append({"line": 5, "i": i, "j": None, "nivel": 0, "msg": f"Iniciando Botella {i}", "bottle_idx": i})
            for j in range(1, pasos_llenado + 1):
                trace.append({"line": 7, "i": i, "j": j, "nivel": 0, "msg": f"Preparando llenado {j}...", "bottle_idx": i})
                nivel = (j / pasos_llenado) * 100
                trace.append({"line": 8, "i": i, "j": j, "nivel": nivel, "msg": f"Calculando nivel: {nivel:.1f}%", "bottle_idx": i})
                trace.append({"line": 9, "i": i, "j": j, "nivel": nivel, "msg": f"Botella {i}: {nivel:.1f}%", "bottle_idx": i})

        trace.append({"line": 11, "i": None, "j": None, "nivel": 100, "msg": "¡Proceso finalizado!", "bottle_idx": -1})
        # Paso extra para que se vea el efecto del último print en el debugger
        trace.append({"line": -1, "i": None, "j": None, "nivel": 100, "msg": "--- Ejecución terminada ---", "bottle_idx": -1})
        return trace

    steps = get_trace()
    return (steps,)


@app.cell
def _(mo):
    get_step, set_step = mo.state(0, allow_self_loops=True)
    return get_step, set_step


@app.cell
def _(get_step, mo, set_step, steps):

    def increment(_):
        set_step(lambda v: v + 1 if v < len(steps) - 1 else v)

    def decrement(_):
        set_step(lambda v: v - 1 if v > 0 else v)

    def reset(_):
        set_step(0)

    prev_btn = mo.ui.button(
        label="⬅️ Anterior", 
        on_click=lambda _: set_step(lambda v: v - 1 if v > 0 else v), 
        disabled=get_step() == 0,
        kind="neutral"
    )
    next_btn = mo.ui.button(
        label="Siguiente ➡️", 
        on_click=lambda _: set_step(lambda v: v + 1 if v < len(steps) - 1 else v), 
        disabled=get_step() == len(steps) - 1, 
        kind="success"
    )
    reset_btn = mo.ui.button(label="🔄 Reiniciar", on_click=lambda _: set_step(0))

    slider = mo.ui.slider(0, len(steps) - 1, value=get_step(), on_change=set_step, label="Pasos")

    controls = mo.hstack([prev_btn, next_btn, reset_btn, slider], justify="start")
    return (controls,)


@app.cell
def _(controls, get_step, mo, steps):
    current_idx = get_step()
    current = steps[current_idx]

    def highlight_code(current_line):
        code_lines = [
            "botellas = 3",
            "pasos_llenado = 3",
            "",
            "# Bucle exterior: cada botella",
            "for i in range(botellas):",
            "    # Bucle interior",
            "    for j in range(1, pasos_llenado + 1):",
            "        nivel = (j / pasos_llenado) * 100",
            "        print(f'Botella {i}: {nivel}%')",
            "",
            "print('¡Proceso finalizado!')"
        ]

        styled_lines = []
        for idx, line in enumerate(code_lines, 1):
            color = "#0ea5e9" if idx == current_line else "transparent"
            bg = "rgba(14, 165, 233, 0.15)" if idx == current_line else "transparent"
            opacity = "1" if idx == current_line else "0.5"
            styled_lines.append(f"<div style='background: {bg}; border-left: 4px solid {color}; padding: 2px 10px; opacity: {opacity}; white-space: pre;'>{idx}: {line}</div>")

        return mo.Html(f"<div style='font-family: \"JetBrains Mono\", monospace; background: #0f172a; color: #f8fafc; padding: 15px; border-radius: 8px; border: 1px solid #1e293b;'>{''.join(styled_lines)}</div>")

    # Visualization Logic
    levels = [0, 0, 0]
    for s in range(current_idx):
        st = steps[s]
        if st['bottle_idx'] != -1 and st['line'] >= 8:
            levels[st['bottle_idx']] = st['nivel']

    def render_bottle(idx, lvl, active):
        border_color = "#14b8a6" if active else "#475569"
        glow = "box-shadow: 0 0 15px rgba(20, 184, 166, 0.4);" if active else ""
        return f"""
        <div style="display: flex; flex-direction: column; align-items: center; width: 60px;">
            <div style="position: relative; height: 160px; width: 50px; border: 3px solid {border_color}; {glow} border-top: none; border-radius: 0 0 8px 8px; background: #1e293b; overflow: hidden;">
                <div style="position: absolute; bottom: 0; left: 0; width: 100%; height: {lvl}%; background: linear-gradient(to top, #14b8a6, #38bdf8); transition: height 0.3s ease;"></div>
            </div>
            <span style="margin-top: 8px; font-size: 12px; color: {border_color}; font-weight: bold;">B{idx}</span>
        </div>
        """

    bottles = mo.Html(f"""
    <div style="display: flex; gap: 30px; justify-content: center; padding: 20px; background: #020617; border-radius: 12px; border: 1px solid #1e293b;">
        {"".join([render_bottle(i, levels[i], current['bottle_idx'] == i) for i in range(3)])}
    </div>
    """)

    # Console
    console_msgs = [steps[s]['msg'] for s in range(current_idx) if steps[s]['line'] in [9, 11]]
    console = mo.Html(f"""
    <div style="background: #000; color: #10b981; font-family: monospace; padding: 10px; height: 250px; overflow-y: auto; border: 1px solid #1e293b; border-radius: 6px; font-size: 13px;">
        {'> ' + '<br>> '.join(console_msgs) if console_msgs else '> Iniciando sistema...'}
    </div>
    """)

    # Layout
    ui = mo.hstack([
        mo.vstack([
            mo.md("### 🕹️ Control & Debug"),
            controls,
            mo.md(f"**Snapshot:** {current_idx} / {len(steps)-1}"),
            highlight_code(current['line'])
        ], align="stretch"),
        mo.vstack([
            mo.md("### 📊 Estado de Botellas"),
            bottles,
            mo.md("### 📟 Salida Console"),
            console
        ], align="stretch")
    ], justify="space-around", gap=2)

    ui
    return


if __name__ == "__main__":
    app.run()
