#coding = utf-8
import os,sys,socket
import hrpyc
import cProfile
import toolutils
import soptoolutils
import itertools
import hou


connection,hou = hrpyc.import_remote_module()
ui = connection.modules.hou.ui
hou.ui = ui
sys.modules["hou"] = hou

def print_Tree(node,indent=0):
    for child in node.children():
        print " " * indent + child.name()
        print_Tree(child,indent+3)

#print_Tree(hou.node('/'))
#hou.hipFile.load("F:/work/strangeTest/uvColorTest.hip")

#hou.hipFile.clear()
# n = hou.node("/obj").createNode("geo")
# n.moveToGoodPosition()
print(hou.ch("obj/geo1/tx"))