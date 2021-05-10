# coding = utf-8
import json
import hou
import os
import stat
from collections import OrderedDict
import json
import sys
current_dir = os.path.dirname(kwargs["type"].definition().libraryFilePath())
parent_dir = os.path.dirname(current_dir)
tar_dir = os.path.join(parent_dir,"scripts/python_modules")
sys.path.append(tar_dir)
import parmFunc as pf
reload(pf)

language_dict = {"width": r"宽度", "depth": r"深度", "width_ramp": r"宽度曲线", "depth_ramp": r"深度曲线",
                 "horizontal_section": r"横切面","water_sink": r"水面下沉","Flow_mask": r"分支延申","FlowBlur": r"分支范围模糊",
                 "mask_distort_amp": r"分支范围扭曲强度","mask_distort_size": r"分支范围扭曲大小","minMask": r"分支遮罩最小值",
                 "rainAmount": r"降雨量","rainDensity": r"降雨强度","spreadIter": r"流动扩散次数","smoothIter": r"流动模糊次数","TurnAngle": r"曲直角度"}

def addCTP(target_node):
    pt_count = len(target_node.geometry().points())
    target_node.setParms({"width_ramp": pt_count})
    target_node.setParms({"depth_ramp": pt_count})
    width_ramp = target_node.parm("width_ramp").evalAsRamp()
    depth_ramp = target_node.parm("depth_ramp").evalAsRamp()
    for pt in range(1, pt_count + 1):
        pos = round(pt / float(pt_count),4)
        width_rampValue = round(width_ramp.lookup(pos),4)
        depth_rampValue = round(depth_ramp.lookup(pos),4)
        target_node.setParms({"width_ramp%spos" % pt: pos})
        target_node.setParms({"depth_ramp%spos" % pt: pos})
        target_node.setParms({"width_ramp%svalue" % pt: width_rampValue})
        target_node.setParms({"depth_ramp%svalue" % pt: depth_rampValue})

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
    data_folder = os.path.dirname(node_path)+"/%s_data"%node_name
    #load data
    pf.loadCurvesData(data_folder,node,post_func=addCTP,language_dict=language_dict)
    print("Loaded!")





