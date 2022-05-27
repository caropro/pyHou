# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0

import hrpyc
import hou
import os
connection,hou = hrpyc.import_remote_module()
ui = connection.modules.hou.ui

hda_path = r"C:\Users\jianx\Documents\houdini19.0\HouLand\OperatorHDAs\Utilities"
targetNode = hou.node("/obj/geo1")

#get hda name list
hdas = [f.split(".")[0] for f in os.listdir(hda_path) if f.endswith(".hda")]
for hda in hdas:
    print(hda)
    #create hda in target folder
    if(hda=="RTF"):
        continue
    targetNode.createNode(hda)
