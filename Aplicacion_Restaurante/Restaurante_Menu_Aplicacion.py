import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from Restaurante_Menu import *

class RestauranteMenuAplicacion (QDialog):
    def __init__(self):
        super().__init__()

        self.MenuAplicacion = Ui_Dialog()
        self.MenuAplicacion.setupUi(self)

        self.MenuAplicacion.Croassant.stateChanged.connect(self.CalculoMenu)
        self.MenuAplicacion.Sandwich.stateChanged.connect(self.CalculoMenu)
        self.MenuAplicacion.Baguette.stateChanged.connect(self.CalculoMenu)
        self.MenuAplicacion.Torta.stateChanged.connect(self.CalculoMenu)
        self.MenuAplicacion.AguaSabor.stateChanged.connect(self.CalculoMenu)
        self.MenuAplicacion.Malteada.stateChanged.connect(self.CalculoMenu)
        self.MenuAplicacion.Cafe.stateChanged.connect(self.CalculoMenu)
        self.MenuAplicacion.Gelatina.stateChanged.connect(self.CalculoMenu)
        self.MenuAplicacion.Flan.stateChanged.connect(self.CalculoMenu)
        self.MenuAplicacion.Helado.stateChanged.connect(self.CalculoMenu)
        self.show()

    def CalculoMenu (self):
        Total_Cuenta=0
        if self.MenuAplicacion.Croassant.isChecked()==True:
            Total_Cuenta+=25.00
        if self.MenuAplicacion.Sandwich.isChecked()==True:
            Total_Cuenta+=18.50
        if self.MenuAplicacion.Baguette.isChecked()==True:
            Total_Cuenta+=20.25
        if self.MenuAplicacion.Torta.isChecked()==True:
            Total_Cuenta+=25.50
        if self.MenuAplicacion.AguaSabor.isChecked()==True:
            Total_Cuenta+=18.00
        if self.MenuAplicacion.Malteada.isChecked()==True:
            Total_Cuenta+=15.00
        if self.MenuAplicacion.Cafe.isChecked()==True:
            Total_Cuenta+=12.50
        if self.MenuAplicacion.Gelatina.isChecked()==True:
            Total_Cuenta+=13.50
        if self.MenuAplicacion.Flan.isChecked()==True:
            Total_Cuenta+=12.00
        if self.MenuAplicacion.Helado.isChecked()==True:
            Total_Cuenta+=15.00

        self.MenuAplicacion.Precio_Outout.setText('${}'.format(Total_Cuenta))

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ejecucion=RestauranteMenuAplicacion()
    ejecucion.show()
    sys.exit(app.exec_())