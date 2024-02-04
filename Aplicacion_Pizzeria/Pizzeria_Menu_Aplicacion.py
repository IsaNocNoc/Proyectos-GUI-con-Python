import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from Pizzeria_Menu import *

class PizzeriaMenuAplicacion(QDialog):
    def __init__(self):
        super().__init__()

        self.MenuPizzeria=Ui_Dialog()
        self.MenuPizzeria.setupUi(self)

        self.MenuPizzeria.Pina.stateChanged.connect(self.CalculoPrecio)
        self.MenuPizzeria.CarnesFrias.stateChanged.connect(self.CalculoPrecio)
        self.MenuPizzeria.Peperoni.stateChanged.connect(self.CalculoPrecio)
        self.MenuPizzeria.Queso.stateChanged.connect(self.CalculoPrecio)
        self.MenuPizzeria.Champinion.stateChanged.connect(self.CalculoPrecio)
        self.MenuPizzeria.Atun.stateChanged.connect(self.CalculoPrecio)

        self.show()
    
    def CalculoPrecio(self):
        PrecioBase=15
        if self.MenuPizzeria.Pina.isChecked()==True:
            PrecioBase+=1.50 
        if self.MenuPizzeria.CarnesFrias.isChecked()==True:
            PrecioBase+=3.25 
        if self.MenuPizzeria.Peperoni.isChecked()==True:
            PrecioBase+=1.20 
        if self.MenuPizzeria.Queso.isChecked()==True:
            PrecioBase+=1.80 
        if self.MenuPizzeria.Champinion.isChecked()==True:
            PrecioBase+=0.70 
        if self.MenuPizzeria.Atun.isChecked()==True:
            PrecioBase+=2.80

        self.MenuPizzeria.Precio_Output.setText('${}'.format(PrecioBase))

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ejecucion=PizzeriaMenuAplicacion()
    ejecucion.show()
    sys.exit(app.exec_())