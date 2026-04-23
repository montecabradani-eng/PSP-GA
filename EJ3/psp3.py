import math

class InversaPsp3:
    def __init__(self, p_dest, grados):
        self.p_dest = p_dest
        self.grados = grados
        
        self.x = 1.0
        self.d = 0.5
        # Error más pequeño para mayor precisión (7 decimales)
        self.error = 0.0000001 

    def curva_t(self, v_x):
        # Cálculos de la distribución t
        t1 = math.gamma((self.grados + 1) / 2)
        t2 = math.sqrt(self.grados * math.pi) * math.gamma(self.grados / 2)
        c = t1 / t2
        b = (1 + (v_x**2 / self.grados))
        e = -(self.grados + 1) / 2
        
        return c * (b ** e)

    def simpson(self, x_fin):
        # Aumentamos n a 1000 para que la integral sea mucho más exacta
        n = 1000
        h = x_fin / n
        
        s = self.curva_t(0) + self.curva_t(x_fin)

        for i in range(1, n):
            px = i * h
            if i % 2 == 0:
                s = s + 2 * self.curva_t(px)
            else:
                s = s + 4 * self.curva_t(px)

        return (h / 3) * s

    def buscar(self):
        self.pact = self.simpson(self.x)
        
        if (self.pact - self.p_dest) > 0:
            self.siga = 1 
        else: 
            self.siga = -1

        # Bucle de búsqueda de X
        while abs(self.pact - self.p_dest) > self.error:
            if self.pact < self.p_dest:
                self.x = self.x + self.d
            else:
                self.x = self.x - self.d

            self.pact = self.simpson(self.x)
            
            if (self.pact - self.p_dest) > 0:
                sigh = 1
            else:
                sigh = -1
            
            if sigh != self.siga:
                self.d = self.d / 2
                self.siga = sigh
                
        return self.x