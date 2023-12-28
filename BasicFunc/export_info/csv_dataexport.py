# coding = utf-8
import hou
import os
import csv
import sys

current_dir = os.path.dirname(kwargs["type"].definition().libraryFilePath())
dataFolder = os.path.join(current_dir.split("Houland")[0], "HouLand\PublicDataHDAs\RiverCluster_data")


def exportCsv(*args, **kwargs):
    node = hou.pwd()
    file_name = node.parm("SetName").eval()
    data_folder = os.path.normpath(dataFolder)
    data_node = node.node("Data")
    data_geo = data_node.geometry()

    data_headers = ["Pos", "Rot", "scale", "geoPath"]
    data_dict = {}
    data_list = []
    for pt in data_geo.points():
        # print(dir(pt))
        PosValue = pt.attribValue("P")
        RotValue = pt.attribValue("rot_data")
        ScaleValue = pt.attribValue("scaleValue")
        geoPath = pt.attribValue("unreal_instance")
        data_dict["Pos"] = PosValue
        data_dict["Rot"] = RotValue
        data_dict["scale"] = ScaleValue
        data_dict["geoPath"] = geoPath
        data_list.append(data_dict)
        data_dict = {}

    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
    dataFile = os.path.join(data_folder, "%s.csv" % file_name)
    with open(dataFile, "w+") as csvFile:
        f_csv = csv.DictWriter(csvFile, data_headers)
        f_csv.writeheader()
        f_csv.writerows(data_list)