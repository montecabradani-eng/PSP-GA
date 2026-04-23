from PyQt6 import uic
from PyQt6.QtWidgets import QDialog 
from EJ3.psp3 import InversaPsp3

class ControlPsp3(QDialog): 
    def __init__(self):
        super().__init__()
        uic.loadUi("EJ3/ui3/psp3.ui", self)
        
        # Conectamos el botón a la función
        self.pushButton.clicked.connect(self.ejecutar_calculo)

    def ejecutar_calculo(self):
        # Sacamos los datos de los cuadritos de texto
        valor_p = self.lineEdit.text()
        valor_dof = self.lineEdit_2.text()
        
        # Los convertimos a números
        p = float(valor_p)
        dof = int(valor_dof)

        # Usamos la clase del otro archivo para calcular
        objeto = InversaPsp3(p, dof)
        resultado = objeto.buscar()

        # Ponemos el resultado en la etiqueta
        self.lineEdit_3.setText(str(round(resultado, 5)))