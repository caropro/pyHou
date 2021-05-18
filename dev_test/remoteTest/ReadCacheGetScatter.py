#coding = utf-8
import os,sys,socket
import hrpyc
import cProfile
import toolutils
import soptoolutils
import itertools
import hou
hou.hda

connection,hou = hrpyc.import_remote_module()
ui = connection.modules.hou.ui
hou.ui = ui




hda_path = CurrentNode.type().definition().libraryFilePath()
sourcePath = os.path.dirname(hda_path).replace("PublicDataHDAs","LandscapeReleasedGeoCache")

hda_path = ""
#init
HdaList = []
for file in os.listdir(path):
    if "cache.hda" in file:
        hda_path = os.path.join(path,file)
        filename = os.path.splitext(file)[0]
        HdaList.append(filename)
        #install_cache_hda
        hou.hda.installFile(hda_path)

CurrentNode = hou.selectedNodes()[0]
for node in CurrentNode.children():
    node.destroy()
merge_node = CurrentNode.createNode("merge", "merge")
for node_name in HdaList:
    cache_node = CurrentNode.createNode(node_name)
    cache_node.allowEditingOfContents(1)
    scatter_cache = cache_node.node("mod_Scatter_scatter_cache")
    scatter_cache.setDisplayFlag(1)
    merge_node.setInput(len(merge_node.inputs()), cache_node, 0)

output = CurrentNode.createNode("output", "output")
output.setInput(0, merge_node)





