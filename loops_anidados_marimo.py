# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo>=0.24.2",
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

Opción A — con uv (recomendado, instala dependencias automáticamente):
   uv run marimo edit loops_anidados_marimo.py

Opción B — con python y pip (pasos manuales):
   1. Asegúrate de tener Python 3.11 o superior instalado.
      Verificá tu versión con:
         python --version
      Si obtenés "Python 3.11.x" o mayor, estás listo.

   2. (Opcional pero recomendado) Creá un entorno virtual para no
      instalar paquetes de forma global en tu sistema:
         python -m venv .venv

      Activá el entorno virtual:
         • En macOS / Linux:   source .venv/bin/activate
         • En Windows:         .venv\Scripts\activate

      Para salir del entorno virtual cuando termines:
         deactivate

   3. Instalá marimo con pip:
         pip install "marimo>=0.24.2"

   4. Ejecutá el notebook en modo edición:
         marimo edit loops_anidados_marimo.py

      O en modo solo lectura (sin poder editar el código):
         marimo run loops_anidados_marimo.py

   5. Se abrirá una pestaña en tu navegador con la aplicación.
      Usá los controles (Anterior / Siguiente) para navegar
      por la ejecución paso a paso.
"""

import marimo

__generated_with = "0.24.2"
app = marimo.App(width="full")

 # @app.cell es un decorator. Los decorators nos permiten modificar o mejorar una función o método. 
 # Son una forma de agregar funcionalidad a una función o método sin cambiar su código. 
 # Por ejemplo, @app.cell hace que la función sea una celda en marimo.
 # Son un concepto avanzado de python que veremos mas adelante. No se preocupen si no lo entienden
@app.cell
def _():
    """
    Importamos la librería marimo. 'mo' es el alias estándar que nos da 
    acceso a todas las herramientas interactivas y de diseño visual.
    """
    # "Traigo" toda la funcionalidad de la librería mo, que está dentro de marimo
    # "mo" va a ser nuestra caja negra de herramientas para generar código marimo 
    import marimo as mo

    # Para el que necesite usar marimo, lo traje y lo dejo disponible, para que lo use en sus celdas
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
    pasos_llenado = 4 # Variable que indica en cuantos pasos se va a llenar cada botella. Es decir, que el for interno vai a dar 4 vueltas por cada vuelta que de el for externo. Es decir, 4 pasos de llenado por cada botella.
    
    def get_trace():
        """
        Simula la ejecución de los bucles anidados "en cámara lenta" y va
        anotando (guardando en una lista) cómo se ve el sistema en cada
        momento importante:

        - En el arranque (los snapshots iniciales).
        - En cada vuelta del bucle EXTERIOR (cuando empezamos con cada botella).
        - En cada vuelta del bucle INTERIOR (cada paso de llenado y su cálculo).
        - Al final, cuando ya se llenaron todas las botellas.

        Esas anotaciones son los "pasos" de la traza: gracias a ellas, el
        visualizador puede mostrar la ejecución sin tener que volver a
        ejecutar el código real.

        ¿Qué es una "traza"?
        --------------------
        Una traza es un registro (una lista) con TODOS los pasos que dio el
        programa, como si le hubiéramos puesto una cámara al código.
        Cada paso guarda una "foto" de cómo estaban las variables en ese
        momento exacto. Después, el visualizador solo tiene que reproducir
        esas fotos en orden (como un video) para mostrar la ejecución paso
        a paso, tanto hacia delante como hacia atrás.

        Formato de cada paso (un diccionario):
            {
                "line": 8,          # línea del código didáctico que se está ejecutando
                "i": 1,             # botella actual (variable del bucle exterior)
                "j": 2,             # paso de llenado actual (variable del bucle interior)
                "nivel": 50.0,      # porcentaje de llenado de la botella (0 a 100)
                "msg": "Calculando nivel: 50.0%",  # mensaje que se muestra en la consola
                "bottle_idx": 1     # índice de la botella activa (-1 = ninguna todavía)
            }

        ¿Por qué -1 en bottle_idx?
        --------------------------
        Los pasos iniciales y finales no pertenecen a ninguna botella, así que
        usamos -1 como "valor centinela" para decirle al programa que en ese
        paso no hay ninguna botella activa.

        Retorna:
            list: Una secuencia de diccionarios (los "pasos"). Esta lista es lo
                  que permite que el visualizador pueda "viajar en el tiempo"
                  (atrás y adelante) sin volver a ejecutar el bucle real.
        """
        # Esta lista almacenará los 'snapshots' de memoria de cada momento del programa.    
        # Es lo que permite que el visualizador pueda 'viajar en el tiempo' (atrás y adelante).
        trace = [] # Es una lista

        # Snapshot inicial
        trace.append({
            "line": 1, 
            "i": None, 
            "j": None, 
            "nivel": 0, 
            "msg": "Inicializando...", 
            "bottle_idx": -1
        })

        trace.append({
            "line": 2, 
            "i": None, 
            "j": None, 
            "nivel": 0, 
            "msg": "Configurando pasos...", 
            "bottle_idx": -1
        })
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
                trace.append({"line": 9, "i": i, "j": j, "nivel": nivel, "msg": f"Botella {i} / Paso {j}: {nivel:.1f}%", "bottle_idx": i})

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
    # mo.state es la "memoria" de Marimo: 
    # get_step lee el contenido (el paso actual)
    # set_step cambia el contenido (el paso actual)
    # allow_self_loops=True permite que la función set_step reciba como argumento el valor actual de la variable.
    # 0 es el valor inicial de la variable.
    get_step, set_step = mo.state(0, allow_self_loops=True)
    return get_step, set_step


@app.cell
def _(get_step, mo, set_step, steps):
    """
    INTERFAZ DE CONTROL: Creamos los botones y el slider para que el usuario
    pueda navegar por los bucles (Anterior, Siguiente, Reiniciar).
    """
    # Definimos la interfaz de control: botones y slider que actualizan el estado.

    def increment(_):
        """
        Avanza la simulación al siguiente paso (botón "Siguiente ➡️").

        Esta función es el "controlador" del botón Siguiente: marimo la
        llama automáticamente cuando el usuario hace clic, pasándole el
        evento en `_`. Usamos el guion bajo como nombre del parámetro como
        convención para decir "recibo este valor pero no me interesa usarlo".

        Lo que hace por dentro:
            - Le pide al estado (set_step) que calcule el nuevo paso.
            - La lambda `lambda v: v + 1 if v < len(steps) - 1 else v`
              significa:
                * Si todavía no estamos en el último paso
                  (v < len(steps) - 1), avanzamos uno: v + 1.
                * Si ya estamos en el último, nos quedamos en el mismo (v),
                  para que el índice nunca se salga de la lista `steps`.
        """
        set_step(lambda v: v + 1 if v < len(steps) - 1 else v)

    def decrement(_):
        """
        Retrocede la simulación al paso anterior (botón "Anterior ⬅️").

        Es el "controlador" del botón Anterior y funciona como un espejo
        de `increment`: en lugar de sumar, resta.

        Lo que hace por dentro:
            - Le pide al estado (set_step) que calcule el nuevo paso.
            - La lambda `lambda v: v - 1 if v > 0 else v` significa:
                * Si todavía no estamos en el primer paso (v > 0),
                  retrocedemos uno: v - 1.
                * Si ya estamos en el paso 0 (el inicial), nos quedamos,
                  para no ir a un índice negativo (que no existe).
        """
        set_step(lambda v: v - 1 if v > 0 else v)

    def reset(_):
        """
        Reinicia la simulación volviendo al paso 0 (botón "Reiniciar 🔄").

        A diferencia de `increment` y `decrement`, no necesita calcular
        nada: le ordena al estado (set_step) que vuelva al valor inicial 0,
        que es el "Snapshot inicial" de la traza (el primero de la lista).
        """
        set_step(0)

    # Botón para retroceder al paso anterior.
    # Usa la funcion decrement(), definida mas arriba, que recibe el clic y decide el nuevo paso.
    # Se deshabilita el botón cuando el paso actual es 0.
    prev_btn = mo.ui.button(
        label="⬅️ Anterior", 
        on_click=decrement, 
        disabled=get_step() == 0,
        kind="neutral"
    )

    # Botón para avanzar al paso siguiente.
    # Usa la funcion increment(), definida mas arriba, que recibe el clic y decide el nuevo paso.
    # Se deshabilita el botón cuando el paso actual es el último.
    next_btn = mo.ui.button(
        label="Siguiente ➡️", 
        on_click=increment, 
        disabled=get_step() == len(steps) - 1, 
        kind="success"
    )

    # Botón para reiniciar el visualizador.
    # Usa la funcion reset(), definida mas arriba, que vuelve al paso 0 sin calcular nada.
    reset_btn = mo.ui.button(label="🔄 Reiniciar", on_click=reset)

    # Control deslizante para avanzar y retroceder en el bucle.
    # El rango es desde 0 hasta la cantidad total de pasos menos 1.
    # El valor inicial es el paso actual (get_step()).
    # El evento on_change llama a set_step con el nuevo valor.
    slider = mo.ui.slider(0, len(steps) - 1, value=get_step(), on_change=set_step, label="Pasos")

    # Agrupamos todos los controles en una fila.
    controls = mo.hstack([prev_btn, next_btn, reset_btn, slider], justify="start")
    return (controls,)


@app.cell(hide_code=True)
def _():
    """
    🎨 PLANTILLAS HTML (la "caja negra" de la interfaz)

    Acá está agrupado TODO el HTML del visualizador, separado de la lógica
    Python. Cada plantilla es un string con "huecos" {campo} que se rellenan
    después con .replace() desde la celda de visualización.

    ¿Por qué .replace() y no .format()? Porque el contenido que guardamos en
    los huecos puede traer llaves { } propias del código didáctico (por
    ejemplo f'Botella {i}: {nivel}%') y .format() las interpretaría como
    huecos nuevos, dando error. .replace() busca el texto exacto del hueco
    y lo cambia, sin interpretar nada más.

    Idea didáctica: podés tomar esta celda como una "caja negra gráfica".
    Hace falta entender qué dibuja cada plantilla a grandes rasgos (una
    botella, la consola, el visor de código), pero no el detalle de cada
    estilo. El HTML dibuja la "pantalla"; el Python es la "lógica".
    """
    # Plantilla de UNA línea del visor de código.
    # Huecos: {bg} color de fondo, {color} borde izquierdo, {opacity} transparencia,
    #         {idx} número de línea, {line} texto del código.
    PLANTILLA_LINEA_CODIGO = (
        "<div style='background: {bg}; border-left: 4px solid {color};"
        " padding: 2px 10px; opacity: {opacity}; white-space: pre;'>"
        "{idx}: {line}</div>"
    )

    # Plantilla del recuadro oscuro que contiene todas las líneas del visor.
    # Hueco: {lineas} las líneas ya armadas y unidas.
    PLANTILLA_CAJA_CODIGO = (
        "<div style='font-family: \"JetBrains Mono\", monospace;"
        " background: midnightblue; color: white; padding: 15px;"
        " border-radius: 8px; border: 1px solid steelblue;'>"
        "{lineas}</div>"
    )

    # Plantilla de UNA botella con su nivel de líquido.
    # Huecos: {border_color} color del borde, {glow} brillo (o vacío),
    #         {lvl} porcentaje de llenado, {idx} número de botella.
    PLANTILLA_BOTELLA = """
    <div style="display: flex; flex-direction: column; align-items: center; width: 60px;">
        <div style="position: relative; height: 160px; width: 50px; border: 3px solid {border_color}; {glow} border-top: none; border-radius: 0 0 8px 8px; background: red; overflow: hidden;">
            <div style="position: absolute; bottom: 0; left: 0; width: 100%; height: {lvl}%; background: linear-gradient(to top, teal, skyblue); transition: height 0.3s ease;"></div>
        </div>
        <span style="margin-top: 8px; font-size: 12px; color: {border_color}; font-weight: bold;">B{idx}</span>
    </div>
    """

    # Plantilla del contenedor que agrupa todas las botellas en una fila.
    # Hueco: {botellas} las botellas ya armadas y unidas.
    PLANTILLA_FILA_BOTELLAS = """
    <div style="display: flex; gap: 30px; justify-content: center; padding: 20px; background: black; border-radius: 12px; border: 1px solid slategray;">
        {botellas}
    </div>
    """

    # Plantilla del recuadro de consola (la "terminal" del programa simulado).
    # Hueco: {lineas} los mensajes ya unidos y con formato de prompt.
    PLANTILLA_CONSOLA = """
    <div style="background: black; color: lime; font-family: monospace; padding: 10px; height: 250px; overflow-y: auto; border: 1px solid slategray; border-radius: 6px; font-size: 13px;">
        {lineas}
    </div>
    """
    return (
        PLANTILLA_BOTELLA,
        PLANTILLA_CAJA_CODIGO,
        PLANTILLA_CONSOLA,
        PLANTILLA_FILA_BOTELLAS,
        PLANTILLA_LINEA_CODIGO,
    )


@app.cell
def _(
    CANT_BOTELLAS,
    PLANTILLA_BOTELLA,
    PLANTILLA_CAJA_CODIGO,
    PLANTILLA_CONSOLA,
    PLANTILLA_FILA_BOTELLAS,
    PLANTILLA_LINEA_CODIGO,
    controls,
    get_step,
    mo,
    pasos_llenado,
    steps,
):
    """
    VISUALIZACIÓN PRINCIPAL: Esta es la celda que 'cobra vida'. 
    Toma el paso actual y renderiza el código resaltado, las botellas y la consola.

    ¿Cómo se dispara? (reactividad de marimo)
    -----------------------------------------
    En marimo, cada celda es una función cuyos parámetros son sus DEPENDENCIAS.
    Esta celda recibe `get_step` (la forma de LEER el estado) y su primera
    línea es current_idx = get_step(). Con eso, marimo deduce:

        "Esta celda necesita saber cuál es el paso actual."

    Cuando el usuario hace clic en un botón (o mueve el slider), ese control
    llama a set_step(...), que es la forma de ESCRIBIR el estado. Al cambiar
    ese valor, marimo detecta el cambio y vuelve a ejecutar automáticamente
    SOLO las celdas que dependen de ese estado — incluida esta. No hace falta
    ningún "refrescar" manual: el notebook se entera solo. A eso se llama
    reactividad.

    La secuencia completa, paso a paso:

        1. Clic en "Siguiente ➡️" (o Anterior ⬅️ / Reiniciar 🔄 / slider)
        2. Se llama a set_step(nuevo_valor)  ->  cambia el estado
        3. marimo detecta el cambio de estado
        4. Re-ejecuta esta celda (y las demás que lean get_step)
        5. current_idx toma el nuevo valor y todo se re-renderiza

    Esa es la gran diferencia con un script Python común: el "orden" no lo
    decide la secuencia de líneas del archivo, sino el grafo de dependencias
    que marimo arma mirando los parámetros de cada celda.

    De dónde sale cada parámetro:
        - get_step       -> de la celda de estado reactivo (lectura del paso).
        - controls       -> de la celda de controles (botones y slider).
        - steps          -> de la celda de simulación (la traza completa).
        - PLANTILLA_*    -> de la celda de plantillas HTML (el "molde" visual).
    """
    # Primera línea de la celda: LEER el paso actual con get_step().
    # Al llamar a get_step() acá, marimo registra que esta celda DEPENDE del
    # estado "paso". Cuando set_step(...) lo cambie (botones o slider), marimo
    # volverá a ejecutar esta celda sola, sin tocar el resto del notebook.
    current_idx = get_step()
    # Con el paso en mano, buscamos su "foto" (snapshot) dentro de la traza.
    # steps es la lista completa que armó get_trace() en la celda de simulación.
    current = steps[current_idx]

    def resaltar_codigo(current_line):
        """
        Dibuja el "visor de código" (el recuadro oscuro) y resalta la línea
        que se está ejecutando en el paso actual de la simulación.

        Parámetros:
            current_line (int): Número de línea que debe quedar resaltada.
                                Por convención, la traza usa -1 para indicar
                                "fin de la ejecución": en ese caso ninguna
                                línea queda resaltada.

        ¿Cómo funciona por dentro?
        -------------------------
        1. Crea `code_lines`: una lista con el código "didáctico" que vemos
           en la pantalla (NO es el código real de este archivo, sino una
           versión simplificada preparada para la clase).
        2. Recorre esa lista con `enumerate(code_lines, 1)`: en cada vuelta
           obtiene el número de línea (idx) y el texto de la línea (line).
           El "1" indica que la cuenta empieza en 1 (y no en 0, como haría
           la función por defecto).
        3. Decide, línea por línea, si es la línea actual y elige el estilo:
           verde + fondo celeste + opacidad total si lo es; rojo +
           transparente + opacidad media si no lo es.
        4. Usa la PLANTILLA_LINEA_CODIGO (definida en la celda de plantillas)
           para envolver cada línea en una mini-capa HTML (<div>) y une todas
           con "".join(styled_lines), formando un único bloque de HTML.
        5. Por último, envuelve el bloque con PLANTILLA_CAJA_CODIGO y
           mo.Html(...) para que marimo lo muestre como HTML real en el
           navegador.

        Retorna:
            mo.Html: El bloque HTML listo para renderizar en la celda.
                     Como es un objeto de marimo, la celda lo muestra
                     automáticamente como parte del output.
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
            "        print(f'Botella {i} / Paso{j}: {nivel}%')",
            "",
            "print('¡Proceso finalizado!')"
        ]

        # Se define una lista con cada una de las líneas del código.
        # A diferencia de code_lines, styled_lines es una lista de strings que representan el código HTML.
        # o sea, una representacion del codigo con estilos aplicados para ser mostrada en el navegador.
        # Cada string contiene el número de línea, el código y el estilo de la línea.
        styled_lines = []
        # enumerate devuelve el índice (idx) y el elemento (line) de la lista code_lines.
        # en este caso el indice es el numero de linea y el elemento es el codigo de la linea
        for idx, line in enumerate(code_lines, 1):
            # Se define el color de la línea vertical de la izquierda del código. Color cyan si es la línea actual, transparente si no.
            color = "green" if idx == current_line else "red"
            # Se define el color de fondo de la línea. Color cyan si es la línea actual, transparente si no.
            bg = "rgba(14, 165, 233, 0.15)" if idx == current_line else "transparent"
            # Se define la opacidad de la línea. 1 si es la línea actual, 0.5 si no.
            opacity = "1" if idx == current_line else "0.5"
            # Se agrega la línea a la lista usando la plantilla HTML.
            # Usamos .replace() (y no .format()) porque el texto de la línea
            # puede traer llaves { } propias del código didáctico (por ejemplo
            # f'Botella {i}: {nivel}%') y .format() las interpretaría como
            # huecos nuevos. .replace() cambia el texto exacto del hueco y no
            # interpreta nada más.
            styled_lines.append(
                PLANTILLA_LINEA_CODIGO
                .replace("{bg}", bg)
                .replace("{color}", color)
                .replace("{opacity}", opacity)
                .replace("{idx}", str(idx))
                .replace("{line}", line)  # siempre por último: line puede contener { }
            )

        # Renderiza el código resaltado usando la plantilla de la caja oscura.
        # El HTML en sí vive en la celda de plantillas; acá solo rellenamos los
        # huecos con .replace() y envolvemos el resultado en mo.Html(...)
        # para que marimo lo muestre en el navegador.
        return mo.Html(
            PLANTILLA_CAJA_CODIGO.replace("{lineas}", "".join(styled_lines))
        )

    # Visualization Logic
    # Lógica de Visualización: Calcula los niveles de las botellas hasta el paso actual.
    levels = [0, 0, 0]
    for s in range(current_idx):
        st = steps[s]
        if st['bottle_idx'] != -1 and st['line'] >= 8:
            levels[st['bottle_idx']] = st['nivel']

    def dibujar_botella(idx, lvl, active):
        """
        Dibuja UNA botella con su nivel de llenado actual y la devuelve como
        un bloque de HTML (todavía como string, sin envolver en mo.Html).

        Esta función se llama una vez por botella. El contenedor que las
        agrupa en fila se arma en la celda principal, uniendo el resultado
        de cada llamada con "".join(...).

        Parámetros:
            idx (int): Índice (posición) de la botella: 0, 1 o 2.
                       Se usa para la etiqueta "B0", "B1", "B2".
            lvl (float): Nivel de llenado en porcentaje (0 = vacía, 100 = llena).
                         Se convierte en la altura del "líquido" dentro de la botella.
            active (bool): True si esta botella es la que se está llenando en el
                           paso actual. Si es True, el borde se pinta de verde
                           y se agrega un brillo (glow); si es False, el borde
                           queda rojo y sin brillo.

        ¿Cómo logra el efecto de llenado?
        ---------------------------------
        El "líquido" es una capa (div) posicionada en el fondo de la botella
        con altura height: {lvl}% y una transición CSS de 0.3 segundos, así
        el cambio de nivel se suaviza en lugar de aparecer de golpe.

        Retorna:
            str: El bloque de HTML de UNA botella, listo para ser unido con
                 los bloques de las demás. El HTML en sí vive en la plantilla
                 PLANTILLA_BOTELLA (celda de plantillas); acá solo calculamos
                 los valores y los rellenamos con .replace(...).
        """
        # Si la botella está activa, el borde es de color teal y tiene un glow
        # Si la botella no está activa, el borde es de color gris y no tiene un glow
        border_color = "yellow" if active else "red"
        # El glow es una sombra que se aplica a la botella
        glow = "box-shadow: 0 0 15px rgba(20, 184, 166, 0.4);" if active else ""
        # Rellenamos la plantilla de la botella con los valores calculados.
        # .replace() cambia cada {hueco} por su valor (igual que una f-string,
        # pero la plantilla queda separada de la lógica Python).
        return (
            PLANTILLA_BOTELLA
            .replace("{border_color}", border_color)
            .replace("{glow}", glow)
            .replace("{lvl}", str(lvl))
            .replace("{idx}", str(idx))
        )
    # Renderiza las botellas en una fila.
    # La expresión de adentro es una COMPRENSIÓN DE LISTA (list comprehension):
    #   [dibujar_botella(i, levels[i], current['bottle_idx'] == i) for i in range(CANT_BOTELLAS)]
    # Recorre i = 0, 1, 2 y, por cada botella, llama a dibujar_botella(...) pasándole:
    #   - i: la posición de la botella (0, 1 o 2).
    #   - levels[i]: su nivel de llenado actual (calculado en el bucle de arriba).
    #   - current['bottle_idx'] == i: True si esta botella es la activa en el paso actual.
    # El resultado es una lista de strings HTML que "pegamos" con "".join(...)
    # para formar una sola fila adentro del contenedor flex.
    # NOTA: usamos la constante CANT_BOTELLAS (no un 3 fijo) para que, si algún
    # día la cambiamos, las botellas se ajusten solas.
    bottles = mo.Html(
        PLANTILLA_FILA_BOTELLAS.replace(
            "{botellas}",
            "".join([
                dibujar_botella(i, levels[i], current['bottle_idx'] == i)
                for i in range(CANT_BOTELLAS)
            ])
        )
    )

    # Renderiza la consola (la "pantalla" del programa simulado).
    # console_msgs es una comprensión de lista que recorre SOLO los pasos ya
    # ejecutados (range(current_idx)) y se queda con los mensajes de las líneas
    # que "imprimen en pantalla" (line 9: el print de cada nivel; line 11: el
    # print final). El resultado es una lista con los mensajes, en orden.
    console_msgs = [steps[s]['msg'] for s in range(current_idx) if steps[s]['line'] in [9, 11]]
    # "' > ' + '<br>> '.join(console_msgs)" une todos los mensajes con un salto
    # de línea (<br>) y les antepone "> " para que parezcan una terminal real.
    # Si todavía no hay mensajes, mostramos "> Iniciando sistema...".
    # Renderiza la consola usando la plantilla PLANTILLA_CONSOLA.
    # Como la plantilla ya trae todo el HTML, acá solo armamos el contenido
    # (la línea de texto que va adentro) y se lo pasamos a .replace(...).
    console = mo.Html(
        PLANTILLA_CONSOLA.replace(
            "{lineas}",
            '> ' + '<br>> '.join(console_msgs) if console_msgs else '> Iniciando sistema...'
        )
    )

    # Layout final: armamos la página completa combinando los bloques de arriba.
    #   mo.hstack(...) -> apila elementos en FILA    (horizontal)
    #   mo.vstack(...) -> apila elementos en COLUMNA (vertical)
    # Columna izquierda: el panel de control y debug (controles, snapshot y
    # el visor de código resaltado).
    # Columna derecha: el estado de las botellas y la consola.
    # Cada vez que el usuario cambia el paso, esta celda se vuelve a ejecutar
    # sola porque usa get_step() al principio; marimo detecta que el estado
    # cambió y re-renderiza todo automáticamente (reactividad).
    ui = mo.hstack([
        mo.vstack([
            mo.md("### 🕹️ Control & Debug"),
            controls,
            mo.md(f"**Snapshot:** {current_idx} / {len(steps)-1}"),
            resaltar_codigo(current['line'])
        ], align="stretch"),
        mo.vstack([
            mo.md("### 📊 Estado de Botellas"),
            bottles,
            mo.md("### 📟 Salida Consolar"),
            console
        ], align="stretch")
    ], justify="space-around", gap=2)

    ui # Esta es la instruccion para que Marimo muestre el resultado de la celda, es equivalente a un print
    return


# Esta es la instruccion para que Marimo ejecute la aplicacion
# Lo que hace es ejecutar la funcion app.run()
if __name__ == "__main__": # Esta convencion hace que el codigo se ejecute solo si el archivo se ejecuta como script standalone
    app.run()
