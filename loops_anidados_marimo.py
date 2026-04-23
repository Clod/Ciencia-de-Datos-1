# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo>=0.23.2",
# ]
# ///

"""
📊 VISUALIZADOR DE BUCLES ANIDADOS (MARIMO)
=========================================

Propósito:
----------
Esta es una herramienta educativa diseñada para ayudar a estudiantes principiantes de 
Python a visualizar el funcionamiento de los bucles anidados (un bucle dentro de otro).

Simulación:
-----------
- Bucle Exterior: Representa cada una de las 3 botellas.
- Bucle Interior: Representa los pasos de llenado de cada botella individual.

Cómo ejecutar:
--------------
1. Asegúrate de tener instalado Python 3.11+ y marimo.
2. Ejecuta el siguiente comando en tu terminal:
   uv run marimo edit loops_anidados_marimo.py
3. Usa los controles (Anterior/Siguiente) para navegar por la ejecución paso a paso.
"""

import marimo

__generated_with = "0.23.2"
app = marimo.App(width="full")


@app.cell
def _():
    """
    Importamos la librería marimo. 'mo' es el alias estándar que nos da 
    acceso a todas las herramientas interactivas y de diseño visual.
    """
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    """Aquí usamos Markdown para mostrar el título y la presentación del ejercicio."""
    mo.md("""
    # 🧪 Visualizador de Bucles Reactivo
    Explora cómo funcionan los bucles anidados paso a paso con la reactividad de **marimo**.
    """)
    return


@app.cell
def _():
    """
    SIMULACIÓN: Esta celda pre-calcula toda la ejecución del bucle. 
    Creamos una 'traza' (trace) con cada paso para que el sistema sepa 
    exactamente qué mostrar en cada momento del tiempo.
    """
    # Definimos las variables a nivel de celda para que sean "globales" en el notebook
    CANT_BOTELLAS = 3 # Variable "constante" (escrita en mayúsculas para indicar que no debe cambiar)
    pasos_llenado = 2

    def get_trace():
        """
        Simula la ejecución de los bucles anidados y captura el estado del sistema 
        en cada punto crítico (iteraciones, cálculos y finalización).

        Retorna:
            list: Una secuencia de diccionarios, donde cada uno representa un 'paso' 
                  con la línea de código actual, valores de i y j, nivel de llenado y mensaje.

        En este caso, las claves del diccionario son:
            line: número de línea del código que se está ejecutando
            i: valor de la variable i en ese momento (índice del bucle exterior que recorre la cantidad de botellas)
            j: valor de la variable j en ese momento (índice del bucle interior que recorre los pasos de llenado)
            nivel: valor de la variable nivel en ese momento (porcentaje de llenado de la botella)
            msg: mensaje que se está mostrando en la consola
            bottle_idx: índice de la botella que se está llenando
        """
        # Esta lista almacenará los 'snapshots' de memoria de cada momento del programa.    
        # Es lo que permite que el visualizador pueda 'viajar en el tiempo' (atrás y adelante).
        trace = [] # Es una lista

        # Snapshot inicial
        trace.append({"line": 1, "i": None, "j": None, "nivel": 0, "msg": "Inicializando...", "bottle_idx": -1})
        trace.append({"line": 2, "i": None, "j": None, "nivel": 0, "msg": "Configurando pasos...", "bottle_idx": -1})
        # Notar que cada elemento de la lista es, a su vez, un diccionario
        # con claves que representan el estado de las variables en ese momento.
        # line: número de línea del código que se está ejecutando
        # i: valor de la variable i en ese momento
        # j: valor de la variable j en ese momento
        # nivel: valor de la variable nivel en ese momento
        # msg: mensaje que se está mostrando
        # bottle_idx: índice de la botella que se está llenando

        # Bucle exterior: cada botella
        for i in range(CANT_BOTELLAS):
            # Me guardo que empiezo a trabajar con la botella i
            trace.append({"line": 5, "i": i, "j": None, "nivel": 0, "msg": f"Iniciando Botella {i}", "bottle_idx": i})
            # Bucle interior: cada paso de llenado de cada botella
            for j in range(1, pasos_llenado + 1):
                # Me guardo que empiezo a trabajar con el paso j de la botella i
                trace.append({"line": 7, "i": i, "j": j, "nivel": 0, "msg": f"Preparando llenado {j}...", "bottle_idx": i})
                nivel = (j / pasos_llenado) * 100
                # Me guardo que calculé el nivel de la botella i
                trace.append({"line": 8, "i": i, "j": j, "nivel": nivel, "msg": f"Calculando nivel: {nivel:.1f}%", "bottle_idx": i})
                # Me guardo que muestro el nivel de la botella i
                trace.append({"line": 9, "i": i, "j": j, "nivel": nivel, "msg": f"Botella {i}: {nivel:.1f}%", "bottle_idx": i})

        trace.append({"line": 11, "i": None, "j": None, "nivel": 100, "msg": "¡Proceso finalizado!", "bottle_idx": -1})
        # Paso extra para que se vea el efecto del último print en el debugger
        trace.append({"line": -1, "i": None, "j": None, "nivel": 100, "msg": "--- Ejecución terminada ---", "bottle_idx": -1})
        return trace

    # Aca se ejecuta la funcion get_trace() y se guarda el resultado en la variable steps
    # Recordar que steps es una lista de diccionarios y que cada uno tiene las claves line, i, j, nivel, msg y bottle_idx
    steps = get_trace()
    return CANT_BOTELLAS, pasos_llenado, steps


