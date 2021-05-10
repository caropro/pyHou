#coding = utf-8
import json
import hou
import os
import stat
from collections import OrderedDict
language_dict = {"width":r"宽度","depth":r"深度","width_ramp":r"宽度曲线","depth_ramp":r"深度曲线","horizontal_section":r"横切面",
                 "water_sink":r"水面下沉","reduce_seg":r"河面缩小段数","river_seg":r"河分段数"}

def add_TMP(attr_name,tmp_type,current_tmpparm):
    attr_label = language_dict.get(attr_name,attr_name)
    if tmp_type == "FloatParmTemplate":
        current_tmpparm.append(hou.FloatParmTemplate(attr_name,attr_label, 1))
    elif tmp_type == "RampParmTemplate":
        current_tmpparm.append(hou.RampParmTemplate(attr_name, attr_label, hou.rampParmType.Float,
                                              default_value=2,default_basis=None, color_type=None))
    elif tmp_type == "IntParmTemplate":
        current_tmpparm.append(hou.IntParmTemplate(attr_name,attr_label, 1))
    return current_tmpparm

def saveCurve(*args, **kwargs):
    node = hou.pwd()
    node_name = node.type().name()
    node_path = node.type().definition().libraryFilePath()
    curves_data = node.node("All_points")
    data_folder = os.path.dirname(node_path)+"/%s_data"%node_name
    if os.path.exists(data_folder):
        for file_del in os.listdir(data_folder):
            file_path = os.path.join(data_folder,file_del)
            os.chmod(file_path,stat.S_IWRITE)
            os.remove(file_path)
    else:
        os.mkdir(data_folder)
    # get curve nodes
    curve_node_list = []
    for pend_node in node.node("Curves").children():
        print(pend_node)
        if pend_node.type().name() == "curve":
            curve_node_list.append(pend_node)
    pointDict = {}
    for point in curves_data.geometry().points():
        curveName = point.attribValue("name")
        point_pos = point.position()
        pos = "{},{},{}".format(*point_pos)
        if not pointDict.get(curveName):
            pointDict[curveName] = {"coords":{"value":""}}
        pointDict[curveName]["coords"]["value"]=pointDict[curveName]["coords"]["value"]+pos+" "
        pointDict[curveName]["coords"]["value"].strip()

    # save every node and every parm
    for curve_node in curve_node_list:
        name = curve_node.name()
        curve_dic= OrderedDict()
        for parm in curve_node.parms():
            if type(parm.eval())!= hou.Ramp:
                curve_dic[parm.name()]={}
                curve_dic[parm.name()]["value"] = parm.eval()

                curve_dic[parm.name()]["temp"] = type(parm.parmTemplate()).__name__
            else:
                curve_dic[parm.name()]={}
                curve_dic[parm.name()]["value"] = parm.evalAsInt()

                curve_dic[parm.name()]["temp"] = type(parm.parmTemplate()).__name__
        curve_dic["coords"] = pointDict.get(name).get("coords")
        data_file = r"%s\%s.json" % (data_folder, name)
        # if not curve_dic.get("width"):
        #     curve_dic["width"] = 10;
        with open(data_file, "w+") as outfile:
            json.dump(curve_dic, outfile)
    print("Save!!!")


def loadCurve(*args, **kwargs):
    node = hou.pwd()
    node_path = node.type().definition().libraryFilePath()
    node_name = node.type().name()
    data_folder = os.path.dirname(node_path)+"/%s_data"%node_name
    curvefolder = node.node("Curves")
    if not os.path.exists(data_folder):
        return
    # delete all child node
    for c_node in curvefolder.children():
        c_node.destroy()

    #read data
    for curve_data in os.listdir(data_folder):
        full_data_path = os.path.join(data_folder,curve_data)
        curve_name = os.path.splitext(curve_data)[0]

        #create curve node
        target_node = curvefolder.createNode("curve",curve_name)

        parm_dic = {}
        with open(full_data_path, "r") as outfile:
            all_info = outfile.read()
            parm_dic = json.loads(all_info,object_pairs_hook=OrderedDict)

        current_tmpparm = target_node.parmTemplateGroup()
        #iteration the k,v in dict_data
        for k,v in parm_dic.items():
            if target_node.parm(k):
                value = v.get("value")
                target_node.setParms({k:value})
            else:
                data_type = v.get("temp")
                value = v.get("value")
                current_tmpparm = add_TMP(k,data_type,current_tmpparm)
                target_node.setParmTemplateGroup(current_tmpparm)
                target_node.setParms({k: value})
    print("Loaded!")


