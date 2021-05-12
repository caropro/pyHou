#coding = utf-8

import os
import hou

print("Start Sum HDA Cal")

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

SumDeal = geoNode.createNode("SumDeal","SumDeal")
print("Create SumDeal Node")
SumDeal.allowEditingOfContents()
SumDeal.setInput(0,BigWorldCacheScatterRead)

SumDeal.parm("Sim").pressButton()
print("Save HDA Result")

#close file
file_name = r"D:/testNewHDA.hip"
hou.hipFile.save(file_name=file_name)

#quit hou
hou.exit()