#coding = utf-8

import os
import hou
print("Start Sum HF Cal")

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

SumHF = geoNode.createNode("SumHF","SumHF")
print("Create SumHF Node")
SumHF.allowEditingOfContents()
SumHF.setInput(0,BigWorldCacheScatterRead)

SumHF.parm("Save").pressButton()
print("Save HF Result")

#close file
file_name = r"D:/testNew.hip"
hou.hipFile.save(file_name=file_name)

#quit hou
hou.exit()