#coding = utf-8
import hou
import os
import json
import sys
from pipeline_control.python_modules import parmFunc
import parmFunc as pf
reload(pf)

def railWayData(target_node):
    current_tmpparm = target_node.parmTemplateGroup()
    current_tmpparm.append(hou.StringParmTemplate("Style","Style",1))
    current_tmpparm.append(hou.FloatParmTemplate("width", "Width", 1))
    target_node.setParmTemplateGroup(current_tmpparm)
    target_node.setParms({"Style":"HRS_Default"})

def saveCurve(*args, **kwargs):
    node = hou.pwd()
    node_name = node.type().name()
    node_path = node.type().definition().libraryFilePath()
    data_folder = os.path.dirname(node_path)+"/%s_data"%node_name
    pf.createFolder(data_folder)
    #save_node
    result = pf.saveCurvesData(node,data_folder)
    if result:
        hou.ui.displayMessage("Save!!")
        return


def loadCurve(*args, **kwargs):
    node = hou.pwd()
    node_path = node.type().definition().libraryFilePath()
    node_name = node.type().name()
    data_folder = os.path.dirname(node_path) + "/%s_data" % node_name
    if not os.path.exists(data_folder):
        return
    # delete all child node
    for c_node in node.children():
        c_node.destroy()

    # read data
    for curve_data in os.listdir(data_folder):
        full_data_path = os.path.join(data_folder, curve_data)
        curve_name = os.path.splitext(curve_data)[0]

        # create curve node
        target_node = node.createNode("curve", curve_name)

        parm_dic = {}
        with open(full_data_path, "r") as outfile:
            all_info = outfile.read()
            parm_dic = json.loads(all_info)

        # add width parm to interface
        current_tmpparm = target_node.parmTemplateGroup()
        current_tmpparm.append(hou.StringParmTemplate("Style", "Style", 1))
        current_tmpparm.append(hou.FloatParmTemplate("width", "Width", 1))
        target_node.setParmTemplateGroup(current_tmpparm)
        target_node.setParms({"Style": "HRS_Default"})
        target_node.setParms(parm_dic)
    hou.ui.displayMessage("Loaded!")
