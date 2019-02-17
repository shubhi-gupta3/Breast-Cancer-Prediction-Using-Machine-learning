# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_copy.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#import ml
from ml import Ui_ml
import sys
from sqllite import login_check
class Ui_Login(object):

    def message(self, msg):
                mess = QtWidgets.QMessageBox()
                mess.setWindowTitle('Message')
                mess.setText(msg)
                mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
                mess.exec_()

    def check(self):

        email = self.lineEdit.text()
        password = self.lineEdit_2.text()

        if(email == ''):
            self.message('Email is a mandatory field')
            
        elif(password == ''):
             self.message('Password is a mandatory field')

        else:
        
            '''conn = pymysql.connect(host='localhost', user='root', password='adminadmin', database='breastcancer', autocommit=True)
            cursor = conn.cursor()

            query = 'select name, password from user_details'
            x = cursor.execute(query, name)

            if(x == 0):
                self.message('Data not found')

            else:
                l = list(cursor)[0]
                
                if(l[1]!=password):
                    self.message('Wrong Password')'''
            res = login_check(email, password)
            #print(res)
            
            if res:
                f = open('log.txt', 'w')
                f.write(str(res[0]))
                f.close()
                #print('file written')
            if not res:
                self.message('Wrong email or password')
            else:
                #ml.main()
                    ml = QtWidgets.QDialog()
                    ui = Ui_ml()
                    ui.setupUi(ml)
                    ml.show()
                    ml.exec_()
                    self.message("Click cancel in login page to logout")
##                    self.close(login.close)
                                
            
        
        
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(300, 252)
        self.groupBox = QtWidgets.QGroupBox(Login)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 241, 161))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(110, 70, 113, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 71, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 110, 113, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 70, 70, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Login)
        self.pushButton.setGeometry(QtCore.QRect(40, 190, 101, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Login)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 190, 114, 32))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Login)
        self.pushButton_2.clicked.connect(Login.close)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login Page"))
        self.groupBox.setTitle(_translate("Login", "Login"))
        self.label_2.setText(_translate("Login", "Password:"))
        self.label.setText(_translate("Login", "Email id:"))
        self.pushButton.setText(_translate("Login", "Go"))
        self.pushButton_2.setText(_translate("Login", "Cancel"))
        self.pushButton.clicked.connect(self.check)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QDialog()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())

