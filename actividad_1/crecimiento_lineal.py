import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from euler import euler
import matplotlib.pyplot as plt

def f(t, x):
    return 1

def solucion(t):
    return t

fig, axes = plt.subplots(2, 2, figsize=(12, 8), sharex=True, sharey=True)
axes = axes.flatten()

axes[0].plot(
    [0, 10],
    [solucion(0), solucion(10)],
    color="black",
    linewidth=2,
)
axes[0].set_title("Solución exacta")

for ax, h, color in zip(
    axes[1:],
    (1, 0.5, 0.1),
    ("tab:blue", "tab:orange", "tab:green"),
):
    t_values, x_values, steps = euler(f, 0, 0, 10, h)
    ax.plot(
        t_values,
        x_values,
        linestyle="-",
        color=color,
    )
    ax.set_title(f"Aproximación de Euler (h={h})")

for ax in axes:
    ax.set_xlabel("t")
    ax.set_ylabel("x(t)")
    ax.grid(True)

fig.suptitle("Solución y aproximaciones de Euler")
fig.tight_layout()
plt.show()
