import marimo

__generated_with = "0.21.1"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import datetime
    from escalas_data import ESCALAS_MATRIX

    return ESCALAS_MATRIX, datetime, mo


@app.cell
def _():
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
def _(mo):
    ui_dict = mo.ui.dictionary({
        'bono': mo.ui.number(value=0, label='BONO'),
        'plus_vacaciones': mo.ui.number(value=178984.77333333343, label='Plus vacaciones'),
        'sueldo_bruto': mo.ui.number(value=3835388, label='Sueldo bruto'),
        'tope_cargas_sociales_abril_2026': mo.ui.number(value=3128545.73, label='Tope cargas sociales Abril 2026'),
        'tope_cargas_sociales_agosto_2026': mo.ui.number(value=3440334.99, label='Tope cargas sociales AGOSTO 2026'),
        'tope_cargas_sociales_diciembre_2026': mo.ui.number(value=3731212.01, label='Tope cargas sociales DICIEMBRE  2026'),
        'tope_cargas_sociales_enero_2026': mo.ui.number(value=3823372.95, label='Tope cargas sociales Enero 2026'),
        'tope_cargas_sociales_febrero_2026': mo.ui.number(value=3932339.08, label='Tope cargas sociales Febrero 2026'),
        'tope_cargas_sociales_julio_2026': mo.ui.number(value=3385490.05, label='Tope cargas sociales Julio 2026'),
        'tope_cargas_sociales_junio_2026': mo.ui.number(value=3335458.18, label='Tope cargas sociales Junio 2026'),
        'tope_cargas_sociales_marzo_2026': mo.ui.number(value=4045590.45, label='Tope cargas sociales Marzo 2026'),
        'tope_cargas_sociales_mayo_2026': mo.ui.number(value=3245240.49, label='Tope cargas sociales Mayo 2026'),
        'tope_cargas_sociales_noviembre_2026': mo.ui.number(value=3645898, label='Tope cargas sociales NOVIEMBRE 2026'),
        'tope_cargas_sociales_octubre_2026': mo.ui.number(value=3571608.54, label='Tope cargas sociales OCTUBRE 2026'),
        'tope_cargas_sociales_septiembre_2026': mo.ui.number(value=3505701.35, label='Tope cargas sociales SEPTIEMBRE 2026'),
    })
    return (ui_dict,)