@app.cell
def _(mo):
    """
    ESTADO REACTIVO: mo.state funciona como el cerebro del visualizador.
    Nos permite guardar en qué paso estamos y actualizar todo el sistema
    automáticamente cada vez que este número cambia.
    """
    # mo.state es la memoria de Marimo: get_step lee el paso actual, set_step lo cambia.
    # allow_self_loops=True permite que la función set_step reciba como argumento el valor actual de la variable.
    # En pocas palabras el estado es la memoria del sistema de marimo que nos permite saber en qué paso estamos.
    # get_step es una función que nos permite obtener el valor actual de la variable.
    # set_step es una función que nos permite establecer el valor actual de la variable.
    # 0 es el valor inicial de la variable.
    get_step, set_step = mo.state(0, allow_self_loops=True)
    return get_step, set_step


@app.cell(hide_code=True)
def _(get_step, mo, set_step, steps):
    """
    INTERFAZ DE CONTROL: Creamos los botones y el slider para que el usuario
    pueda navegar por los bucles (Anterior, Siguiente, Reiniciar).
    """
    # Definimos la interfaz de control: botones y slider que actualizan el estado.

    def increment(_):
        set_step(lambda v: v + 1 if v < len(steps) - 1 else v)

    def decrement(_):
        set_step(lambda v: v - 1 if v > 0 else v)

    def reset(_):
        set_step(0)

    # Botón para retroceder al paso anterior.
    # Se define una funcion lambda que llama a set_step con el valor anterior (v - 1).
    # Se deshabilita el botón cuando el paso actual es 0.
    prev_btn = mo.ui.button(
        label="⬅️ Anterior", 
        on_click=lambda _: set_step(lambda v: v - 1 if v > 0 else v), 
        disabled=get_step() == 0,
        kind="neutral"
    )

    # Botón para avanzar al paso siguiente.
    # Se define una funcion lambda que llama a set_step con el valor siguiente (v + 1).
    # Se deshabilita el botón cuando el paso actual es el último.
    next_btn = mo.ui.button(
        label="Siguiente ➡️", 
        on_click=lambda _: set_step(lambda v: v + 1 if v < len(steps) - 1 else v), 
        disabled=get_step() == len(steps) - 1, 
        kind="success"
    )

    # Botón para reiniciar el visualizador.
    # Se define una funcion lambda que llama a set_step con el valor 0.
    reset_btn = mo.ui.button(label="🔄 Reiniciar", on_click=lambda _: set_step(0))

    # Control deslizante para avanzar y retroceder en el bucle.
    # El rango es desde 0 hasta la cantidad total de pasos menos 1.
    # El valor inicial es el paso actual (get_step()).
    # El evento on_change llama a set_step con el nuevo valor.
    slider = mo.ui.slider(0, len(steps) - 1, value=get_step(), on_change=set_step, label="Pasos")

    # Agrupamos todos los controles en una fila.
    controls = mo.hstack([prev_btn, next_btn, reset_btn, slider], justify="start")
    return (controls,)


