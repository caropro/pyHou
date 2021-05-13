#coding = utf-8
import os
import numpy
import math
import json
import struct
import time
import hou

#
# currentNode = hou.pwd()
# Hda_path = currentNode.parent().type().definition().libraryFilePath()
#
# currentNode = hou.pwd()
# Hda_path = currentNode.parent().type().definition().libraryFilePath()
# pr_file = os.path.join(Hda_path.split("HouLand")[0],r"TerrainData\WorldTiles_0\1.prmap")
# pr_file = os.path.normpath(pr_file)
# spr_file = os.path.join(Hda_path.split("HouLand")[0],r"TerrainData\WorldTiles_0\1.sprmap")
# spr_file = os.path.normpath(spr_file)
# recordFile = os.path.join(Hda_path.split("HouLand")[0],r"HouLand\DesignerFunctions\Data\DataTime.txt")
# recordFile = os.path.normpath(recordFile)
# dataDictFile =os.path.join(Hda_path.split("HouLand")[0],r"HouLand\DesignerFunctions\Data\dataDict.json")
# dataDictFile = os.path.normpath(dataDictFile)
#
#
# #createFolder
# if not os.path.exists(os.path.dirname(recordFile)):
#     os.makedirs(os.path.dirname(recordFile))
#
#current time data
c_time =time.time()

pr_file = r"E:\REF\Art\TerrainData\WorldTiles_0\1.prmap"
spr_file = r"E:\REF\Art\TerrainData\WorldTiles_0\1.sprmap"
dataDictFile = "dataDict.json"
recordFile = "DataTime.txt"

def readData(filepath):
    filesizex = 0
    filesiezy = 0
    count = 0
    dataDict = {}
    with open(filepath, "rb") as dataFile:
        # pass first line
        dataFile.read(16)
        # read second 2
        headData = dataFile.read(4)
        filesizex, = struct.unpack("i", headData)
        headData = dataFile.read(4)
        filesiezy, = struct.unpack("i", headData)

        # pass the rest data
        dataFile.read(8)

        for xpos in range(filesizex):
            ypos = 0
            # if ypos less than max value
            while ypos < filesiezy:
                data = dataFile.read(1)
                if not data:
                    break
                decimal = struct.unpack("B", data)[0]
                # pass the 0b
                data = bin(decimal)  # [2:]
                datalength = len(data)
                if datalength < 8:
                    # fill data length with 0
                    data = "0" * (8 - datalength) + data
                elif datalength > 8:
                    data = data[-8:]
                data = data.replace("b", "0")
                for f_p in range(8):
                    ypos += 1
                    if data[f_p] == "1":
                        dataDict["{},{}".format(xpos, ypos)] = data[f_p]
    return  dataDict


if(os.path.exists(recordFile)):
    with open(recordFile,"r") as df:
        timecode = float(df.read())
else:
    timecode = 0

currenttimecode = os.path.getmtime(pr_file)

dataDict={}
if "%.02f"%timecode != "%.02f"%currenttimecode or not os.path.exists(dataDictFile):
    print "Update Data"
    with open(recordFile,"w") as df:
        df.write(str(currenttimecode))
    # read data from file and save cache file
    dataDict = readData(pr_file)
    with open(dataDictFile, "w+") as file:
        json.dump(dataDict, file)
else:
    print "SameFile,Read From Cache File"
    #read cache file data
    with open(dataDictFile, "r") as file:
        all_info = file.read()
        dataDict = json.loads(all_info)

c_time =time.time() - c_time
print "Time Consume: %s"%c_time


#
# current_node = hou.pwd()
# delete_list = []
# geo = current_node.geometry()
# for point in geo.points():
#     pos = point.position()
#     data_pos = "{},{}".format(int(round(pos[0]+4032)),int(round(pos[2]+4032)))
#     if not dataDict.get(data_pos):
#         delete_list.append(point)
# if delete_list:
#     geo.deletePoints(delete_list)