@app.cell
def _(datetime, ui_dict):
    anterior = 0
    bono = ui_dict.value['bono'] if 'bono' in ui_dict.value else 0
    conyuge = 0
    cuota_medico_asistencial = 0
    descuentos = 0
    empleada_dom_stica = 0
    plus_vacaciones = ui_dict.value['plus_vacaciones'] if 'plus_vacaciones' in ui_dict.value else 178984.77333333343
    sueldo_bruto = ui_dict.value['sueldo_bruto'] if 'sueldo_bruto' in ui_dict.value else 3835388
    tablas_b10 = 0
    tablas_b11 = 0
    tablas_b12 = 0
    tablas_b2 = 1
    tablas_deducci_n_especial = 0
    tablas_ganancia_no_imponible = 0
    tablas_mes = 0
    tablas_tabla_de_deducciones = 0
    tablas_var_1 = 83.01
    tablas_var_10 = 830.1
    tablas_var_11 = 913.11
    tablas_var_12 = 996.12
    tablas_var_2 = 166.02
    tablas_var_3 = 249.03000000000003
    tablas_var_4 = 332.04
    tablas_var_5 = 415.05
    tablas_var_6 = 498.06
    tablas_var_7 = 581.07
    tablas_var_8 = 664.08
    tablas_var_9 = 747.09
    tope_cargas_sociales_abril_2026 = ui_dict.value['tope_cargas_sociales_abril_2026'] if 'tope_cargas_sociales_abril_2026' in ui_dict.value else 3128545.73
    tope_cargas_sociales_agosto_2026 = ui_dict.value['tope_cargas_sociales_agosto_2026'] if 'tope_cargas_sociales_agosto_2026' in ui_dict.value else 3440334.99
    tope_cargas_sociales_diciembre_2026 = ui_dict.value['tope_cargas_sociales_diciembre_2026'] if 'tope_cargas_sociales_diciembre_2026' in ui_dict.value else 3731212.01
    tope_cargas_sociales_enero_2026 = ui_dict.value['tope_cargas_sociales_enero_2026'] if 'tope_cargas_sociales_enero_2026' in ui_dict.value else 3823372.95
    tope_cargas_sociales_febrero_2026 = ui_dict.value['tope_cargas_sociales_febrero_2026'] if 'tope_cargas_sociales_febrero_2026' in ui_dict.value else 3932339.08
    tope_cargas_sociales_julio_2026 = ui_dict.value['tope_cargas_sociales_julio_2026'] if 'tope_cargas_sociales_julio_2026' in ui_dict.value else 3385490.05
    tope_cargas_sociales_junio_2026 = ui_dict.value['tope_cargas_sociales_junio_2026'] if 'tope_cargas_sociales_junio_2026' in ui_dict.value else 3335458.18
    tope_cargas_sociales_marzo_2026 = ui_dict.value['tope_cargas_sociales_marzo_2026'] if 'tope_cargas_sociales_marzo_2026' in ui_dict.value else 4045590.45
    tope_cargas_sociales_mayo_2026 = ui_dict.value['tope_cargas_sociales_mayo_2026'] if 'tope_cargas_sociales_mayo_2026' in ui_dict.value else 3245240.49
    tope_cargas_sociales_noviembre_2026 = ui_dict.value['tope_cargas_sociales_noviembre_2026'] if 'tope_cargas_sociales_noviembre_2026' in ui_dict.value else 3645898
    tope_cargas_sociales_octubre_2026 = ui_dict.value['tope_cargas_sociales_octubre_2026'] if 'tope_cargas_sociales_octubre_2026' in ui_dict.value else 3571608.54
    tope_cargas_sociales_septiembre_2026 = ui_dict.value['tope_cargas_sociales_septiembre_2026'] if 'tope_cargas_sociales_septiembre_2026' in ui_dict.value else 3505701.35
    var_012026_b1 = datetime.datetime(2026, 1, 1)
    var_012026_b26 = datetime.datetime(2026, 1, 1)
    var_012026_b42 = 0
    var_012026_b89 = 1
    return (
        bono,
        conyuge,
        cuota_medico_asistencial,
        descuentos,
        empleada_dom_stica,
        plus_vacaciones,
        sueldo_bruto,
        tablas_deducci_n_especial,
        tablas_ganancia_no_imponible,
        tope_cargas_sociales_enero_2026,
        var_012026_b42,
        var_012026_b89,
    )


