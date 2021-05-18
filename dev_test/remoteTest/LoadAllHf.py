#coding = utf-8
import os,sys,socket
import hrpyc
import cProfile
import toolutils
import soptoolutils
import itertools

connection,hou = hrpyc.import_remote_module()
sys.modules["hou"] = hou
#tile list
bgeo_path = r"E:\REF\art_dev\Art\HouLand\LandscapeHDAs"
files = [tile for tile in os.listdir(bgeo_path) if tile.endswith("bgeo") and tile.startswith("Tile") and not "Lake" in tile and not "River" in tile or tile.startswith("Seam")]
tilefiles = [tile for tile in files if tile.endswith("bgeo")]
seamtiles = [tile for tile in tilefiles if tile.startswith("Seamed")]
# print(seamtiles)

for seam in seamtiles:
    tilename = seam[-9:-5]
    tilefiles = [tile for tile in tilefiles if not tilename in tile]

print(tilefiles)
print(len(tilefiles))
print(len(seamtiles))
subnode = hou.selectedNodes()[0]
for tile in tilefiles:
    tile_path = os.path.normpath(os.path.join(bgeo_path,tile))
    file_node = subnode.createNode("file")
    file_node.parm("file").set(tile_path)
for tile in seamtiles:
    tile_path = os.path.normpath(os.path.join(bgeo_path, tile))
    file_node = subnode.createNode("file")
    file_node.parm("file").set(tile_path)