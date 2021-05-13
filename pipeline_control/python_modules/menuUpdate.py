#coding = utf-8
import hou
from PySide2 import QtWidgets,QtGui,QtCore
from functools import partial

class AddParms(QtWidgets.QFrame):
    def __init__(self):
        super(AddParms, self).__init__()
        self.setParent(hou.qt.floatingPanelWindow(None),QtCore.Qt.Window)
        self.setWindowTitle("MenuConvert")
        self.setUi()
        self.signalconnect()
        self.show()
    def setUi(self):
        source_parm = QtWidgets.QLabel("From:")
        self.SourceparmName = QtWidgets.QLineEdit("Parm_Name")
        tar_parm = QtWidgets.QLabel("To:")
        self.TargetparmName = QtWidgets.QLineEdit("Parm_Name")
        self.confirm = QtWidgets.QPushButton("Convert")
        #set layout
        init_layout = QtWidgets.QHBoxLayout()
        init_layout.addWidget(source_parm)
        init_layout.addWidget(self.SourceparmName)
        init_layout.addWidget(tar_parm)
        init_layout.addWidget(self.TargetparmName)
        init_layout.addWidget(self.confirm)
        self.setLayout(init_layout)

    def signalconnect(self):
        self.confirm.clicked.connect(self.Transfer)

    def Transfer(self,*args, **kwargs):
        if hou.selectedNodes():
            parmName = self.SourceparmName.text().replace(" ","_")
            menu_name = self.TargetparmName.text().replace(" ","_")
            source_node = hou.selectedNodes()[-1]
            source_menu = source_node.parm(parmName).parmTemplate()
            source_lables = source_menu.menuLabels()
            source_items = source_menu.menuItems()
            print(source_items)
            #part 2
            node = hou.node(hou.ui.selectNode())
            parm_template = node.parmTemplateGroup()
            target_menu = node.parm(menu_name).parmTemplate()
            target_menu.setMenuLabels(list(source_lables))
            target_menu.setMenuItems(list(source_items))
            parm_template.replace(menu_name, target_menu)
            node.setParmTemplateGroup(parm_template)
            hou.ui.displayMessage("Done!!")
        else:
            hou.ui.displayMessage("Select Source Nodes First")
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