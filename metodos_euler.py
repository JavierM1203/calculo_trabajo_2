

def euler(f, x0, t0, tf, h):
    valores_t = [t0]
    valores_x = [x0]
    
    t = t0
    x = x0
    pasos = 0
    
    while t < tf:
        x += h * f(t, x)
        t += h
        pasos += 1
        
        valores_t.append(t)
        valores_x.append(x)
    
    return valores_t, valores_x, pasos

def euler_mejorado(f, x0, t0, tf, h):
    valores_t = [t0]
    valores_x = [x0]
    
    t = t0
    x = x0
    pasos = 0
    
    while t < tf:
        k1 = h * f(t, x)
        k2 = h * f(t + h, x + k1)
        x += (k1 + k2) / 2
        t += h
        pasos += 1
        
        valores_t.append(t)
        valores_x.append(x)
    
    return valores_t, valores_x, pasos