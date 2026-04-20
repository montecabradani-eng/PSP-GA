import os
from PyQt6 import QtWidgets, uic
from EJ1.psp1 import Ej1 

class VentanaPSP(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        
        uic.loadUi("ventana_psp (2).ui", self)

        self.tableWidget.setRowCount(2)
        self.tableWidget.setColumnCount(10)
        
        self.label_9.setText("")
        self.label_8.setText("")
        self.label_12.setText("")
        self.label_10.setText("")
        self.label_11.setText("")

        self.est_proxy = [130, 650, 99, 150, 128, 302, 95, 945, 368, 961]
        self.plan_added = [163, 765, 141, 166, 137, 355, 136, 1206, 433, 1130]
        self.act_added = [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601]
        self.act_hours = [15.0, 69.9, 6.5, 22.4, 28.4, 65.9, 19.4, 198.7, 38.8, 138.2]

        self.pushButton.clicked.connect(self.test_1)
        self.pushButton_3.clicked.connect(self.test_2)
        self.pushButton_2.clicked.connect(self.test_3)
        self.pushButton_4.clicked.connect(self.test_4)
        self.pushButton_5.clicked.connect(self.procesar_calculo)


    def test_1(self):
        self.llenar_tabla(self.est_proxy, self.act_added)

    def test_2(self):
        self.llenar_tabla(self.est_proxy, self.act_hours)

    def test_3(self):
        self.llenar_tabla(self.plan_added, self.act_added)

    def test_4(self):
        self.llenar_tabla(self.plan_added, self.act_hours)

    def llenar_tabla(self, datos_x, datos_y):
        for i in range(10):
            self.item_x = QtWidgets.QTableWidgetItem(str(datos_x[i]))
            self.item_y = QtWidgets.QTableWidgetItem(str(datos_y[i]))
            self.tableWidget.setItem(0, i, self.item_x)
            self.tableWidget.setItem(1, i, self.item_y)

    def procesar_calculo(self):
        self.x_vals = []
        self.y_vals = []
        
        for i in range(10):
            self.texto_x = self.tableWidget.item(0, i).text()
            self.texto_y = self.tableWidget.item(1, i).text()
            self.x_vals.append(float(self.texto_x))
            self.y_vals.append(float(self.texto_y))

        if self.lineEdit.text() == "":
            xk_val = 386.0
        else:
            xk_val = float(self.lineEdit.text())

        ej = Ej1(self.x_vals, self.y_vals, self.xk_val)
        ej.calcular()

        self.label_9.setText(str(round(ej.b1, 8)))
        self.label_8.setText(str(round(ej.b0, 8)))
        self.label_12.setText(str(round(ej.r_xy, 8)))
        self.label_10.setText(str(round(ej.r2, 8)))
        self.label_11.setText(str(round(ej.yk, 8)))