@app.cell(hide_code=True)
def _(CANT_BOTELLAS, controls, get_step, mo, pasos_llenado, steps):
    """
    VISUALIZACIÓN PRINCIPAL: Esta es la celda que 'cobra vida'. 
    Toma el paso actual y renderiza el código resaltado, las botellas y la consola.
    """
    # Celda principal de visualización: se refresca cada vez que el paso cambia.
    current_idx = get_step()
    # Accedemos al elemento i-ésimo del vector 
    current = steps[current_idx]

    def highlight_code(current_line):
        """
        Resalta la línea de código actual.
        """
        # Se define una lista con cada una de las líneas del código.
        # Usamos una lista porque es una coleccion ordenada de elementos.
        # Y cada elemento es una string que representa una línea del código.
        # No usamos diccionario para code_lines porque no tenemos pares clave-valor.
        code_lines = [
            f"botellas = {CANT_BOTELLAS}",
            f"pasos_llenado = {pasos_llenado}",
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

        # Se define una lista con cada una de las líneas del código.
        # A diferencia de code_lines, styled_lines es una lista de strings que representan el código HTML.
        # o sea, una representacion del codigo con estilos aplicados para ser mostrada en el navegador.
        # Cada string contiene el número de línea, el código y el estilo de la línea.
        styled_lines = []
        for idx, line in enumerate(code_lines, 1):
            # Se define el color de la línea vertical de la izquierda del código. Color cyan si es la línea actual, transparente si no.
            color = "green" if idx == current_line else "red"
            # Se define el color de fondo de la línea. Color cyan si es la línea actual, transparente si no.
            bg = "rgba(14, 165, 233, 0.15)" if idx == current_line else "transparent"
            # Se define la opacidad de la línea. 1 si es la línea actual, 0.5 si no.
            opacity = "1" if idx == current_line else "0.5"
            # Se agrega la línea a la lista de líneas estilizadas.
            styled_lines.append(f"<div style='background: {bg}; border-left: 4px solid {color}; padding: 2px 10px; opacity: {opacity}; white-space: pre;'>{idx}: {line}</div>")

        # Renderiza el código resaltado.
        # Para ello se utiliza la librería mo.Html y se le pasa como parámetro un string con el código HTML.
        # El string se construye con f-strings y se le pasa como parámetro un string con el código HTML.
        return mo.Html(f"<div style='font-family: \"JetBrains Mono\", monospace; background: midnightblue; color: white; padding: 15px; border-radius: 8px; border: 1px solid steelblue;'>{''.join(styled_lines)}</div>")

    # Visualization Logic
    # Lógica de Visualización: Calcula los niveles de las botellas hasta el paso actual.
    levels = [0, 0, 0]
    for s in range(current_idx):
        st = steps[s]
        if st['bottle_idx'] != -1 and st['line'] >= 8:
            levels[st['bottle_idx']] = st['nivel']

    def render_bottle(idx, lvl, active):
        """Renderiza una botella con el nivel especificado."""
        # Si la botella está activa, el borde es de color teal y tiene un glow
        # Si la botella no está activa, el borde es de color gris y no tiene un glow
        border_color = "teal" if active else "gray"
        # El glow es una sombra que se aplica a la botella
        glow = "box-shadow: 0 0 15px rgba(20, 184, 166, 0.4);" if active else ""
        # Renderiza una bottela con un contenedor de borde teal y fondo gris oscuro
        return f"""
        <div style="display: flex; flex-direction: column; align-items: center; width: 60px;">
            <div style="position: relative; height: 160px; width: 50px; border: 3px solid {border_color}; {glow} border-top: none; border-radius: 0 0 8px 8px; background: darkslategrey; overflow: hidden;">
                <div style="position: absolute; bottom: 0; left: 0; width: 100%; height: {lvl}%; background: linear-gradient(to top, teal, skyblue); transition: height 0.3s ease;"></div>
            </div>
            <span style="margin-top: 8px; font-size: 12px; color: {border_color}; font-weight: bold;">B{idx}</span>
        </div>
        """
    # Renderiza las botellas
    bottles = mo.Html(f"""
    <div style="display: flex; gap: 30px; justify-content: center; padding: 20px; background: black; border-radius: 12px; border: 1px solid slategray;">
        {"".join([render_bottle(i, levels[i], current['bottle_idx'] == i) for i in range(3)])}
    </div>
    """)

    # Renderiza la consola
    console_msgs = [steps[s]['msg'] for s in range(current_idx) if steps[s]['line'] in [9, 11]]
    console = mo.Html(f"""
    <div style="background: black; color: lime; font-family: monospace; padding: 10px; height: 250px; overflow-y: auto; border: 1px solid slategray; border-radius: 6px; font-size: 13px;">
        {'> ' + '<br>> '.join(console_msgs) if console_msgs else '> Iniciando sistema...'}
    </div>
    """)

    # Layout: dos columnas, la izquierda con el código y los controles, la derecha con las botellas y la consola
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
            mo.md("### 📟 Salida Consola"),
            console
        ], align="stretch")
    ], justify="space-around", gap=2)

    ui # Esta es la instruccion para que Marimo muestre el resultado de la celda, es equivalente a un print
    return

# Esta es la instruccion para que Marimo inicie la aplicacion
# Si no se incluye esta linea, no se ejecutara el codigo
# Y debemos asegurarnos que este debajo de la definicion de app
if __name__ == "__main__":
    app.run()
