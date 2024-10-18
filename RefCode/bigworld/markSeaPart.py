#coding = utf-8
import os
import hou
import hrpyc

connection,hou = hrpyc.import_remote_module()

vex_code = """if (detail(0,"area_name")==""){@mask = 1;}"""
def Update():
    CurrentNode = hou.selectedNodes()[0]
    for node in CurrentNode.children():
        node.destroy()
    merge_node = CurrentNode.createNode("merge", "merge")
    #hda_path = CurrentNode.type().definition().libraryFilePath()
    #sourcePath = os.path.dirname(hda_path).replace("PublicDataHDAs","LandscapeReleasedGeoCache")
    sourcePath = r"E:\REF\Art\HouLand\LandscapeReleasedGeoCache"
    for data in os.listdir(sourcePath):
        data_path = os.path.join(sourcePath, data)
        print(data)
        data_name = os.path.splitext(data)[0]
        ReadNode = CurrentNode.createNode("file", data_name)
        ReadNode.parm("file").set(data_path)
        vexNode = CurrentNode.createNode("volumewrangle")
        vexNode.parm("snippet").set(vex_code)
        vexNode.setInput(0, ReadNode, 0)
        merge_node.setInput(len(merge_node.inputs()), vexNode, 0)
        print data

    # heightfield_tilesplice1 Tile
    Seam_node = CurrentNode.createNode("volumesplice", "splice")
    Seam_node.setInput(0, merge_node, 0)

    output = CurrentNode.createNode("output", "output")
    output.setInput(0, Seam_node)
    # NodeList =


Update()