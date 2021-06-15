# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0


import hou
import json
import os


def saveCurve(*args, **kwargs):
    curve_dic = {}
    node = hou.selectedNodes()[0]
    node_name = node.name()
    if os.path.exists(r"D:/%s" % node_name):
        for file_del in os.listdir("D:/%s" % node_name):
            os.remove(os.path.join(r"D:/%s" % node_name, file_del))
    else:
        os.mkdir(r"D:\%s" % node_name)
    # get curve nodes
    curve_node_list = []
    for pend_node in node.children():
        print(pend_node)
        if pend_node.type().name() == "curve":
            curve_node_list.append(pend_node)
    if not curve_node_list:
        return
    # save every node and every parm
    for curve_node in curve_node_list:
        name = curve_node.name()
        for parm in curve_node.parms():
            curve_dic[parm.name()] = parm.eval()
        test_path = r"D:\%s\%s.json" % (node_name, name)
        with open(test_path, "w+") as outfile:
            json.dump(curve_dic, outfile)

    # curve_node = node.node("Target_node")
    #
    # # get point info
    # curve_points = curve_node.parm("coords").eval().strip().replace(", ", ",").split(" ")
    #
    # point_count = 0
    # point_dic = {}
    # for point in curve_points:
    #     point_x = point.split(",")[0]
    #     point_y = point.split(",")[1]
    #     point_z = point.split(",")[2]
    #     point_dic[point_count] = {"pos_x": point_x, "pos_y": point_y, "pos_z": point_z}
    #     point_count += 1
