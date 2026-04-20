class Ej1(object):
    def __init__(self, data_x, data_y, xk=386):
        self.x = data_x
        self.y = data_y
        self.n = len(self.x)
        self.xk = xk
        self.b1 = 0.0
        self.b0 = 0.0
        self.r_xy = 0.0
        self.r2 = 0.0
        self.yk = 0.0

    def calcular(self):
        if self.n == 0:
            return

        self.sum_x = sum(self.x)
        self.sum_y = sum(self.y)
        self.sum_x2 = sum(xi**2 for xi in self.x)
        self.sum_y2 = sum(yi**2 for yi in self.y)
        self.sum_xy = sum(self.x[i] * self.y[i] for i in range(self.n))
        self.numerador_b1 = (self.n * self.sum_xy) - (self.sum_x * self.sum_y)
        self.denominador_b1 = (self.n * self.sum_x2) - (self.sum_x**2)
        
        if self.denominador_b1 != 0:
            self.b1 = self.numerador_b1 / self.denominador_b1
        else:
            self.b1 = 0.0
        
        self.b0 = (self.sum_y - (self.b1 * self.sum_x)) / self.n
        self.numerador_r = (self.n * self.sum_xy) - (self.sum_x * self.sum_y)
        self.termino1 = (self.n * self.sum_x2) - (self.sum_x**2)
        self.termino2 = (self.n * self.sum_y2) - (self.sum_y**2)
        self.denominador_r = (self.termino1 * self.termino2)**0.5
        
        if self.denominador_r != 0:
            self.r_xy = self.numerador_r / self.denominador_r
        else:
            self.r_xy = 0.0
        

        self.r2 = self.r_xy ** 2
        self.yk = self.b0 + (self.b1 * self.xk)