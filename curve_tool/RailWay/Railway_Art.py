# coding = utf-8
import hou
import os
import sys
import json
import os
import sys
current_dir = os.path.dirname(kwargs["type"].definition().libraryFilePath())
parent_dir = os.path.dirname(current_dir)
tar_dir = os.path.join(parent_dir, "scripts/python_modules")
sys.path.append(tar_dir)
import parmFunc as pf

reload(pf)


def railWayData(target_node):
    current_tmpparm = target_node.parmTemplateGroup()
    current_tmpparm.append(hou.StringParmTemplate("Style", "Style", 1))
    current_tmpparm.append(hou.FloatParmTemplate("width", "Width", 1))
    target_node.setParmTemplateGroup(current_tmpparm)
    target_node.setParms({"Style": "HRS_Default"})


def saveCurve(*args, **kwargs):
    node = hou.pwd()
    node_name = node.type().name()
    node_path = node.type().definition().libraryFilePath()
    data_folder = os.path.dirname(node_path) + "/%s_data" % node_name
    pf.createFolder(data_folder)
    # save_node
    result = pf.saveCurvesData(node, data_folder)
    if result:
        hou.ui.displayMessage("Save!!")
        return


def loadCurve(*args, **kwargs):
    node = hou.pwd()
    node_path = node.type().definition().libraryFilePath()
    node_name = node.type().name()
    data_folder = os.path.dirname(node_path) + "/%s_data" % node_name
    # load data
    pf.loadCurvesData(data_folder, node, pre_func=railWayData)
    print("Loaded!")
