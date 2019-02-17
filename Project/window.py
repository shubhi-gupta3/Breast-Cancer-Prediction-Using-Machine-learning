# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from login import Ui_Login
#from login_copy import Ui_Login
from ml import Ui_ml
from signup import Ui_Signup 
#from ml1 import Ui_ml

class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(380, 233)
        self.centralWidget = QtWidgets.QWidget(Window)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(60, 30, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(170, 90, 59, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 140, 114, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 140, 114, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 180, 114, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 180, 114, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        Window.setCentralWidget(self.centralWidget)
        self.retranslateUi(Window)
        self.pushButton_4.clicked.connect(Window.close)
        QtCore.QMetaObject.connectSlotsByName(Window)
        self.pushButton_3.clicked.connect(self.log)
        self.pushButton_2.clicked.connect(self.sign)
        self.pushButton.clicked.connect(self.form)

    def log(self):
        Login = QtWidgets.QDialog()
        ui = Ui_Login()
        ui.setupUi(Login)
        Login.show()
        Login.exec_()

    def sign(self):
        Signup = QtWidgets.QDialog()
        ui = Ui_Signup()
        ui.setupUi(Signup)
        Signup.show()
        Signup.exec_()

    def form(self):
        ml = QtWidgets.QDialog()
        ui = Ui_ml()
        ui.setupUi(ml)
        ml.show()
        ml.exec_()

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Welcome to Breast Cancer Prediction"))
        self.label.setText(_translate("Window", "Breast Cancer Prediction"))
        self.label_2.setText(_translate("Window", "Version 1.0"))
        self.pushButton.setText(_translate("Window", "Guest"))
        self.pushButton_2.setText(_translate("Window", "Sign Up"))
        self.pushButton_3.setText(_translate("Window", "Login"))
        self.pushButton_4.setText(_translate("Window", "Exit"))
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = Ui_Window()
    ui.setupUi(Window)
##    Window.setWindowFlags( QtCore.Qt.WindowMinimizeButtonHint)
##    Window.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
    Window.show()
    sys.exit(app.exec_())


