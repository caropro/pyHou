# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import numpy as np
import hou
import logging
import copy
from pcgRuleprocessor.pcgFunctions import *
import json,os
from random import sample

#set static seed ensure the same result
np.random.seed(0)

debug = False
# init log level
logging.basicConfig(level=logging.INFO)

node = hou.pwd()
geo = node.geometry()

#config file path
rulePath = node.parm("ConfigFile").eval()

# add point attrib
if not geo.findPointAttrib("cornertype"):
    geo.addAttrib(hou.attribType.Point, "cornertype", -1)
if not geo.findPointAttrib("CornerType"):
    geo.addAttrib(hou.attribType.Point, "CornerType", -1)
geo.addAttrib(hou.attribType.Point, "cornerWidth", 0)
geo.addAttrib(hou.attribType.Point, "AssetName", "")
geo.addAttrib(hou.attribType.Point, "SectionType", -1)

# create point group
geo.createPointGroup("CornerPoint")
geo.createPointGroup("SectionPoint")

#create global attr
geo.addAttrib(hou.attribType.Global, "OneSide", [""])

#get global attr
# Alert is attr to mark unclosed roof line
if geo.findGlobalAttrib("Alert"):
    Alert = geo.attribValue("Alert")
else:
    Alert = 0

# Read Rule Config or read from detail attr
with open(rulePath, "r") as datafile:
    datastring = datafile.read()
    datapack = json.loads(datastring)

#get rule data for current floor
currentprim = geo.prims()[0]
currentFloor = currentprim.attribValue("floor")+1
currentSections = list(geo.attribValue("SectionList"))
currentArea = currentprim.attribValue("area")

# get current rules if not exist use default rules
CurrentRules = datapack.get("Level").get(str(currentFloor))
if not CurrentRules:
    CurrentRules = datapack.get("Level").get("Default")

CurrentTypes = CurrentRules.get("Types")
#special rules
#global all powerful(the all powerfull style can do all the convert job)
global all_powerful
all_powerful = ""
if datapack.get("Special"):
    all_powerful = datapack.get("Special").get("all_powerful")

#Geo info
LowerFloorGeo = node.inputs()[3].geometry()
BreakPoint_Path = node.evalParm("spare_input0")
if hou.node(BreakPoint_Path):
    BreakPointGeo = hou.node(BreakPoint_Path).geometry()
else:
    BreakPointGeo = None

UpperData_Path = node.evalParm("spare_input1")
if hou.node(UpperData_Path):
    UpperGeo = hou.node(UpperData_Path).geometry()
    if UpperGeo.findGlobalAttrib("OneSide"):
        UpperOneSide = UpperGeo.attribValue("OneSide")
    else:
        UpperOneSide = []
else:
    UpperGeo = None
    UpperOneSide = []

# Corner index,pos,Dir,asset,size
CornerData = {}

# Global Section Asset
SectionAssetsNode = node.inputs()[2]
SectionAssetsGeo = SectionAssetsNode.geometry()
SectionAssets = SectionAssetsGeo.prims()

