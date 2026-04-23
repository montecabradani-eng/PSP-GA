import sys
from PyQt6 import QtWidgets, uic

from EJ1.control_main import MenuPrincipal
from EJ2.control_psp2 import ControlPsp2
from EJ3.control_psp3 import ControlPsp3

class SelectorMenu(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ventana_psp (2).ui", self) #Aquí es como abres el archivo.ui, ventana psp es como es el primer menú
        # que seleeciona el ejercicio, lo pongo como aparece en el archivo y ya

        self.pushButton.clicked.connect(self.abrir_ejercicio_1)
        self.pushButton_2.clicked.connect(self.abrir_ejercicio_2)
        self.pushButton_3.clicked.connect(self.abrir_ejercicio_3)
        #como para abrir el ejercicio es con un push button, la funcion que se usa es el clicked.connect

    def abrir_ejercicio_1(self):
        self.ventana1 = MenuPrincipal()
        self.ventana1.show()

    def abrir_ejercicio_2(self):
        self.ventana2 = ControlPsp2()
        self.ventana2.show()
        
    def abrir_ejercicio_3(self):
        self.ventana3 = ControlPsp3()
        self.ventana3.show()
        
    #estas funciones son fáciles, solo anexo un nombre al archivo correspondiente a psp 1 y 2, y al final pongo el
    #.show para que salte esa misma ventana

app = QtWidgets.QApplication(sys.argv)  #Esto tiene que ir aqui
progra = SelectorMenu() #Solo es crear un nombre sencillo para todo lo que acabamos de crear
progra.show() #condensa todo lo que acabamos de hacer para que pueda mostrarse
sys.exit(app.exec()) #para iniciar y abrir correctamente