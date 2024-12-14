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

ConfigPath=r"F:\m2_doc\PCGBuilding\BLD_A.json"
ExportPath = r"F:\m2_doc\PCGBuilding\bld_Export_A"
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
    RuleFile = BuildingData["RuleFile"]

ExportName = name

#Set Config
pcgbuildingcalflow.parm("Scanpath").set(BlocksPath)
pcgbuildingcalflow.parm("hdap_AssetDir").set(AssetPath)
pcgbuildingcalflow.parm("PerTypeRandCount").set(PerCount)
pcgbuildingcalflow.parm("hdap_FloorSetting").set(2)
pcgbuildingcalflow.parm("hdap_ConfigFile").set(RuleFile)

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