def CalPoints(CurrentRules):
    """
    :param CurrentRules: Rule Dict Data
    Cal Corner Type First and Record data according to the rules
    Cal Section Type Second
    :return:
    """
    global hitResult,Overlap, last_distance, section_seed,Door_SameSide,Door_EdgeLimit, TmpCornerIList, TmpCornerList
    Overlap = False
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
        Door_EdgeLimit = DoorRule.get("Edge_Length")
        Door_SameSide = DoorRule.get("Same Side")

    DoorPosList = []
    DooridList = []

    last_distance_list = []

    # get Corner data list BaseData
    OrgAssetData, CornerSortList = CornerAssetData(currentSections)
    OrgCornerList = CornerSortList["Corner"]
    OrgCornerIList = CornerSortList["CornerI"]
    StyleLimit = {}
    CornerLimit = []


    CurrentLevelGrammar = CurrentRules.get("Grammar",{})
    #Create Corner Style Limit Dict
    if CurrentRules.get("StyleLimit"):
        StyleLimit = copy.deepcopy(CurrentRules.get("StyleLimit"))
        CornerLimit = CurrentRules.get("Grammar",{}).get("Corner",{}).get("NCT",[])


    #Init Grammar Data
    SectionGrammar_dict = CurrentLevelGrammar.get("Section",{})
    CornerGrammarSet_dict = CurrentLevelGrammar.get("Corner",{}).get("GrammarCornerSet",{})
    CornerGrammarAssetList = []
    CornerGrammarMark = False
    CornerGrammarUnitSize = False
    # Get Corner Grammar if exist change current pts(AssetName,cornerWidth)
    if len(CornerGrammarSet_dict) > 0:
        # rand select one corner grammar
        CornerGrammarSet_list = list(CornerGrammarSet_dict.keys())
        CornerGrammar = random.choice(CornerGrammarSet_list)
        CornerTypeList = CornerGrammarSet_dict.get(CornerGrammar, {}).get("StyleList", [])
        if CornerTypeList:
            CornerGrammarMark = True
            CornerGrammarUnitSize = CornerGrammarSet_dict.get(CornerGrammar, {}).get("useUnitSize", False)

    Stylelist = []
    edgeCount = 0
    CornerLimitMark = False
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

        if CornerGrammarMark:
            #ReFilter the Asset Data Ensure split the asset name and get the style can be found
        # in CornerTypeList
            print(f"CornerGrammarUnitSize:{CornerGrammarUnitSize}")
            if CornerGrammarUnitSize:
                AssetData = {k: v for k, v in AssetData.items() if v["style"] in CornerTypeList and v["UnitSize"]==1}
            else:
                AssetData = {k: v for k, v in AssetData.items() if v["style"] in CornerTypeList}
            CornerList = [v["id"] for k, v in AssetData.items() if "CornerI" not in k.split("_")[3]]
            CornerIList = [v["id"] for k, v in AssetData.items() if "CornerI" in k.split("_")[3]]

        print(f"AssetData---------{AssetData}")
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
        last_distance_list.append(last_distance)
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
            searchIndex = lastindex if minDistance==last_distance else 0
            if CornerRecordList.get(str(searchIndex)) and CornerRecordList.get(str(searchIndex)).get("assetname"):
                lastStyle = CornerRecordList[str(searchIndex)]["assetname"].split("_")[2]
                UnitNoDoorCornerList = [v["id"] for k, v in AssetData.items() if
                                        v["id"] in NoDoorCornerList and v["UnitSize"] == 1 and v["style"]==lastStyle]
                UnitNoDoorCornerIList = [v["id"] for k, v in AssetData.items() if
                                         v["id"] in NoDoorCornerIList and v["UnitSize"] == 1 and v["style"]==lastStyle]

        #Corner Type Filter
        if CornerType < 4 and CornerType>=0:
            if C_DoorCount == DoorCount or minDistance < Door_DistLimit:
                cornertype = RandFromList(seed, NoDoorCornerList)
            else:
                cornertype = RandFromList(seed, CornerList)
        else:
            if C_DoorCount == DoorCount or minDistance < Door_DistLimit:
                cornertype = RandFromList(seed, NoDoorCornerIList)
            else:
                cornertype = RandFromList(seed, CornerIList)

        if Alert and pt.attribValue("cornertype") >= 0 and (index==0 or index==(len_count-1)):
            cornertype = pt.attribValue("cornertype")
            N = pt.attribValue("N")
            CornerType = pt.attribValue("CornerType")


        assetname = [k for k, v in AssetData.items() if v["id"] == cornertype][0]
        assetsize = [v["UnitSize"] for k, v in AssetData.items() if v["id"] == cornertype][0]
        assettype = assetname.split("_")[1]
        assetStyle = assetname.split("_")[2]

        #Refresh Size Filter
        if assetsize >= minDistance:
            seed+=1
            #if the size is bigger than the distance,then use the unitsize asset
            if CornerType < 4:
                cornertype = RandFromList(seed, UnitNoDoorCornerList)
            else:
                cornertype = RandFromList(seed, UnitNoDoorCornerIList)
            assetname = [k for k, v in AssetData.items() if v["id"] == cornertype][0]
            assettype = assetname.split("_")[1]
            assetStyle = assetname.split("_")[2]

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

                Vertical = StyleLimit.get(assetStyle,{}).get("Vertical",False)
                Breakpoint = StyleLimit.get(assetStyle,{}).get("BreakPoint",False)
                Depth_limit = StyleLimit.get(assetStyle,{}).get("Depth_limit",0)
                if Vertical:
                    #intersection test
                    print(f"Vertical Test:{Vertical}")
                    sample_pos = current_pos + hou.Vector3(0, -4, 0)
                    hitResult = LowerFloorGeo.nearestPoint(sample_pos,max_radius=0.1)
                if Breakpoint:
                    #overlaping test
                    sample_pos = current_pos
                    Overlap = BreakPointGeo.nearestPoint(sample_pos,max_radius=1)
                ChangeType = False
                if (Vertical and not hitResult) or minDistance<Depth_limit or Overlap:
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
                elif CornerLimitMark and assetStyle in CornerLimit:
                    TmpCornerList = [AssetData.get(k).get("id") for k, v in AssetData.items() if
                                     v.get("style") not in StyleLimitList and v.get("style") not in CornerLimit and "CornerI" not in k.split("_")[3]]
                    TmpCornerIList = [AssetData.get(k).get("id") for k, v in AssetData.items() if
                                      v.get("style") not in StyleLimitList and v.get("style") not in CornerLimit and"CornerI" in k.split("_")[3]]
                    CornerLimitMark = False
                    ChangeType = True

                if ChangeType:
                    #Change to Other Type
                    if CornerType < 4:
                        cornertype = RandFromList(seed, TmpCornerList)
                    else:
                        cornertype = RandFromList(seed, TmpCornerIList)
                else:
                    StyleLimit[assetStyle]["CornerLimit"] = StyleLimit.get(assetStyle).get("CornerLimit",0) - 1
                    if(StyleLimit.get(assetStyle).get("CornerLimit")==0):
                        #No need to pop the ban list
                        #update assetlist
                        #the CornerList will reset in the next loop,so maybe it also no need to be popped
                        CornerList = [id for id in CornerList if id not in [v["id"] for k, v in AssetData.items() if v["style"] == assetStyle]]
                    if assetStyle in CornerLimit:
                        CornerLimitMark = True

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
        pt.setAttribValue("CornerType",CornerType)

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
    LimitData = {"DoorRestCount": DoorRestCount , "StyleLimit":StyleLimit , "SideLimit":[]}

    for pt in pts:
        edgeCount+=1
        # if edgeCount!=6:
        #     continue
        index = pt.number()
        nextindex = index + 1 if index != (len_count - 1) else 0
        #unclosed roof line
        if Alert and nextindex==0:
            return
        StartPos = CornerRecordList[str(index)]["pos"]
        NextPos = CornerRecordList[str(index)]["npos"]
        EdgeLength = StartPos.distanceTo(NextPos)
        StartAsset = CornerRecordList[str(index)]["assetname"]
        NextAsset = CornerRecordList[str(nextindex)]["assetname"]

        StartType = StartAsset.split("_")[2]
        NextType = NextAsset.split("_")[2]



        return
        if False:
            pass
        else:
            #Cal per Edge
            LimitData,DoorPosList = CalEdge(StartPos, StartAsset, NextPos, NextAsset, index, LimitData,last_distance_list[pts.index(pt)],DoorPosList,section_seed)

