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

**Lambda:** Funciones anónimas. Se escriben en una sola línea.

**Una forma de definir una función (no se usa en python)**

def f(param1, param2):  
    return param1+param2

**La forma que se usa en python**

f = lambda param1, param2: param1+param2

- **Bucles anidados**
  - Bucle exterior
  - Bucle interior
  - Variable contador
  - Variables de estado