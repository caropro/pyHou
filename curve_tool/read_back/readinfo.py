#coding = utf-8
import hou
import log

current_node = hou.pwd()
geo = current_node.geometry()
curve_data = current_node.parent()
parent = curve_data.parent()
root_node = parent.parent()
data_node = hou.node(current_node.inputs()[1].path())

curve_node_list = []
curve_list=[]
for pend_node in data_node.children():
    # print(pend_node)
    if pend_node.type().name() == "curve":
        curve_node_list.append(pend_node)

attrib = geo.addAttrib(hou.attribType.Point,"data","x")
for curve_node in curve_node_list:
    curve_path = curve_node.path()
    point = geo.createPoint()
    point.setAttribValue(attrib,curve_path)
