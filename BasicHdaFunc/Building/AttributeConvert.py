# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import hrpyc
import hou
connection,hou = hrpyc.import_remote_module()
#ui = connection.modules.hou.ui


node = hou.pwd()
geo = node.geometry()

datanode = node.inputs()[1]
datageo = datanode.geometry()
# Add code to modify contents of geo.
# Use drop down menu to select examples.

pts = datageo.points()
attrDict = {attr.name().split("_")[-1]:attr.name() for attr in datageo.pointAttribs()}
#print(attrDict)

geo.addAttrib(hou.attribType.Point,"Type","")
geo.addAttrib(hou.attribType.Point,"instance_path","")
geo.addAttrib(hou.attribType.Point,"FloorNumber",0)
geo.addAttrib(hou.attribType.Point,"scale_x",0.0)
geo.addAttrib(hou.attribType.Point,"scale_y",0.0)
geo.addAttrib(hou.attribType.Point,"scale_z",0.0)

for pt in pts:
    new_pt = geo.createPoint()
    #print(dir(new_pt))
    for attr,attr_find in attrDict.items():
        attr_value = pt.attribValue(attr_find)
        #print(attr)
        if(geo.findPointAttrib(attr)):
            if(attr == "FloorNumber"):
                attr_value = int(attr_value)
            new_pt.setAttribValue(attr,attr_value)
