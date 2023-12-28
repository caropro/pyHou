#coding = utf-8
import json
import hou
import os
import stat

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
    curve_dict = {}
    for point in curves_data.geometry().points():
        curveName = point.attribValue("name")
        width = point.attribValue("width")
        point_pos = point.position()
        pos = "{},{},{}".format(*point_pos)
        if not curve_dict.get(curveName):
            curve_dict[curveName]={"coords":"","width":10, "close": 0, "type":0, "method": 1}
        curve_dict[curveName]["coords"]=curve_dict[curveName]["coords"]+pos+" "
        curve_dict[curveName]["coords"].strip()
        curve_dict[curveName]["width"] = width
    # save every node and every parm
    for curve in curve_dict:
        data_dict = curve_dict.get(curve)
        data_file = r"%s\%s.json" % (data_folder, curve)
        with open(data_file, "w+") as outfile:
            json.dump(data_dict, outfile)
    print("Save!!!")


def loadCurve(*args, **kwargs):
    node = hou.pwd()
    node_path = node.type().definition().libraryFilePath()
    node_name = node.type().name()
    curves_node = node.node("Curves")
    data_folder = os.path.dirname(node_path)+"/%s_data"%node_name
    if not os.path.exists(data_folder):
        return
    # delete all child node
    for c_node in curves_node.children():
        c_node.destroy()

    #read data
    for curve_data in os.listdir(data_folder):
        full_data_path = os.path.join(data_folder,curve_data)
        curve_name = os.path.splitext(curve_data)[0]

        #create curve node
        target_node = curves_node.createNode("curve",curve_name)

        parm_dic = {}
        with open(full_data_path, "r") as outfile:
            all_info = outfile.read()
            parm_dic = json.loads(all_info)

        #add width parm to interface
        current_tmpparm = target_node.parmTemplateGroup()
        current_tmpparm.append(hou.FloatParmTemplate("width","Width",1))
        target_node.setParmTemplateGroup(current_tmpparm)
        target_node.setParms(parm_dic)
    print("Loaded!")


