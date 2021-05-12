# coding = utf-8
import hou
import os
import csv
import sys

current_dir = os.path.dirname(kwargs["type"].definition().libraryFilePath())
dataFolder = os.path.join(current_dir.split("HouLand")[0], "HouLand\PublicDataHDAs\FoliageCluster_data")


def exportCsv(*args, **kwargs):
    node = hou.pwd()
    Area = node.parm("Area").eval()
    file_name = node.parm("Filename").eval()
    data_folder = os.path.normpath(os.path.join(dataFolder, Area))
    data_node = node.node("Data")
    data_geo = data_node.geometry()
    SetTypes = [node.parm("SetName_%s" % x + 1).eval() for x in range(node.parm("CircleOc").eval())]

    data_headers = ["Foliage_Circles", "Pos", "Rot", "scale", "geoPath", "bboxMax"]
    data_dict = {}
    data_list = []
    for pt in data_geo.points():
        # print(dir(pt))
        PosValue = pt.attribValue("P")
        RotValue = pt.attribValue("rot_data")
        ScaleValue = pt.attribValue("scaleValue")
        geoPath = pt.attribValue("unreal_instance")
        bboxMax = pt.attribValue("bmax")
        data_dict["Foliage_Circles"] = str(SetTypes)
        data_dict["Pos"] = PosValue
        data_dict["Rot"] = RotValue
        data_dict["scale"] = ScaleValue
        data_dict["geoPath"] = geoPath
        data_dict["bboxMax"] = bboxMax
        data_list.append(data_dict)
        data_dict = {}

    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
    dataFile = os.path.join(data_folder, "%s.csv" % file_name)
    with open(dataFile, "w+") as csvFile:
        f_csv = csv.DictWriter(csvFile, data_headers)
        f_csv.writeheader()
        f_csv.writerows(data_list)