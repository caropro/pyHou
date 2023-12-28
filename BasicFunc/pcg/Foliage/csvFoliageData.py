# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import os
import csv
import hou
#read dataTable csv data convert to houdini data point
csv_file = r"D:\Top_PDG\FoliageData\Foliage_v2.csv"

node = hou.pwd()
geo = node.geometry()

datalist=[]
with open(csv_file,"r") as dataFile:
    reader = csv.DictReader(dataFile)
    for row in reader:
        datalist.append(row)

AttrList = [x for x,y in row.items() if x!="---"]
#print(AttrList)

UnFloatAttr = ["FoliageMesh","Tree","Bush","Misc","PlanetPos_N"]
for Attr in AttrList:
    if Attr in UnFloatAttr:
        continue
    else:
        geo.addAttrib(hou.attribType.Point,Attr,0.0)

geo.addAttrib(hou.attribType.Point,"type","")
geo.addAttrib(hou.attribType.Point,"unreal_instance","")

for data in datalist:
    new_pt = geo.createPoint()
    for key,value in data.items():
        if key == "---":
            continue
        elif key in UnFloatAttr:
            if key== "FoliageMesh":
                new_pt.setAttribValue("unreal_instance", value)
            elif key in ["Tree","Bush","Misc"] and value=="True":
                new_pt.setAttribValue("type", key)
            else:
                continue
        else:
            new_pt.setAttribValue(key,float(value))
