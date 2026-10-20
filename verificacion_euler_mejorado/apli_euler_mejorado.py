import sys
from pathlib import Path
import math
sys.path.append(str(Path(__file__).resolve().parent.parent))
from metodos_euler import euler, euler_mejorado

def f(t, x):
    return -solucion(t)

def solucion(t):
    return math.exp(-t)

valores_h = [1, 0.5, 0.1]

metodos = (
    ("Euler", euler),
    ("Euler mejorado", euler_mejorado),
)

print(
    f"{'Método':<18} | {'h':>8} | {'Valor final':>14} | "
    f"{'Error final':>14} | {'Pasos':>5}"
)
print("-" * 72)

for nombre_metodo, metodo in metodos:
    for h in valores_h:
        valores_t, valores_x, pasos = metodo(f, 1, 0, 10, h)
        valor_final = valores_x[-1]
        error_final = abs(valor_final - solucion(valores_t[-1]))

        print(
            f"{nombre_metodo:<18} | {h:8g} | {valor_final:14.8g} | "
            f"{error_final:14.8g} | {pasos:5d}"
        )