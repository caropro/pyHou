#coding = utf-8
import hou
from PySide2 import QtWidgets,QtGui,QtCore
from functools import partial

class AddParms(QtWidgets.QFrame):
    def __init__(self):
        super(AddParms, self).__init__()
        self.setParent(hou.qt.floatingPanelWindow(None),QtCore.Qt.Window)
        self.datatype = ['Button', 'Data', 'Float', 'Folder', 'FolderSet', 'Int', 'Label', 'Menu', 'Ramp', 'Separator', 'String', 'Toggle']
        self.setUi()
        self.signalconnect()
        self.show()
    def setUi(self):
        parmName_label = QtWidgets.QLabel("Attr_name")
        self.parmName = QtWidgets.QLineEdit("Enter the Parm Name")
        parmSize_label = QtWidgets.QLabel("Attr_Size")
        self.parmSize = QtWidgets.QLineEdit("Size_num")
        self.typelist = QtWidgets.QComboBox()
        self.confirm = QtWidgets.QPushButton("Build")
        self.remove = QtWidgets.QPushButton("Remove")
        self.typelist.addItems(self.datatype)
        #set layout
        init_layout = QtWidgets.QHBoxLayout()
        init_layout.addWidget(parmName_label)
        init_layout.addWidget(self.parmName)
        init_layout.addWidget(parmSize_label)
        init_layout.addWidget(self.parmSize)
        init_layout.addWidget(self.typelist)
        init_layout.addWidget(self.confirm)
        init_layout.addWidget(self.remove)
        self.setLayout(init_layout)

    def signalconnect(self):
        self.confirm.clicked.connect(self.addParms)
        self.remove.clicked.connect(self.removeParms)

    def addParms(self,*args, **kwargs):
        if hou.selectedNodes():
            parmName = self.parmName.text().replace(" ","_")
            try:
                parmSize = int(self.parmSize.text())
            except:
                parmSize = 1;
            parmType = "%sParmTemplate" % self.typelist.currentText()
            for node in hou.selectedNodes():
                print (node)
                print (parmName)
                print (parmSize)
                print (parmType)
                current_tmpparm = node.parmTemplateGroup()
                current_tmpparm = self.add_TMP(parmName, parmSize,parmType, current_tmpparm)
                node.setParmTemplateGroup(current_tmpparm)
            hou.ui.displayMessage("Done!")
        else:
            hou.ui.displayMessage("Select Nodes First")
            return

    def removeParms(self,*args, **kwargs):
        if hou.selectedNodes():
            parmName = self.parmName.text().replace(" ","_")
            try:
                parmSize = int(self.parmSize.text())
            except:
                parmSize = 1;
            parmType = "%sParmTemplate" % self.typelist.currentText()
            for node in hou.selectedNodes():
                try:
                    current_tmpparm = node.parmTemplateGroup()
                    current_tmpparm.remove(parmName)
                    node.setParmTemplateGroup(current_tmpparm)
                except:
                    continue
            hou.ui.displayMessage("Done!")
        else:
            hou.ui.displayMessage("Select Nodes First")
            return

    def add_TMP(self,attr_name,attr_size,tmp_type, current_tmpparm):
        attr_label = attr_name
        if tmp_type == "RampParmTemplate":
            current_tmpparm.append(hou.RampParmTemplate(attr_name, attr_label, hou.rampParmType.Float,
                                                        default_value=1, default_basis=None, color_type=None))
        elif tmp_type == "ButtonParmTemplate" or tmp_type == "FolderParmTemplate" or tmp_type == "LabelParmTemplate" or tmp_type == "ToggleParmTemplate":
            parm = partial(getattr(hou, tmp_type), name=attr_name, label=attr_label)
            current_tmpparm.append(parm())
        elif tmp_type == "SeparatorParmTemplate":
            parm = partial(getattr(hou, tmp_type), name=attr_name)
            current_tmpparm.append(parm())
        else:
            parm = partial(getattr(hou, tmp_type), name=attr_name, label=attr_label,num_components=attr_size)
            current_tmpparm.append(parm())
        return current_tmpparm


def run():
    tool = AddParms()
