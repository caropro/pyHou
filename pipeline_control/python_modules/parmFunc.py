#coding = utf-8
import hou
import os
import stat
from collections import OrderedDict
import json

def add_TMP(attr_name, tmp_type, current_tmpparm,language_dict=None):
    attr_label = attr_name
    if language_dict:
        attr_label = language_dict.get(attr_name, attr_name)
    if tmp_type == "FloatParmTemplate":
        current_tmpparm.append(hou.FloatParmTemplate(attr_name, attr_label, 1))
    elif tmp_type == "RampParmTemplate":
        current_tmpparm.append(hou.RampParmTemplate(attr_name, attr_label, hou.rampParmType.Float,
                                                    default_value=2, default_basis=None, color_type=None))
    elif tmp_type == "IntParmTemplate":
        current_tmpparm.append(hou.IntParmTemplate(attr_name, attr_label, 1))
    elif tmp_type == "StringParmTemplate":
        current_tmpparm.append(hou.StringParmTemplate(attr_name,attr_label, 1))
    elif tmp_type == "ToggleParmTemplate":
        current_tmpparm.append(hou.ToggleParmTemplate(attr_name,attr_label, 0))
    elif tmp_type == "SeparatorParmTemplate":
        current_tmpparm.append(hou.SeparatorParmTemplate(attr_name, attr_label, 1))
    return current_tmpparm

# create folder and reright the dir
def createFolder(data_path):
    #if folder dose not exist create new one(root one)
    print data_path
    if not os.path.exists(data_path):
        os.mkdir(data_path)
        return

# save curve data
def saveCurvesData(node,data_folder):
    # get file list
    file_list = []
    for level in os.walk(data_folder):
        dataDir = level[0]
        file_list.extend([os.path.join(dataDir, f) for f in level[2] if f.endswith("json")])

    curve_node_list = []
    for pend_node in node.children():
        print(pend_node)
        if pend_node.type().name() == "curve":
            curve_node_list.append(pend_node)
    # save every node and every parm
    for curve_node in curve_node_list:
        name = curve_node.name()
        curve_dic= OrderedDict()
        for parm in curve_node.parms():
            if type(parm.eval())!= hou.Ramp:
                curve_dic[parm.name()]={}
                curve_dic[parm.name()]["value"] = parm.eval()
                if isinstance(parm.eval(),float):
                    curve_dic[parm.name()]["value"]=round(parm.eval(),4)
                curve_dic[parm.name()]["temp"] = type(parm.parmTemplate()).__name__
            else:
                curve_dic[parm.name()]={}
                curve_dic[parm.name()]["value"] = parm.evalAsInt()
                curve_dic[parm.name()]["temp"] = type(parm.parmTemplate()).__name__
        data_file = r"%s\%s.json" % (data_folder, name)
        fullname = r"%s.json" % (name)
        file_path = [file for file in file_list if fullname in file]
        if (file_path):
            data_file = file_path[0]
            file_list.remove(data_file)
        with open(data_file, "w+") as outfile:
            json.dump(curve_dic, outfile)
    #remove rest file

    if file_list:
        for file_del in file_list:
            os.chmod(file_del,stat.S_IWRITE)
            os.remove(file_del)
    return True

def loadCurvesData(data_folder,node,pre_func=None,post_func=None,language_dict=None):
    if not os.path.exists(data_folder):
        return
    # delete all child node
    for c_node in node.children():
        c_node.destroy()
    #read data
    for level in os.walk(data_folder):
        dataDir = level[0]
        file_list = [f for f in level[2] if f.endswith("json")]
        for curve_data in file_list:
            full_data_path = os.path.join(dataDir,curve_data)
            curve_name = os.path.splitext(curve_data)[0]
            #create curve node
            target_node = node.createNode("curve",curve_name)
            parm_dic = {}
            with open(full_data_path, "r") as outfile:
                all_info = outfile.read()
                parm_dic = json.loads(all_info,object_pairs_hook=OrderedDict)
            current_tmpparm = target_node.parmTemplateGroup()
            if pre_func:
                pre_func(target_node)
            #iteration the k,v in dict_data
            for k,v in parm_dic.items():
                if target_node.parm(k):
                    value = v.get("value")
                    target_node.setParms({k:value})
                else:
                    data_type = v.get("temp")
                    value = v.get("value")
                    current_tmpparm = add_TMP(k,data_type,current_tmpparm,language_dict)
                    target_node.setParmTemplateGroup(current_tmpparm)
                    target_node.setParms({k: value})
            if post_func:
                post_func(target_node)

def loadCurvesDataSub(data_folder,node,pre_func=None,post_func=None,language_dict=None):
    #create sub folder in hda node
    pass