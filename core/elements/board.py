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
        "costo mantencion C(t) (USD)": valores_funcion,
    }

    # Si el modelo tiene derivada, la usamos
    if hasattr(modelo, "evaluar_Cp"):
        derivada_funcion = [modelo.evaluar_Cp(t) for t in tiempos]
        data["tasa de crecimiento C'(t) (USD/año)"] = derivada_funcion

    # Si el modelo tiene método de costo acumulado, lo usamos
    if hasattr(modelo, "costo_acumulado"):
        costo_acumulado = [round(modelo.costo_acumulado(t), 2) for t in tiempos]
        data["Costo acumulado S(t) (USD)"] = costo_acumulado

    df = pd.DataFrame(data)
    
    # Formatear columnas monetarias con símbolo de dólar
    for col in df.columns:
        if "USD" in col and col != "Tiempo":
            df[col] = df[col].apply(lambda x: f"${x:,.2f}")
    
    return df