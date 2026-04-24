from PyQt6 import uic, QtWidgets
from EJ4.psp4 import calcular_psp4

class ControlPsp4(QtWidgets.QDialog):
    def __init__(self):
        super(ControlPsp4, self).__init__()
        uic.loadUi("EJ4/ui4/psp4.ui", self)
        self.pushButton.clicked.connect(self.ejecutar_calculos)

    def ejecutar_calculos(self):
        dx = []
        dy = []
        
        for i in range(10):
            ix = self.tableWidget.item(0, i)
            iy = self.tableWidget.item(1, i)
            
            if ix != None and iy != None:
                tx = ix.text()
                ty = iy.text()
                if tx != "" and ty != "":
                    dx.append(float(tx))
                    dy.append(float(ty))

        if len(dx) >= 3:
            xk = float(self.lineEdit.text())
            res = calcular_psp4(dx, dy, xk)
            
            self.lineEdit_2.setText(str(round(res['y_k'], 5)))
            self.lineEdit_3.setText(str(round(res['rango'], 5)))
            self.lineEdit_4.setText(str(round(res['lpi'], 5)))
            self.lineEdit_5.setText(str(round(res['upi'], 5)))