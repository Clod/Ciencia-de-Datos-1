import marimo

app = marimo.App(width='full')

@app.cell
def __():
    import marimo as mo
    import datetime
    from escalas_data import ESCALAS_MATRIX
    return mo, datetime, ESCALAS_MATRIX

@app.cell
def __(mo):
    def if_func(condition, true_val, false_val): return true_val if condition else false_val

    def vlookup(value, matrix, col_index, range_lookup=True):
        idx = col_index - 1
        best_row = None
        if value is None: return 0
        for row in matrix:
            try:
                if row[0] is None: continue
                if row[0] <= value: best_row = row
                else: break
            except: continue
        return best_row[idx] if best_row else 0
    return if_func, vlookup

@app.cell
def __(datetime):
    anterior = 0  # Anterior (B98)
    bono = 0  # BONO (A33)
    conyuge = 0  # conyuge (A73)
    cuota_medico_asistencial = 0  # Cuota Medico asistencial (A68)
    descuentos = 0  # Descuentos (A48)
    empleada_dom_stica = 0  # Empleada Doméstica (A75)
    plus_vacaciones = 178984.77333333343  # Plus vacaciones (B28)
    sueldo_bruto = 3835388  # Sueldo bruto (B27)
    tope_cargas_sociales_abril_2026 = 3128545.73  # Tope cargas sociales Abril 2026 (B17)
    tope_cargas_sociales_agosto_2026 = 3440334.99  # Tope cargas sociales AGOSTO 2026 (B21)
    tope_cargas_sociales_diciembre_2026 = 3731212.01  # Tope cargas sociales DICIEMBRE  2026 (B25)
    tope_cargas_sociales_enero_2026 = 3823372.95  # Tope cargas sociales Enero 2026 (B5)
    tope_cargas_sociales_febrero_2026 = 3932339.08  # Tope cargas sociales Febrero 2026 (B6)
    tope_cargas_sociales_julio_2026 = 3385490.05  # Tope cargas sociales Julio 2026 (B20)
    tope_cargas_sociales_junio_2026 = 3335458.18  # Tope cargas sociales Junio 2026 (B19)
    tope_cargas_sociales_marzo_2026 = 4045590.45  # Tope cargas sociales Marzo 2026 (B16)
    tope_cargas_sociales_mayo_2026 = 3245240.49  # Tope cargas sociales Mayo 2026 (B18)
    tope_cargas_sociales_noviembre_2026 = 3645898  # Tope cargas sociales NOVIEMBRE 2026 (B24)
    tope_cargas_sociales_octubre_2026 = 3571608.54  # Tope cargas sociales OCTUBRE 2026 (B23)
    tope_cargas_sociales_septiembre_2026 = 3505701.35  # Tope cargas sociales SEPTIEMBRE 2026 (B22)
    var_012026_b1 = 0  # None (B1)
    var_012026_b26 = 0  # None (B26)
    var_012026_b42 = 0  # None (B42)
    var_012026_b89 = 1  # None (B89)
    return anterior, bono, conyuge, cuota_medico_asistencial, descuentos, empleada_dom_stica, plus_vacaciones, sueldo_bruto, tope_cargas_sociales_abril_2026, tope_cargas_sociales_agosto_2026, tope_cargas_sociales_diciembre_2026, tope_cargas_sociales_enero_2026, tope_cargas_sociales_febrero_2026, tope_cargas_sociales_julio_2026, tope_cargas_sociales_junio_2026, tope_cargas_sociales_marzo_2026, tope_cargas_sociales_mayo_2026, tope_cargas_sociales_noviembre_2026, tope_cargas_sociales_octubre_2026, tope_cargas_sociales_septiembre_2026, var_012026_b1, var_012026_b26, var_012026_b42, var_012026_b89

@app.cell
def __(mo, sueldo_bruto):
    mo.md("### B30 - SAC Prorrateado\n**Formula:** `=(B27)/12`")
    sac_prorrateado = (sueldo_bruto)/12
    mo.output.replace(sac_prorrateado)
    return sac_prorrateado,

@app.cell
def __(mo, sac_prorrateado, sueldo_bruto):
    mo.md("### B31 - Result\n**Formula:** `=+B27+B30`")
    var_012026_b31 = sueldo_bruto+sac_prorrateado
    mo.output.replace(var_012026_b31)
    return var_012026_b31,

