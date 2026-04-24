import math
from EJ1.psp1 import Ej1
from EJ3.psp3 import InversaPsp3

def calcular_psp4(datos_x, datos_y, x_k):
    n = len(datos_x)
    gl = n - 2
    
    if gl <= 0:
        return None

    reg = Ej1(datos_x, datos_y, x_k)
    reg.calcular()
    b0, b1 = reg.b0, reg.b1
    
    yk = b0 + (b1 * x_k)
    
    suma_ec = sum([(datos_y[i] - (b0 + b1 * datos_x[i]))**2 for i in range(n)])
    sigma = math.sqrt(suma_ec / gl)
    
    t = InversaPsp3(0.35, gl).buscar()
    
    avg_x = sum(datos_x) / n
    sum_var_x = sum([(xi - avg_x)**2 for xi in datos_x])
    
    if sum_var_x == 0:
        raiz = math.sqrt(1 + (1/n))
    else:
        raiz = math.sqrt(1 + (1/n) + ((x_k - avg_x)**2 / sum_var_x))
        
    rango = t * sigma * raiz
    
    return {
        "y_k": yk,
        "sigma": sigma,
        "valor_t": t,
        "rango": rango,
        "lpi": yk - rango,
        "upi": yk + rango
    }