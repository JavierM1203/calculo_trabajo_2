import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 14})

V0 = 1000
n_max = 10

def modelo_discreto(V0, hk, n_max):
    # V_{n+1} = (1 - hk) V_n
    valores_V = [V0]
    for n in range(n_max):
        valores_V.append((1 - hk) * valores_V[-1])
    return valores_V

def graficar(valores_hk, titulo):
    fig, ax = plt.subplots(figsize=(10, 6))
    valores_n = range(n_max + 1)
    for hk, color in zip(valores_hk, ("tab:blue", "tab:orange", "tab:green")):
        ax.plot(
            valores_n,
            modelo_discreto(V0, hk, n_max),
            marker="o",
            color=color,
            label=f"hk = {hk}",
        )
    ax.axhline(0, color="black", linewidth=1)
    ax.set_title(titulo)
    ax.set_xlabel("Paso n")
    ax.set_ylabel("Equipos vulnerables $V_n$")
    ax.grid(True)
    ax.legend()
    fig.tight_layout()
    plt.show()

graficar((0.3, 0.7, 1), "Modelo discreto con 0 < hk ≤ 1")
graficar((1.5, 2, 2.2), "Modelo discreto con hk > 1")

for hk in (0.3, 0.7, 1, 1.5, 2, 2.2):
    valores_V = modelo_discreto(V0, hk, n_max)
    print(f"hk = {hk}: " + ", ".join(f"{v:.1f}" for v in valores_V[:5]) + f", ..., V_10 = {valores_V[-1]:.2f}")