@app.cell
def __(bono, mo, sueldo_bruto):
    mo.md("### B37 - Sub Total Ganancia Bruta\n**Formula:** `=B33+B27`")
    sub_total_ganancia_bruta = bono+sueldo_bruto
    mo.output.replace(sub_total_ganancia_bruta)
    return sub_total_ganancia_bruta,

@app.cell
def __(mo, tope_cargas_sociales_enero_2026):
    mo.md("### B39 - Jubilac.\n**Formula:** `=-B5*11%`")
    jubilac = -tope_cargas_sociales_enero_2026*11/100
    mo.output.replace(jubilac)
    return jubilac,

@app.cell
def __(mo, tope_cargas_sociales_enero_2026):
    mo.md("### B40 - Ley 19032\n**Formula:** `=-B5*3%`")
    ley_19032 = -tope_cargas_sociales_enero_2026*3/100
    mo.output.replace(ley_19032)
    return ley_19032,

@app.cell
def __(mo, tope_cargas_sociales_enero_2026):
    mo.md("### B41 - Obra social\n**Formula:** `=-B5*3%`")
    obra_social = -tope_cargas_sociales_enero_2026*3/100
    mo.output.replace(obra_social)
    return obra_social,

@app.cell
def __(jubilac, ley_19032, mo, obra_social, var_012026_b42):
    mo.md("### B43 - Total Descuentos\n**Formula:** `=SUM(B39:B42)`")
    total_descuentos = sum([jubilac, ley_19032, obra_social, var_012026_b42])
    mo.output.replace(total_descuentos)
    return total_descuentos,

@app.cell
def __(bono, mo, sueldo_bruto):
    mo.md("### B45 - Ingresos gravados (menos SAC)\n**Formula:** `=B27++B33`")
    ingresos_gravados_menos_sac = sueldo_bruto++bono
    mo.output.replace(ingresos_gravados_menos_sac)
    return ingresos_gravados_menos_sac,

@app.cell
def __(mo, plus_vacaciones):
    mo.md("### B47 - Prorrateo vacaciones\n**Formula:** `=+B28/12`")
    prorrateo_vacaciones = plus_vacaciones/12
    mo.output.replace(prorrateo_vacaciones)
    return prorrateo_vacaciones,

@app.cell
def __(descuentos, mo, prorrateo_vacaciones):
    mo.md("### B49 - Result\n**Formula:** `=SUM(B47:B48)`")
    var_012026_b49 = sum([prorrateo_vacaciones, descuentos])
    mo.output.replace(var_012026_b49)
    return var_012026_b49,

@app.cell
def __(ingresos_gravados_menos_sac, mo, prorrateo_vacaciones):
    mo.md("### B52 - Ingresos Gravados Acumulados SUELDO MAS VACACIONES\n**Formula:** `=B45+B47`")
    ingresos_gravados_acumulados_sueldo_mas_vacaciones = ingresos_gravados_menos_sac+prorrateo_vacaciones
    mo.output.replace(ingresos_gravados_acumulados_sueldo_mas_vacaciones)
    return ingresos_gravados_acumulados_sueldo_mas_vacaciones,

@app.cell
def __(cargas_soc_sac, mo, sac_prorrateado):
    mo.md("### B54 - Ajuste al neto SAC\n**Formula:** `=-B30+B61`")
    ajuste_al_neto_sac = -sac_prorrateado+cargas_soc_sac
    mo.output.replace(ajuste_al_neto_sac)
    return ajuste_al_neto_sac,

@app.cell
def __(ajuste_al_neto_sac, mo):
    mo.md("### B55 - Ajuste al neto SAC ACUM \n**Formula:** `=B54`")
    ajuste_al_neto_sac_acum = ajuste_al_neto_sac
    mo.output.replace(ajuste_al_neto_sac_acum)
    return ajuste_al_neto_sac_acum,

@app.cell
def __(descuentos, mo, total_descuentos):
    mo.md("### B57 - TOTAL CARGAS\n**Formula:** `=B48+B43`")
    total_cargas = descuentos+total_descuentos
    mo.output.replace(total_cargas)
    return total_cargas,

@app.cell
def __(mo, total_descuentos):
    mo.md("### B59 - CARGAS ACUM\n**Formula:** `=B43`")
    cargas_acum = total_descuentos
    mo.output.replace(cargas_acum)
    return cargas_acum,

