# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import hou
import os
import sys
from imp import reload
current_dir = os.path.dirname(kwargs["type"].definition().libraryFilePath())
parent_dir = os.path.dirname(current_dir)
tar_dir = os.path.join(parent_dir,"scripts/python_modules")
sys.path.append(tar_dir)
import parmFunc as pf
reload(pf)

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
    pf.loadCurvesData(data_folder, node)
    print("Loaded!")