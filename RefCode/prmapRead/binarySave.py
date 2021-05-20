#coding = utf-8
import zipfile
import json

# import struct
# pr_file = r"E:\REF\Art\TerrainData\WorldTiles_0\Tile_L1D1\1.prmap"
# with open(pr_file,"rb") as file:
#      test =file.read(1)
#      decimal = struct.unpack("b",test)[0]
#      data = bin(decimal)[2:]
#      length = len(data)
#      if length<8:
#           data = "0" + data
#      print data
#
# print struct.calcsize('b')
# parm_dic = {}
# with open("dataDice.json","r") as file:
#      all_info = file.read()
#      print(all_info)
#      parm_dic = json.loads(all_info)


# with zipfile.ZipFile("data.zip","w",zipfile.ZIP_DEFLATED) as myzip:
#      myzip.write("dataDice.json")


with zipfile.ZipFile("data.zip","r",zipfile.ZIP_DEFLATED) as myzip:
     with myzip.open("dataDice.json") as datafile:
          data = datafile.read()
          parm_dic = json.loads(data)

print(parm_dic)