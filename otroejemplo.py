from PyQt5 import QtWidgets
import nuevoejemplo
import sys
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
