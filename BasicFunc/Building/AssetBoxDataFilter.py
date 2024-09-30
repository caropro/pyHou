# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0


#filter asset data with box size
#use box size to gen datatable and export related asset file
import hou
import math
import json
import os

import hrpyc
connection,hou = hrpyc.import_remote_module()
# ui = connection.modules.hou.ui

node = hou.selectedNodes()[0]
geo = node.geometry()

#bld
#height range 8-15
#width range 10-30


#80% 8-10
A_list = []
#15% 11-14
B_list = []
#5% 14-16
C_list = []

height_list = []
width_list = []
pts = geo.points()

removelist = []
for pt in pts:
    asset_type = pt.attribValue("type")
    asset_height = pt.attribValue("height")
    asset_depth = pt.attribValue("depth")
    asset_width = pt.attribValue("width")
    height_list.append(round(asset_height))
    width_list.append(round(asset_width))
    if asset_height >= 8 and asset_height <= 10:
        if(len(A_list) < 12):
            A_list.append(pt)
        else:
            removelist.append(pt)
    elif asset_height >= 11 and asset_height <= 14:
        if(len(B_list) < 8):
            B_list.append(pt)
        else:
            removelist.append(pt)
    elif asset_height >= 14 and asset_height <= 16:
        if(len(C_list) < 4):
            C_list.append(pt)
        else:
            removelist.append(pt)



for pt in removelist:
    geo.deletePoint(pt)