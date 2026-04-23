from PyQt6 import uic
from PyQt6.QtWidgets import QDialog 
from EJ3.psp3 import InversaPsp3

class ControlPsp3(QDialog): 
    def __init__(self):
        super().__init__()
        uic.loadUi("EJ3/ui3/psp3.ui", self) #Llamamos a la función como siempre
        
        self.pushButton.clicked.connect(self.ejecutar_calculo) #aquí para que al momento de presionar el boton de calcular
        # si se calcule como se lo pedimos

    def ejecutar_calculo(self):
        valor_p = self.lineEdit.text()
        valor_dof = self.lineEdit_2.text()
        #asocia los valores con las celdas del QT designer
        
        p = float(valor_p)
        dof = int(valor_dof)
        objeto = InversaPsp3(p, dof)
        resultado = objeto.buscar()        
        # aquí simplemente convierte el texto de las celdas del QT a valores, luego hace que los valores los corra en la función
        # de calcular de psp3.py, y por último encuentra el resultado para poder pasartelo en el lineEdit_3 que es el de resultado

        self.lineEdit_3.setText(str(round(resultado, 5)))
        # simplemente te enlaza para poder mostrarte el resultado