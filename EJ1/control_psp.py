import os
from PyQt6 import QtWidgets, uic
from EJ1.psp1 import Ej1 

class VentanaPSP(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_ui = os.path.join(directorio_actual, "ventana_psp (2).ui")

        try:
            uic.loadUi(ruta_ui, self)
        except Exception as e:
            print(f"Error crítico: No se encontró el archivo UI en {ruta_ui}")

        self.tableWidget.setRowCount(2)
        self.tableWidget.setColumnCount(10)
        for r in range(2):
            for c in range(10):
                if not self.tableWidget.item(r, c):
                    self.tableWidget.setItem(r, c, QtWidgets.QTableWidgetItem("0"))
        
        self.label_9.setText("")
        self.label_8.setText("")
        self.label_12.setText("")
        self.label_10.setText("")
        self.label_11.setText("")

        self.est_proxy = [130, 650, 99, 150, 128, 302, 95, 945, 368, 961]
        self.plan_added = [163, 765, 141, 166, 137, 355, 136, 1206, 433, 1130]
        self.act_added = [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601]
        self.act_hours = [15.0, 69.9, 6.5, 22.4, 28.4, 65.9, 19.4, 198.7, 38.8, 138.2]

        self.pushButton.clicked.connect(lambda: self.llenar_tabla(self.est_proxy, self.act_added))
        self.pushButton_3.clicked.connect(lambda: self.llenar_tabla(self.est_proxy, self.act_hours))
        self.pushButton_2.clicked.connect(lambda: self.llenar_tabla(self.plan_added, self.act_added))
        self.pushButton_4.clicked.connect(lambda: self.llenar_tabla(self.plan_added, self.act_hours))
        self.pushButton_5.clicked.connect(self.procesar_calculo)

    def llenar_tabla(self, datos_x, datos_y):
        for i in range(10):
            self.tableWidget.setItem(0, i, QtWidgets.QTableWidgetItem(str(datos_x[i])))
            self.tableWidget.setItem(1, i, QtWidgets.QTableWidgetItem(str(datos_y[i])))

    def procesar_calculo(self):
        try:
            x_vals, y_vals = [], []
            for i in range(10):
                item_x = self.tableWidget.item(0, i)
                item_y = self.tableWidget.item(1, i)
                val_x = item_x.text() if item_x and item_x.text() else "0"
                val_y = item_y.text() if item_y and item_y.text() else "0"
                x_vals.append(float(val_x))
                y_vals.append(float(val_y))

            xk_val = float(self.lineEdit.text()) if self.lineEdit.text() else 386
            ej = Ej1(x_vals, y_vals, xk_val)
            ej.calcular()

            self.label_9.setText(f"{ej.b1:.8f}")
            self.label_8.setText(f"{ej.b0:.8f}")
            self.label_12.setText(f"{ej.r_xy:.8f}")
            self.label_10.setText(f"{ej.r2:.8f}")
            self.label_11.setText(f"{ej.yk:.8f}")
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error", f"Datos inválidos: {e}")