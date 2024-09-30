# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import json
import os
import math
import random
import numpy as np
import hou
import logging
import copy

from layout.assetlayoutinterface import Asset

# init log level
logging.basicConfig(level=logging.INFO)

node = hou.pwd()
geo = node.geometry()

# Add code to modify contents of geo.
# Use drop down menu to select examples.
rulePath = node.parm("ConfigFile").eval()

# add point attrib
geo.addAttrib(hou.attribType.Point, "cornertype", -1)
geo.addAttrib(hou.attribType.Point, "cornerWidth", 0)
geo.addAttrib(hou.attribType.Point, "AssetName", "")
geo.addAttrib(hou.attribType.Point, "SectionType", -1)
# create point group
geo.createPointGroup("CornerPoint")
geo.createPointGroup("SectionPoint")

# Read Rule Config
with open(rulePath, "r") as datafile:
    datastring = datafile.read()
    # print(datastring)
    datapack = json.loads(datastring)

currentprim = geo.prims()[0]
currentFloor = currentprim.attribValue("floor")
currentFloor += 1
currentSections = list(geo.attribValue("SectionList"))
currentArea = currentprim.attribValue("area")

CurrentRules = datapack.get("Level").get(str(currentFloor))
if not CurrentRules:
    CurrentRules = datapack.get("Level").get("Default")

LowerFloorGeo = node.inputs()[3].geometry()

# Corner Data Function
def CornerAssetData(currentSections=currentSections):
    """
        Corner Assets For Current Floor and Current Style
    """
    CornerSortList = {"Corner": [], "ConrerI": []}
    AssetData = {}
    CornerNode = node.inputs()[1]
    CornerGeo = CornerNode.geometry()
    CornerSortList["Corner"] = list(CornerGeo.attribValue("cornerList"))
    CornerSortList["CornerI"] = list(CornerGeo.attribValue("RcornerList"))
    CornerAssets = CornerGeo.prims()
    for asset in CornerAssets:
        id = CornerAssets.index(asset)
        CornerAsset_name = asset.attribValue("name")
        CornerAsset_Pos = asset.attribValue("Pos")
        CornerAsset_Style = asset.attribValue("Style")
        CornerAsset_UnitSize = asset.attribValue("UnitSize")
        if CornerAsset_Style not in currentSections:
            continue
        # print(f"name:{CornerAsset_name}\npos:{CornerAsset_Pos}\nstyle:{CornerAsset_Style}\nunitSize:{CornerAsset_UnitSize}")
        AssetData[CornerAsset_name] = {"pos": CornerAsset_Pos, "id": id, "style": CornerAsset_Style,
                                       "UnitSize": CornerAsset_UnitSize}
    return AssetData, CornerSortList


# Corner index,pos,Dir,asset,size
CornerData = {}

# Global Section Asset
SectionAssetsNode = node.inputs()[2]
SectionAssetsGeo = SectionAssetsNode.geometry()
SectionAssets = SectionAssetsGeo.prims()


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
    return Cd, CornerType, N

def RandFromList(seed, ResourceList):
    random.seed(seed)
    return ResourceList[int(random.random() * len(ResourceList))]

