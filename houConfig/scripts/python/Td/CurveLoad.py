# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import json
import os
import hou


def loadCurve(*args, **kwargs):
    node = hou.selectedNodes()[0]
    node_name = node.name()
    test_path = r"D:\%s" % node_name
    if not os.path.exists(test_path):
        return
    # delete all child node
    for node in node.children():
        node.destroy()

    # read data
    for curve_data in os.listdir(test_path):
        full_data_path = os.path.join(test_path, curve_data)
        curve_name = os.path.splitext(curve_data)[0]

        # create curve node
        target_node = node.createNode("curve", curve_name)

        parm_dic = {}
        with open(full_data_path, "r") as outfile:
            all_info = outfile.read()
            parm_dic = json.loads(all_info)

        # add width parm to interface
        current_tmpparm = target_node.parmTemplateGroup()
        current_tmpparm.append(hou.FloatParmTemplate("width", "Width", 1))
        target_node.setParmTemplateGroup(current_tmpparm)
        target_node.setParms(parm_dic)
    print("Loaded!")
