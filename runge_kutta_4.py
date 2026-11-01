
def RK4(f, x0, t0, tf, h):
    valores_t = [t0]
    valores_x = [x0]
    
    t = t0
    x = x0
    pasos = 0
    
    while t < tf:
        k1 = f(t, x)
        k2 = f(t + (h / 2), x + (k1 * (h / 2)))
        k3 = f(t + (h / 2), x + (k2 * (h / 2)))
        k4 = f(t + h, x + (h * k3))
        
        x += (k1 + (2 * k2) + (2 * k3) + k4) * h / 6
        t += h
        pasos += 1
        
        valores_t.append(t)
        valores_x.append(x)
    
    return valores_t, valores_x, pasos