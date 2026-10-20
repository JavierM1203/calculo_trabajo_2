import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from metodos_euler import euler
import matplotlib.pyplot as plt
import math

def f(t, x):
    return -solucion(t)

def solucion(t):
    return math.exp(-t)


valores_h = [1, 0.5, 0.1, 0.05, 0.01]

plt.figure(figsize=(10, 6))
resultados = []

for h in valores_h:
    valores_t, valores_x, pasos = euler(f, 1, 0, 10, h)
    errores = [
        abs(x_aprox - solucion(t))
        for t, x_aprox in zip(valores_t, valores_x)
    ]
    plt.plot(valores_t, errores, label=f"Euler (h = {h})")
    resultados.append((h, pasos, errores[-1], max(errores)))

print(f"{'h':>8} | {'Número de pasos':>15} | {'Error final':>14} | {'Error máximo':>14}")
print("-" * 63)
for h, pasos, error_final, error_maximo in resultados:
    print(
        f"{h:8g} | {pasos:15d} | "
        f"{error_final:14.8g} | {error_maximo:14.8g}"
    )

plt.xlabel("t")
plt.ylabel("Error absoluto")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()