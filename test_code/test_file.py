#coding = utf-8
import hou
import os,sys
from PySide2 import QtWidgets, QtCore, QtGui, QtUiTools

class testWin(QtWidgets.QWidget):
    def __init__(self):
        super(testWin, self).__init__(parent=None)
        self.setWindowTitle("Test")
        self.show()

a = QtWidgets.QApplication(sys.argv)
app = testWin()
app()
a.exec_()



