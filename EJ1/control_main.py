import os
from PyQt6 import QtWidgets, uic
from EJ1.psp1 import Ej1 

class MenuPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.carpeta_del_codigo = os.path.dirname(__file__)
        self.ruta_del_ui = os.path.join(self.carpeta_del_codigo, "menu_principal (1).ui")

        uic.loadUi(self.ruta_del_ui, self)

        self.pushButton.clicked.connect(self.ejecutar_calculo_regresion)

    def ejecutar_calculo_regresion(self):
        self.x_vals = []
        self.y_vals = []
        
        for i in range(10):
            self.item_x = self.tableWidget.item(0, i)
            self.item_y = self.tableWidget.item(1, i)

            self.x_vals.append(float(self.item_x.text()))
            self.y_vals.append(float(self.item_y.text()))

        if self.lineEdit.text() == "":
            self.xk_val = 386.0
        else:
            self.xk_val = float(self.lineEdit.text())

        ej = Ej1(self.x_vals, self.y_vals, self.xk_val)
        ej.calcular()

        self.lineEdit_2.setText(str(round(ej.b0, 8)))
        self.lineEdit_3.setText(str(round(ej.b1, 8)))
        self.lineEdit_4.setText(str(round(ej.r2, 8)))
        self.lineEdit_5.setText(str(round(ej.r_xy, 8)))
        self.lineEdit_6.setText(str(round(ej.yk, 8)))