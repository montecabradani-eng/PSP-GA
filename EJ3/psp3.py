import math

class InversaPsp3:
    def __init__(self, p_dest, grados):
        self.p_dest = p_dest
        self.grados = grados
        
        self.x = 1.0
        self.d = 0.5
        self.error = 0.0000001
        #el numéro tan grande aquí es para que las x sean más precisas, mientras más 0 
        # más preciso pero también con muchos ceros se me traba 

    def ct(self, v_x):
        t1 = math.gamma((self.grados + 1) / 2)
        t2 = math.sqrt(self.grados * math.pi) * math.gamma(self.grados / 2)
        c = t1 / t2
        b = (1 + (v_x**2 / self.grados))
        e = -(self.grados + 1) / 2
        
        return c * (b ** e)

    def simpson(self, x_fin):
        n = 1000
        h = x_fin / n
        
        s = self.ct(0) + self.ct(x_fin)

        for i in range(1, n):
            px = i * h
            if i % 2 == 0:
                s = s + 2 * self.ct(px)
            else:
                s = s + 4 * self.ct(px)

        return (h / 3) * s

    def buscar(self):
        self.pact = self.simpson(self.x)
        
        if (self.pact - self.p_dest) > 0:
            self.siga = 1 
        else: 
            self.siga = -1

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