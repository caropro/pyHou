#coding = utf-8

import os
import hou
print("Start River Cal")


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

SumRiver = geoNode.createNode("SumRiver","SumRiver")
print("Create SumRiver Node")
SumRiver.allowEditingOfContents()
SumRiver.setInput(0,BigWorldCacheScatterRead)

SumRiver.parm("Sim").pressButton()
print("Save SumRiver Result")

#close file
file_name = r"D:/testNewSumRiver.hip"
hou.hipFile.save(file_name=file_name)

#quit hou
hou.exit()