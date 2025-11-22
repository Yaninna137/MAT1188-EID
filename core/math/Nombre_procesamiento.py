'''
En esta carpeta se debe crear las funcioanlidades operativas de la matematicas
para un mejor rendimiento utilzar POO
DEjo un ejemplo de como debera estructurar la primer parte
Fragmento de otro codigo
'''
from dataclasses import dataclass
from math import cos, sin, pi

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