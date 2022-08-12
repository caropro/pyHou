# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import hrpyc
import os
import re

connection,hou = hrpyc.import_remote_module()
ui = connection.modules.hou.ui

import re

# current node
node = hou.pwd()
geo = node.geometry()
# input data
datanode = node.inputs()[1]
datageo = datanode.geometry()

# get datadict
pts = datageo.points()
pattern = re.compile(r'\d+')

attrDict = {}
for attr in datageo.pointAttribs():
    Number = pattern.findall(attr.name())
    if Number:
        ShortName = attr.name().split(Number[0] + "_")[-1]
    else:
        ShortName = attr.name()
    attrDict[ShortName] = attr.name()

geo.addAttrib(hou.attribType.Point, "Type", "")
geo.addAttrib(hou.attribType.Point, "unreal_instance", "")
floatAttrs = ["Level",
              "ViabilityRadius",
              "PriorityRadius",
              "MinScale", "MaxScale",
              "Slope_Min", "Slope_Max",
              "Wet_Min", "Wet_Max",
              "Altitude_Max", "Altitude_Min",
              "OCC_Min", "OCC_Max", ]

for floatAttr in floatAttrs:
    geo.addAttrib(hou.attribType.Point, floatAttr, 0.0)

PartList = ["Tree", "Bush", "Misc"]

for pt in pts:
    new_pt = geo.createPoint()
    for attr, attr_find in attrDict.items():
        if not attr:
            continue
        attr_value = pt.attribValue(attr_find)
        # print("AttrattrName: {}\n AttrVal: {}".format(attr_find,attr_value))

        if attr == "FoliageMesh":
            new_pt.setAttribValue("unreal_instance", attr_value)
        elif attr in PartList:
            print(attr)
        elif attr in floatAttrs:
            new_pt.setAttribValue(attr, float(attr_value))
