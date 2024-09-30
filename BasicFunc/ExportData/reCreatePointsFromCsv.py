# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import os
import csv
#import hou

# import hrpyc
# connection,hou = hrpyc.import_remote_module()
# ui = connection.modules.hou.ui
#read dataTable csv data convert to houdini data point
csv_file = r"D:\geoCsv\Test.csv"



datalist=[]
with open(csv_file,"r") as dataFile:
    reader = csv.DictReader(dataFile)
    for row in reader:
        datalist.append(row)

AttrList = [x for x,y in row.items() if x!="---"]
print(AttrList)
print(datalist)


def rename(newname):
    def decorator(f):
        f.__name__ = newname
        return f
    return decorator
@rename("f(x)")
def hahah(x):
    print(x)

print(hahah.__name__)
# node = hou.pwd()
# geo = node.geometry()

# UnFloatAttr = ["FoliageMesh","Tree","Bush","Misc","PlanetPos_N"]
# for Attr in AttrList:
#     if Attr in UnFloatAttr:
#         continue
#     else:
#         geo.addAttrib(hou.attribType.Point,Attr,0.0)
#
# geo.addAttrib(hou.attribType.Point,"type","")
# geo.addAttrib(hou.attribType.Point,"scale",[10.0,10.0,10.0])
# geo.addAttrib(hou.attribType.Point,"rotation",[0.0,0.0,0.0])
#
# for data in datalist:
#     new_pt = geo.createPoint()
#     pos = data.get("Transform")
#     pos = pos.split("(")[1].split(")")[0]
#     pos_x = float(pos.split(",")[0])
#     pos_y = float(pos.split(",")[1])
#     pos_z = float(pos.split(",")[2])
#
#     rot = data.get("Rotation")
#     rot = rot.split("(")[1].split(")")[0]
#     rot_x = float(rot.split(",")[0].split("=")[1])
#     rot_y = float(rot.split(",")[1].split("=")[1])
#     rot_z = float(rot.split(",")[2].split("=")[1])
#
#     scale = data.get("Scale")
#     scale = scale.split("(")[1].split(")")[0]
#     scale_x = float(scale.split(",")[0])
#     scale_y = float(scale.split(",")[1])
#     scale_z = float(scale.split(",")[2])
#
#     new_pt.setPosition([pos_x,pos_z,pos_y])
#     new_pt.setAttribValue("type",data["InsName"])
#     new_pt.setAttribValue("scale", [scale_x, scale_y, scale_z])
#     new_pt.setAttribValue("rotation", [rot_x, rot_y, rot_z])

    #print(pos_x,pos_y,pos_z)