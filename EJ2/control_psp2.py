from PyQt6 import uic, QtWidgets
from EJ2.psp2 import Intnum

class ControlPsp2(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("EJ2/simpson.ui", self)

        self.pushButton.clicked.connect(self.clic)

    def clic(self):
        x_val = float(self.lineEdit.text())
        d_val = float(self.lineEdit_2.text())

        obj = Intnum(x_val, d_val)
        res = obj.calcular_integral()

        self.lineEdit_3.setText(str(res))