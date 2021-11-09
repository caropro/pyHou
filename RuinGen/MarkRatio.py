# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0

import hrpyc

connection,hou = hrpyc.import_remote_module()
ui = connection.modules.hou.ui

import hou

node = hou.selectedNodes()[-1]
geo = node.geometry()

root_node = node.parent()
# Add code to modify contents of geo.
# Use drop down menu to select examples.
pts = geo.points()
count = root_node.parm("BigObjs").eval()
#new Attr
RatioAttr = geo.addAttrib(hou.attribType.Point, "Ratio", 0)

index = 1
if(count):
    for pt in pts:
        ratio_name = "ScatterRatio_big%s"%index
        ratio = root_node.parm(ratio_name).eval()
        index += 1
        pt.setAttribValue(RatioAttr,ratio)

print("Done")