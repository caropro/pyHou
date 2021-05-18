#coding = utf-8
import os,sys,socket
import hrpyc
import cProfile
import toolutils
import soptoolutils
import itertools

connection,hou = hrpyc.import_remote_module()
ui = connection.modules.hou.ui
hou.ui = ui
sys.modules["hou"] = hou

#TargetNode = hou.selectedNodes()[0]
data_node = hou.node("/obj/Geo_RepairHouLandSeam/HouLandSeamRepairer")
# data_node = TargetNode.parent()
print(data_node)

layerDict = {}
areaCount = data_node.parm("areas").eval()
print(areaCount)
for area_index in range(areaCount):
    area_index+=1
    areaname = data_node.parm("area_name_%s"%area_index).eval()
    arealayerCount = data_node.parm("area_mapping_%s"%area_index).evalAsInt()
    layerDict[areaname]={}
    for layerindex in range(arealayerCount):
        layerindex+=1
        print((area_index,layerindex))
        layername = data_node.parm("layer_%s_%s"%(area_index,layerindex)).eval()
        texturename = data_node.parm("texture_%s_%s"%(area_index,layerindex)).eval()
        layerDict[areaname][layername] = texturename

print(layerDict)