# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from sqllite import entry_sign
from ml import Ui_ml

q="Female"
n=e=p="null"
a=18
class Ui_Signup(object):

    def message(self, msg):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle('Message')
        mess.setText(msg)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def lol(self):
        #self.message("Your account won't be created if you do not get a dialog box of successful account creation")
        name = self.lineEdit.text()
        age = self.lineEdit_2.text()
        
        gender = str(self.comboBox.currentText())
        email = self.lineEdit_3.text()
        password = self.lineEdit_4.text()
        if(name == ''):
            self.message('Name is a mandatory field')
            
        elif(password == ''):
             self.message('Password is a mandatory field')
            
        if(age == ''):
            self.message('Age is a mandatory field')
            
        elif(email == ''):
             self.message('Email id is a mandatory field')

        try:
             x = int(age)
        except:
           self.message('Age should be a positive number')
        else:
            entry_sign(name,gender,email,password,age)
            self.message("Account Created Successfully")
##            ml = QtWidgets.QDialog()
##            ui = Ui_ml()
##            ui.setupUi(ml)
##            ml.show()
##            ml.exec_()
    ##        message()
    ##        proceed()
            self.message("Click cancel in signup page to logout")
##            Signup.close()
            
            
    def proceed(self):
        ml = QtWidgets.QDialog()
        ui = Ui_ml()
        ui.setupUi(ml)
        ml.show()
        ml.exec_()

        
       

    def setupUi(self, Signup):        
        Signup.setObjectName("Signup")
        Signup.resize(370, 325)
        self.groupBox = QtWidgets.QGroupBox(Signup)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 331, 251))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.pushButton = QtWidgets.QPushButton(Signup)
        self.pushButton.setGeometry(QtCore.QRect(110, 280, 114, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Signup)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 280, 114, 32))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Signup)
        
        self.pushButton_2.clicked.connect(Signup.close)
        
        QtCore.QMetaObject.connectSlotsByName(Signup)

        self.pushButton.clicked.connect(self.lol)

    def retranslateUi(self, Signup):

        _translate = QtCore.QCoreApplication.translate
        Signup.setWindowTitle(_translate("Signup", "Signup Page"))
        self.groupBox.setTitle(_translate("Signup", "Sign Up"))
        self.label.setText(_translate("Signup", "Name:"))
        self.label_2.setText(_translate("Signup", "Age:"))
        self.label_3.setText(_translate("Signup", "Gender:"))
        self.comboBox.setItemText(0, _translate("Signup", "Female"))
        self.comboBox.setItemText(1, _translate("Signup", "Male"))
        self.comboBox.setItemText(2, _translate("Signup", "Others"))
        self.label_4.setText(_translate("Signup", "Email:"))
        self.label_5.setText(_translate("Signup", "Password:"))
        self.pushButton.setText(_translate("Signup", "Create"))
        self.pushButton_2.setText(_translate("Signup", "Cancel"))
        #self.pushButton.clicked.connect(self.lol)
        

    
        #print(name, age, gender, email, password)
        #sql.myList = [name, age, gender, email, password]
        #sql.insert_query()
        #sql.select_query()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Signup = QtWidgets.QDialog()
    ui = Ui_Signup()
    ui.setupUi(Signup)
    Signup.show()
    sys.exit(app.exec_())
##    app.exec_()

