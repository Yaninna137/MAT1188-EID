'''
En esta carpeta se debe crear las funcioanlidades operativas de la matematicas
para un mejor rendimiento utilzar POO
DEjo un ejemplo de como debera estructurar la primer parte
Fragmento de otro codigo
'''
from dataclasses import dataclass
from math import cos, sin, pi
import sympy as sp
import numpy as np

@dataclass
class Elipse:
    h: int
    k: int
    a: int
    b: int
    orientacion: str  # 'horizontal' o 'vertical'

    def __post_init__(self):
        if self.a == 0 and self.b == 0:
            raise ValueError("No es posible evualuar porque a y b son 0")
        if self.a == 0:
            raise ValueError("No es posible evaluar porque a es 0 ")
        if self.b == 0:
            raise ValueError("No es posible evaluar porque b es 0")
        if self.a < 0 or self.b < 0:
            raise ValueError("Los valores de 'a' y 'b' deben ser positivos.")
        

class ModeloCosto:
    def __init__(self, funcion_str: str):
        self.t = sp.Symbol("t", real=True)
        
        funcion_str = funcion_str.replace("^", "**").strip()
        
        try:
            self.funcion = sp.sympify(funcion_str)
        except Exception:
            raise ValueError("La función ingresada no es válida. Usa sintaxis de Python/SymPy, ejemplo: 2*t**2 + 5*t + 10")
        
        if not self.funcion.free_symbols:
            raise ValueError("La función debe depender de t.")
        
        self.derivada = sp.diff(self.funcion, self.t)
        self.integral_indef = sp.integrate(self.funcion, self.t)
        
        self.funcion_num = sp.lambdify(self.t, self.funcion, "numpy")
        self.derivada_num = sp.lambdify(self.t, self.derivada, "numpy")

    def evaluar_C(self, t_val):
        return float(self.funcion_num(t_val))

    def evaluar_Cp(self, t_val):
        return float(self.derivada_num(t_val))

    def costo_acumulado(self, T):
        t_vals = np.linspace(0, T, 400)
        y_vals = self.funcion_num(t_vals)

        area = np.trapz(y_vals, t_vals)

        return float(12 * area)

    def generar_tabla(self, T):
        datos = []
        for i in range(T + 1):
            C = self.evaluar_C(i)
            Cp = self.evaluar_Cp(i)
            S = self.costo_acumulado(i)
            datos.append([i, C, Cp, S])
        return datos
