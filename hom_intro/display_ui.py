#coding = utf-8
import hou
import os,sys

from hutil.Qt import QtWidgets,QtCore,QtGui,QtUiTools

current_path = os.path.dirname(__file__)
sys.path.append(current_path)

class win(QtWidgets.QWidget):
    def __init__(self):
        super(win, self).__init__(parent=hou.ui.floatingPanels)

        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(os.path.join(current_path,"win.ui"))
        main_layout = QtWidgets.QHBoxLayout()
        main_layout.addWidget(self.ui)
        self.setLayout(main_layout)

def run():
    app = win()
    app.setParent(hou.qt.mainWindow(None),QtCore.Qt.Window)
    app.show()

