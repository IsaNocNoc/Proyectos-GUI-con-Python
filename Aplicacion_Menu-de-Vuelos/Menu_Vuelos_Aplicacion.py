import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from Menu_Vuelos import *

class MenuVuelosAplicacion (QDialog):
    def __init__(self):
        super().__init__()

        self.ListaSeleccion=Ui_Dialog
        self.ListaSeleccion.setupUi(self)

        self.ListaSeleccion.SL_PrimeraClase.toggled.connect(self.TextoInformativo)
        self.ListaSeleccion.SL_ClaseNegocio.toggled.connect(self.TextoInformativo)
        self.ListaSeleccion.SL_ClaseEconomico.toggled.connect(self.TextoInformativo)
        self.show()

        self.ListaSeleccion.Btn_Sleccion.clicked.connect(self.SeleccionBoton)
        self.show()

    def TextoInformativo(self):
        costo_vuelo=0

        if self.ListaSeleccion.SL_PrimeraClase.isChecked()==True:
            costo_vuelo=190
            self.ListaSeleccion.Texto_Info.setText('El costo de primera clase es {}'.format(costo_vuelo))

        if self.ListaSeleccion.SL_ClaseNegocio.isChecked()==True:
            costo_vuelo=150
            print("Este es un vuelo de negocios")

        if self.ListaSeleccion.SL_ClaseEconomico.isChecked()==True:
            costo_vuelo=120
            print("Este es un vuelo economico")

    def SeleccionBoton(self):
        if self.ListaSeleccion.SL_PrimeraClase.isChecked()==True:
            self.ListaSeleccion.Texto_Output.setText('Usted escogio el vuelo de primera clase')

        if self.ListaSeleccion.SL_ClaseNegocio.isChecked()==True:
            self.ListaSeleccion.Texto_Output.setText('Usted escogio el vuelo de clase de negocio')

        if self.ListaSeleccion.SL_ClaseEconomico.isChecked()==True:
            self.ListaSeleccion.Texto_Output.setText('Usted escogio el vuelo de clase de economico')

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ejecucion=MenuVuelosAplicacion()
    ejecucion.show()
    sys.exit(sys.exec_())