import pandas as pd
import numpy as np

def board(modelo, T, num_puntos):
    """
    Crea una tabla con valores de tiempo, función, derivada y costo acumulado
    a partir del modelo matemático.
    """
    tiempos = np.linspace(0, T, num_puntos)

    # Siempre calculamos C(t) desde el modelo
    valores_funcion = [modelo.evaluar_C(t) for t in tiempos]

    data = {
        "Tiempo": tiempos,
        "Valor función C(t)": valores_funcion,
    }

    # Si el modelo tiene derivada, la usamos
    if hasattr(modelo, "evaluar_C_derivada"):
        derivada_funcion = [modelo.evaluar_C_derivada(t) for t in tiempos]
        data["Derivada C'(t)"] = derivada_funcion

    # Si el modelo tiene método de costo acumulado, lo usamos
    if hasattr(modelo, "evaluar_costo_acumulado"):
        costo_acumulado = [modelo.evaluar_costo_acumulado(t) for t in tiempos]
        data["Costo acumulado S(t)"] = costo_acumulado

    df = pd.DataFrame(data)
    return df