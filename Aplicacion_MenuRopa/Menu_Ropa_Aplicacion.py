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
        
        if self.ListaRopa.Extrachica.isChecked()==True:
            Talla_seleccion='XS'
            self.ListaRopa.Texto_Output_1.setText('La Talla seleccionada es {}'.format(Talla_seleccion))
        if self.ListaRopa.Chica.isChecked()==True:
            Talla_seleccion='Talla Chica'
            self.ListaRopa.Texto_Output_1.setText('La Talla seleccionada es {}'.format(Talla_seleccion))
        if self.ListaRopa.Mediana.isChecked()==True:
            Talla_seleccion='Talla Mediana'
            self.ListaRopa.Texto_Output_1.setText('La Talla seleccionada es {}'.format(Talla_seleccion))
        if self.ListaRopa.Grande.isChecked()==True:
            Talla_seleccion='Talla Grande'
            self.ListaRopa.Texto_Output_1.setText('La Talla seleccionada es {}'.format(Talla_seleccion))
        

        if self.ListaRopa.PagoTarjetas.isChecked()==True:
            metodo_pago='Pago con Tarjeta'
            self.ListaRopa.Texto_OutPut2.setText('El metodod de pago es {}'. format(metodo_pago))
        if self.ListaRopa.PagoEfectivo.isChecked()==True:
            metodo_pago='Pago con Efectivo'
            self.ListaRopa.Texto_OutPut2.setText('El metodod de pago es {}'. format(metodo_pago))
        if self.ListaRopa.PagoTransaccion.isChecked()==True:
            metodo_pago='Pago contransaccion'
            self.ListaRopa.Texto_OutPut2.setText('El metodod de pago es {}'. format(metodo_pago))


if __name__ == '__main__':
    app=QApplication(sys.argv)
    ejecucion=MenuRopaAplicacion()
    ejecucion.show()
    sys.exit(app.exec_())