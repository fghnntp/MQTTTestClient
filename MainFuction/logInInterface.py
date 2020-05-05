# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logInInterface.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogLoginInterface(object):
    def setupUi(self, DialogLoginInterface):
        DialogLoginInterface.setObjectName("DialogLoginInterface")
        DialogLoginInterface.resize(500, 300)
        self.pushButtonLogin = QtWidgets.QPushButton(DialogLoginInterface)
        self.pushButtonLogin.setGeometry(QtCore.QRect(200, 230, 100, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButtonLogin.setFont(font)
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.widget = QtWidgets.QWidget(DialogLoginInterface)
        self.widget.setGeometry(QtCore.QRect(50, 50, 401, 141))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEditUser = QtWidgets.QLineEdit(self.widget)
        self.lineEditUser.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditUser.setObjectName("lineEditUser")
        self.gridLayout.addWidget(self.lineEditUser, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEditPassword = QtWidgets.QLineEdit(self.widget)
        self.lineEditPassword.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.gridLayout.addWidget(self.lineEditPassword, 1, 1, 1, 1)

        self.retranslateUi(DialogLoginInterface)
        QtCore.QMetaObject.connectSlotsByName(DialogLoginInterface)

    def retranslateUi(self, DialogLoginInterface):
        _translate = QtCore.QCoreApplication.translate
        DialogLoginInterface.setWindowTitle(_translate("DialogLoginInterface", "Dialog"))
        self.pushButtonLogin.setText(_translate("DialogLoginInterface", "登入"))
        self.label.setText(_translate("DialogLoginInterface", "账号："))
        self.label_2.setText(_translate("DialogLoginInterface", "密码："))
