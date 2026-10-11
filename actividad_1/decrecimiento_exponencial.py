import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from euler import euler
import matplotlib.pyplot as plt
import math

def f(t, x):
    return -solucion(t)

def solucion(t):
    return math.exp(-t)

t_exacta = [i / 100 for i in range(1001)]
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(
    t_exacta,
    [solucion(t) for t in t_exacta],
    label="Solución exacta",
    color="black",
    linewidth=2,
)

for h, color in (
    (1, "tab:blue"),
    (0.5, "tab:orange"),
    (0.1, "tab:green"),
    (0.01, "tab:red"),
):
    t_values, x_values, _ = euler(f, 1, 0, 10, h)
    ax.plot(
        t_values,
        x_values,
        linestyle="-",
        color=color,
        label=f"Euler (h={h})",
    )

ax.set_xlabel("t")
ax.set_ylabel("x(t)")
ax.set_title("Decaimiento exponencial: solución y aproximaciones de Euler")
ax.grid(True)
ax.legend()
fig.tight_layout()
plt.show()
