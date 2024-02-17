import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from Calculadora import *

class CalculadoraAplicacion (QDialog):
    def __init__(self):
        super().__init__()

        self.CalculadoraApli=Ui_Dialog()
        self.CalculadoraApli.setupUi(self)

        self.CalculadoraApli.Suma.clicked.connect(self.sumarOP)
        self.CalculadoraApli.resta.clicked.connect(self.restaOP)
        self.CalculadoraApli.multiply.clicked.connect(self.multiOP)
        self.CalculadoraApli.div.clicked.connect(self.divOp)
        self.show()

    def sumarOP(self):
        suma=0
        variable=0
        variable2=0

        if len(self.CalculadoraApli.Var1.text())>0:
            variable = int(self.CalculadoraApli.Var1.text())
        if len(self.CalculadoraApli.Var2.text())>0:
            variable2 = int(self.CalculadoraApli.Var2.text())
        suma = variable+variable2
        self.CalculadoraApli.Result_Output.setText(str(suma))

    def restaOP(self):
        resta=0
        variable=0
        variable2=0

        if len(self.CalculadoraApli.Var1.text())>0:
            variable = int(self.CalculadoraApli.Var1.text())
        if len(self.CalculadoraApli.Var2.text())>0:
            variable2 = int(self.CalculadoraApli.Var2.text())
        resta = variable-variable2
        self.CalculadoraApli.Result_Output.setText(str(resta))

    def multiOP(self):
        multiply=0
        variable=0
        variable2=0

        if len(self.CalculadoraApli.Var1.text())>0:
            variable = int(self.CalculadoraApli.Var1.text())
        if len(self.CalculadoraApli.Var2.text())>0:
            variable2 = int(self.CalculadoraApli.Var2.text())
        multiply = variable * variable2
        self.CalculadoraApli.Result_Output.setText(str(multiply))

    def divOp(self):
        div=0
        variable=0
        variable2=0

        if len(self.CalculadoraApli.Var1.text())>0:
            variable = int(self.CalculadoraApli.Var1.text())
        if len(self.CalculadoraApli.Var2.text())>0:
            variable2 = int(self.CalculadoraApli.Var2.text())
        div = variable/variable2
        self.CalculadoraApli.Result_Output.setText(str(div))

if __name__=='__main__':
    app=QApplication(sys.argv)
    ejecucion=CalculadoraAplicacion()
    ejecucion.show()
    sys.exit(app.exec_())
