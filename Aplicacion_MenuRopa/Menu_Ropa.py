# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Menu_Ropa.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(333, 448)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        self.Talla_Label = QtWidgets.QLabel(Dialog)
        self.Talla_Label.setGeometry(QtCore.QRect(40, 20, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Talla_Label.setFont(font)
        self.Talla_Label.setObjectName("Talla_Label")
        self.PagoLabel = QtWidgets.QLabel(Dialog)
        self.PagoLabel.setGeometry(QtCore.QRect(40, 190, 251, 21))
        self.PagoLabel.setObjectName("PagoLabel")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(39, 49, 231, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.Conjunto_Tallas = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.Conjunto_Tallas.setContentsMargins(0, 0, 0, 0)
        self.Conjunto_Tallas.setObjectName("Conjunto_Tallas")
        self.Extrachica = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Extrachica.setFont(font)
        self.Extrachica.setObjectName("Extrachica")
        self.Conjunto_Tallas.addWidget(self.Extrachica)
        self.Chica = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Chica.setFont(font)
        self.Chica.setObjectName("Chica")
        self.Conjunto_Tallas.addWidget(self.Chica)
        self.Mediana = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Mediana.setFont(font)
        self.Mediana.setObjectName("Mediana")
        self.Conjunto_Tallas.addWidget(self.Mediana)
        self.Grande = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Grande.setFont(font)
        self.Grande.setObjectName("Grande")
        self.Conjunto_Tallas.addWidget(self.Grande)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(40, 220, 239, 121))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.Conjunto_Pagos = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.Conjunto_Pagos.setContentsMargins(0, 0, 0, 0)
        self.Conjunto_Pagos.setObjectName("Conjunto_Pagos")
        self.PagoTarjetas = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.PagoTarjetas.setFont(font)
        self.PagoTarjetas.setObjectName("PagoTarjetas")
        self.Conjunto_Pagos.addWidget(self.PagoTarjetas)
        self.PagoEfectivo = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.PagoEfectivo.setFont(font)
        self.PagoEfectivo.setObjectName("PagoEfectivo")
        self.Conjunto_Pagos.addWidget(self.PagoEfectivo)
        self.PagoTransaccion = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.PagoTransaccion.setFont(font)
        self.PagoTransaccion.setObjectName("PagoTransaccion")
        self.Conjunto_Pagos.addWidget(self.PagoTransaccion)
        self.Texto_Outout = QtWidgets.QLabel(Dialog)
        self.Texto_Outout.setGeometry(QtCore.QRect(40, 370, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Texto_Outout.setFont(font)
        self.Texto_Outout.setText("")
        self.Texto_Outout.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Texto_Outout.setObjectName("Texto_Outout")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Menu de Ropa"))
        self.Talla_Label.setText(_translate("Dialog", "Escoje Tu Talla:"))
        self.PagoLabel.setText(_translate("Dialog", "Escoje tu metodo de pago:"))
        self.Extrachica.setText(_translate("Dialog", "xs"))
        self.Chica.setText(_translate("Dialog", "s"))
        self.Mediana.setText(_translate("Dialog", "M"))
        self.Grande.setText(_translate("Dialog", "L"))
        self.PagoTarjetas.setText(_translate("Dialog", "Tarjeta de Debito/Credito"))
        self.PagoEfectivo.setText(_translate("Dialog", "Pago Contra entrga"))
        self.PagoTransaccion.setText(_translate("Dialog", "Consignacion Bancaria"))
