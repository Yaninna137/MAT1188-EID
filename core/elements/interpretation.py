'''
Genera la interpretación automática de resultados del modelo matemático.
'''

def Interpretation(datos):
    """
    Genera una interpretación automática a partir del conjunto de datos enviado.

    datos debe ser un diccionario con:
    {
        "C0": valor inicial C(0),
        "CT": valor C(T),
        "Cp0": derivada en t=0,
        "CpT": derivada en t=T,
        "S_T": costo acumulado en [0, T],
        "T": número de años
    }
    """

    C0 = datos["C0"]
    CT = datos["CT"]
    Cp0 = datos["Cp0"]
    CpT = datos["CpT"]
    S_T = datos["S_T"]
    T = datos["T"]

    interpretacion = ""

    # Crecimiento del costo mensual
    if Cp0 > 0 and CpT > Cp0:
        interpretacion += (
            "• El costo mensual crece de manera **acelerada**, lo que indica que "
            "el servidor demanda más recursos a medida que envejece.<br>"
        )
    elif Cp0 > 0 and CpT < Cp0:
        interpretacion += (
            "• El costo mensual aumenta, pero a un ritmo **cada vez menor**.<br>"
        )
    elif Cp0 < 0:
        interpretacion += (
            "• La función inicia con un costo decreciente, lo cual es **inusual** en modelos de mantención.<br>"
        )
    else:
        interpretacion += (
            "• La variación del costo no sigue un patrón claro.<br>"
        )

    # Comparacion de C(0) vs C(T)
    if CT > C0:
        interpretacion += (
            f"• Después de {T} años, el costo mensual pasó de {C0:.2f} a {CT:.2f}, "
            "mostrando un **aumento significativo**.<br>"
        )

    if CT > 2 * C0:
        interpretacion += (
            "• El costo final es **más del doble** del costo inicial. "
            "Esto suele ser indicio de desgaste severo del hardware.<br>"
        )

    # Interpretacion del costo acumulado
    if S_T > 4000:
        interpretacion += (
            f"• El costo acumulado total S(T) ≈ {S_T:.0f} USD es **muy elevado**, "
            "lo que sugiere que mantener el servidor es poco rentable.<br>"
        )
    elif S_T > 2000:
        interpretacion += (
            f"• El costo acumulado S(T) ≈ {S_T:.0f} USD indica que el gasto "
            "empieza a ser relevante para decisiones de reemplazo.<br>"
        )
    else:
        interpretacion += (
            f"• El costo acumulado S(T) ≈ {S_T:.0f} USD es **moderado** para el periodo analizado.<br>"
        )

    # Recomendacion final
    if CT > 2 * C0 or S_T > 3000:
        interpretacion += (
            "• Según el comportamiento del costo mensual y el costo acumulado, "
            f"se recomienda **evaluar el reemplazo entre los años {T-1} y {T}**.<br>"
        )
    else:
        interpretacion += (
            "• No se observa una presión inmediata para reemplazar el hardware; "
            "el sistema puede seguir operando sin problemas significativos.<br>"
        )

    return interpretacion