@app.cell
def __(mo, tope_cargas_sociales_enero_2026):
    mo.md("### B61 - CARGAS SOC SAC \n**Formula:** `=+(($B$5/12*0.17))`")
    cargas_soc_sac = ((tope_cargas_sociales_enero_2026/12*0.17))
    mo.output.replace(cargas_soc_sac)
    return cargas_soc_sac,

@app.cell
def __(ajuste_al_neto_sac, bono, descuentos, mo, prorrateo_vacaciones, sueldo_bruto, total_descuentos):
    mo.md("### B62 - Ganancia neta mensual SDO VAC Y SAC MENOS CARGAS\n**Formula:** `=B27+B47+B43+B48-B54+B33`")
    ganancia_neta_mensual_sdo_vac_y_sac_menos_cargas = sueldo_bruto+prorrateo_vacaciones+total_descuentos+descuentos-ajuste_al_neto_sac+bono
    mo.output.replace(ganancia_neta_mensual_sdo_vac_y_sac_menos_cargas)
    return ganancia_neta_mensual_sdo_vac_y_sac_menos_cargas,

@app.cell
def __(ganancia_neta_mensual_sdo_vac_y_sac_menos_cargas, mo):
    mo.md("### B64 - Ganancia Neta acumulada \n**Formula:** `=B62`")
    ganancia_neta_acumulada = ganancia_neta_mensual_sdo_vac_y_sac_menos_cargas
    mo.output.replace(ganancia_neta_acumulada)
    return ganancia_neta_acumulada,

@app.cell
def __(gcia_neta_suj_a_imp_acumulada_antes_de_osde, mo):
    mo.md("### B69 - tope 5% de gcia neta del ejercicio acumulada\n**Formula:** `=B83*5/100`")
    tope_5_de_gcia_neta_del_ejercicio_acumulada = gcia_neta_suj_a_imp_acumulada_antes_de_osde*5/100
    mo.output.replace(tope_5_de_gcia_neta_del_ejercicio_acumulada)
    return tope_5_de_gcia_neta_del_ejercicio_acumulada,

@app.cell
def __(ganancia_no_imponible, mo):
    mo.md("### B71 - Ganancia no Imponible\n**Formula:** `='Tablas '!B3`")
    ganancia_no_imponible = ganancia_no_imponible
    mo.output.replace(ganancia_no_imponible)
    return ganancia_no_imponible,

@app.cell
def __(deducci_n_especial, mo):
    mo.md("### B72 - Deducción especial\n**Formula:** `='Tablas '!B4`")
    deducci_n_especial = deducci_n_especial
    mo.output.replace(deducci_n_especial)
    return deducci_n_especial,

@app.cell
def __(conyuge, cuota_medico_asistencial, deducci_n_especial, empleada_dom_stica, ganancia_no_imponible, mo):
    mo.md("### B76 - Deduccion SAC especial\n**Formula:** `=SUM(B71:B75)/12`")
    deduccion_sac_especial = sum([ganancia_no_imponible, deducci_n_especial, conyuge, cuota_medico_asistencial, empleada_dom_stica])/12
    mo.output.replace(deduccion_sac_especial)
    return deduccion_sac_especial,

@app.cell
def __(conyuge, cuota_medico_asistencial, deducci_n_especial, deduccion_sac_especial, empleada_dom_stica, ganancia_no_imponible, mo):
    mo.md("### B77 - Sub Total Deducciones Personales\n**Formula:** `=SUM(B71:B76)`")
    sub_total_deducciones_personales = sum([ganancia_no_imponible, deducci_n_especial, conyuge, cuota_medico_asistencial, empleada_dom_stica, deduccion_sac_especial])
    mo.output.replace(sub_total_deducciones_personales)
    return sub_total_deducciones_personales,

@app.cell
def __(cuota_medico_asistencial, ganancia_neta_acumulada, mo, sub_total_deducciones_personales):
    mo.md("### B83 - Gcia Neta Suj a Imp acumulada antes de osde\n**Formula:** `=B64-B77+B68`")
    gcia_neta_suj_a_imp_acumulada_antes_de_osde = ganancia_neta_acumulada-sub_total_deducciones_personales+cuota_medico_asistencial
    mo.output.replace(gcia_neta_suj_a_imp_acumulada_antes_de_osde)
    return gcia_neta_suj_a_imp_acumulada_antes_de_osde,

