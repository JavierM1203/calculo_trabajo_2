import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from metodos_euler import euler
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 14})

V0 = 1000
k = 0.3
h = 0.1
valores_lambda = (
    (0, "tab:blue"),
    (50, "tab:orange"),
    (100, "tab:green"),
    (200, "tab:red"),
)
tiempos_consulta = [5, 10, 15, 20]

def valor_en(valores_t, valores_x, t_buscado):
    indice = min(
        range(len(valores_t)),
        key=lambda i: abs(valores_t[i] - t_buscado),
    )
    return valores_x[indice]


fig, ax = plt.subplots(figsize=(10, 6))
resultados = []

for lam, color in valores_lambda:
    def f(t, V, lam=lam):
        return lam - k * V

    valores_t, valores_V, _ = euler(f, V0, 0, 20, h)
    ax.plot(
        valores_t,
        valores_V,
        color=color,
        linewidth=2.5,
        label=f"λ = {lam}",
    )
    # Valor de equilibrio V = λ / k (donde V'(t) = 0)
    ax.axhline(lam / k, color=color, linestyle="--", linewidth=1.5)
    resultados.append((lam, [valor_en(valores_t, valores_V, t) for t in tiempos_consulta]))

ax.set_title("Equipos vulnerables con aparición de nuevas vulnerabilidades (k = 0.3)")
ax.set_xlabel("Tiempo t")
ax.set_ylabel("Equipos vulnerables V(t)")
ax.grid(True)
ax.legend()
fig.tight_layout()
plt.show()

print(f"{'λ':>5} | {'λ/k':>7} | " + " | ".join(f"{'t = ' + str(t):>8}" for t in tiempos_consulta))
print("-" * 55)
for lam, valores in resultados:
    print(f"{lam:5d} | {lam / k:7.2f} | " + " | ".join(f"{v:8.2f}" for v in valores))