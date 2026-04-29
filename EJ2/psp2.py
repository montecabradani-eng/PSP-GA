import math

class Intnum:
    def __init__(self, x, dof):
        self.x = x
        self.dof = dof
        self.error_aceptable = 0.00000001

    def funt(self, x):
        term1 = math.gamma((self.dof + 1) / 2)
        term2 = (math.sqrt(self.dof * math.pi) * math.gamma(self.dof / 2))
        constante = term1 / term2

        exponente = -(self.dof + 1) / 2
        base = (1 + (x**2 / self.dof))
        
        return constante * (base ** exponente)

    def calint(self):
        num_seg = 10
        resant = 0.0
        error = 1.0
        resact = 0.0
        
        while error > self.error_aceptable:
            W = self.x / num_seg
            sumatoria = self.funt(0) + self.funt(self.x)
            
            for i in range(1, num_seg):
                valor_x = i * W
                if i % 2 == 0:
                    sumatoria += 2 * self.funt(valor_x)
                else:
                    sumatoria += 4 * self.funt(valor_x)
            
            resact = (W / 3) * sumatoria
            error = abs(resact - resant)
            
            if error > self.error_aceptable:
                resant = resact
                num_seg *= 2 
            
        return resact