def CalGrammar(GrammerSelection,StartPos,StartAsset,NextPos,NextAsset,index,EdgeLength):
    CurrentSize = int(StartAsset.split("_")[-1][0])
    NextSize = int(NextAsset.split("_")[-1][0])
    CurrentDir = (NextPos - StartPos).normalized()
    StartPos = StartPos + CurrentDir * CurrentSize
    TypeDict = {"W":"Wall","D":"Door","Ww":"Window","R":"Roof","F":"Floor","C":"Ceiling"}
    print(f"EdgeLength {EdgeLength}")
    #init variable
    RestLength = EdgeLength - CurrentSize - NextSize

    #get Grammar Data
    GrammarData = list(GrammerSelection.values())[0]
    Grammar = GrammarData.get("Grammar","")
    minLength = GrammarData.get("minLength",0)
    CornerSet = GrammarData.get("CornerSet",[])

    print(f"RestLength:{RestLength}-----------------Grammar:{Grammar}")
    GrammarAssetList = []

    PendingList = {}
    GramarSections = Grammar.split("|")

    index = 0
    #normal Setting
    for GrammarSection in GramarSections:
        # print(GrammarSection)
        #special mark append to pending list
        if "*" in GrammarSection or "^" in GrammarSection:
            PendingList[index] = GrammarSection
        else:
            AssetType = GrammarSection.split("_")[1][:-1]
            AssetStyle = GrammarSection.split("_")[0]
            AssetSize = GrammarSection.split("_")[-1]
            #set var
            AssetVar = int(GrammarSection.split("_")[1][-1])

            #first mark the type
            AssetType = TypeDict.get(AssetType,"")

            # print(f"AssetType--------------------------------{AssetType}")
            # print(f"AssetStyle-------------------------------{AssetStyle}")
            # print(f"AssetVar--------------------------------{AssetVar}")
            # print(f"AssetSize-------------------------------{AssetSize}")
            for prim in SectionAssets:
                assetname = prim.attribValue("name")
                Pos = prim.attribValue("Pos")
                Style = prim.attribValue("Style")
                Type = prim.attribValue("Type")
                UnitSize = prim.attribValue("UnitSize")
                #print(Type,Style,Pos,UnitSize)
                if AssetType == Type and AssetStyle == Style and UnitSize == int(AssetSize):
                    GrammarAssetList.append(assetname)
                    RestLength -= UnitSize
                    break

        index += 1

    print(f"GrammarAssetList:{GrammarAssetList}")
    print(f"RestLength:{RestLength}-----------------PendingList:{PendingList}")

    if RestLength and PendingList:
        pendingCount = len(PendingList)
        loop_count = 0
        count_offset = 0
        for index,section in PendingList.items():
            last = False
            loop_count += 1
            if loop_count == pendingCount:
                last = True
            index += count_offset
            AssetType = section.split("_")[1][:-1]
            #if the last char is special mark remove it
            AssetSize = section.split("_")[-1][:-1] if section.split("_")[-1][-1] in ["*","^"] else section.split("_")[-1]
            AssetStyle = section.split("_")[0]
            AssetType = TypeDict.get(AssetType, "")
            # print(f"AssetType:{AssetType}-----------------AssetStyle:{AssetStyle}")
            # print(f"RestLength:{RestLength}-----------------")
            count = 1
            for prim in SectionAssets:
                assetname = prim.attribValue("name")
                Pos = prim.attribValue("Pos")
                Style = prim.attribValue("Style")
                Type = prim.attribValue("Type")
                UnitSize = prim.attribValue("UnitSize")
                print(Type, Style, Pos, UnitSize)
                if AssetType == Type and AssetStyle == Style:
                    if "*" in section:
                        #symmetry
                        count = int(RestLength/UnitSize/2)
                        if last:
                            print("Last!!!!!!!!")
                            count = int(RestLength/UnitSize)
                    for i in range(count):
                        GrammarAssetList.insert(index,assetname)
                        RestLength -= UnitSize
                    break
            count_offset = count

    print(f"RestLength:{RestLength}-----------------GrammarAssetList:{GrammarAssetList}")

    for asset in GrammarAssetList:
        StartPos, OffsetSize = CreatePoint(asset, StartPos, CurrentDir)
    pass