@app.cell
def __(ganancia_neta_acumulada, mo, sub_total_deducciones_personales):
    mo.md("### B84 - Ganancia Neta Sujeta a Impuesto acumulada\n**Formula:** `=B64-B77`")
    ganancia_neta_sujeta_a_impuesto_acumulada = ganancia_neta_acumulada-sub_total_deducciones_personales
    mo.output.replace(ganancia_neta_sujeta_a_impuesto_acumulada)
    return ganancia_neta_sujeta_a_impuesto_acumulada,

@app.cell
def __(ganancia_neta_sujeta_a_impuesto_acumulada, mo):
    mo.md("### B85 - Result\n**Formula:** `=B84`")
    var_012026_b85 = ganancia_neta_sujeta_a_impuesto_acumulada
    mo.output.replace(var_012026_b85)
    return var_012026_b85,

@app.cell
def __(mo, var_012026_b85):
    mo.md("### B86 - Base Imponible\n**Formula:** `=B85`")
    base_imponible = var_012026_b85
    mo.output.replace(base_imponible)
    return base_imponible,

@app.cell
def __(ESCALAS_MATRIX, base_imponible, if_func, mo, vlookup):
    mo.md("### B90 - Impuesto (Anual)\n**Formula:** `=IF(B86>0,(VLOOKUP(B86,Escalas!$A$19:$E$27,3)),0)`")
    impuesto_anual = if_func(base_imponible>0,(vlookup(base_imponible,ESCALAS_MATRIX[18:27],3)),0)
    mo.output.replace(impuesto_anual)
    return impuesto_anual,

@app.cell
def __(ESCALAS_MATRIX, base_imponible, if_func, mo, vlookup):
    mo.md("### B91 - Porcentaje\n**Formula:** `=IF(B86>0,VLOOKUP(B86,Escalas!$A$19:$E$27,4),0)`")
    porcentaje = if_func(base_imponible>0,vlookup(base_imponible,ESCALAS_MATRIX[18:27],4),0)
    mo.output.replace(porcentaje)
    return porcentaje,

@app.cell
def __(ESCALAS_MATRIX, base_imponible, if_func, mo, var_012026_b89, vlookup):
    mo.md("### B92 - Sobre excedente de\n**Formula:** `=IF(B86>0,(VLOOKUP(B$86,Escalas!$A$19:$E$27,5)*B89),0)`")
    sobre_excedente_de = if_func(base_imponible>0,(vlookup(base_imponible,ESCALAS_MATRIX[18:27],5)*var_012026_b89),0)
    mo.output.replace(sobre_excedente_de)
    return sobre_excedente_de,

@app.cell
def __(base_imponible, if_func, mo, sobre_excedente_de):
    mo.md("### B94 - Base cálculo\n**Formula:** `=IF(B86>0,+B86-B92,0)`")
    base_c_lculo = if_func(base_imponible>0,+base_imponible-sobre_excedente_de,0)
    mo.output.replace(base_c_lculo)
    return base_c_lculo,

@app.cell
def __(base_c_lculo, mo, porcentaje):
    mo.md("### B95 - % calculado\n**Formula:** `=+B91*B94`")
    calculado = porcentaje*base_c_lculo
    mo.output.replace(calculado)
    return calculado,

@app.cell
def __(calculado, impuesto_anual, mo):
    mo.md("### B97 - TOTAL IMPUESTO ANUAL\n**Formula:** `=+B90+B95`")
    total_impuesto_anual = impuesto_anual+calculado
    mo.output.replace(total_impuesto_anual)
    return total_impuesto_anual,

@app.cell
def __(impuesto_mes, mo):
    mo.md("### B99 - Acumulado\n**Formula:** `=+B103`")
    acumulado = impuesto_mes
    mo.output.replace(acumulado)
    return acumulado,

@app.cell
def __(mo, total_impuesto_anual):
    mo.md("### B103 - Impuesto Mes\n**Formula:** `=+B97`")
    impuesto_mes = total_impuesto_anual
    mo.output.replace(impuesto_mes)
    return impuesto_mes,

if __name__ == '__main__':
    app.run()
