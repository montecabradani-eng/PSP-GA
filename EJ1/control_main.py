import os
from PyQt6 import QtWidgets, uic
from EJ1.psp1 import Ej1 

class MenuPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        dir_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_ui = os.path.join(dir_actual, "menu_principal (1).ui")
        
        try:
            uic.loadUi(ruta_ui, self)
        except Exception as e:
            print(f"Error al cargar la interfaz: {e}")

        self.pushButton.clicked.connect(self.ejecutar_calculo_regresion)

    def ejecutar_calculo_regresion(self):
        try:
            x_vals = []
            y_vals = []
            
            for i in range(10):
                item_x = self.tableWidget.item(0, i)
                item_y = self.tableWidget.item(1, i) 
                
                val_x = item_x.text().strip() if item_x and item_x.text().strip() else "0"
                val_y = item_y.text().strip() if item_y and item_y.text().strip() else "0"
                
                x_vals.append(float(val_x))
                y_vals.append(float(val_y))

            texto_xk = self.lineEdit.text().strip()
            xk_val = float(texto_xk) if texto_xk else 386.0


            ej = Ej1(x_vals, y_vals, xk_val)
            ej.calcular()

            self.lineEdit_2.setText(f"{ej.b0:.8f}")
            self.lineEdit_3.setText(f"{ej.b1:.8f}")
            self.lineEdit_4.setText(f"{ej.r2:.8f}")
            self.lineEdit_5.setText(f"{ej.r_xy:.8f}")
            self.lineEdit_6.setText(f"{ej.yk:.8f}")

        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Error", "Ingresa solo números en la tabla.")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error Crítico", f"Detalle: {str(e)}")