def CalEdge(StartPos, StartAsset, NextPos, NextAsset, index, LimitData,last_distance,DoorPosList,section_seed=0):
    if debug:logging.log(logging.INFO, f"NewStart-----init variable---------------{index}")
    global CurrentAsset,ConvertAssetlist,CurrentType,UpperOneSide
    #downVector
    down = hou.Vector3(0, -20, 0)
    #LastSocket
    LastSocket = ""
    LastAsset = ""
    CurrentAsset = StartAsset

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

    DoorPosList = DoorPosList
    DoorMark = 0
    DoorRestCount = LimitData.get("DoorRestCount")
    Edge_distance = StartPos.distanceTo(NextPos)
    Stylelimit = LimitData.get("StyleLimit")
    #SideLimit is a list to record the side exist asset
    SideLimit = LimitData.get("SideLimit")
    ContinueStyleLimit = [style for style, styleRule in Stylelimit.items() if style==CurrentSocket and styleRule.get("Continuous")]
    Continuous_Count = [styleRule.get("Continuous_Count") for style, styleRule in Stylelimit.items() if style==CurrentSocket and styleRule.get("Continuous_Count")]
    Continuous_Switch = False

    #corner extend count
    CornerExtendCount_Start = [styleRule.get("CornerExtendCount",0) for style, styleRule in Stylelimit.items() if styleRule.get("CornerExtendCount",0) and style==CurrentSocket]
    CornerExtendCount_Next = [styleRule.get("CornerExtendCount",0) for style, styleRule in Stylelimit.items() if styleRule.get("CornerExtendCount",0) and style==NextSocket]
    CornerExtendCount_Start = CornerExtendCount_Start[0] if CornerExtendCount_Start else 0
    CornerExtendCount_Next = CornerExtendCount_Next[0] if CornerExtendCount_Next else 0

    # Dir,Size,StartPos
    CurrentDir = (NextPos - StartPos).normalized()
    RestDist = Edge_distance - CurrentSize - NextSize
    costDist = CurrentSize
    initRest = RestDist
    RestDist = int(RestDist)
    StartPos = StartPos + CurrentDir * CurrentSize
    must_Convert = 0
    initLimitKeyList = []
    if DoorRestCount == 0:
        initLimitKeyList.append("Door")

    loopCount = 1
    pointcreated = 0
    LimitKeyList = []
    while RestDist > 0 and loopCount < 100:
        # print(RestDist,"_"*15)
        #each loop refresh the limit list
        initLimitKeyList = []
        LimitKeyList = []
        for Style, LimitStyleRule in Stylelimit.items():
            LimitDist = LimitStyleRule.get("Depth_limit", 0)
            Edge_Length = LimitStyleRule.get("Edge_Length", 0)
            if initRest < LimitDist or Edge_distance < LimitDist :
                initLimitKeyList.append(Style)
            if Edge_Length > 0 and (Edge_Length > costDist or Edge_Length > RestDist):
                initLimitKeyList.append(Style)

        initLimitKeyList += list(set(SideLimit))
        LimitKeyList = list(initLimitKeyList)
        if DoorRestCount == 0:
            LimitKeyList.append("Door")
        halfList = []

        #PlatformTest
        hitVector = hou.Vector3(0, 0, 0)
        SurfVector = hou.Vector3(0, 0, 0)
        uvw = hou.Vector3(0, 0, 0)
        hitResult = LowerFloorGeo.intersect(StartPos, down, hitVector, SurfVector, uvw)
        if (hitResult>=0 and currentFloor>1) or currentFloor<=1:
            if debug:logging.log(logging.INFO, f"***********************************May Have Door")
            if DoorRestCount>0:
                DoorMark = 1
            else:
                DoorMark = 0
        #OneSide Test
        sample_pos = StartPos + hou.Vector3(0, 4, 0) + CurrentDir
        OneSideNpt = UpperGeo.nearestPoint(sample_pos, max_radius=2)
        #get attr from OneSideNpt
        OneSideStyle=""

        # print(f"OneSideNpt is {OneSideNpt}")
        if OneSideNpt and UpperGeo:
            OneSideStyle = OneSideNpt.attribValue("Style")
            OneSideSize = OneSideNpt.attribValue("UnitSize")
            # print(f"Before--------------------------------{OneSideNpt.attribValue('name')} --------------------- {OneSideNpt.attribValue('Style')}")
            #confirm check
            sample_pos = StartPos + hou.Vector3(0, 4, 0) + CurrentDir * OneSideSize
            OneSideNpt = UpperGeo.nearestPoint(sample_pos, max_radius=0.1)
            # print(f"After---------------OneSideNpt-----------------{OneSideNpt} ---------------------")
            if not OneSideNpt:
                OneSideStyle = ""
            else:
                OneSideStyle = OneSideNpt.attribValue("Style")

        if UpperOneSide and (OneSideStyle not in UpperOneSide or not OneSideStyle):
            LimitKeyList += list([UpperOneSide])
            LimitKeyList = list(set(LimitKeyList))

        #get additional sockets list from dict
        AdditionalSocket = Stylelimit.get(CurrentSocket,{}).get("AdditionalSocket",[])
        updateAdditionalSocket = Stylelimit.get(CurrentSocket,{}).get("Socketlimit",{}).get(LastSocket,[])
        #update Socket by AssetTypelimit
        if Stylelimit.get(CurrentSocket,{}).get("AssetTypelimit"):
            for asset_type,asset_limit in Stylelimit.get(CurrentSocket,{}).get("AssetTypelimit").items():
                if asset_type in LastAsset:
                    updateAdditionalSocket = asset_limit
                    break

        ExceptionList = Stylelimit.get(CurrentSocket,{}).get("Exception",[])
        #OverWrite
        if updateAdditionalSocket:
            AdditionalSocket = updateAdditionalSocket
        # print(f"AdditionalSocket:{AdditionalSocket}                LastAsset:{LastAsset}")

        # Refresh SocketAsset List
        if (CurrentSocket not in ContinueStyleLimit and NextSocket not in ContinueStyleLimit):
            if debug:logging.log(logging.INFO, f"Not use ContinueStyleLimit")
            LimitKeyList += ContinueStyleLimit

        if CurrentSocket in ContinueStyleLimit:
            # if Start Socket as same as the End Socket, then the current Style must be the same one
            if RestDist>=Continuous_Count[0]:
                #enough dist for limit count
                Continuous_Switch = True
                LimitKeyList = [style for style in CurrentTypes if style not in ContinueStyleLimit]

        SectionAssetlist = updateSocketList(CurrentSocket, LimitKeyList, RestDist, AdditionalSocket=AdditionalSocket,ExceptionList=ExceptionList)
        NextSectionAssetlist = updateSocketList(NextSocket, LimitKeyList, RestDist, AdditionalSocket=AdditionalSocket,ExceptionList=ExceptionList)

        if ExceptionList and debug:
            print(f"ExceptionList:{ExceptionList}--------SectionAssetlist:{SectionAssetlist}")
        #Door and No Door
        DoorAssetlist = [asset for asset in SectionAssetlist if "Door" in asset and int(asset.split("_")[-1][0])<=RestDist]
        SectionAssetlist = [asset for asset in SectionAssetlist if "Door" not in asset]

        if CurrentSocket != NextSocket:
            if debug:logging.log(logging.INFO, f"In Loop Convert Section from {CurrentSocket} to {NextSocket}")
            convert_key = f"{CurrentSocket}to{NextSocket}"
            ConvertAssetlist = updateSocketList(CurrentSocket, LimitKeyList, RestDist, ConvertKey=convert_key,AdditionalSocket=AdditionalSocket,ExceptionList=ExceptionList)
            must_Convert = 1
        else:
            must_Convert = 0

        #init value
        HalfMark = 0
        if CornerExtendCount_Start and RestDist>CornerExtendCount_Start:
            if debug:logging.log(logging.INFO, f"Corner Extend Section from {CurrentSocket} to {NextSocket},RestDist:{RestDist},SectionAssetlist:{SectionAssetlist}")
            # print(f"Corner Extend Section from {CurrentSocket} to {NextSocket},RestDist:{RestDist},SectionAssetlist:{SectionAssetlist}")
            halfList = CornerExtend(CurrentSocket,EndSocket=NextSocket,CornerExtendCount=CornerExtendCount_Start,SectionAssetlist=SectionAssetlist)
            #reset to 0
            CornerExtendCount_Start = 0
        elif CornerExtendCount_Next and RestDist<=CornerExtendCount_Next and initRest>CornerExtendCount_Next:
            # print(f"Corner Extend Section from {CurrentSocket} to {NextSocket},RestDist:{RestDist},SectionAssetlist:{NextSectionAssetlist}")
            #update asset with current socket type
            halfList = CornerExtend(CurrentSocket,EndSocket=NextSocket,CornerExtendCount=CornerExtendCount_Next,toMark=True,SectionAssetlist=NextSectionAssetlist)
            #reset to 0
            CornerExtendCount_Next = 0
        elif must_Convert and RestDist <= 3:
            if debug:logging.log(logging.INFO, f"Must Convert Convert Section from {CurrentSocket} to {NextSocket}")
            # Half Setting
            if RestDist <= 2:
                ConvertList = [ConvertAsset for ConvertAsset in ConvertAssetlist if
                               f"{CurrentSocket}to{NextSocket}" in ConvertAsset]
                if ConvertList:
                    CurrentAsset = ConvertList[0]
                    CurrentSocket = NextSocket
                if all_powerful:
                    if debug:logging.log(logging.INFO, f"Use All Powerful")
                    CurrentAsset = RandFromList(section_seed, ConvertAssetlist)
                    CurrentSocket = NextSocket
            else:
                currentSeed = loopCount + index + pointcreated +currentFloor

                SectionAsset_NOConnectionlist = [asset for asset in SectionAssetlist if
                                                 asset.split("_")[3] not in ["Left", "Right", "Center"]]
                CurrentAsset = RandFromList(currentSeed, SectionAsset_NOConnectionlist)
        else:

            #0 or 1
            HalfMark = np.random.randint(0, 2)
            if HalfMark>0 and RestDist>=3 and not CurrentSocket in ["R1","R2","R3","R4"]:
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

            SectionAsset_NoOneSideList = [asset for asset in SectionAssetlist if asset.split("_")[2] not in UpperOneSide and int(asset.split("_")[-1][0])<= RestDist]
            SectionAsset_NOConnectionlist = [asset for asset in SectionAssetlist if asset.split("_")[3] not in ["Left", "Right", "Center"] and int(asset.split("_")[-1][0])<= RestDist ]
            SectionAsset_NOConvertlist = [asset for asset in SectionAsset_NOConnectionlist if "to" not in asset.split("_")[2] and int(asset.split("_")[-1][0])<= RestDist]
            currentSeed = loopCount + index + pointcreated + currentFloor + section_seed

            #use Door or Not
            DoorUse = np.random.randint(0, 2)
            if DoorUse>0 and DoorMark>0 and DoorAssetlist:
                CurrentAsset = RandFromList(currentSeed, DoorAssetlist)
                # print("Door Check")
            elif UpperGeo and UpperOneSide and OneSideStyle in UpperOneSide and OneSideNpt:
                # print("OneSide Check")
                #rand 0 or 1
                if np.random.randint(0, 2):
                    CurrentAsset = OneSideNpt.attribValue("name")
                else:
                    CurrentAsset = RandFromList(currentSeed, SectionAsset_NoOneSideList)
            elif must_Convert==0 and RestDist<4:
                # print("Convert Check")
                if UpperOneSide:
                    CurrentAsset = RandFromList(currentSeed,SectionAsset_NoOneSideList)
                else:
                    CurrentAsset = RandFromList(currentSeed, SectionAsset_NOConnectionlist)
            else:
                if UpperOneSide:
                    CurrentAsset = RandFromList(currentSeed, SectionAsset_NoOneSideList)
                else:
                    CurrentAsset = RandFromList(currentSeed, SectionAsset_NOConnectionlist)

            # print("!"*10,CurrentAsset)
            if not CurrentAsset:
                CurrentAsset = RandFromList(currentSeed, SectionAsset_NOConnectionlist)

            if RestDist==1 and CurrentSocket==NextSocket:
                SectionAsset_NOCClist = [asset for asset in SectionAssetlist if
                                                 asset.split("_")[3] not in ["Left", "Right", "Center"] and asset.split("_")[2] == NextSocket and asset.split("_")[-1]=="1m"]
                # Last Section
                CurrentAsset = RandFromList(currentSeed, SectionAsset_NOCClist)

        # print(f"CurrentAsset______________{CurrentAsset}")

        LastSocket = CurrentSocket
        if halfList:
            for asset in halfList:
                StartPos, OffsetSize = CreatePoint(asset, StartPos, CurrentDir)
                pointcreated += 1
                RestDist -= OffsetSize
                loopCount += 1
                #half list all the same socket doesn't need to update
        else:
            CurrentSocket = CurrentAsset.split("_")[2]
            # Update Socket if Convert
            if "to" in CurrentAsset:
                # convert section
                CurrentSocket = CurrentSocket.split("to")[-1]

            if "Door" in CurrentAsset:
                DoorRestCount -= 1
                DoorPosList.append(StartPos+CurrentDir*CurrentSize)

            StartPos, OffsetSize = CreatePoint(CurrentAsset, StartPos, CurrentDir)
            pointcreated += 1
            RestDist -= OffsetSize
            costDist += OffsetSize
            loopCount += 1
        # print(f"CurrentAsset :{CurrentAsset}")
        LastAsset = CurrentAsset

        # if style in style limit and sameSide is false then append to the side limit
        if Stylelimit.get(CurrentSocket,{}) and Stylelimit.get(CurrentSocket,{}).get("One_Side",False):
            #set one_side attr to geo attr
            SideLimit.append(CurrentSocket)
            geo.setGlobalAttribValue("OneSide",list(SideLimit))

    LimitData["SideLimit"] = SideLimit
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

