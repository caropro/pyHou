#coding=utf8
import sys
import os
from PySide2 import QtGui, QtWidgets, QtCore

class input_Window(QtWidgets.QFrame):
    def __init__(self):
        # tool setting
        super(input_Window, self).__init__(parent=None)
        self.setWindowTitle("get input value")
        # ui setting
        # hda name
        hda_name_layout = QtWidgets.QHBoxLayout()
        hda_name_label = QtWidgets.QLabel(r"Hda名称:")
        self.hda_name_input = QtWidgets.QLineEdit(r"Hda名称")
        hda_name_layout.addWidget(hda_name_label)
        hda_name_layout.addWidget(self.hda_name_input)

        # hda path
        hda_path_layout = QtWidgets.QHBoxLayout()
        hda_path_label = QtWidgets.QLabel(r"Hda保存路径:")
        self.hda_path_input = QtWidgets.QLineEdit("$HIP")
        hda_path_layout.addWidget(hda_path_label)
        hda_path_layout.addWidget(self.hda_path_input)

        send_btn = QtWidgets.QPushButton(r"生成")
        layout = QtWidgets.QVBoxLayout()
        layout.addLayout(hda_name_layout)
        layout.addLayout(hda_path_layout)
        layout.addWidget(send_btn)
        self.setLayout(layout)
        # connect signal
        send_btn.clicked.connect(self.get_input_value)

        self.setStyle(QtWidgets.QStyleFactory.create("Breeze"))
    def get_input_value(self):
        hda_name = self.hda_name_input.text()
        hda_path = self.hda_path_input.text()
        print(hda_name,hda_path)
        self.close()

app = QtWidgets.QApplication(sys.argv)
a = input_Window()
a.show()
app.exec_()
