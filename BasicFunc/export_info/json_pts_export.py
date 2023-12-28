#coding = utf-8
import json
import hou
import os

def saveCurve(*args, **kwargs):
    node = hou.pwd()
    node_name = node.type().name()
    node_path = node.type().definition().libraryFilePath()
    data_folder = os.path.dirname(node_path)+"/%s_data"%node_name
    data_file = r"%s\%s.json" % (data_folder, node_name)
    if os.path.exists(data_folder):
        for file_del in os.listdir(data_folder):
            os.remove(os.path.join(data_folder,file_del))
    else:
        os.mkdir(data_folder)

    # get curve nodes
    tar_node = node.node("OUT")
    info_dict = {}
    dic = []
    for pt in tar_node.geometry().points():
        info_dict = {}
        pos = pt.attribValue("P")
        new_pos = []
        new_pos.append(pos[0]*100)
        new_pos.append(pos[2]*100)
        new_pos.append(pos[1]*100)
        info_dict["position"]=new_pos
        index = pt.number()
        if index%2 ==0:
            info_dict["TID"] = 0
        else:
            info_dict["TID"] = 1
        info_dict["extra_info"]=pt.attribValue("extra_info")
        dic.append(info_dict)
    with open(data_file, "w+") as outfile:
        info = json.dumps(dic,indent=4)
        outfile.write(info)
    print("Save!!!")
