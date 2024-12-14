# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import hou
import json,os,random
from random import sample
import numpy as np

# For Corner Normal and Type
def NormalCal(LastDir, NextDir):
    nx = NextDir.x()
    nz = NextDir.z()
    lx = LastDir.x()
    lz = LastDir.z()
    if nz > 0 and lx < 0:
        Cd = hou.Color(1.0, 1.0, 1.0)
        N = hou.Vector3(-1, 0, 0)
        CornerType = 0
    elif nx > 0 and lz > 0:
        Cd = hou.Color(1.0, 0, 0)
        N = hou.Vector3(0, 0, 1)
        CornerType = 1
    elif nz < 0 and lx > 0:
        Cd = hou.Color(0, 1.0, 0)
        N = hou.Vector3(1, 0, 0)
        CornerType = 2
    elif nx < 0 and lz < 0:
        Cd = hou.Color(0, 0, 1.0)
        N = hou.Vector3(0, 0, -1)
        CornerType = 3
    elif nx < 0 and lz > 0:
        Cd = hou.Color(1, 1.0, 0)
        N = hou.Vector3(-1, 0, 0)
        CornerType = 4
    elif nz > 0 and lx > 0:
        Cd = hou.Color(1.0, 0.5, 0)
        N = hou.Vector3(0, 0, 1)
        CornerType = 5
    elif nx > 0 and lz < 0:
        Cd = hou.Color(1, 0.5, 0.5)
        N = hou.Vector3(1, 0, 0)
        CornerType = 6
    elif nz < 0 and lx < 0:
        Cd = hou.Color(1.0, 0.5, 1)
        N = hou.Vector3(0, 0, -1)
        CornerType = 7
    else:
        #flatten Alert Not corner
        Cd = hou.Color(1,1,1)
        N = NextDir
        CornerType = -1
    return Cd, CornerType, N

# Corner Data Function
def CornerAssetData(current_sections=None, pt_SR="", node=hou.pwd()):
    """
        Corner Assets For Current Floor and Current Style
    """
    if current_sections is None:
        current_sections = []
    corner_sort_list = {"Corner": [], "CornerI": []}
    AssetData = {}
    CornerNode = node.inputs()[1]
    CornerGeo = CornerNode.geometry()
    corner_sort_list["Corner"] = list(CornerGeo.attribValue("cornerList"))
    corner_sort_list["CornerI"] = list(CornerGeo.attribValue("RcornerList"))
    CornerAssets = CornerGeo.prims()

    for asset in CornerAssets:
        id = CornerAssets.index(asset)
        CornerAsset_name = asset.attribValue("name")
        CornerAsset_Pos = asset.attribValue("Pos")
        CornerAsset_Style = asset.attribValue("Style")
        CornerAsset_UnitSize = asset.attribValue("UnitSize")
        if CornerAsset_Style not in current_sections or (pt_SR and pt_SR not in CornerAsset_Pos):
            #pop id from list if the asset does not match the current section
            if id in corner_sort_list["Corner"]:
                corner_sort_list["Corner"].remove(id)
            if id in corner_sort_list["CornerI"]:
                corner_sort_list["CornerI"].remove(id)
            continue
        AssetData[CornerAsset_name] = {"Pos": CornerAsset_Pos, "id": id, "style": CornerAsset_Style,
                                       "UnitSize": CornerAsset_UnitSize}
    return AssetData, corner_sort_list

def RandFromList(seed, ResourceList):
    if not ResourceList:
        return None
    random.seed(seed)
    return ResourceList[int(random.random() * len(ResourceList))]

def halfSetting(SectionAssetlist, RestDist, LimitKeyList, must_Convert,CurrentRules={}):
    """
    :param Socket: current Socket
    :param SectionAssetlist:
    :param RestDist:
    :param LimitKeyList:
    :return:
    """
    halfList = []
    if must_Convert:
        # Left 1m section for Convert
        RestDist -= 1
    SectionAssetlist = [asset for asset in SectionAssetlist if asset.split("_")[3] in ["Left", "Right", "Center"]]
    if not CurrentRules.get("AssetType",{}).get("Window",{}):
        return []
    Continuous_Limit = CurrentRules.get("AssetType").get("Window").get("Combine").get("Continuous")
    if Continuous_Limit:
        if RestDist > Continuous_Limit:
            RestDist = Continuous_Limit
    #logging.log(logging.INFO,"RestDist:{RestDist}--------------------------------------------------")
    if not SectionAssetlist:
        return []
    # Rand Select Length from 2-6 window parts
    if RestDist==2:
        LengthSelection = 2
    else:
        LengthSelection = np.random.randint(2, RestDist+1)
    LeftList = [Section for Section in SectionAssetlist if "Left" in Section]
    RightList = [Section for Section in SectionAssetlist if "Right" in Section]
    CenterList = [Section for Section in SectionAssetlist if "Center" in Section]

    LengthSelection = min(LengthSelection,6)
    L = LeftList[0]
    R = RightList[0]
    # init list with left and rigth
    # start with left end with right
    halfList.append(L)
    halfList.append(R)
    LengthSelectionForReturn = LengthSelection
    LengthSelection -= 2
    # add center
    while LengthSelection > 0:
        # rand select c from CenterList
        C = CenterList[np.random.randint(0, len(CenterList))]
        UnitSize = int(C.split("_")[-1][0])
        halfList.insert(-1, C)
        LengthSelection -= UnitSize

    return halfList