def CalPoints(CurrentRules):
    """
    :param CurrentRules: Rule Dict Data
    Cal Corner Type First and Record data according to the rules
    Cal Section Type Second
    :return:
    """
    CornerRecordList = {}
    pts = currentprim.points()
    pts.pop()
    len_count = len(pts)
    # get Rule Limit Count

    # Door Type
    C_DoorCount = 0
    Door_DistLimit = 0
    DoorCount = 999
    if CurrentRules.get("AssetType") != {}:
        DoorRule = CurrentRules.get("AssetType").get("Door")
        Door_AreaLimit = DoorRule.get("Area limit")
        Door_DistLimit = DoorRule.get("Distance limit")
        DoorCount = DoorRule.get("Count exceed") if currentArea > Door_AreaLimit else DoorRule.get("Count below")
        Door_EdgeLimit = DoorRule.get("Edge Length")
        Door_SameSide = DoorRule.get("Same Side")

    DoorPosList = []
    DooridList = []

    # get Corner data list
    AssetData, CornerSortList = CornerAssetData(currentSections)
    CornerList = CornerSortList["Corner"]
    CornerIList = CornerSortList["CornerI"]

    StyleLimit = {}
    #Create Corner Style Limit Dict
    if CurrentRules.get("StyleLimit"):
        StyleLimit = copy.deepcopy(CurrentRules.get("StyleLimit"))

    for pt in pts:
        seed = pt.attribValue("seed")
        index = pts.index(pt)
        lastindex = index - 1
        nextindex = index + 1 if index != (len_count - 1) else 0
        current_pos = pt.position()

        last_targetPoint = pts[lastindex]
        last_pos = last_targetPoint.position()

        next_targetPoint = pts[nextindex]
        next_pos = next_targetPoint.position()
        last_distance = current_pos.distanceTo(last_pos)
        next_distance = current_pos.distanceTo(next_pos)

        minDistance = min(last_distance, next_distance)

        NextDir = (next_pos - current_pos).normalized()
        LastDir = (current_pos - last_pos).normalized()

        Cd, CornerType, N = NormalCal(LastDir, NextDir)

        # pre filter
        # Door Limit
        DoorAssetList = [v["id"] for k, v in AssetData.items() if k.split("_")[1] == "Door"]
        NoDoorCornerList = [id for id in CornerList if id not in DoorAssetList]
        NoDoorCornerIList = [id for id in CornerIList if id not in DoorAssetList]

        if CornerType < 4:
            cornertype = RandFromList(seed, CornerList)
        else:
            cornertype = RandFromList(seed, CornerIList)

        if C_DoorCount == DoorCount or minDistance < Door_DistLimit:
            if CornerType < 4:
                cornertype = RandFromList(seed, NoDoorCornerList)
            else:
                cornertype = RandFromList(seed, NoDoorCornerIList)

        assetname = [k for k, v in AssetData.items() if v["id"] == cornertype][0]
        assettype = assetname.split("_")[1]
        assetStyle = assetname.split("_")[2]
        print(assetStyle)
        # Door Limit
        if C_DoorCount < DoorCount and assettype == "Door":
            passValue = True
            # print(DooridList)
            # same side filter
            if (lastindex in DooridList) or (nextindex in DooridList):
                passValue = False
            else:
                # dist filter
                for otherDoorPos in DoorPosList:
                    dist = otherDoorPos.distanceTo(current_pos)
                    print(f"dist Door:{dist}")
                    if dist < 5:
                        print("Change")
                        passValue = False
                        break
            if passValue:
                DoorPosList.append(current_pos)
                DooridList.append(index)
                C_DoorCount += 1
            else:
                # change to Other Type
                if CornerType < 4:
                    cornertype = RandFromList(seed, NoDoorCornerList)
                else:
                    cornertype = RandFromList(seed, NoDoorCornerIList)
                pass
            assetname = [k for k, v in AssetData.items() if v["id"] == cornertype][0]
            assettype = assetname.split("_")[1]
        else:
            #Style Limit
            StyleLimitList = [k for k, v in StyleLimit.items()]
            print(StyleLimitList)
            if assetStyle in StyleLimitList:
                if StyleLimit[assetStyle]["CornerLimit"]==0:
                    TmpCornerList = [AssetData.get(k).get("id") for k, v in AssetData.items() if v.get("style") not in StyleLimitList and "CornerI" not in k.split("_")[3]]
                    TmpCornerIList = [AssetData.get(k).get("id") for k, v in AssetData.items() if v.get("style") not in StyleLimitList and "CornerI" in k.split("_")[3]]
                    #Change to Other Type
                    if CornerType < 4:
                        cornertype = RandFromList(seed, TmpCornerList)
                    else:
                        cornertype = RandFromList(seed, TmpCornerIList)
                else:
                    StyleLimit[assetStyle]["CornerLimit"] = StyleLimit.get(assetStyle).get("CornerLimit") - 1
                    if(StyleLimit.get(assetStyle).get("CornerLimit")==0):
                        #pop
                        StyleLimit.pop(assetStyle)
                        #update assetlist
                        CornerList = [id for id in CornerList if id not in [v["id"] for k, v in AssetData.items() if v["style"] == assetStyle]]
                        CornerIList

            pass

        # Corner Mark
        pt.setAttribValue("Cd", Cd.rgb())
        pt.setAttribValue("N", list(N))
        pt.setAttribValue("cornertype", int(cornertype))
        target_size = [v["UnitSize"] for k, v in AssetData.items() if v["id"] == cornertype][0]
        pt.setAttribValue("cornerWidth", target_size)
        cornerGroup = geo.findPointGroup("CornerPoint")
        cornerGroup.add(pt)
        # print(target_size)
        CornerRecordList[str(index)] = {"assetname": assetname, "pos": current_pos, "npos": next_pos, "lpos": last_pos}

    DoorRestCount = DoorCount - C_DoorCount
    WindowRestCount = 0
    #StyleLimit
    StyleLimit = CurrentRules.get("StyleLimit")
    LimitData = {"DoorRestCount": DoorRestCount , "StyleLimit":StyleLimit}



    for pt in pts:
        index = pts.index(pt)
        nextindex = index + 1 if index != (len_count - 1) else 0
        StartPos = CornerRecordList[str(index)]["pos"]
        NextPos = CornerRecordList[str(index)]["npos"]
        StartAsset = CornerRecordList[str(index)]["assetname"]
        NextAsset = CornerRecordList[str(nextindex)]["assetname"]
        LimitData = CalEdge(StartPos, StartAsset, NextPos, NextAsset, index, LimitData,last_distance)