@app.cell
def _(mo, ui_dict):
    topes = [ui_dict[k] for k in ['tope_cargas_sociales_abril_2026', 'tope_cargas_sociales_agosto_2026', 'tope_cargas_sociales_diciembre_2026', 'tope_cargas_sociales_enero_2026', 'tope_cargas_sociales_febrero_2026', 'tope_cargas_sociales_julio_2026', 'tope_cargas_sociales_junio_2026', 'tope_cargas_sociales_marzo_2026', 'tope_cargas_sociales_mayo_2026', 'tope_cargas_sociales_noviembre_2026', 'tope_cargas_sociales_octubre_2026', 'tope_cargas_sociales_septiembre_2026']]
    others = [ui_dict[k] for k in ['bono', 'plus_vacaciones', 'sueldo_bruto']]
    layout = mo.vstack([
        mo.md('# Simulación de Liquidación 2026'),
        mo.md('## Parámetros de Simulación'),
        mo.md('### Topes Cargas Sociales'),
        mo.hstack(topes, wrap=True),
        mo.md('### Otros Ingresos'),
        mo.hstack(others, wrap=True),
    ])
    mo.output.replace(layout)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # A contiuación se detallan los cálculos de cada una de las variables.
    ## Esto es un subtítulo

    La idea es que acá se pueden agregar explicaciones sobre legislación y hasta vínculos.

    *Por ejemplo:* http://arca.gob.ar
    """)
    return


@app.cell
def _(mo, sueldo_bruto):
    mo.md("### B30 - SAC Prorrateado\n**Formula:** `=(B27)/12`")
    sac_prorrateado = (sueldo_bruto)/12
    _fmt = f"${sac_prorrateado:,.2f}" if isinstance(sac_prorrateado, (int, float)) else sac_prorrateado
    mo.output.replace(mo.md(f"**El SAC prorrateado es:** `{_fmt}`"))
    return (sac_prorrateado,)


@app.cell
def _(mo, sac_prorrateado, sueldo_bruto):
    mo.md("### B31 - Result\n**Formula:** `=+B27+B30`")
    var_012026_b31 = sueldo_bruto+sac_prorrateado
    _fmt = f"${var_012026_b31:,.2f}" if isinstance(var_012026_b31, (int, float)) else var_012026_b31
    mo.output.replace(mo.md(f"**Este es un resultado intermedio que no sé qué es:** `{_fmt}`"))
    return


@app.cell
def _(bono, mo, sueldo_bruto):
    mo.md("### B37 - Sub Total Ganancia Bruta\n**Formula:** `=B33+B27`")
    sub_total_ganancia_bruta = bono+sueldo_bruto
    _fmt = f"${sub_total_ganancia_bruta:,.2f}" if isinstance(sub_total_ganancia_bruta, (int, float)) else sub_total_ganancia_bruta
    mo.output.replace(mo.md(f"**Sub Total Ganancia Bruta:** `{_fmt}`"))
    return


@app.cell
def _(mo, tope_cargas_sociales_enero_2026):
    mo.md("### B39 - Jubilac.\n**Formula:** `=-B5*11%`")
    jubilac = -tope_cargas_sociales_enero_2026*11/100
    _fmt = f"${jubilac:,.2f}" if isinstance(jubilac, (int, float)) else jubilac
    mo.output.replace(mo.md(f"**Jubilac:** `{_fmt}`"))
    return (jubilac,)


@app.cell
def _(mo, tope_cargas_sociales_enero_2026):
    mo.md("### B40 - Ley 19032\n**Formula:** `=-B5*3%`")
    ley_19032 = -tope_cargas_sociales_enero_2026*3/100
    _fmt = f"${ley_19032:,.2f}" if isinstance(ley_19032, (int, float)) else ley_19032
    mo.output.replace(mo.md(f"**Result:** `{_fmt}`"))
    return (ley_19032,)


@app.cell
def _(mo, tope_cargas_sociales_enero_2026):
    mo.md("### B41 - Obra social\n**Formula:** `=-B5*3%`")
    obra_social = -tope_cargas_sociales_enero_2026*3/100
    _fmt = f"${obra_social:,.2f}" if isinstance(obra_social, (int, float)) else obra_social
    mo.output.replace(mo.md(f"**Result:** `{_fmt}`"))
    return (obra_social,)


@app.cell
def _(jubilac, ley_19032, mo, obra_social, var_012026_b42):
    mo.md("### B43 - Total Descuentos\n**Formula:** `=SUM(B39:B42)`")
    total_descuentos = sum([jubilac, ley_19032, obra_social, var_012026_b42])
    _fmt = f"${total_descuentos:,.2f}" if isinstance(total_descuentos, (int, float)) else total_descuentos
    mo.output.replace(mo.md(f"**Result:** `{_fmt}`"))
    return (total_descuentos,)


@app.cell
def _(bono, mo, sueldo_bruto):
    mo.md("### B45 - Ingresos gravados (menos SAC)\n**Formula:** `=B27++B33`")
    ingresos_gravados_menos_sac = sueldo_bruto++bono
    _fmt = f"${ingresos_gravados_menos_sac:,.2f}" if isinstance(ingresos_gravados_menos_sac, (int, float)) else ingresos_gravados_menos_sac
    mo.output.replace(mo.md(f"**Result:** `{_fmt}`"))
    return (ingresos_gravados_menos_sac,)


@app.cell
def _(mo, plus_vacaciones):
    mo.md("### B47 - Prorrateo vacaciones\n**Formula:** `=+B28/12`")
    prorrateo_vacaciones = plus_vacaciones/12
    _fmt = f"${prorrateo_vacaciones:,.2f}" if isinstance(prorrateo_vacaciones, (int, float)) else prorrateo_vacaciones
    mo.output.replace(mo.md(f"**Result:** `{_fmt}`"))
    return (prorrateo_vacaciones,)


@app.cell
def _(descuentos, mo, prorrateo_vacaciones):
    mo.md("### B49 - Result\n**Formula:** `=SUM(B47:B48)`")
    var_012026_b49 = sum([prorrateo_vacaciones, descuentos])
    _fmt = f"${var_012026_b49:,.2f}" if isinstance(var_012026_b49, (int, float)) else var_012026_b49
    mo.output.replace(mo.md(f"**Result:** `{_fmt}`"))
    return


@app.cell
def _(ingresos_gravados_menos_sac, mo, prorrateo_vacaciones):
    mo.md("### B52 - Ingresos Gravados Acumulados SUELDO MAS VACACIONES\n**Formula:** `=B45+B47`")
    ingresos_gravados_acumulados_sueldo_mas_vacaciones = ingresos_gravados_menos_sac+prorrateo_vacaciones
    _fmt = f"${ingresos_gravados_acumulados_sueldo_mas_vacaciones:,.2f}" if isinstance(ingresos_gravados_acumulados_sueldo_mas_vacaciones, (int, float)) else ingresos_gravados_acumulados_sueldo_mas_vacaciones
    mo.output.replace(mo.md(f"**Result:** `{_fmt}`"))
    return


@app.cell
def _(cargas_soc_sac, mo, sac_prorrateado):
    mo.md("### B54 - Ajuste al neto SAC\n**Formula:** `=-B30+B61`")
    ajuste_al_neto_sac = -sac_prorrateado+cargas_soc_sac
    _fmt = f"${ajuste_al_neto_sac:,.2f}" if isinstance(ajuste_al_neto_sac, (int, float)) else ajuste_al_neto_sac
    mo.output.replace(mo.md(f"**Result:** `{_fmt}`"))
    return (ajuste_al_neto_sac,)


@app.cell
def _(ajuste_al_neto_sac, mo):
    mo.md("### B55 - Ajuste al neto SAC ACUM \n**Formula:** `=B54`")
    ajuste_al_neto_sac_acum = ajuste_al_neto_sac
    _fmt = f"${ajuste_al_neto_sac_acum:,.2f}" if isinstance(ajuste_al_neto_sac_acum, (int, float)) else ajuste_al_neto_sac_acum
    mo.output.replace(mo.md(f"**Result:** `{_fmt}`"))
    return


@app.cell
def _(descuentos, mo, total_descuentos):
    mo.md("### B57 - TOTAL CARGAS\n**Formula:** `=B48+B43`")
    total_cargas = descuentos+total_descuentos
    _fmt = f"${total_cargas:,.2f}" if isinstance(total_cargas, (int, float)) else total_cargas
    mo.output.replace(mo.md(f"**Result:** `{_fmt}`"))
    return


@app.cell
def _(mo, total_descuentos):
    mo.md("### B59 - CARGAS ACUM\n**Formula:** `=B43`")
    cargas_acum = total_descuentos
    _fmt = f"${cargas_acum:,.2f}" if isinstance(cargas_acum, (int, float)) else cargas_acum
    mo.output.replace(mo.md(f"**Result:** `{_fmt}`"))
    return


@app.cell
def _(mo, tope_cargas_sociales_enero_2026):
    mo.md("### B61 - CARGAS SOC SAC \n**Formula:** `=+(($B$5/12*0.17))`")
    cargas_soc_sac = ((tope_cargas_sociales_enero_2026/12*0.17))
    _fmt = f"${cargas_soc_sac:,.2f}" if isinstance(cargas_soc_sac, (int, float)) else cargas_soc_sac
    mo.output.replace(mo.md(f"**Result:** `{_fmt}`"))
    return (cargas_soc_sac,)


@app.cell
def _(
    ajuste_al_neto_sac,
    bono,
    descuentos,
    mo,
    prorrateo_vacaciones,
    sueldo_bruto,
    total_descuentos,
):
    mo.md("### B62 - Ganancia neta mensual SDO VAC Y SAC MENOS CARGAS\n**Formula:** `=B27+B47+B43+B48-B54+B33`")
    ganancia_neta_mensual_sdo_vac_y_sac_menos_cargas = sueldo_bruto+prorrateo_vacaciones+total_descuentos+descuentos-ajuste_al_neto_sac+bono
    _fmt = f"${ganancia_neta_mensual_sdo_vac_y_sac_menos_cargas:,.2f}" if isinstance(ganancia_neta_mensual_sdo_vac_y_sac_menos_cargas, (int, float)) else ganancia_neta_mensual_sdo_vac_y_sac_menos_cargas
    mo.output.replace(mo.md(f"**Result:** `{_fmt}`"))
    return (ganancia_neta_mensual_sdo_vac_y_sac_menos_cargas,)


@app.cell
def _(ganancia_neta_mensual_sdo_vac_y_sac_menos_cargas, mo):
    mo.md("### B64 - Ganancia Neta acumulada \n**Formula:** `=B62`")
    ganancia_neta_acumulada = ganancia_neta_mensual_sdo_vac_y_sac_menos_cargas
    _fmt = f"${ganancia_neta_acumulada:,.2f}" if isinstance(ganancia_neta_acumulada, (int, float)) else ganancia_neta_acumulada
    mo.output.replace(mo.md(f"**Result:** `{_fmt}`"))
    return (ganancia_neta_acumulada,)


@app.cell
def _(gcia_neta_suj_a_imp_acumulada_antes_de_osde, mo):
    mo.md("### B69 - tope 5% de gcia neta del ejercicio acumulada\n**Formula:** `=B83*5/100`")
    tope_5_de_gcia_neta_del_ejercicio_acumulada = gcia_neta_suj_a_imp_acumulada_antes_de_osde*5/100
    _fmt = f"${tope_5_de_gcia_neta_del_ejercicio_acumulada:,.2f}" if isinstance(tope_5_de_gcia_neta_del_ejercicio_acumulada, (int, float)) else tope_5_de_gcia_neta_del_ejercicio_acumulada
    mo.output.replace(mo.md(f"**Result:** `{_fmt}`"))
    return


@app.cell
def _(mo, tablas_ganancia_no_imponible):
    mo.md("### B71 - Ganancia no Imponible\n**Formula:** `='Tablas '!B3`")
    ganancia_no_imponible = tablas_ganancia_no_imponible
    _fmt = f"${ganancia_no_imponible:,.2f}" if isinstance(ganancia_no_imponible, (int, float)) else ganancia_no_imponible
    mo.output.replace(mo.md(f"**Result:** `{_fmt}`"))
    return (ganancia_no_imponible,)


@app.cell
def _(mo, tablas_deducci_n_especial):
    mo.md("### B72 - Deducción especial\n**Formula:** `='Tablas '!B4`")
    deducci_n_especial = tablas_deducci_n_especial
    _fmt = f"${deducci_n_especial:,.2f}" if isinstance(deducci_n_especial, (int, float)) else deducci_n_especial
    mo.output.replace(mo.md(f"**Result:** `{_fmt}`"))
    return (deducci_n_especial,)


@app.cell
def _(
    conyuge,
    cuota_medico_asistencial,
    deducci_n_especial,
    empleada_dom_stica,
    ganancia_no_imponible,
    mo,
):
    mo.md("### B76 - Deduccion SAC especial\n**Formula:** `=SUM(B71:B75)/12`")
    deduccion_sac_especial = sum([ganancia_no_imponible, deducci_n_especial, conyuge, cuota_medico_asistencial, empleada_dom_stica])/12
    _fmt = f"${deduccion_sac_especial:,.2f}" if isinstance(deduccion_sac_especial, (int, float)) else deduccion_sac_especial
    mo.output.replace(mo.md(f"**Result:** `{_fmt}`"))
    return (deduccion_sac_especial,)


@app.cell
def _(
    conyuge,
    cuota_medico_asistencial,
    deducci_n_especial,
    deduccion_sac_especial,
    empleada_dom_stica,
    ganancia_no_imponible,
    mo,
):
    mo.md("### B77 - Sub Total Deducciones Personales\n**Formula:** `=SUM(B71:B76)`")
    sub_total_deducciones_personales = sum([ganancia_no_imponible, deducci_n_especial, conyuge, cuota_medico_asistencial, empleada_dom_stica, deduccion_sac_especial])
    _fmt = f"${sub_total_deducciones_personales:,.2f}" if isinstance(sub_total_deducciones_personales, (int, float)) else sub_total_deducciones_personales
    mo.output.replace(mo.md(f"**Result:** `{_fmt}`"))
    return (sub_total_deducciones_personales,)


@app.cell
def _(
    cuota_medico_asistencial,
    ganancia_neta_acumulada,
    mo,
    sub_total_deducciones_personales,
):
    mo.md("### B83 - Gcia Neta Suj a Imp acumulada antes de osde\n**Formula:** `=B64-B77+B68`")
    gcia_neta_suj_a_imp_acumulada_antes_de_osde = ganancia_neta_acumulada-sub_total_deducciones_personales+cuota_medico_asistencial
    _fmt = f"${gcia_neta_suj_a_imp_acumulada_antes_de_osde:,.2f}" if isinstance(gcia_neta_suj_a_imp_acumulada_antes_de_osde, (int, float)) else gcia_neta_suj_a_imp_acumulada_antes_de_osde
    mo.output.replace(mo.md(f"**Result:** `{_fmt}`"))
    return (gcia_neta_suj_a_imp_acumulada_antes_de_osde,)


@app.cell
def _(ganancia_neta_acumulada, mo, sub_total_deducciones_personales):
    mo.md("### B84 - Ganancia Neta Sujeta a Impuesto acumulada\n**Formula:** `=B64-B77`")
    ganancia_neta_sujeta_a_impuesto_acumulada = ganancia_neta_acumulada-sub_total_deducciones_personales
    _fmt = f"${ganancia_neta_sujeta_a_impuesto_acumulada:,.2f}" if isinstance(ganancia_neta_sujeta_a_impuesto_acumulada, (int, float)) else ganancia_neta_sujeta_a_impuesto_acumulada
    mo.output.replace(mo.md(f"**Result:** `{_fmt}`"))
    return (ganancia_neta_sujeta_a_impuesto_acumulada,)


@app.cell
def _(ganancia_neta_sujeta_a_impuesto_acumulada, mo):
    mo.md("### B85 - Result\n**Formula:** `=B84`")
    var_012026_b85 = ganancia_neta_sujeta_a_impuesto_acumulada
    _fmt = f"${var_012026_b85:,.2f}" if isinstance(var_012026_b85, (int, float)) else var_012026_b85
    mo.output.replace(mo.md(f"**Result:** `{_fmt}`"))
    return (var_012026_b85,)


@app.cell
def _(mo, var_012026_b85):
    mo.md("### B86 - Base Imponible\n**Formula:** `=B85`")
    base_imponible = var_012026_b85
    _fmt = f"${base_imponible:,.2f}" if isinstance(base_imponible, (int, float)) else base_imponible
    mo.output.replace(mo.md(f"**Result:** `{_fmt}`"))
    return (base_imponible,)


@app.cell
def _(ESCALAS_MATRIX, base_imponible, if_func, mo, vlookup):
    mo.md("### B90 - Impuesto (Anual)\n**Formula:** `=IF(B86>0,(VLOOKUP(B86,Escalas!$A$19:$E$27,3)),0)`")
    impuesto_anual = if_func(base_imponible>0,(vlookup(base_imponible,ESCALAS_MATRIX[18:27],3)),0)
    _fmt = f"${impuesto_anual:,.2f}" if isinstance(impuesto_anual, (int, float)) else impuesto_anual
    mo.output.replace(mo.md(f"**Result:** `{_fmt}`"))
    return (impuesto_anual,)


@app.cell
def _(ESCALAS_MATRIX, base_imponible, if_func, mo, vlookup):
    mo.md("### B91 - Porcentaje\n**Formula:** `=IF(B86>0,VLOOKUP(B86,Escalas!$A$19:$E$27,4),0)`")
    porcentaje = if_func(base_imponible>0,vlookup(base_imponible,ESCALAS_MATRIX[18:27],4),0)
    _fmt = f"${porcentaje:,.2f}" if isinstance(porcentaje, (int, float)) else porcentaje
    mo.output.replace(mo.md(f"**Result:** `{_fmt}`"))
    return (porcentaje,)


@app.cell
def _(ESCALAS_MATRIX, base_imponible, if_func, mo, var_012026_b89, vlookup):
    mo.md("### B92 - Sobre excedente de\n**Formula:** `=IF(B86>0,(VLOOKUP(B$86,Escalas!$A$19:$E$27,5)*B89),0)`")
    sobre_excedente_de = if_func(base_imponible>0,(vlookup(base_imponible,ESCALAS_MATRIX[18:27],5)*var_012026_b89),0)
    _fmt = f"${sobre_excedente_de:,.2f}" if isinstance(sobre_excedente_de, (int, float)) else sobre_excedente_de
    mo.output.replace(mo.md(f"**Result:** `{_fmt}`"))
    return (sobre_excedente_de,)


@app.cell
def _(base_imponible, if_func, mo, sobre_excedente_de):
    mo.md("### B94 - Base cálculo\n**Formula:** `=IF(B86>0,+B86-B92,0)`")
    base_c_lculo = if_func(base_imponible>0,+base_imponible-sobre_excedente_de,0)
    _fmt = f"${base_c_lculo:,.2f}" if isinstance(base_c_lculo, (int, float)) else base_c_lculo
    mo.output.replace(mo.md(f"**Result:** `{_fmt}`"))
    return (base_c_lculo,)


@app.cell
def _(base_c_lculo, mo, porcentaje):
    mo.md("### B95 - % calculado\n**Formula:** `=+B91*B94`")
    calculado = porcentaje*base_c_lculo
    _fmt = f"${calculado:,.2f}" if isinstance(calculado, (int, float)) else calculado
    mo.output.replace(mo.md(f"**Result:** `{_fmt}`"))
    return (calculado,)


@app.cell
def _(calculado, impuesto_anual, mo):
    mo.md("### B97 - TOTAL IMPUESTO ANUAL\n**Formula:** `=+B90+B95`")
    total_impuesto_anual = impuesto_anual+calculado
    _fmt = f"${total_impuesto_anual:,.2f}" if isinstance(total_impuesto_anual, (int, float)) else total_impuesto_anual
    mo.output.replace(mo.md(f"**Result:** `{_fmt}`"))
    return (total_impuesto_anual,)


@app.cell
def _(impuesto_mes, mo):
    mo.md("### B99 - Acumulado\n**Formula:** `=+B103`")
    acumulado = impuesto_mes
    _fmt = f"${acumulado:,.2f}" if isinstance(acumulado, (int, float)) else acumulado
    mo.output.replace(mo.md(f"**Result:** `{_fmt}`"))
    return


@app.cell
def _(mo, total_impuesto_anual):
    mo.md("### B103 - Impuesto Mes\n**Formula:** `=+B97`")
    impuesto_mes = total_impuesto_anual
    _fmt = f"${impuesto_mes:,.2f}" if isinstance(impuesto_mes, (int, float)) else impuesto_mes
    mo.output.replace(mo.md(f"**Result:** `{_fmt}`"))
    return (impuesto_mes,)


if __name__ == "__main__":
    app.run()
