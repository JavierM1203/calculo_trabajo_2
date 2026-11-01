import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from metodos_euler import euler
import matplotlib.pyplot as plt
import math

plt.rcParams.update({"font.size": 14})

V0 = 1000
organizaciones = (
    ("A", 0.1, "tab:blue"),
    ("B", 0.3, "tab:orange"),
    ("C", 0.7, "tab:green"),
)
valores_h = (
    (1, "tab:blue"),
    (0.5, "tab:orange"),
    (0.1, "tab:green"),
)
tiempos_consulta = [5, 10, 15]

def solucion(t, k):
    return V0 * math.exp(-k * t)

def valor_en(valores_t, valores_x, t_buscado):
    indice = min(
        range(len(valores_t)),
        key=lambda i: abs(valores_t[i] - t_buscado),
    )
    return valores_x[indice]


# Figura 1: aproximaciones de Euler para cada organización
# Figuras 1, 2 y 3: aproximaciones de Euler para cada organización
t_exacta = [i / 50 for i in range(1001)]

for nombre, k, _ in organizaciones:
    def f(t, V, k=k):
        return -k * V

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(
        t_exacta,
        [solucion(t, k) for t in t_exacta],
        label="Solución de referencia",
        color="black",
        linewidth=2.5,
    )
    for h, color in valores_h:
        valores_t, valores_V, _ = euler(f, V0, 0, 20, h)
        ax.plot(
            valores_t,
            valores_V,
            marker="o" if h == 1 else None,
            markersize=5,
            color=color,
            label=f"Euler (h = {h})",
        )
    ax.set_title(f"Organización {nombre} (k = {k})")
    ax.set_xlabel("Tiempo t")
    ax.set_ylabel("Equipos vulnerables V(t)")
    ax.grid(True)
    ax.legend()
    fig.tight_layout()
    plt.show()

# Figura 2: comparación entre organizaciones (h = 0.1)
fig, ax = plt.subplots(figsize=(10, 6))

for nombre, k, color in organizaciones:
    def f(t, V, k=k):
        return -k * V

    valores_t, valores_V, _ = euler(f, V0, 0, 20, 0.1)
    ax.plot(
        valores_t,
        valores_V,
        color=color,
        linewidth=2.5,
        label=f"Organización {nombre} (k = {k})",
    )

ax.set_xlabel("Tiempo t")
ax.set_ylabel("Equipos vulnerables V(t)")
ax.grid(True)
ax.legend()
fig.tight_layout()
plt.show()


# Tablas: valores y errores absolutos en t = 5, 10, 15
for nombre, k, _ in organizaciones:
    def f(t, V, k=k):
        return -k * V

    print(f"\nOrganización {nombre} (k = {k})")
    print(
        f"{'t':>3} | {'V ref':>8} | {'h':>4} | {'V aprox':>8} | "
        f"{'Error':>8} | {'Pasos':>5}"
    )
    print("-" * 52)
    for t in tiempos_consulta:
        for h, _ in valores_h:
            valores_t, valores_V, pasos = euler(f, V0, 0, 20, h)
            V_aprox = valor_en(valores_t, valores_V, t)
            error = abs(solucion(t, k) - V_aprox)
            print(
                f"{t:3d} | {solucion(t, k):8.2f} | {h:4g} | {V_aprox:8.2f} | "
                f"{error:8.2f} | {pasos:5d}"
            )