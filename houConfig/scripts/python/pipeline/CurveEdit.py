# coding = utf-8
import hou
from PySide2 import QtWidgets, QtGui, QtCore
from functools import partial


class editCurve(QtWidgets.QWidget):
    def __init__(self):
        super(editCurve, self).__init__()
        self.currentCurve = None
        self.setParent(hou.qt.floatingPanelWindow(None), QtCore.Qt.Window)
        self.setWindowTitle("CurvePointEdit")
        self.setUi()
        self.signalconnect()
        self.show()

    def setUi(self):
        self.pos_table = QtWidgets.QTableWidget(0, 3)
        self.pos_table.setHorizontalHeaderLabels(["x", "y", "z"])
        self.pos_table.setSortingEnabled(False)
        self.CCLabel = QtWidgets.QLabel("CurrentCurve:")
        self.updatebtm = QtWidgets.QPushButton("UpdateCurve")
        self.confirmbtm = QtWidgets.QPushButton("SaveResult")

        self.pos_mod = QtWidgets.QTableWidget(0, 3)
        self.pos_mod.setHorizontalHeaderLabels(["pos_x", "pos_y", "pos_z"])
        self.pos_mod.setMaximumHeight(100)
        self.pos_mod.insertRow(0)
        self.pos_mod.setItem(0, 0, QtWidgets.QTableWidgetItem("0"))
        self.pos_mod.setItem(0, 1, QtWidgets.QTableWidgetItem("0"))
        self.pos_mod.setItem(0, 2, QtWidgets.QTableWidgetItem("0"))
        self.add_btm = QtWidgets.QPushButton("Add")
        self.set_btm = QtWidgets.QPushButton("SetSingle")

        # baisc layout
        btm_layout = QtWidgets.QHBoxLayout()
        btm_layout.addWidget(self.CCLabel)
        btm_layout.addWidget(self.updatebtm)
        btm_layout.addWidget(self.confirmbtm)
        # mod layout
        mod_layout = QtWidgets.QHBoxLayout()
        mod_layout.addWidget(self.pos_mod)
        mod_layout.addWidget(self.add_btm)
        mod_layout.addWidget(self.set_btm)

        # display layout
        dis_layout = QtWidgets.QVBoxLayout()
        dis_layout.addLayout(btm_layout)
        dis_layout.addLayout(mod_layout)
        dis_layout.addWidget(self.pos_table)

        self.setLayout(dis_layout)

    def signalconnect(self):
        self.updatebtm.clicked.connect(self.updateInfo)
        self.confirmbtm.clicked.connect(self.saveData)
        self.add_btm.clicked.connect(partial(self.Mod, 1))
        self.set_btm.clicked.connect(partial(self.Mod, 0))

    def updateInfo(self, *args, **kwargs):
        current_curve = hou.selectedNodes()[0]
        if (current_curve.type().name() != "curve"):
            return
        # Change Label
        self.CCLabel.setText("CurrentCurve: %s" % current_curve.name())
        # update variable
        self.currentCurve = current_curve

        # reset table
        point_data = self.currentCurve.parm("coords").eval()
        rows = [x for x in range(self.pos_table.rowCount())][::-1]
        for row in rows:
            self.pos_table.removeRow(row)

        # update table
        count = 0
        for point in point_data.strip().split(" "):
            pos_list = point.split(",")
            self.pos_table.insertRow(count)
            self.pos_table.setItem(count, 0, QtWidgets.QTableWidgetItem(pos_list[0]))
            self.pos_table.setItem(count, 1, QtWidgets.QTableWidgetItem(pos_list[1]))
            self.pos_table.setItem(count, 2, QtWidgets.QTableWidgetItem(pos_list[2]))
            count += 1

    def Mod(self, Type):
        x_val = float(self.pos_mod.item(0, 0).text())
        y_val = float(self.pos_mod.item(0, 1).text())
        z_val = float(self.pos_mod.item(0, 2).text())
        if Type:
            rows = [x for x in range(self.pos_table.rowCount())][::-1]
            for point in rows:
                x = float(self.pos_table.item(point, 0).text())
                y = float(self.pos_table.item(point, 1).text())
                z = float(self.pos_table.item(point, 2).text())
                n_x = x + x_val
                n_y = y + y_val
                n_z = z + z_val
                self.pos_table.setItem(point, 0, QtWidgets.QTableWidgetItem(str(n_x)))
                self.pos_table.setItem(point, 1, QtWidgets.QTableWidgetItem(str(n_y)))
                self.pos_table.setItem(point, 2, QtWidgets.QTableWidgetItem(str(n_z)))
        else:
            rows = [x for x in range(self.pos_table.rowCount())][::-1]
            for point in rows:
                if x_val:
                    self.pos_table.setItem(point, 0, QtWidgets.QTableWidgetItem(str(x_val)))
                if y_val:
                    self.pos_table.setItem(point, 1, QtWidgets.QTableWidgetItem(str(y_val)))
                if z_val:
                    self.pos_table.setItem(point, 2, QtWidgets.QTableWidgetItem(str(z_val)))

    def saveData(self):
        coords = ""
        rows = [x for x in range(self.pos_table.rowCount())][::-1]
        for point in rows:
            x = self.pos_table.item(point, 0).text()
            y = self.pos_table.item(point, 1).text()
            z = self.pos_table.item(point, 2).text()
            coords = "{1},{2},{3} {0}".format(coords, x, y, z)

        self.currentCurve.parm("coords").set(coords)


def run():
    tool = editCurve()