def updateSocketList(Socket, keywords, sizeLimit, ConvertKey="", AdditionalSocket=None,ExceptionList=None):
    """
    Filter the list by Socket Mark
    :param Socket: Current Socket
    :param keywords: Filter Keywords
    :param sizeLimit: Size Limit
    :param ConvertKey: Convert Key
    :param AdditionalSocket: Additional Socket
    :param ExceptionList: Exception List
    """
    #get global all_powerful
    if AdditionalSocket is None:
        AdditionalSocket = []
    global all_powerful
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

        #special connection style
        if all_powerful in assetname and sizeLimit >= UnitSize:
            newArray.append(assetname)
            continue

        if Socket == all_powerful and sizeLimit >= UnitSize:
            # current Socket is all powerful type can connect with any style asset
            # size and style match
            if not keywords or (Type not in keywords and Pos not in keywords and (Style not in keywords and Style not in ExceptionList)):
                if ConvertKey:
                    continue
                # pos and type not in forbidden list
                newArray.append(assetname)
        elif ((Socket == Style) or (Style in AdditionalSocket) or (Type in ExceptionList)) and sizeLimit >= UnitSize:
            #convert section filter first
            if "to" in assetname.split("_")[2]:
                SocketA = assetname.split("_")[2].split("to")[0]
                SocketB = assetname.split("_")[2].split("to")[-1]
                if assetname.split("_")[2] == ConvertKey:
                    ConvertArray.append(assetname)
                if SocketA in keywords or SocketB in keywords:
                    continue
            elif ConvertKey:
                #pass current Socket without "to" keyword
                continue
            # size and style match
            if not keywords or (Type not in keywords and Pos not in keywords and Style not in keywords):
                # pos and type not in forbidden list
                newArray.append(assetname)

    if all_powerful:
        return newArray
    elif ConvertKey:
        if debug:logging.log(logging.INFO, f"Update Socket List Convert Section from {Socket} to {ConvertKey}")
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

