# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.guardarButton = QtWidgets.QPushButton(self.centralwidget)
        self.guardarButton.setGeometry(QtCore.QRect(480, 360, 93, 28))
        self.guardarButton.setObjectName("guardarButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 70, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 130, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 180, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 230, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 280, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.nombreEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nombreEdit.setGeometry(QtCore.QRect(150, 80, 151, 31))
        self.nombreEdit.setObjectName("nombreEdit")
        self.Interpretedit = QtWidgets.QLineEdit(self.centralwidget)
        self.Interpretedit.setGeometry(QtCore.QRect(150, 130, 151, 31))
        self.Interpretedit.setObjectName("Interpretedit")
        self.albumEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.albumEdit.setGeometry(QtCore.QRect(150, 180, 151, 31))
        self.albumEdit.setObjectName("albumEdit")
        self.anioEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.anioEdit.setGeometry(QtCore.QRect(150, 230, 151, 31))
        self.anioEdit.setObjectName("anioEdit")
        self.generoEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.generoEdit.setGeometry(QtCore.QRect(150, 280, 151, 31))
        self.generoEdit.setObjectName("generoEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.guardarButton.setText(_translate("MainWindow", "Guardar"))
        self.label.setText(_translate("MainWindow", "Nombre"))
        self.label_2.setText(_translate("MainWindow", "Interprete"))
        self.label_3.setText(_translate("MainWindow", "Album"))
        self.label_4.setText(_translate("MainWindow", "Año"))
        self.label_5.setText(_translate("MainWindow", "Genero"))
