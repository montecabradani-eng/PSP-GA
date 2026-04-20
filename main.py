import sys
from PyQt6 import QtWidgets
from EJ1.control_main import MenuPrincipal

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = MenuPrincipal()
    ventana.show()
    sys.exit(app.exec())