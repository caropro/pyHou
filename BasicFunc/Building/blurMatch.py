# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import hrpyc
# import hou
connection,hou = hrpyc.import_remote_module()
ui = connection.modules.hou.ui


currentNode = hou.selectedNodes()[0]
print(currentNode)
geo = currentNode.geometry()

parentNode = currentNode.parent()
DataNode = parentNode.node("BoxData")
DataGeo = DataNode.geometry()

def GetDataPack(geo):
    # get DataGeo's attribute
    attrlist = [attr.name() for attr in geo.pointAttribs()]
    print(attrlist)
    DataPack = {}
    #loop point in GataGeo
    for pt in geo.points():
        AssetName = pt.attribValue("name")
        #bound info
        height = pt.attribValue("height")
        width = pt.attribValue("width")
        depth = pt.attribValue("depth")
        #ratio info
        ratio = pt.attribValue("ratio")
        #area info
        # area = pt.attribValue("area")
        DataPack[AssetName] = {"height":height,"width":width,"depth":depth,"ratio":ratio}
    return DataPack

def compareDataPack():
    pass

def sortedList():
    pass




DataPack = GetDataPack(DataGeo)
print(DataPack)






