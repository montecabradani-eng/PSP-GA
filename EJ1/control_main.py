from PyQt6 import QtWidgets, uic
from EJ1.psp1 import Ej1 
# Llamas de psp1 la clase para poder heredar sus funciones

class MenuPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        uic.loadUi("EJ1/ui1/menu_principal (1).ui", self)

        self.pushButton.clicked.connect(self.clical)

    def clical(self):
        x = []
        y = []

        for i in range(10):
            dato_x = self.tableWidget.item(0, i).text()
            dato_y = self.tableWidget.item(1, i).text()
            # aquí solamente te asocia los datos en "x" y "y" de la tabla, básicamente lee los valores asociados en las casillas para 
            # tomar los valores
            
            x.append(float(dato_x))
            y.append(float(dato_y))
            # para convertir el dato de texto de la tabla en número

        if self.lineEdit.text() == "":
            valor_xk = 386.0    #indica que el valor xk por defecto es de 386 si el cuadro está vacío
        else:
            valor_xk = float(self.lineEdit.text()) #con esto te permite modificar el valor si así lo requieres

        ejer1 = Ej1(x, y, valor_xk)
        ejer1.calcular()
        # esto hace que toma los valores que le llegaron de x, y y xk para poder hacer el calculo de psp1 y así
        # sacar los resultados

        self.lineEdit_2.setText(str(round(ejer1.b0, 4)))
        self.lineEdit_2.setStyleSheet("color: black;")
        self.lineEdit_3.setText(str(round(ejer1.b1, 4)))
        self.lineEdit_3.setStyleSheet("color: black;")
        self.lineEdit_4.setText(str(round(ejer1.r2, 4)))
        self.lineEdit_4.setStyleSheet("color: black;")
        self.lineEdit_5.setText(str(round(ejer1.r_xy, 4)))
        self.lineEdit_5.setStyleSheet("color: black;")
        self.lineEdit_6.setText(str(round(ejer1.yk, 4)))
        self.lineEdit_6.setStyleSheet("color: black;")
        # llena las lineas de texto del programa con lo que corresponde en b0, b1, rxy, r2 y así. El round es para reondear
        # y aquí indico que son para 4 decimales