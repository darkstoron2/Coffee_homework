# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(305, 353)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 40, 81, 20))
        self.label.setObjectName("label")
        self.lineName = QtWidgets.QLineEdit(Form)
        self.lineName.setGeometry(QtCore.QRect(130, 40, 113, 20))
        self.lineName.setObjectName("lineName")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 101, 20))
        self.label_2.setObjectName("label_2")
        self.comboBoxRoasting = QtWidgets.QComboBox(Form)
        self.comboBoxRoasting.setGeometry(QtCore.QRect(130, 80, 111, 22))
        self.comboBoxRoasting.setObjectName("comboBoxRoasting")
        self.comboBoxGG = QtWidgets.QComboBox(Form)
        self.comboBoxGG.setGeometry(QtCore.QRect(130, 110, 111, 22))
        self.comboBoxGG.setObjectName("comboBoxGG")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 121, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 81, 16))
        self.label_4.setObjectName("label_4")
        self.lineTaste = QtWidgets.QLineEdit(Form)
        self.lineTaste.setGeometry(QtCore.QRect(130, 150, 113, 20))
        self.lineTaste.setObjectName("lineTaste")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 180, 47, 13))
        self.label_5.setObjectName("label_5")
        self.linePrice = QtWidgets.QLineEdit(Form)
        self.linePrice.setGeometry(QtCore.QRect(130, 180, 113, 20))
        self.linePrice.setObjectName("linePrice")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 220, 91, 20))
        self.label_6.setObjectName("label_6")
        self.lineVolume = QtWidgets.QLineEdit(Form)
        self.lineVolume.setGeometry(QtCore.QRect(130, 220, 113, 20))
        self.lineVolume.setObjectName("lineVolume")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(110, 290, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Название сорта"))
        self.label_2.setText(_translate("Form", "Степень прожарки"))
        self.label_3.setText(_translate("Form", "Молотый или в зернах"))
        self.label_4.setText(_translate("Form", "Описание вкуса"))
        self.label_5.setText(_translate("Form", "Цена"))
        self.label_6.setText(_translate("Form", "Объем упаковки"))
        self.pushButton.setText(_translate("Form", "Изменить"))