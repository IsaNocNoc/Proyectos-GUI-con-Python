import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from CopiarPegar import *

#en el GUI tienes que hacer la siguiente conexion (Editar señales/slots)
#para el input
#Pressed()->SelectAll()
#released()->copy()
# y para el ouput
#pressed()->clear()
#released()->paste()

class CopiarPegarAplicacion (QDialog):
    def __init__(self):
        super().__init__()

        self.CopyPaste=Ui_Dialog()
        self.CopyPaste.setupUi(self)
        self.show()


if __name__=='__main__':
    app=QApplication(sys.argv)
    ejecucion=CopiarPegarAplicacion()
    ejecucion.show()
    sys.exit(app.exec_())