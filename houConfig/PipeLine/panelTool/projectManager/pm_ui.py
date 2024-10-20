# Form implementation generated from reading ui file 'D:\Code\pyHou\houConfig\PipeLine\panelTool\projectManager\pm_ui.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(536, 518)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.ToolTitle = QtWidgets.QLabel(Form)
        self.ToolTitle.setStyleSheet("font: 20pt \"Microsoft YaHei UI\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.0340909 rgba(0, 0, 142, 255), stop:1 rgba(0, 146, 180, 255));\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-width:5px;")
        self.ToolTitle.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.ToolTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ToolTitle.setObjectName("ToolTitle")
        self.verticalLayout.addWidget(self.ToolTitle)
        self.ProjectName = QtWidgets.QLabel(Form)
        self.ProjectName.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(221, 96, 0, 255), stop:1 rgba(72, 230, 230, 255));\n"
"gridline-color: rgb(255, 170, 0);\n"
"\n"
"border-width:5px;\n"
"border-radius:10ps;")
        self.ProjectName.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ProjectName.setObjectName("ProjectName")
        self.verticalLayout.addWidget(self.ProjectName)
        self.ProjectPath = QtWidgets.QLabel(Form)
        self.ProjectPath.setStyleSheet("font: 14pt \"Microsoft YaHei UI\";\n"
"font: 700 9pt \"Microsoft YaHei UI\";")
        self.ProjectPath.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ProjectPath.setObjectName("ProjectPath")
        self.verticalLayout.addWidget(self.ProjectPath)
        self.FileList = QtWidgets.QListWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.FileList.sizePolicy().hasHeightForWidth())
        self.FileList.setSizePolicy(sizePolicy)
        self.FileList.setStyleSheet("font: 14pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(94, 94, 94);\n"
"alternate-background-color: rgb(0, 255, 255);\n"
"color: rgb(255, 85, 0);")
        self.FileList.setObjectName("FileList")
        item = QtWidgets.QListWidgetItem()
        self.FileList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.FileList.addItem(item)
        self.verticalLayout.addWidget(self.FileList)
        spacerItem = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.BtmLayout = QtWidgets.QHBoxLayout()
        self.BtmLayout.setObjectName("BtmLayout")
        self.ChangeBtm = QtWidgets.QPushButton(Form)
        self.ChangeBtm.setObjectName("ChangeBtm")
        self.BtmLayout.addWidget(self.ChangeBtm)
        self.RefreshBtm = QtWidgets.QPushButton(Form)
        self.RefreshBtm.setObjectName("RefreshBtm")
        self.BtmLayout.addWidget(self.RefreshBtm)
        self.verticalLayout.addLayout(self.BtmLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ToolTitle.setText(_translate("Form", "ProjectManagerTool"))
        self.ProjectName.setText(_translate("Form", "ProjectName"))
        self.ProjectPath.setText(_translate("Form", "ProjectPath"))
        __sortingEnabled = self.FileList.isSortingEnabled()
        self.FileList.setSortingEnabled(False)
        item = self.FileList.item(0)
        item.setText(_translate("Form", "Test1"))
        item = self.FileList.item(1)
        item.setText(_translate("Form", "Test2"))
        self.FileList.setSortingEnabled(__sortingEnabled)
        self.ChangeBtm.setText(_translate("Form", "ChangeProject"))
        self.RefreshBtm.setText(_translate("Form", "Refresh"))
