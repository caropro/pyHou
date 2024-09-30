#coding = utf-8

import os
import hou
print("Start Sea Cal Step 1")


#import hda

#create file
#create node
ObjNode = hou.node("/obj")
geoNode = ObjNode.createNode("geo","Geo")

#CreateBigWorldHfNode

BigWorldCacheScatterRead = geoNode.createNode("BigWorldCacheScatterRead","BigWorldCacheScatterRead")
print("Create BigWorldCacheScatterRead Node")
BigWorldCacheScatterRead.allowEditingOfContents()
BigWorldCacheScatterRead.parm("ReadHF").pressButton()
print("Load Hfs")

SumSeaGen = geoNode.createNode("SumSeaGen","SumSeaGen")
print("Create SumSeaGen Node")
SumSeaGen.allowEditingOfContents()
SumSeaGen.setInput(0,BigWorldCacheScatterRead)

SumSeaGen.parm("simStep1").pressButton()
print("Save simStep1 Result")

#close file
file_name = r"D:/testNewSumSeaGen_Step1.hip"
hou.hipFile.save(file_name=file_name)

#quit hou
hou.exit()