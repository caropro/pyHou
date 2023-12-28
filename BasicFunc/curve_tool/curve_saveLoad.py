# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import hou
import json
import os
import logging


def SaveCurve(*args, **kwargs):
    node = hou.pwd()
    filePath = node.parm("CurveFile").eval()
    #
    node_name = node.type().name()
    node_path = node.type().definition().libraryFilePath()
    data_folder = os.path.dirname(node_path) + "/%s_data" % node_name

    # get curve node
    CurveNode = node.node("BaseCurve")
    point_data = CurveNode.parm("coords").eval()
    if (filePath.endswith("json")):
        curve_dic = {}
        curve_dic["coords"] = point_data
        with open(filePath, "w+") as outfile:
            json.dump(curve_dic, outfile)

        hou.ui.displayMessage("Save!")


def ReadCurve(*args, **kwargs):
    node = hou.pwd()
    filePath = node.parm("CurveFile").eval()
    #
    node_name = node.type().name()
    node_path = node.type().definition().libraryFilePath()
    data_folder = os.path.dirname(node_path) + "/%s_data" % node_name

    # get curve node
    CurveNode = node.node("BaseCurve")

    if (filePath.endswith("json")):
        with open(filePath, "r+") as outfile:
            parm_dic = json.loads(outfile)
        CurveNode.setParms(parm_dic)
        hou.ui.displayMessage("Load!")
