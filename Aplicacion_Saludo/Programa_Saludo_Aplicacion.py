import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from Programa_Saludo import *

class ProgramSaludoAplicacion (QDialog):
    def __init__(self):#inicio de la ejecucion del programa
        super().__init__()#asegura que la clase padre se ejecute primero antes que la clase hija

        self.Dialogo=Ui_Dialog()#clase principal del GUI
        self.Dialogo.setupUi(self)#funcion principal del GUI

        #el boton llama a la funcion "mostrar saludos" 
        self.Dialogo.pb_BotonEjecucion.clicked.connect(self.mostrar_saludos)
        self.show()#muestra la ejecucion

    #funcion para mostrar el saludo
    def mostrar_saludos(self):
        mensaje = self.Dialogo.ln_CuadroTextoInput.text()#llama el texto puesto en el cuadro de texto
        self.Dialogo.lbl_TextoMostrar.setText("Hola "+ mensaje + "\nBienvenido!")#muestra el texto en el label

if __name__ == '__main__':
    app=QApplication(sys.argv) #arranca el programa
    dialogo= ProgramSaludoAplicacion()#ejecuta la clase que ejecuta el programa
    dialogo.show()#comando para mostrar el programa en ejecucion
    sys.exit(app.exec_())#cerrar el programa con el boton "x"
