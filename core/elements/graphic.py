import matplotlib.pyplot as plt
import numpy as np

'''
Crear los graficos de cada seccion
'''

def GRAPHIC_A(modelo, T):
    t = np.linspace(0, T, 100)
    print([modelo.evaluar_C(x) for x in t])
    y = [modelo.evaluar_C(x) for x in t]

    fig, ax = plt.subplots()
    ax.plot(t, y)
    ax.set_title("Función C(t)")
    ax.set_xlabel("t (años)")
    ax.set_ylabel("Costo mensual")
    return fig


def GRAPHIC_B():
    # === Gráfico de C()t - Análisi con Derivadas
    pass

def GRAPHIC_C(modelo, T):
    t_vals = np.linspace(0, T, 200)

    S_vals = []
    for t in t_vals:
        S_vals.append(modelo.costo_acumulado(t))

    fig, ax = plt.subplots()
    ax.plot(t_vals, S_vals)
    ax.set_title("Costo acumulado S(t)", fontsize=14)
    ax.set_xlabel("t (años)")
    ax.set_ylabel("Costo acumulado")

    return fig

def GRAPHIC_D(modelo, T):
    """
    Gráfico del área bajo la curva C(t) desde t=0 hasta t=T
    """

    t_vals = np.linspace(0, T, 400)
    C_vals = [modelo.evaluar_C(t) for t in t_vals]

    fig, ax = plt.subplots()

    ax.plot(t_vals, C_vals, linewidth=2)

    ax.fill_between(t_vals, C_vals, alpha=0.3)

    ax.set_title("Área bajo la curva C(t)", fontsize=14)
    ax.set_xlabel("t (años)")
    ax.set_ylabel("Costo mensual")

    return fig