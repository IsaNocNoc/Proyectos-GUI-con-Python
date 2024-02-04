import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from Menu_Ropa import *

class MenuRopaAplicacion(QDialog):
    def __init__(self):
        super().__init__()

        self.ListaRopa=Ui_Dialog()
        self.ListaRopa.setupUi(self)

        self.ListaRopa.Extrachica.toggled.connect(self.mostrar_informacion)
        self.ListaRopa.Chica.toggled.connect(self.mostrar_informacion)
        self.ListaRopa.Mediana.toggled.connect(self.mostrar_informacion)
        self.ListaRopa.Grande.toggled.connect(self.mostrar_informacion)
        self.show()

        self.ListaRopa.PagoTarjetas.toggled.connect(self.mostrar_informacion)
        self.ListaRopa.PagoEfectivo.toggled.connect(self.mostrar_informacion)
        self.ListaRopa.PagoTransaccion.toggled.connect(self.mostrar_informacion)

        self.show()

    def mostrar_informacion(self):
        Talla_seleccion=''
        metodo_pago=''

        if self.ListaRopa.Extrachica.isChecked==True:
            Talla_seleccion='XS'
        if self.ListaRopa.Chica.isChecked==True:
            Talla_seleccion='Talla Chica'
        if self.ListaRopa.Mediana.isChecked==True:
            Talla_seleccion='Talla Mediana'
        if self.ListaRopa.Grande.isChecked==True:
            Talla_seleccion='Talla Grande'

        if self.ListaRopa.PagoTarjetas.isChecked==True:
            Talla_seleccion='Pago con Tarjeta'
        if self.ListaRopa.PagoEfectivo.isChecked==True:
            Talla_seleccion='Pago con Efectivo'
        if self.ListaRopa.PagoTransaccion.isChecked==True:
            Talla_seleccion='Pago contransaccion'

        self.ListaRopa.Texto_Outout.setText('La Talla seleccionada es {} \nEl metodo de pago es {}'.format(Talla_seleccion,metodo_pago))
        
if __name__ == '__main__':
    app=QApplication(sys.argv)
    ejecucion=MenuRopaAplicacion()
    ejecucion.show()
    sys.exit(app.exec_())