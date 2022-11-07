# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import hrpyc

connection,hou = hrpyc.import_remote_module()
ui = connection.modules.hou.ui

# import hou

import numpy

node = hou.pwd()
geo = node.geometry()

# Add code to modify contents of geo.
# Use drop down menu to select examples.

OrderList = ["Layer_BaseA","Layer_BaseB","Layer_Slope","Layer_Flow",
"Layer_Vegetation","Layer_Curvature","Layer_Foundation",
"Layer_RiverBank","Layer_River","Layer_Bed","Layer_RoadA","Layer_RoadB"]
OrderList.reverse()

AreaList = ["Area_Meadow","Area_Desert","Area_Snow"]

def liter(pos):
    RestVal = 0.9;
    for layer in OrderList:
        LayerPrim = LayerDict.get(layer)
        if not LayerPrim:
            continue
        layerVal = LayerPrim.voxel(pos)
        LayerPrim.setVoxel(pos, layerVal)
        sub = RestVal - layerVal
        if RestVal == 0:
            LayerPrim.setVoxel(pos, 0)
        elif sub < 0:
            LayerPrim.setVoxel(pos, RestVal)
            RestVal = 0
        else:
            RestVal = sub
    return

def area_Liter(pos):
    AreaVal = 0.1
    TotalArea = 0
    #CalSum
    for Area in AreaList:
        AreaPrim = AreaDict.get(Area)
        if AreaPrim:
            layerVal = AreaPrim.voxel(pos)
            TotalArea += layerVal
    #SetVal
    for Area in AreaList:
        AreaPrim = AreaDict.get(Area)
        if AreaPrim:
            layerVal = AreaPrim.voxel(pos)
            AreaPrim.setVoxel(pos, 0.1*(layerVal/TotalArea))



#Record Area Info
AreaDict = {}
for prim in geo.prims():
    name = prim.attribValue("name")
    if prim.type() == hou.primType.Volume and name in AreaList:
        AreaDict[name] = prim

#Record Display Layer Info
LayerDict = {}
for prim in geo.prims():
    name = prim.attribValue("name")
    if prim.type() == hou.primType.Volume and name in OrderList:
        LayerDict[name] = prim

pt = geo.point(0);
center = pt.position()
center = [0, 0, 0]

res_x, res_y, res_z = geo.prim(0).resolution()
posList = [[x_pos, y_pos, z_pos] for x_pos in range(res_x) for y_pos in range(res_y) for z_pos in range(res_z)]

for pos in posList:
    liter(pos)
    area_Liter(pos)