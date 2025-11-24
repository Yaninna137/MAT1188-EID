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


def GRAPHIC_B(modelo, T, xy_evaluado=None):
    # === Gráfico de C()t - Análisi con Derivadas
    t = np.linspace(0, T, 100)
    y = [modelo.evaluar_Cp(x) for x in t]

    fig, ax = plt.subplots(figsize=(4,3))
    if xy_evaluado:
        plt.scatter([xy_evaluado[0]], [xy_evaluado[1]], color='red', zorder=5)
    ax.plot(t, y, color='orange')
    ax.set_title("Derivada de C(t)")
    ax.set_xlabel("t (años)")
    ax.set_ylabel("Tasa de cambio del costo")
    return fig

    
def GRAPHIC_C():
    # === Gráfico de la integral acumulada - Costo acumulado
    pass
def GRAPHIC_D():
    # === Gráfico de Área bajo la curva(t) - Costo acumulado
    pass
