#coding = utf-8
import hou
import os
import sys

HouLandPath = r"E:\REF\Art\HouLand\LandscapeHDAs"

for fpathe,dirs,fs in os.walk("E:\REF\Art\HouLand"):
    for f in fs:
        HDAPath = os.path.join(fpathe,f)
        if(HDAPath.endswith(".hda")):
            try:
                hou.hda.installFile(HDAPath)
            except:
                raise ZeroDivisionError

file_name = r"D:/testNew.hip"

ObjNode = hou.node("/obj")
#create Geo
geoNode = ObjNode.createNode("geo","Geo")

# HDANames = ["DesertArea","ForestArea","FrozenPlatform","IceTown","InitialOrigin","JadePlace","Searinglands","SteelCity"]
HDANames = ["InitialOrigin"]
for i in HDANames:
    hou.hda.installFile(os.path.join(HouLandPath,i+".hda"))
    SeamHDANode = geoNode.createNode(i,i)
    print(i+"________Loading")
    SeamHDANode.allowEditingOfContents()
    SeamHDANode.parm("export_tile").pressButton()

print("Done")
hou.hipFile.save(file_name=file_name)