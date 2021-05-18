# coding = utf-8
import os
import hou


def Update():
    CurrentNode = hou.pwd()
    for node in CurrentNode.children():
        node.destroy()
    merge_node = CurrentNode.createNode("merge", "merge")
    hda_path = CurrentNode.type().definition().libraryFilePath()
    sourcePath = os.path.dirname(hda_path).replace("PublicDataHDAs","LandscapeReleasedGeoCache")
    for data in os.listdir(sourcePath):
        data_path = os.path.join(sourcePath, data)
        print(data)
        data_name = os.path.splitext(data)[0]
        ReadNode = CurrentNode.createNode("file", data_name)
        ReadNode.parm("file").set(data_path)
        merge_node.setInput(len(merge_node.inputs()), ReadNode, 0)
        print data

    # heightfield_tilesplice1 Tile
    Seam_node = CurrentNode.createNode("volumesplice", "splice")
    Seam_node.setInput(0, merge_node, 0)

    output = CurrentNode.createNode("output", "output")
    output.setInput(0, Seam_node)
    # NodeList =





