El objetivo de es poner en práctica los conceptos que enseño el profe Román en las clases de un modo más visual que lo que permite la enseñaza de la teoría.

**La única pregunta tonta es la que no se formula**

 Vamos a usar Marimo que es una evolución de Jupyter notebooks 100% (Jupyter guarda en JSON)

La idea no es que entiendan todo al detalle. En general esto rara vez pasa. Uno casi siempre toca una partecita de algo más grande.  


Con el profe Román nos parece una herramienta muy potente y queríamos que la conocieran.

La idea es que tengan un programa ejecutable que les permita jugar haciendo modificaciones y viendo los efectos

Todo lo que es HTML puede ser considerado como una "caja girs". Es decir que lo puedo tomar como "caja negra" que genera un elemento gráfico

o pudeo modificarlo para ubicarme en la salida gráfica qué es lo que está dibujando. Para eso puse nombres de colores en lugar de códigos.

Conceptos que vamos a ver:

**Docstrings:** """Texto explicativo de lo que hace el código. Se puede poner en varias líneas"""

**Variables "constantes": **No es una regla, pero por convención se escriben en mayúsculas. 

**Diccionarios: **"cajitas" que guardan información en pares clave-valor.

**Listas:** Colecciones ordenadas de elementos.

**Funciones:** Bloques de código que realizan una tarea específica.

**Lambda:** Funciones anónimas. Se escriben en una sola línea. No las vimos todavía en clases pero lo importante es que entiendan que se usa de modo análogo a lo que vimos en clases.

**Forma estándar de definir una función**

def f(param1, param2):
    return param1+param2

**Forma compacta con lambda**

f = lambda param1, param2: param1+param2

En el visualizador usamos def para increment(), decrement() y reset(), y lambda solo para la actualización en set_step().


**Decorators: ** por ejemplo la línea @app.cell es un decorator. Pensemos que es una forma de agregarle funcionalidad a una función o método sin mostrar explícitamente en el código


**Bucles anidados**
  - Bucle exterior
  - Bucle interior
  - Variable contador
  - Variables de estado

Conceptos nuevos que fuimos agregando al visualizador:

**Comprensión de listas (list comprehension):** Forma compacta de construir una lista. Por ejemplo:

[f(x) for x in coleccion]

Es equivalente a:

resultado = []
for x in coleccion:
    resultado.append(f(x))

En el visualizador las usamos, por ejemplo, para armar cada botella
o para filtrar los mensajes de la consola.

**enumerate(...):** Función que recorre una lista y además nos da el
índice (la posición) de cada elemento. Por eso la usamos en el visor
de código: necesitamos el número de línea además del texto.

**" ".join(lista):** "Pega" los elementos de una lista en un solo texto.
El string que anteponemos ("", "> ", "<br>> ", etc.) es el separador que
va entre elemento y elemento. Con "" los unimos sin separadores.

**F-strings (f"..."):** Texto con "huecos" que se rellenan con valores de
variables. Ej: f"Botella {i} / Paso {j}: {nivel:.1f}%" muestra el valor actual de i, j y nivel.

**Estado reactivo (mo.state):** La "memoria" del visualizador. Con
get_step() leemos el paso actual y con set_step lo cambiamos. Cada vez que
el paso cambia, marimo vuelve a ejecutar las celdas que lo usan: por eso la
pantalla se actualiza sola sin escribir un while de actualización.

**Traza y "snapshots":** La traza es una lista donde cada elemento es un
diccionario = una "foto" del estado del programa en un momento exacto
(línea, i, j, nivel, mensaje). Gracias a esas fotos podemos viajar hacia
adelante y hacia atrás sin volver a ejecutar el código real.

**Valor centinela (-1):** Un valor especial que significa "ninguno". En la
traza usamos bottle_idx = -1 en los pasos iniciales y finales, cuando no
hay ninguna botella activa.

**on_click: **Los botones se configuran con on_click=funcion. Cuando el
usuario hace clic, marimo llama a esa función y le pasa el evento. Ese
parámetro se llama "_" por convención cuando no nos interesa usarlo. En este
notebook las funciones son increment(), decrement() y reset(): fijense cómo
sus docstrings explican lo mismo que antes hacían las lambdas inline.

**Plantillas HTML (la "caja negra" gráfica):** Todo el HTML del visualizador
está agrupado en la celda "🎨 PLANTILLAS HTML", separado de la lógica Python.
Cada plantilla es un string con "huecos" {campo} que se rellenan después con
.replace() desde la celda de visualización. Así el código Python queda limpio
(no vemos ninguna etiqueta <div> en la lógica) y si querés cambiar un color o
un tamaño, sabés exactamente dónde buscar.

**¿Por qué .replace() y no f-strings?** Porque el contenido que metemos en los
huecos puede traer llaves { } propias del código didáctico (por ejemplo
f'Botella {i} / Paso{j}: {nivel}%'), y .replace() cambia el texto exacto del hueco sin
interpretar nada más.
