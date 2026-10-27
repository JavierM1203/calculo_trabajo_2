import sys
import math
from pathlib import Path
import matplotlib.pyplot as plt
sys.path.append(str(Path(__file__).resolve().parent.parent))
from metodos_euler import euler, euler_mejorado
from runge_kutta_4 import RK4

def f(t, x):
    return x * (1 - x)

def solucion(t):
    exponencial = math.exp(t - t0)
    return x0 * exponencial / (1 - x0 + x0 * exponencial)

metodos = (
    ("Euler", euler),
    ("Euler mejorado", euler_mejorado),
    ("Runge-Kutta 4", RK4)
)

h = 0.5 # Modificar tamaño de paso
t0 = 0
tf = 8
x0 = 0.1

fig, ax = plt.subplots(figsize=(10, 6))
t_exacta = [t0 + (tf - t0) * i / 100 for i in range(101)]
ax.plot(
    t_exacta,
    [solucion(t) for t in t_exacta],
    label="Solución exacta",
    color="black",
    linestyle="--",
)

fig_error, ax_error = plt.subplots(figsize=(10, 6))
for nombre, metodo in metodos:
    valores_t, valores_x, _ = metodo(f, x0, t0, tf, h)
    ax.plot(valores_t, valores_x, label=nombre)
    errores = [
        abs(x_aproximado - solucion(t))
        for t, x_aproximado in zip(valores_t, valores_x)
    ]
    ax_error.plot(valores_t, errores, label=nombre)

ax.set_title(f"Comparación de métodos numéricos (h = {h})")
ax.set_xlabel("t")
ax.set_ylabel("x(t)")
ax.grid(True)
ax.legend()
fig.tight_layout()

ax_error.set_title(f"Error absoluto en función de t (h = {h})")
ax_error.set_xlabel("t")
ax_error.set_ylabel("|x aproximado - x exacto|")
ax_error.grid(True)
ax_error.legend()
fig_error.tight_layout()
plt.show()