# Formula Analysis for Worksheet 012026

This file contains the formulas found in column B and their dependencies, labelled with the content from **Column A** (Row Description).

### B30 - SAC Prorrateado
**Formula:** `=(B27)/12`

| Dependency | Label (From Column A) |
| :--- | :--- |
| B27 | Sueldo bruto |

---

### B31 - No Description
**Formula:** `=+B27+B30`

| Dependency | Label (From Column A) |
| :--- | :--- |
| B27 | Sueldo bruto |
| B30 | SAC Prorrateado |

---

### B37 - Sub Total Ganancia Bruta
**Formula:** `=B33+B27`

| Dependency | Label (From Column A) |
| :--- | :--- |
| B33 | BONO |
| B27 | Sueldo bruto |

---

### B39 - Jubilac.
**Formula:** `=-B5*11%`

| Dependency | Label (From Column A) |
| :--- | :--- |
| B5 | Tope cargas sociales Enero 2026 |

---

### B40 - Ley 19032
**Formula:** `=-B5*3%`

| Dependency | Label (From Column A) |
| :--- | :--- |
| B5 | Tope cargas sociales Enero 2026 |

---

### B41 - Obra social
**Formula:** `=-B5*3%`

| Dependency | Label (From Column A) |
| :--- | :--- |
| B5 | Tope cargas sociales Enero 2026 |

---

### B43 - Total Descuentos
**Formula:** `=SUM(B39:B42)`

| Dependency | Label (From Column A) |
| :--- | :--- |
| B39:B42 | Jubilac. |

---

### B45 - Ingresos gravados (menos SAC)
**Formula:** `=B27++B33`

| Dependency | Label (From Column A) |
| :--- | :--- |
| B27 | Sueldo bruto |
| B33 | BONO |

---

### B47 - Prorrateo vacaciones
**Formula:** `=+B28/12`

| Dependency | Label (From Column A) |
| :--- | :--- |
| B28 | Plus vacaciones |

---

### B49 - No Description
**Formula:** `=SUM(B47:B48)`

| Dependency | Label (From Column A) |
| :--- | :--- |
| B47:B48 | Prorrateo vacaciones |

---

### B52 - Ingresos Gravados Acumulados SUELDO MAS VACACIONES
**Formula:** `=B45+B47`

| Dependency | Label (From Column A) |
| :--- | :--- |
| B45 | Ingresos gravados (menos SAC) |
| B47 | Prorrateo vacaciones |

---

### B54 - Ajuste al neto SAC
**Formula:** `=-B30+B61`

| Dependency | Label (From Column A) |
| :--- | :--- |
| B30 | SAC Prorrateado |
| B61 | CARGAS SOC SAC  |

---

### B55 - Ajuste al neto SAC ACUM 
**Formula:** `=B54`

| Dependency | Label (From Column A) |
| :--- | :--- |
| B54 | Ajuste al neto SAC |

---

### B57 - TOTAL CARGAS
**Formula:** `=B48+B43`

| Dependency | Label (From Column A) |
| :--- | :--- |
| B48 | Descuentos |
| B43 | Total Descuentos |

---

### B59 - CARGAS ACUM
**Formula:** `=B43`

| Dependency | Label (From Column A) |
| :--- | :--- |
| B43 | Total Descuentos |

---

### B61 - CARGAS SOC SAC 
**Formula:** `=+(($B$5/12*0.17))`

| Dependency | Label (From Column A) |
| :--- | :--- |
| $B$5 | Tope cargas sociales Enero 2026 |

---

### B62 - Ganancia neta mensual SDO VAC Y SAC MENOS CARGAS
**Formula:** `=B27+B47+B43+B48-B54+B33`

| Dependency | Label (From Column A) |
| :--- | :--- |
| B27 | Sueldo bruto |
| B47 | Prorrateo vacaciones |
| B43 | Total Descuentos |
| B48 | Descuentos |
| B54 | Ajuste al neto SAC |
| B33 | BONO |

---

### B64 - Ganancia Neta acumulada 
**Formula:** `=B62`

| Dependency | Label (From Column A) |
| :--- | :--- |
| B62 | Ganancia neta mensual SDO VAC Y SAC MENOS CARGAS |

---

### B69 - tope 5% de gcia neta del ejercicio acumulada
**Formula:** `=B83*5/100`

| Dependency | Label (From Column A) |
| :--- | :--- |
| B83 | Gcia Neta Suj a Imp acumulada antes de osde |

---

### B71 - Ganancia no Imponible
**Formula:** `='Tablas '!B3`

| Dependency | Label (From Column A) |
| :--- | :--- |
| 'Tablas '!B3 | Ganancia No Imponible |

---

### B72 - Deducción especial
**Formula:** `='Tablas '!B4`

| Dependency | Label (From Column A) |
| :--- | :--- |
| 'Tablas '!B4 | Deducción Especial |

---

### B76 - Deduccion SAC especial
**Formula:** `=SUM(B71:B75)/12`

| Dependency | Label (From Column A) |
| :--- | :--- |
| B71:B75 | Ganancia no Imponible |

---

### B77 - Sub Total Deducciones Personales
**Formula:** `=SUM(B71:B76)`

