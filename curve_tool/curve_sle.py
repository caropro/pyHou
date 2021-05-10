# coding = utf-8
import json
import hou
import os


def saveCurve(*args, **kwargs):
    node = hou.pwd()
    container = hou.pwd().node("Curve_container")
    node_name = node.type().name()
    node_path = node.type().definition().libraryFilePath()
    data_folder = os.path.dirname(node_path) + "/%s_data" % node_name
    if os.path.exists(data_folder):
        for file_del in os.listdir(data_folder):
            os.remove(os.path.join(data_folder, file_del))
    else:
        os.mkdir(data_folder)

    # get curve nodes
    curve_node_list = []
    for pend_node in container.children():
        # print(pend_node)
        if pend_node.type().name() == "curve":
            curve_node_list.append(pend_node)
    # save every node and every parm
    for curve_node in curve_node_list:
        name = curve_node.name()
        curve_dic = {}
        for parm in curve_node.parms():
            curve_dic[parm.name()] = parm.eval()
            # print parm.name()
            # print parm.eval()
        data_file = r"%s\%s.json" % (data_folder, name)
        if not curve_dic.get("width"):
            curve_dic["width"] = 10;
        with open(data_file, "w+") as outfile:
            json.dump(curve_dic, outfile)
    hou.ui.displayMessage("Save!")


def loadCurve(*args, **kwargs):
    node = hou.pwd()
    container = hou.pwd().node("Curve_container")
    node_path = node.type().definition().libraryFilePath()
    node_name = node.type().name()
    data_folder = os.path.dirname(node_path) + "/%s_data" % node_name
    if not os.path.exists(data_folder):
        return
    # delete all child node
    for c_node in container.children():
        c_node.destroy()

    # read data
    for curve_data in os.listdir(data_folder):
        full_data_path = os.path.join(data_folder, curve_data)
        curve_name = os.path.splitext(curve_data)[0]

        # create curve node
        target_node = container.createNode("curve", curve_name)

        parm_dic = {}
        with open(full_data_path, "r") as outfile:
            all_info = outfile.read()
            parm_dic = json.loads(all_info)

        # add width parm to interface
        current_tmpparm = target_node.parmTemplateGroup()
        current_tmpparm.append(hou.FloatParmTemplate("width", "Width", 1))
        target_node.setParmTemplateGroup(current_tmpparm)
        target_node.setParms(parm_dic)
    hou.ui.displayMessage("Loaded!")


def add_curve(*args, **kwargs):
    node = hou.pwd()
    container = node.node("Curve_container")
    curve_count = node.parm("add_count").eval()
    if curve_count:
        for i in range(curve_count):
            # add curve node
            container.createNode("curve")
    container.layoutChildren()
    hou.ui.displayMessage("Added!")


def clear_curve(*args, **kwargs):
    container = hou.pwd().node("Curve_container")
    for pend_node in container.children():
        # print(pend_node)
        if pend_node.type().name() == "curve":
            pend_node.destroy()
    hou.ui.displayMessage("All Curves Clear!")

def merge_curve(*args, **kwargs):
    container = hou.pwd().node("Curve_container")
    curve_list = []
    merge_node = None
    for pend_node in container.children():
        # curve_list
        if pend_node.type().name() == "curve":
            curve_list.append(pend_node)
        if pend_node.type().name() == "merge":
            merge_node = pend_node
    if merge_node:
        count = 0
        for curve in curve_list:
            merge_node.setInput(count, curve, 0)
            count += 1
    else:
        merge_node = container.createNode("merge")
        count = 0
        for curve in curve_list:
            merge_node.setInput(count, curve, 0)
            count += 1
    merge_node.setRenderFlag(True)
    merge_node.setDisplayFlag(True)
    hou.ui.displayMessage("Done!")