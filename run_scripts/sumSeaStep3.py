#coding = utf-8

import os
import hou
print("Start Sea Cal Step 3")


#import hda

#create file

#create node
ObjNode = hou.node("/obj")
geoNode = ObjNode.createNode("geo","Geo")

SumSeaGen = geoNode.createNode("SumSeaGen","SumSeaGen")
print("Create SumSeaGen Node")
SumSeaGen.allowEditingOfContents()
SumSeaGen.parm("simStep3").pressButton()
print("Save simStep3 Result")

#close file
file_name = r"D:/testNewSumSeaGen_Step3.hip"
hou.hipFile.save(file_name=file_name)

#quit hou
hou.exit()