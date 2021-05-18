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


print dir(hou.ui.displayMessage)

hou.ui.displayMessage("yes")