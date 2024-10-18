# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import json
import os
import random
from random import sample
import numpy as np
import hou
import logging
import copy

debug = False
# init log level
logging.basicConfig(level=logging.INFO)

node = hou.pwd()
geo = node.geometry()

#config file path
rulePath = node.parm("ConfigFile").eval()

# add point attrib
geo.addAttrib(hou.attribType.Point, "cornertype", -1)
geo.addAttrib(hou.attribType.Point, "cornerWidth", 0)
geo.addAttrib(hou.attribType.Point, "AssetName", "")
geo.addAttrib(hou.attribType.Point, "SectionType", -1)
# create point group
geo.createPointGroup("CornerPoint")
geo.createPointGroup("SectionPoint")

#get global attr
#Alert is attr to mark unclosed roof line
if geo.findPointAttrib("Alert"):
    Alert = geo.attribValue("Alert")
else:
    Alert = 0

# Read Rule Config or read from detail attr
with open(rulePath, "r") as datafile:
    datastring = datafile.read()
    datapack = json.loads(datastring)

currentprim = geo.prims()[0]
currentFloor = currentprim.attribValue("floor")
currentFloor += 1
currentSections = list(geo.attribValue("SectionList"))
currentArea = currentprim.attribValue("area")

# get current rules if not exist use default rules
CurrentRules = datapack.get("Level").get(str(currentFloor))
if not CurrentRules:
    CurrentRules = datapack.get("Level").get("Default")

CurrentTypes = CurrentRules.get("Types")

#Geo info
LowerFloorGeo = node.inputs()[3].geometry()
BreakPoint_Path = node.evalParm("spare_input0")
if hou.node(BreakPoint_Path):
    BreakPointGeo = hou.node(BreakPoint_Path).geometry()
else:
    BreakPointGeo = None

