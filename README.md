# Ciencia de Datos — Diplomatura

Repositorio de práctica de la Diplomatura en Ciencia de Datos. Contiene visualizadores ejecutables en Marimo para bucles anidados, simulación de fórmulas y escalas.

## Requisitos

1. Instalar Python 3.11 o superior.
2. Instalar Marimo 0.24.2 o superior.
3. Usar `uv` cuando esté disponible para resolver dependencias.

## Ejecución

1. Editar un visualizador con `uv run marimo edit loops_anidados_marimo.py`.
2. Ejecutar sin edición con `marimo run loops_anidados_marimo.py`.
3. Repetir el comando sobre `formula_simulation.py` para la simulación de fórmulas.
4. Abrir la pestaña del navegador generada por Marimo.

## Estructura principal

1. `loops_anidados_marimo.py` es el visualizador reactivo de bucles anidados.
2. `loops_anidados_marimo.md` es la guía didáctica del visualizador.
3. `loops_anidados_marimo_referencia.md` es la referencia de conceptos del visualizador.
4. `formula_simulation.py` es la simulación de fórmulas salariales.
5. `escalas_data.py` es la matriz de datos de escalas usada por la simulación.
6. `clase_01.ipynb` y `clase02.ipynb` son los cuadernos de clase.
7. `AMBROSIS 2026 02 V3.xlsx` es el dato fuente de escalas.

## Visualizadores

1. El visualizador de bucles simula 3 botellas con 4 pasos de llenado cada una.
2. La simulación de fórmulas replica `VLOOKUP`, `IF` y cálculos de plus y bono.
3. Las plantillas HTML viven en la celda `🎨 PLANTILLAS HTML`, separadas de la lógica Python.

## Validación manual

No existe suite automatizada de pruebas. Validación significa comprobación manual con Marimo.

1. Ejecutar `marimo run <file>.py` como prueba de carga.
2. Cambiar una entrada de la interfaz y confirmar el recómputo de celdas dependientes.
3. Confirmar la ausencia de archivos nuevos sin aprobación.

## Capturas

No existen capturas PNG en el repositorio. Las exportaciones HTML cumplen esa función.

1. `loops_anidados.html` es la exportación del visualizador de bucles.
2. `maquina_de_cafe.html` es la exportación del ejemplo de máquina de café.
3. `git.html` es la exportación de la guía de git.