def CornerExtend(StartSocket,EndSocket,CornerExtendCount,toMark=False,SectionAssetlist=None):
    """
    :param StartSocket:
    :param EndSocket:
    :param CornerExtendCount:
    """
    if toMark:
        start_assets_list = [asset for asset in SectionAssetlist if asset.split("_")[2] == all_powerful]
        end_assets_list = [asset for asset in SectionAssetlist if asset.split("_")[2] == EndSocket]
        ExtendList = []
        #to mark, startSocket add one ,rest fullfilled by endSocket
        for i in range(0,CornerExtendCount):
            if i == 0 and len(start_assets_list)>0:
                StartAsset = start_assets_list[0]
                ExtendList.append(StartAsset)
            else:
                EndAsset = end_assets_list[0]
                ExtendList.append(EndAsset)
    else:
        start_assets_list = [asset for asset in SectionAssetlist if asset.split("_")[2] == StartSocket]
        end_assets_list = [asset for asset in SectionAssetlist if asset.split("_")[2] == all_powerful]
        ExtendList = []
        #from mark, endSocket add one at the end of the list,rest fullfilled by startSocket
        for i in range(0,CornerExtendCount+1):
            if i != CornerExtendCount:
                StartAsset = start_assets_list[0]
                ExtendList.append(StartAsset)
            else:
                EndAsset = end_assets_list[0]
                ExtendList.append(EndAsset)
    return ExtendList

CalPoints(CurrentRules=CurrentRules)