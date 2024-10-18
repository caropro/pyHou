# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import os
import hou
import json
import pdb
from cmdTest import RunPDG
try:
    import pdgcmd
    import pdgjson
except ImportError:
    from pdgjob import pdgcmd
    from pdgjob import pdgjson
printlog = pdgcmd.printlog

printlog("Running Houdini {} with PID {}".format(
    hou.applicationVersionString(), os.getpid()))

ConfigPath=r"D:\pcgConfig.json"
ExportPath = r"D:/BuildingFBX/"
PerCount = 4

# #create geo node
ObjNode = hou.node("/obj")
geoNode = ObjNode.createNode("geo","Geo")

# #Create PDG HDA
pcgbuildingcalflow = geoNode.createNode("PCGBuildingCalFlow","pcgbuildingcalflow")
printlog("----Create pcgbuildingcalflow Node----")

#Read Config File
with open(ConfigPath,"r") as f:
    data = json.load(f)
    printlog("Read Config File")

for name,BuildingData in data.items():
    AssetPath = BuildingData["AssetPath"]
    BlocksPath = BuildingData["BlocksPath"]
    FirstFloor = BuildingData["FirstFloor"]
    OtherFloor = BuildingData["OtherFloor"]

# print("AssetPath:",AssetPath)
# print("BlocksPath:",BlocksPath)
# print("FirstFloor:",FirstFloor)
# print("OtherFloor:",OtherFloor)
ExportName = name

FirstFloorS = [Section for Section in FirstFloor.split(" ") if not "R" in Section]
FirstFloorS = " ".join(FirstFloorS)
FirstFloorR = [Section for Section in FirstFloor.split(" ") if "R" in Section]
FirstFloorR = " ".join(FirstFloorR)
OtherFloorS = [Section for Section in OtherFloor.split(" ") if not "R" in Section]
OtherFloorS = " ".join(OtherFloorS)
OtherFloorR = [Section for Section in OtherFloor.split(" ") if "R" in Section]
OtherFloorR = " ".join(OtherFloorR)

# print("FirstFloorS:",FirstFloorS)
# print("FirstFloorR:",FirstFloorR)
# print("OtherFloorS:",OtherFloorS)
# print("OtherFloorR:",OtherFloorR)

#Set Config
pcgbuildingcalflow.parm("Scanpath").set(BlocksPath)
pcgbuildingcalflow.parm("hdap_AssetDir").set(AssetPath)
pcgbuildingcalflow.parm("PerTypeRandCount").set(PerCount)
pcgbuildingcalflow.parm("hdap_FloorSetting").set(2)
pcgbuildingcalflow.parm("hdap_Roof_Asset_1").set(FirstFloorR)
pcgbuildingcalflow.parm("hdap_Section_Asset_1").set(FirstFloorS)
pcgbuildingcalflow.parm("hdap_Roof_Asset_2").set(OtherFloorR)
pcgbuildingcalflow.parm("hdap_Section_Asset_2").set(OtherFloorS)

pcgbuildingcalflow.parm("hdap_ExportDir").set(ExportPath)
pcgbuildingcalflow.parm("hdap_FileName").set(f"{ExportName}_`@pdg_index`")

#unlock node
pcgbuildingcalflow.allowEditingOfContents()

#save file
file_name = r"D:/TestPDG2.hip"
hou.hipFile.save(file_name=file_name)


RunPDG(file_name)

ExportPath =os.path.normpath(ExportPath)
# open directory in explorer
os.system(f"explorer {ExportPath}")