# Corner Data Function
def CornerAssetData(currentSections=None, pt_SR=""):
    """
        Corner Assets For Current Floor and Current Style
    """
    if currentSections is None:
        currentSections = []
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
        if CornerAsset_Style not in currentSections or (pt_SR and pt_SR not in CornerAsset_Pos):
            #pop id from list if the asset does not match the current section
            if id in CornerSortList["Corner"]:
                CornerSortList["Corner"].remove(id)
            if id in CornerSortList["CornerI"]:
                CornerSortList["CornerI"].remove(id)
            continue
        AssetData[CornerAsset_name] = {"Pos": CornerAsset_Pos, "id": id, "style": CornerAsset_Style,
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
    else:
        #flatten Alert Not corner
        Cd = hou.Color(1,1,1)
        N = NextDir
        CornerType = -1
    return Cd, CornerType, N

def RandFromList(seed, ResourceList):
    if not ResourceList:
        return None
    random.seed(seed)
    return ResourceList[int(random.random() * len(ResourceList))]

def CalPoints(CurrentRules):
    """
    :param CurrentRules: Rule Dict Data
    Cal Corner Type First and Record data according to the rules
    Cal Section Type Second
    :return:
    """
    global hitResult, last_distance, section_seed,Door_SameSide,Door_EdgeLimit
    CornerRecordList = {}
    pts = currentprim.points()
    if not Alert:
        pts.pop()#remove last vertex
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

    if debug: print(f"currentSections {currentSections}")
    # get Corner data list BaseData
    OrgAssetData, CornerSortList = CornerAssetData(currentSections)
    OrgCornerList = CornerSortList["Corner"]
    OrgCornerIList = CornerSortList["CornerI"]
    StyleLimit = {}

    #Create Corner Style Limit Dict
    if CurrentRules.get("StyleLimit"):
        StyleLimit = copy.deepcopy(CurrentRules.get("StyleLimit"))

    Stylelist = []
    for pt in pts:
        #get seed
        seed = pt.attribValue("seed")
        section_seed = pt.attribValue("section_seed")

        #Check if it has SR need,init value first
        pt_SR = None
        if not geo.findPointAttrib("SR"):
            #use same data
            AssetData = OrgAssetData
            CornerList = OrgCornerList
            CornerIList = OrgCornerIList
            pass
        else:
            #use SR data filter
            pt_SR = pt.attribValue("SR")
            AssetData, CornerSortList = CornerAssetData(currentSections,pt_SR)
            CornerList = CornerSortList["Corner"]
            CornerIList = CornerSortList["CornerI"]

        #current point number(used to be list index)
        index = pt.number()
        lastindex = index - 1
        nextindex = index + 1 if index != (len_count - 1) else 0
        current_pos = pt.position()

        last_targetPoint = pts[lastindex]
        last_pos = last_targetPoint.position()
        next_targetPoint = pts[nextindex]
        next_pos = next_targetPoint.position()

        last_distance = current_pos.distanceTo(last_pos)
        next_distance = current_pos.distanceTo(next_pos)

        #if to close to the other point ,it might use the same type but in unit size
        minDistance = min(last_distance, next_distance)

        NextDir = (next_pos - current_pos).normalized()
        LastDir = (current_pos - last_pos).normalized()

        # for roof part
        if index==0 and Alert:
            LastDir = NextDir
        elif index == (len_count - 1) and Alert:
            NextDir = LastDir

        #update Corner Type
        Cd, CornerType, N = NormalCal(LastDir, NextDir)

        # Door Limit
        DoorAssetList = [v["id"] for k, v in AssetData.items() if k.split("_")[1] == "Door"]
        NoDoorCornerList = [id for id in CornerList if id not in DoorAssetList]
        NoDoorCornerIList = [id for id in CornerIList if id not in DoorAssetList]
        UnitNoDoorCornerList = [v["id"] for k, v in AssetData.items() if v["id"] in NoDoorCornerList and v["UnitSize"]==1]
        UnitNoDoorCornerIList = [v["id"] for k, v in AssetData.items() if v["id"] in NoDoorCornerIList and v["UnitSize"]==1]

        if (minDistance==last_distance or nextindex==0) and index!=0:
            #use same type
            if debug:  print(CornerRecordList)
            searchIndex = lastindex if minDistance==last_distance else 0
            if CornerRecordList.get(str(searchIndex)) and CornerRecordList.get(str(searchIndex)).get("assetname"):
                lastStyle = CornerRecordList[str(searchIndex)]["assetname"].split("_")[2]
                UnitNoDoorCornerList = [v["id"] for k, v in AssetData.items() if
                                        v["id"] in NoDoorCornerList and v["UnitSize"] == 1 and v["style"]==lastStyle]
                UnitNoDoorCornerIList = [v["id"] for k, v in AssetData.items() if
                                         v["id"] in NoDoorCornerIList and v["UnitSize"] == 1 and v["style"]==lastStyle]



        #Corner Type Filter
        if CornerType < 4:
            if C_DoorCount == DoorCount or minDistance < Door_DistLimit:
                cornertype = RandFromList(seed, NoDoorCornerList)
            else:
                cornertype = RandFromList(seed, CornerList)
        else:
            if C_DoorCount == DoorCount or minDistance < Door_DistLimit:
                cornertype = RandFromList(seed, NoDoorCornerIList)
            else:
                cornertype = RandFromList(seed, CornerIList)

        if debug: print(f"AssetData {AssetData}")
        assetname = [k for k, v in AssetData.items() if v["id"] == cornertype][0]
        assetsize = [v["UnitSize"] for k, v in AssetData.items() if v["id"] == cornertype][0]
        assettype = assetname.split("_")[1]
        assetStyle = assetname.split("_")[2]

        #Refresh Size Filter
        if assetsize >= minDistance:
            seed+=1
            if CornerType < 4:
                cornertype = RandFromList(seed, UnitNoDoorCornerList)
            else:
                cornertype = RandFromList(seed, UnitNoDoorCornerIList)

        # Door Limit
        if C_DoorCount < DoorCount and assettype == "Door":
            passValue = True
            # same side filter
            if ((lastindex in DooridList) or (nextindex in DooridList)) and Door_SameSide:
                passValue = False
            else:
                # dist filter
                for otherDoorPos in DoorPosList:
                    dist = otherDoorPos.distanceTo(current_pos)
                    if dist < 5:
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
        else:
            #Style Limit
            StyleLimitList = [k for k, v in StyleLimit.items()]
            if assetStyle in StyleLimitList:
                Vertical = StyleLimit.get(assetStyle).get("Vertical")
                Depth_limit = StyleLimit.get(assetStyle).get("Depth_limit")
                if Vertical:
                    #intersection test
                    sample_pos = current_pos + hou.Vector3(0, -4, 0)
                    # print(f"sample_pos {sample_pos}")
                    hitResult = LowerFloorGeo.nearestPoint(sample_pos,max_radius=1)

                ChangeType = False
                if (Vertical and not hitResult) or minDistance<Depth_limit:
                    #change Style
                    TmpCornerList = [AssetData.get(k).get("id") for k, v in AssetData.items() if
                                     v.get("style") not in StyleLimitList and "CornerI" not in k.split("_")[3]]
                    TmpCornerIList = [AssetData.get(k).get("id") for k, v in AssetData.items() if
                                      v.get("style") not in StyleLimitList and "CornerI" in k.split("_")[3]]
                    ChangeType = True
                elif StyleLimit[assetStyle]["CornerLimit"]==0:
                    TmpCornerList = [AssetData.get(k).get("id") for k, v in AssetData.items() if v.get("style") not in StyleLimitList and "CornerI" not in k.split("_")[3]]
                    TmpCornerIList = [AssetData.get(k).get("id") for k, v in AssetData.items() if v.get("style") not in StyleLimitList and "CornerI" in k.split("_")[3]]
                    ChangeType = True

                if ChangeType:
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

        #After Filter
        assetname = [k for k, v in AssetData.items() if v["id"] == cornertype][0]
        assettype = assetname.split("_")[1]

        Stylelist.append(assetname.split("_")[2])

        # Corner Mark
        pt.setAttribValue("Cd", Cd.rgb())
        pt.setAttribValue("N", list(N))
        pt.setAttribValue("cornertype", int(cornertype))
        pt.setAttribValue("AssetName", str(assetname))
        target_size = [v["UnitSize"] for k, v in AssetData.items() if v["id"] == cornertype][0]
        pt.setAttribValue("cornerWidth", target_size)
        if CornerType == -1:
            pt.setAttribValue("cornertype", -1)
            pt.setAttribValue("AssetName", "")
            pt.setAttribValue("cornerWidth", 0)
            assetname = ""
        else:
            cornerGroup = geo.findPointGroup("CornerPoint")
            cornerGroup.add(pt)
        CornerRecordList[str(index)] = {"assetname": assetname, "pos": current_pos, "npos": next_pos, "lpos": last_pos}

    DoorRestCount = DoorCount - C_DoorCount
    WindowRestCount = 0
    # StyleLimit
    StyleLimit = CurrentRules.get("StyleLimit")
    LimitData = {"DoorRestCount": DoorRestCount , "StyleLimit":StyleLimit}
    #logging.log(logging.INFO,f"DoorRestCount:{DoorRestCount}")
    for pt in pts:
        index = pt.number()
        nextindex = index + 1 if index != (len_count - 1) else 0
        #unclosed roof line
        if Alert and nextindex==0:
            return
        StartPos = CornerRecordList[str(index)]["pos"]
        NextPos = CornerRecordList[str(index)]["npos"]
        StartAsset = CornerRecordList[str(index)]["assetname"]
        NextAsset = CornerRecordList[str(nextindex)]["assetname"]
        #Cal per Edge
        LimitData,DoorPosList = CalEdge(StartPos, StartAsset, NextPos, NextAsset, index, LimitData,last_distance,DoorPosList,section_seed)

def CalEdge(StartPos, StartAsset, NextPos, NextAsset, index, LimitData,last_distance,DoorPosList,section_seed=0):
    # logging.log(logging.INFO, f"NewStart------------init variable---------------------------------------------{index}")
    global CurrentAsset, ConvertAssetlist,CurrentType
    DoorPosList = DoorPosList
    DoorMark = 0
    DoorRestCount = LimitData.get("DoorRestCount")
    Edge_distance = StartPos.distanceTo(NextPos)
    Stylelimit = LimitData.get("StyleLimit")
    ContinueStyleLimit = [style for style,styleRule in Stylelimit.items() if styleRule.get("Continuous")]
    Continuous_Count = [styleRule.get("Continuous_Count") for style, styleRule in Stylelimit.items() if styleRule.get("Continuous_Count")]
    Continuous_Switch = False

    #downVector
    down = hou.Vector3(0, -20, 0)

    if StartAsset:
        # StartAsset
        CurrentType = StartAsset.split("_")[1]
        CurrentSocket = StartAsset.split("_")[2]
        if "to" in CurrentSocket:
            # convert section
            CurrentSocket = CurrentSocket.split("to")[-1]
        CurrentSize = int(StartAsset.split("_")[-1][0])
    else:
        CurrentType = NextAsset.split("_")[1]
        CurrentSocket = NextAsset.split("_")[2]
        CurrentSize = -1

    if NextAsset:
        # TargetAsset
        NextType = NextAsset.split("_")[1]
        NextSocket = NextAsset.split("_")[2]
        if "to" in NextSocket:
            # convert section
            NextSocket = NextSocket.split("to")[0]
        NextSize = int(NextAsset.split("_")[-1][0])
    else:
        NextType = StartAsset.split("_")[1]
        NextSocket = StartAsset.split("_")[2]
        NextSize = -1

    # Dir,Size,StartPos
    CurrentDir = (NextPos - StartPos).normalized()
    RestDist = Edge_distance - CurrentSize - NextSize
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

    loopCount = 1
    RecordSocket = CurrentSocket
    pointcreated = 0
    while RestDist > 0:
        LimitKeyList = []
        if DoorRestCount == 0:
            LimitKeyList.append("Door")
        halfList = []

        # Refresh SocketAsset List
        if (CurrentSocket not in ContinueStyleLimit and NextSocket not in ContinueStyleLimit):
            # logging.log(logging.INFO, f"Not use ContinueStyleLimit")
            LimitKeyList += ContinueStyleLimit
        if (CurrentSocket in ContinueStyleLimit and NextSocket in ContinueStyleLimit) or CurrentSocket in ContinueStyleLimit:
            # if Start Socket as same as the End Socket, then the current Style must be the same one
            # print(f"ContinueStyleLimit List:{ContinueStyleLimit}")
            # logging.log(logging.INFO, f"Continuous_Count:{Continuous_Count}")
            if RestDist>=Continuous_Count[0]:
                #enough dist for limit count
                Continuous_Switch = True
                LimitKeyList = [style for style in CurrentTypes if style not in ContinueStyleLimit]

        SectionAssetlist = updateSocketList(CurrentSocket, LimitKeyList, RestDist)
        #Door and No Door
        DoorAssetlist = [asset for asset in SectionAssetlist if "Door" in asset]
        SectionAssetlist = [asset for asset in SectionAssetlist if "Door" not in asset]

        if CurrentSocket != NextSocket:
            # logging.log(logging.INFO, f"In Loop Convert Section from {CurrentSocket} to {NextSocket}")
            ConvertKey = f"{CurrentSocket}to{NextSocket}"
            ConvertAssetlist = updateSocketList(CurrentSocket, LimitKeyList, RestDist, ConvertKey=ConvertKey)
            # print(LimitKeyList,RestDist)
            must_Convert = 1
        else:
            must_Convert = 0

        hitVector = hou.Vector3(0, 0, 0)
        SurfVector = hou.Vector3(0, 0, 0)
        uvw = hou.Vector3(0, 0, 0)
        hitResult = LowerFloorGeo.intersect(StartPos, down, hitVector, SurfVector, uvw)
        # print(hitResult)
        if (hitResult>=0 and currentFloor>1) or currentFloor<=1:
            #logging.log(logging.INFO, f"***********************************May Have Door")
            if DoorRestCount>0:
                DoorMark = 1
            else:
                DoorMark = 0
        if must_Convert and RestDist <= 3:
            # logging.log(logging.INFO, f"Must Convert Convert Section from {CurrentSocket} to {NextSocket}")
            # Half Setting
            if RestDist <= 2:
                ConvertList = [ConvertAsset for ConvertAsset in ConvertAssetlist if
                               f"{CurrentSocket}to{NextSocket}" in ConvertAsset]
                # logging.log(logging.INFO, f"ConvertAssetlist:{ConvertAssetlist}")
                if ConvertList:
                    CurrentAsset = ConvertList[0]
                    CurrentSocket = NextSocket
            else:
                currentSeed = loopCount + index + pointcreated +currentFloor

                SectionAsset_NOConnectionlist = [asset for asset in SectionAssetlist if
                                                 asset.split("_")[3] not in ["Left", "Right", "Center"]]

                CurrentAsset = RandFromList(currentSeed, SectionAsset_NOConnectionlist)
        else:
            #0 or 1
            HalfMark = np.random.randint(0, 2)
            #logging.log(logging.INFO, f"Rand Select: {HalfMark} \nRestDist:{RestDist}xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            if HalfMark>0 and RestDist>=2 and not CurrentSocket in ["R1","R2","R3","R4"]:
                halfList = halfSetting(SectionAssetlist, RestDist, LimitKeyList, must_Convert)

            #Set Door
            if DoorMark:
                #current position
                DoorPos = StartPos
                #dist compare from list
                if DoorPosList:
                    for otherDoorPos in DoorPosList:
                        dist = otherDoorPos.distanceTo(DoorPos)
                        if dist < 5:
                            DoorMark = 0
                            break

            SectionAsset_NOConnectionlist = [asset for asset in SectionAssetlist if asset.split("_")[3] not in ["Left", "Right", "Center"]]
            currentSeed = loopCount + index + pointcreated + currentFloor + section_seed

            #use Door or Not
            DoorUse = np.random.randint(0, 2)
            #print(f"DoorUse:{DoorUse},   DoorMark:{DoorMark},   DoorAssetlist:{DoorAssetlist}")
            if DoorUse>0 and DoorMark>0:
                CurrentAsset = RandFromList(currentSeed, DoorAssetlist)
            else:
                CurrentAsset = RandFromList(currentSeed, SectionAsset_NOConnectionlist)

            if not CurrentAsset:
                CurrentAsset = RandFromList(currentSeed, SectionAsset_NOConnectionlist)

            if RestDist==1 and CurrentSocket==NextSocket:
                SectionAsset_NOCClist = [asset for asset in SectionAssetlist if
                                                 asset.split("_")[3] not in ["Left", "Right", "Center"] and asset.split("_")[2] == NextSocket]
                # Last Section
                CurrentAsset = RandFromList(currentSeed, SectionAsset_NOCClist)

        if debug:print(CurrentAsset)
        # print(halfList)
        if halfList:
            for asset in halfList:
                # print(asset)
                StartPos, OffsetSize = CreatePoint(asset, StartPos, CurrentDir)
                pointcreated += 1
                RestDist -= OffsetSize
                loopCount += 1
        else:
            # print(f"CurrentAsset:{CurrentAsset}")
            # Update Socket if Convert
            if "to" in CurrentAsset:
                # convert section
                CurrentSocket = CurrentAsset.split("_")[2]
                CurrentSocket = CurrentSocket.split("to")[-1]

            if "Door" in CurrentAsset:
                DoorRestCount -= 1
                DoorPosList.append(StartPos+CurrentDir*CurrentSize)
            # print(f"CurrentAsset:{CurrentAsset}")
            StartPos, OffsetSize = CreatePoint(CurrentAsset, StartPos, CurrentDir)
            pointcreated += 1
            RestDist -= OffsetSize
            loopCount += 1

    LimitData["DoorRestCount"] = DoorRestCount
    return LimitData,DoorPosList

def CreatePoint(AssetName, Pos, Dir):
    global AssetId
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
    ConvertArray = []
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
                if assetname.split("_")[2] == ConvertKey:
                    ConvertArray.append(assetname)
                if SocketA in keywords or SocketB in keywords:
                    continue

            # size and style match
            if not keywords or (Type not in keywords and Pos not in keywords and Style not in keywords):
                # pos and type not in forbidden list
                newArray.append(assetname)

    if ConvertKey:
        #logging.log(logging.INFO, f"Update Socket List Convert Section from {Socket} to {ConvertKey}")
        return ConvertArray

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
    if not CurrentRules.get("AssetType").get("Window"):
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

#run function
CalPoints(CurrentRules=CurrentRules)