def CalEdge(StartPos, StartAsset, NextPos, NextAsset, index, LimitData,last_distance):
    logging.log(logging.INFO, f"NewStart------------init variable---------------------------------------------{index}")
    DoorRestCount = LimitData.get("DoorRestCount")
    Edge_distance = StartPos.distanceTo(NextPos)
    Stylelimit = LimitData.get("StyleLimit")
    ContinueStyleLimit = [style for style,styleRule in Stylelimit.items() if styleRule.get("Continuous")]

    #downVector
    down = hou.Vector3(0, -15, 0)

    # StartAsset
    CurrentType = StartAsset.split("_")[1]
    CurrentSocket = StartAsset.split("_")[2]
    if "to" in CurrentSocket:
        # convert section
        CurrentSocket = CurrentSocket.split("to")[-1]
    CurrentSize = int(StartAsset.split("_")[-1][0])

    # TargetAsset
    NextType = NextAsset.split("_")[1]
    NextSocket = NextAsset.split("_")[2]
    if "to" in NextSocket:
        # convert section
        NextSocket = NextSocket.split("to")[0]
    NextSize = int(NextAsset.split("_")[-1][0])

    # Dir,Size,StartPos
    CurrentDir = (NextPos - StartPos).normalized()
    RestDist = Edge_distance - CurrentSize - NextSize
    RestDist = int(RestDist)
    init_Dist = RestDist
    StartPos = StartPos + CurrentDir * CurrentSize
    must_Convert = 0
    LimitKeyList = []
    if DoorRestCount == 0:
        LimitKeyList.append("Door")
    for Style,LimitStyleRule in Stylelimit.items():
        LimitDist = LimitStyleRule.get("Depth_limit")
        if last_distance < LimitDist:
            LimitKeyList.append(Style)

    logging.log(logging.INFO, f"Init Data List")
    logging.log(logging.INFO, f"LimitKeyList:{LimitKeyList}")
    SectionAssetlist = updateSocketList(CurrentSocket, LimitKeyList, RestDist)
    ConvertAssetlist = []
    if CurrentSocket != NextSocket:
        logging.log(logging.INFO, f"Convert Section from {CurrentSocket} to {NextSocket}")
        ConvertKey = f"{CurrentSocket}to{NextSocket}"
        ConvertAssetlist = updateSocketList(ConvertKey, LimitKeyList, RestDist, ConvertKey)
        must_Convert = 1
    loopCount = 1

    RecordSocket = CurrentSocket
    pointcreated = 0
    while RestDist > 0:
        if DoorRestCount == 0:
            LimitKeyList.append("Door")
        halfList = []
        # Refresh SocketAsset List
        if (CurrentSocket not in ContinueStyleLimit and NextSocket not in ContinueStyleLimit):
            LimitKeyList += ContinueStyleLimit
        SectionAssetlist = updateSocketList(CurrentSocket, LimitKeyList, RestDist)
        if CurrentSocket != NextSocket:

            logging.log(logging.INFO, f"Convert Section from {CurrentSocket} to {NextSocket}")
            ConvertKey = f"{CurrentSocket}to{NextSocket}"
            ConvertAssetlist = updateSocketList(CurrentSocket, LimitKeyList, RestDist, ConvertKey)
            must_Convert = 1
        else:
            must_Convert = 0

        hitVector = hou.Vector3(0, 0, 0)
        SurfVector = hou.Vector3(0, 0, 0)
        uvw = hou.Vector3(0, 0, 0)
        hitResult = LowerFloorGeo.intersect(StartPos, down, hitVector, SurfVector, uvw)
        print(hitResult)
        if hitResult<0:
            logging.log(logging.INFO, f"***********************************Door Hit Nothing")
            #no Door in list
            SectionAssetlist = [asset for asset in SectionAssetlist if "Door" not in asset]
        else:
            logging.log(logging.INFO, f"***********************************Door Hit Something")

        print(SectionAssetlist)
        if must_Convert and RestDist <= 3:
            logging.log(logging.INFO, f"Convert Section from {CurrentSocket} to {NextSocket}")
            # Half Setting
            if RestDist <= 2:
                ConvertList = [ConvertAsset for ConvertAsset in ConvertAssetlist if
                               f"{CurrentSocket}to{NextSocket}" in ConvertAsset]
                # print(ConvertList, ConvertAssetlist)
                if ConvertList:
                    CurrentAsset = ConvertList[0]
                    CurrentSocket = NextSocket
            else:
                currentSeed = loopCount + index + pointcreated + RestDist

                SectionAsset_NOConnectionlist = [asset for asset in SectionAssetlist if
                                                 asset.split("_")[3] not in ["Left", "Right", "Center"]]

                CurrentAsset = RandFromList(currentSeed, SectionAsset_NOConnectionlist)
        else:
            #0 or 1
            HalfMark = np.random.randint(0, 2)
            logging.log(logging.INFO, f"Rand Select: {HalfMark}")
            if HalfMark>0:
                print(f"RestDist:{RestDist}xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                halfList = halfSetting(SectionAssetlist, RestDist, LimitKeyList, must_Convert)

            SectionAsset_NOConnectionlist = [asset for asset in SectionAssetlist if asset.split("_")[3] not in ["Left", "Right", "Center"]]

            currentSeed = loopCount + index + pointcreated + RestDist
            # print(SectionAsset_NOConnectionlist,SectionAssetlist)
            CurrentAsset = RandFromList(currentSeed, SectionAsset_NOConnectionlist)

            if RestDist==1 and CurrentSocket==NextSocket:
                SectionAsset_NOCClist = [asset for asset in SectionAssetlist if
                                                 asset.split("_")[3] not in ["Left", "Right", "Center"] and asset.split("_")[2] == NextSocket]
                # Last Section
                CurrentAsset = RandFromList(currentSeed, SectionAsset_NOCClist)

        # print(halfList)
        if halfList:
            for asset in halfList:
                # print(asset)
                StartPos, OffsetSize = CreatePoint(asset, StartPos, CurrentDir)
                pointcreated += 1
                RestDist -= OffsetSize
                loopCount += 1
        else:
            # print(f"DoorRestCount:{DoorRestCount}")
            # Update Socket if Convert
            if "to" in CurrentAsset:
                # convert section
                CurrentSocket = CurrentAsset.split("_")[2]
                CurrentSocket = CurrentSocket.split("to")[-1]

            if "Door" in CurrentAsset:
                DoorRestCount -= 1
            # print(f"CurrentAsset:{CurrentAsset}")
            StartPos, OffsetSize = CreatePoint(CurrentAsset, StartPos, CurrentDir)
            pointcreated += 1
            RestDist -= OffsetSize
            loopCount += 1

    LimitData["DoorRestCount"] = DoorRestCount
    return LimitData

def CreatePoint(AssetName, Pos, Dir):
    Socket = AssetName.split("_")[2]
    Size = int(AssetName.split("_")[-1][0])

    up_vector = hou.Vector3(0, 1, 0)
    N_vector = Dir.cross(up_vector)

    # search Asset id
    for prim in SectionAssets:
        if prim.attribValue("name") == AssetName:
            AssetId = prim.attribValue("SectionType")
            break

    Newpos = Pos + Dir * Size * 0.5
    point = geo.createPoint()
    point.setPosition(Newpos)
    point.setAttribValue("AssetName", AssetName)
    point.setAttribValue("SectionType", AssetId)
    point.setAttribValue("N", list(N_vector))
    SectionGroup = geo.findPointGroup("SectionPoint")
    SectionGroup.add(point)
    return Newpos + Dir * Size * 0.5, Size

def updateSocketList(Socket, keywords, sizeLimit, ConvertKey=""):
    """
    Filter the list by Socket Mark
    """
    sizeLimit = int(sizeLimit)
    newArray = []
    assetname = ""

    for prim in SectionAssets:
        assetname = prim.attribValue("name")
        Pos = prim.attribValue("Pos")
        Style = prim.attribValue("Style")
        Type = prim.attribValue("Type")
        UnitSize = prim.attribValue("UnitSize")
        if Socket == Style and sizeLimit >= UnitSize:
            if "to" in assetname.split("_")[2]:
                SocketA = assetname.split("_")[2].split("to")[0]
                SocketB = assetname.split("_")[2].split("to")[-1]
                if SocketA in keywords or SocketB in keywords:
                    continue
            # size and style match
            if not keywords or (Type not in keywords and Pos not in keywords and Style not in keywords):
                # pos and type not in forbidden list
                newArray.append(assetname)

    if ConvertKey:
        logging.log(logging.INFO, f"Convert Section from {Socket} to {ConvertKey}")
        newArray = [asset for asset in newArray if asset.split("_")[2] == ConvertKey]

    return newArray

def halfSetting(SectionAssetlist, RestDist, LimitKeyList, must_Convert):
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
    Continuous_Limit = CurrentRules.get("AssetType").get("Window").get("Combine").get("Continuous")
    print(f"RestDist Before:{RestDist}--------------------------------------------------")
    if Continuous_Limit:
        if RestDist > Continuous_Limit:
            RestDist = Continuous_Limit
    print(f"RestDist:{RestDist}--------------------------------------------------")
    if not SectionAssetlist:
        return []
    # Rand Select Length from 2-6
    if RestDist==2:
        LengthSelection = 2
    else:
        LengthSelection = np.random.randint(2, RestDist)
    LeftList = [Section for Section in SectionAssetlist if "Left" in Section]
    RightList = [Section for Section in SectionAssetlist if "Right" in Section]
    CenterList = [Section for Section in SectionAssetlist if "Center" in Section]

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

#run function
CalPoints(CurrentRules=CurrentRules)