| Dependency | Label (From Column A) |
| :--- | :--- |
| B71:B76 | Ganancia no Imponible |

---

### B83 - Gcia Neta Suj a Imp acumulada antes de osde
**Formula:** `=B64-B77+B68`

| Dependency | Label (From Column A) |
| :--- | :--- |
| B64 | Ganancia Neta acumulada  |
| B77 | Sub Total Deducciones Personales |
| B68 | Cuota Medico asistencial |

---

### B84 - Ganancia Neta Sujeta a Impuesto acumulada
**Formula:** `=B64-B77`

| Dependency | Label (From Column A) |
| :--- | :--- |
| B64 | Ganancia Neta acumulada  |
| B77 | Sub Total Deducciones Personales |

---

### B85 - =A62
**Formula:** `=B84`

| Dependency | Label (From Column A) |
| :--- | :--- |
| B84 | Ganancia Neta Sujeta a Impuesto acumulada |

---

### B86 - Base Imponible
**Formula:** `=B85`

| Dependency | Label (From Column A) |
| :--- | :--- |
| B85 | =A62 |

---

### B90 - Impuesto (Anual)
**Formula:** `=IF(B86>0,(VLOOKUP(B86,Escalas!$A$19:$E$27,3)),0)`

| Dependency | Label (From Column A) |
| :--- | :--- |
| B86 | Base Imponible |
| B86 | Base Imponible |
| Escalas!$A$19:$E$27 | 0 |

---

### B91 - Porcentaje
**Formula:** `=IF(B86>0,VLOOKUP(B86,Escalas!$A$19:$E$27,4),0)`

| Dependency | Label (From Column A) |
| :--- | :--- |
| B86 | Base Imponible |
| B86 | Base Imponible |
| Escalas!$A$19:$E$27 | 0 |

---

### B92 - Sobre excedente de
**Formula:** `=IF(B86>0,(VLOOKUP(B$86,Escalas!$A$19:$E$27,5)*B89),0)`

| Dependency | Label (From Column A) |
| :--- | :--- |
| B86 | Base Imponible |
| B$86 | Base Imponible |
| Escalas!$A$19:$E$27 | 0 |
| B89 | Empty |

---

### B94 - Base cálculo
**Formula:** `=IF(B86>0,+B86-B92,0)`

| Dependency | Label (From Column A) |
| :--- | :--- |
| B86 | Base Imponible |
| B86 | Base Imponible |
| B92 | Sobre excedente de |

---

### B95 - % calculado
**Formula:** `=+B91*B94`

| Dependency | Label (From Column A) |
| :--- | :--- |
| B91 | Porcentaje |
| B94 | Base cálculo |

---

### B97 - TOTAL IMPUESTO ANUAL
**Formula:** `=+B90+B95`

| Dependency | Label (From Column A) |
| :--- | :--- |
| B90 | Impuesto (Anual) |
| B95 | % calculado |

---

### B99 - Acumulado
**Formula:** `=+B103`

| Dependency | Label (From Column A) |
| :--- | :--- |
| B103 | Impuesto Mes |

---

### B103 - Impuesto Mes
**Formula:** `=+B97`

| Dependency | Label (From Column A) |
| :--- | :--- |
| B97 | TOTAL IMPUESTO ANUAL |

---

# Unique Inputs and References Summary
Below is a list of all unique cells and ranges referenced in the formulas above, with their corresponding labels from Column A.

| Cell/Range | Label (Column A) |
| :--- | :--- |
| $B$5 | Tope cargas sociales Enero 2026 |
| B$86 | Base Imponible |
| B103 | Impuesto Mes |
| B27 | Sueldo bruto |
| B28 | Plus vacaciones |
| B30 | SAC Prorrateado |
| B33 | BONO |
| B39:B42 | Jubilac. |
| B43 | Total Descuentos |
| B45 | Ingresos gravados (menos SAC) |
| B47 | Prorrateo vacaciones |
| B47:B48 | Prorrateo vacaciones |
| B48 | Descuentos |
| B5 | Tope cargas sociales Enero 2026 |
| B54 | Ajuste al neto SAC |
| B61 | CARGAS SOC SAC  |
| B62 | Ganancia neta mensual SDO VAC Y SAC MENOS CARGAS |
| B64 | Ganancia Neta acumulada  |
| B68 | Cuota Medico asistencial |
| B71:B75 | Ganancia no Imponible |
| B71:B76 | Ganancia no Imponible |
| B77 | Sub Total Deducciones Personales |
| B83 | Gcia Neta Suj a Imp acumulada antes de osde |
| B84 | Ganancia Neta Sujeta a Impuesto acumulada |
| B85 | =A62 |
| B86 | Base Imponible |
| B89 | Empty |
| B90 | Impuesto (Anual) |
| B91 | Porcentaje |
| B92 | Sobre excedente de |
| B94 | Base cálculo |
| B95 | % calculado |
| B97 | TOTAL IMPUESTO ANUAL |
| Escalas!$A$19:$E$27 | 0 |
| Tablas !B3 | Ganancia No Imponible |
| Tablas !B4 | Deducción Especial |
