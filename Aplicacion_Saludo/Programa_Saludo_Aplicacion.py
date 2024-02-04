import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from Programa_Saludo import *

class ProgramSaludoAplicacion (QDialog):
    def __init__(self):
        super().__init__()

        self.Dialogo=Ui_Dialog()
        self.Dialogo.setupUi(self)

        self.Dialogo.pb_BotonEjecucion.clicked.connect(self.mostrar_saludos)
        self.show()

    def mostrar_saludos(self):
        mensaje = self.Dialogo.ln_CuadroTextoInput.text()
        self.Dialogo.lbl_TextoMostrar.setText("Hola "+ mensaje + "\nBienvenido!")

if __name__ == '__main__':
    app=QApplication(sys.argv)
    dialogo= ProgramSaludoAplicacion()
    dialogo.show()
    sys.exit(app.exec_())
