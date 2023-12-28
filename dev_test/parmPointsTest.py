#coding = utf-8
import os,sys,socket
import hrpyc
import cProfile
import toolutils
import soptoolutils
import itertools

connection,hou = hrpyc.import_remote_module()
ui = connection.modules.hou.ui
# hou.ui = ui
# sys.modules["hou"] = hou

import pprint
targetNodes = hou.selectedNodes()
firstNode = targetNodes[0]
parentNode = firstNode.parent()

copyNode = parentNode.node("rename")

for node in targetNodes:
    NewCopy = hou.copyNodesTo((copyNode,),parentNode)[0]
    NewCopy.setInput(0,node)


