# coding = utf-8
import json
import hou
import os


def resetNode(*args, **kwargs):
    node = hou.pwd()
    container = node.node("Curve_data")
    # delete all child node
    for c_node in container.children():
        c_node.destroy()

def updateCurve(*args, **kwargs):
    resetNode()
    node = hou.pwd()
    curve_data = node.node("Curve_data")
    parent = node.parent()
    data_node = parent.node("Railway_Art")
    curve_node_list = []
    curve_list=[]
    for pend_node in data_node.children():
        # print(pend_node)
        if pend_node.type().name() == "curve":
            curve_node_list.append(pend_node)
    # create_mergeNode
    curve_merge = curve_data.createNode("object_merge")
    curve_merge.parm("numobj").set(len(curve_node_list))
    count = 1
    for curve_node in curve_node_list:
        curve_path = curve_node.path()
        curve_merge.parm("objpath%s"%count).set(curve_path)
        count+=1

    output = curve_data.createNode("output")
    output.setInput(0, curve_merge, 0)

    hou.ui.displayMessage("Done!")


