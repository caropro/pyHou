# coding = utf-8
import hou
from PySide2 import QtWidgets, QtCore, QtGui, QtUiTools
# from hutil.Qt import QtWidgets,QtCore,QtGui,QtUiTools
import os
import sys
from functools import partial

# add ui file path
current_path = os.path.dirname(__file__)
sys.path.append(current_path)


# load ui file
class geoInfo(QtWidgets.QWidget):
    def __init__(self):
        super(geoInfo, self).__init__()
        ui_loader = QtUiTools.QUiLoader()
        self.ui = ui_loader.load(os.path.join(current_path + "/geoinfo.ui"))
        main_layout = QtWidgets.QHBoxLayout()
        main_layout.addWidget(self.ui)
        self.setLayout(main_layout)

        # init variable
        # detail channel
        self.geo_sw = False
        # attribute list
        self.current_attributes = []
        self.current_type = None
        self.current_elements = None
        # data dict
        self.attr_dict = {}
        self.ele_dict = {}
        # connect signal
        self.connect_signal()
        self.refresh()

    def connect_signal(self):
        self.ui.refresh_btn.clicked.connect(self.refresh)
        self.ui.pts_btn.clicked.connect(partial(self.btn_sw, self.ui.pts_btn))
        self.ui.vtx_btn.clicked.connect(partial(self.btn_sw, self.ui.vtx_btn))
        self.ui.prim_btn.clicked.connect(partial(self.btn_sw, self.ui.prim_btn))
        self.ui.detail_btn.clicked.connect(partial(self.btn_sw, self.ui.detail_btn))

    def btn_sw(self, clicked_btn):
        # set btn status
        self.ui.pts_btn.setChecked(False)
        self.ui.vtx_btn.setChecked(False)
        self.ui.prim_btn.setChecked(False)
        self.ui.detail_btn.setChecked(False)
        clicked_btn.setChecked(True)

        # get data from dict
        self.current_type = self.attr_dict.get(clicked_btn.text(), None)
        self.current_elements = self.ele_dict.get(clicked_btn.text(), None)

        # receive the judgement value if current type is detail
        if clicked_btn.text() == "Detail":
            self.geo_sw = True
        else:
            self.geo_sw = False
        # update table
        self.update_info()

    def data_init(self):
        # get current selected node
        if not hou.selectedNodes():
            hou.ui.displayMessage("Select Node First")
            return
        self.selected_node = hou.selectedNodes()[0]
        self.geo = self.selected_node.geometry()

        # create data dict
        self.attr_dict["Pts"] = self.geo.pointAttribs()
        self.attr_dict["Vtx"] = self.geo.vertexAttribs()
        self.attr_dict["Prim"] = self.geo.primAttribs()
        self.attr_dict["Detail"] = self.geo.globalAttribs()
        self.ele_dict["Pts"] = self.geo.points()
        self.ele_dict["Vtx"] = []
        for pt in self.geo.points():
            for vtx in pt.vertices():
                self.ele_dict["Vtx"].append(vtx)
        self.ele_dict["Prim"] = self.geo.prims()
        self.ele_dict["Detail"] = [x.name() for x in self.geo.globalAttribs()]

        # default current info init
        if not self.current_type:
            self.current_type = self.geo.pointAttribs()
            self.current_elements = self.geo.points()

    def refresh(self):
        self.data_init()
        node_name = self.selected_node.name()
        self.ui.node_label.setText(node_name)
        self.update_info()
        self.ui.pts_btn.setChecked(True)
        self.ui.vtx_btn.setChecked(False)
        self.ui.prim_btn.setChecked(False)
        self.ui.detail_btn.setChecked(False)

    def update_info(self):
        # reset table
        self.reset_Table()
        # no attributes in current type return dirctly
        if not self.current_type:
            return
        # reset attributes name list
        self.current_attributes = []
        # receive attr name list
        self.update_attr_list(self.current_type, self.current_attributes)
        # create the table
        self.row_count = 0
        ele_list = []
        # if detail
        if self.geo_sw:
            # receive attr from dict
            for attr in self.current_type:
                for count in range(attr.size()):
                    # arrange the parm in vertical line
                    self.ui.info_table.insertRow(self.row_count)
                    if attr.size() > 1:
                        attr_value = self.geo.attribValue(attr.name())[count]
                        ele_list.append("%s.[%s]" % (attr.name(), count))
                    else:
                        attr_value = self.geo.attribValue(attr.name())
                        ele_list.append(attr.name())
                    table_item = QtWidgets.QTableWidgetItem("%s" % attr_value)
                    self.ui.info_table.setItem(self.row_count, 0, table_item)
                    self.row_count += 1
            self.ui.info_table.setVerticalHeaderLabels(ele_list)
            return
        else:
            for ele in self.current_elements:
                col = 0
                ele_list.append(str(self.row_count))
                self.ui.info_table.insertRow(self.row_count)
                for attr in self.current_type:
                    for count in range(attr.size()):
                        if attr.size() > 1:
                            attr_value = ele.attribValue(attr.name())[count]
                        else:
                            attr_value = ele.attribValue(attr.name())
                        table_item = QtWidgets.QTableWidgetItem("%s" % attr_value)
                        self.ui.info_table.setItem(self.row_count, col, table_item)
                        col += 1
                self.row_count += 1
            self.ui.info_table.setVerticalHeaderLabels(ele_list)

    def reset_Table(self):
        for row in [x for x in range(self.ui.info_table.rowCount())][::-1]:
            self.ui.info_table.removeRow(row)
        for col in [x for x in range(self.ui.info_table.columnCount())][::-1]:
            self.ui.info_table.removeColumn(col)

    def update_attr_list(self, attrs, attr_list):
        # init col count
        self.col_count = 0
        if self.geo_sw:
            self.ui.info_table.insertColumn(0)
            self.ui.info_table.setHorizontalHeaderLabels(["Detail"])
        else:
            for attr in attrs:
                if attr.size() > 1:
                    for i in range(attr.size()):
                        self.ui.info_table.insertColumn(self.col_count)
                        attr_list.append("%s.[%s]" % (attr.name(), i))
                        self.col_count += 1
                else:
                    self.ui.info_table.insertColumn(self.col_count)
                    attr_list.append(attr.name())
                    self.col_count += 1
            self.ui.info_table.setHorizontalHeaderLabels(attr_list)


def show_window():
    app = geoInfo()
    app.setParent(hou.qt.floatingPanelWindow(None), QtCore.Qt.Window)
    app.show()
