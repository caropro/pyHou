# coding = utf-8
import json
import hou
import os, sys, socket
import hrpyc
# import toolutils
# import soptoolutils
#
# connection, hou = hrpyc.import_remote_module()
# ui = connection.modules.hou.ui
# hou.ui = ui
# sys.modules["hou"] = hou

def Save():
    CurrentNode = hou.selectedNodes()[0]
    hda_path = CurrentNode.type().definition().libraryFilePath()
    level_a = CurrentNode.parm("root").eval()
    level_b = CurrentNode.parm("child").eval()
    data_path = os.path.normpath(os.path.join(os.path.dirname(hda_path), "BioCurve", level_a, level_b))
    if not os.path.exists(data_path):
        os.makedirs(data_path)

    curvenodes = [node for node in CurrentNode.children() if node.type().name() == 'curve']
    curve_data = {}
    for curve in curvenodes:
        scatter = curve.outputs()[0]
        nxt_node = scatter.outputs()[0]
        #mark dp_cluster node
        if(nxt_node.type().name()=='Depoly_cluster'):
            dp_node = nxt_node
        else:
            dp_node = None
        curve_data["Curve"] = {attr.name(): attr.eval() for attr in curve.allParms()}
        curve_data["Scatter"] = {attr.name(): attr.eval() for attr in scatter.allParms()}
        if(dp_node):
            curve_data["DP"] = {attr.name(): attr.eval() for attr in dp_node.allParms()}
        else:
            curve_data["DP"] = None


        print("___________________________")
        curve_path = os.path.join(data_path,"%s.json"%curve.name())
        if (os.path.exists(curve_path)):
            os.remove(curve_path)
        with open(curve_path, "w+") as outfile:
            json.dump(curve_data, outfile)
        #reset data
        curve_data={}


def Read():
    CurrentNode = hou.selectedNodes()[0]
    for c_node in CurrentNode.children():
        c_node.destroy()
    hda_path = CurrentNode.type().definition().libraryFilePath()
    level_a = CurrentNode.parm("root").eval()
    level_b = CurrentNode.parm("child").eval()
    data_path = os.path.normpath(os.path.join(os.path.dirname(hda_path), "BioCurve", level_a, level_b))
    if not os.path.exists(data_path):
        hou.ui.displayMessage("Path Does not exist")
        return

    merge_node = CurrentNode.createNode("merge")
    file_list = [f for f in os.listdir(data_path) if f.endswith("json")]
    parm_dic = {}
    for jsonFile in file_list:
        json_name=jsonFile.split(".")[0]
        jsonFilePath = os.path.join(data_path,jsonFile)
        with open(jsonFilePath, "r") as outfile:
            all_info = outfile.read()
            parm_dic = json.loads(all_info)

        curve_node = CurrentNode.createNode("curve",json_name)
        curve_data = parm_dic.get("Curve")
        for k,v in curve_data.items():
            curve_node.setParms({k: v})

        scatter_node = CurrentNode.createNode("scatter", "%s_Scatter"%json_name)
        Scatter_data = parm_dic.get("Scatter")
        for k, v in Scatter_data.items():
            scatter_node.setParms({k: v})

        scatter_node.setInput(0,curve_node, 0)
        final_node = scatter_node

        if(parm_dic.get("DP")):
            dp_node = CurrentNode.createNode("Depoly_cluster", "%s_Depoly_cluster" % json_name)
            dp_data = parm_dic.get("DP")
            dp_node.setParms({"min_R": dp_data.get("min_R")})
            dp_node.setParms({"max_R": dp_data.get("max_R")})
            dp_node.setParms({"min_num": dp_data.get("min_num")})
            dp_node.setParms({"max_num": dp_data.get("max_num")})
            dp_node.setParms({"fuse": dp_data.get("fuse")})
            dp_node.setInput(0,scatter_node, 0)
            final_node = dp_node

        merge_node.setInput(len(merge_node.inputs()), final_node, 0)
        # reset data
        parm_dic = {}

    output = CurrentNode.createNode("output", "output")
    output.setInput(0, merge_node,0)
