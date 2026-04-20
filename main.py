import sys
from PyQt6 import QtWidgets, uic

from EJ1.control_main import MenuPrincipal
from EJ2.control_psp2 import ControlPsp2

class SelectorMenu(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ventana_psp (2).ui", self)

        self.pushButton.clicked.connect(self.abrir_ejercicio_1)
        self.pushButton_2.clicked.connect(self.abrir_ejercicio_2)

    def abrir_ejercicio_1(self):
        self.ventana1 = MenuPrincipal()
        self.ventana1.show()

    def abrir_ejercicio_2(self):
        self.ventana2 = ControlPsp2()
        self.ventana2.show()

app = QtWidgets.QApplication(sys.argv)
progra = SelectorMenu()
progra.show()
sys.exit(app.exec())