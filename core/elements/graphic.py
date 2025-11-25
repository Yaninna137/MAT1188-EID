import plotly.graph_objects as go
import numpy as np

'''
Crear los gráficos de cada sección usando Plotly
'''

def GRAPHIC_A(modelo, T):
    t = np.linspace(0, T, 100)
    y = [modelo.evaluar_C(x) for x in t]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t, y=y, mode='lines', name='C(t)'))
    fig.update_layout(
        title="Función C(t)",
        xaxis_title="t (años)",
        yaxis_title="Costo mensual",
        template="plotly_white"
    )
    return fig


def GRAPHIC_B(modelo, T, xy_evaluado=None):
    # === Gráfico de C'(t) - Análisis con derivadas
    t = np.linspace(0, T, 100)
    y = [modelo.evaluar_Cp(x) for x in t]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t, y=y, mode='lines', name="C'(t)", line=dict(color='orange')))

    if xy_evaluado:
        fig.add_trace(go.Scatter(
            x=[xy_evaluado[0]], 
            y=[xy_evaluado[1]], 
            mode='markers', 
            marker=dict(color='red', size=10),
            name=f"C'({xy_evaluado[0]:.2f})"
        ))

    fig.update_layout(
        title="Derivada de C(t)",
        xaxis_title="t (años)",
        yaxis_title="Tasa de cambio del costo",
        template="plotly_white"
    )

    return fig


def GRAPHIC_C(modelo, T):
    # === Gráfico de la integral acumulada S(t)
    t_vals = np.linspace(0, T, 200)

    S_vals = []
    for t in t_vals:
        S_vals.append(modelo.costo_acumulado(t))

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t_vals, y=S_vals, mode='lines', name='S(t)'))
    fig.update_layout(
        title="Costo acumulado S(t)",
        xaxis_title="t (años)",
        yaxis_title="Costo acumulado",
        template="plotly_white"
    )

    return fig


def GRAPHIC_D(modelo, T):
    """
    Gráfico del área bajo la curva C(t) desde t=0 hasta t=T
    """
    t_vals = np.linspace(0, T, 400)
    C_vals = [modelo.evaluar_C(t) for t in t_vals]

    fig = go.Figure()
    
    # Área bajo la curva
    fig.add_trace(go.Scatter(
        x=t_vals, 
        y=C_vals, 
        fill='tozeroy', 
        mode='lines',
        name='C(t)',
        fillcolor='rgba(0, 100, 250, 0.3)',
        line=dict(width=2)
    ))

    fig.update_layout(
        title="Área bajo la curva C(t)",
        xaxis_title="t (años)",
        yaxis_title="Costo mensual",
        template="plotly_white"
    )

    return fig