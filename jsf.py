from PyQt5 import QtWidgets, uic
import sys
app = QtWidgets.QApplication([])
win = uic.loadUi("ejemplo.ui") .ui 
win.show()
sys.exit(app.exec())
