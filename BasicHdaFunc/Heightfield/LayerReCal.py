# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import hrpyc

connection,hou = hrpyc.import_remote_module()
ui = connection.modules.hou.ui

# import hou

# node = hou.pwd()
node = hou.selectedNodes()[0]
geo = node.geometry()

# import terraintoolutils
# LayerList =  terraintoolutils.buildNameMenu(node)

OrderList = ["BaseLayer_A","BaseLayer_B","LayerSlope","LayerFlow","LayerVegetation","LayerCurvature","water_river","water_bed","water_bank","River"]
OrderList.reverse()

def liter(pos):
    RestVal = 1;
    for layer in OrderList:
        LayerPrim = LayerDict.get(layer)
        if not LayerPrim:
            continue
        layerVal = LayerPrim.sample(pos)
        tmp = RestVal;
        RestVal-=layerVal
        if(RestVal<0):
            prim.setVoxel(pos, tmp);
            RestVal = 0
    return

res_x,res_y,res_z = geo.prim(0).resolution()
print(res_x,res_y,res_z)

LayerDict = {}
for prim in geo.prims():
    name = prim.attribValue("name")
    if prim.type()==hou.primType.Volume and name in OrderList:
        LayerDict[name] = prim

posList = [(x_pos,y_pos,0) for x_pos in range(res_x) for y_pos in range(res_y)]
for pos in posList:
    liter(pos)