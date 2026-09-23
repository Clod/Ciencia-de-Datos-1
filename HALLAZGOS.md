# HALLAZGOS

## 2026-09-23 — Tipo inconsistente en ESCALAS_MATRIX

El archivo `escalas_data.py:223` almacena `'23333.68'` como texto entre comillas. Las celdas vecinas de la misma columna almacenan números sin comillas. La función `vlookup` de `formula_simulation.py:20-30` devuelve la celda sin conversión de tipo. La suma posterior de esa celda con números produce error de tipo o concatenación inválida. No se modificó la celda porque la corrección excede el alcance de la tarea Bootstrap Guidelines.
