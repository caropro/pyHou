#coding = utf-8
import os,sys,socket
import hrpyc
import cProfile
import toolutils
import soptoolutils
import itertools

connection,hou = hrpyc.import_remote_module()
ui = connection.modules.hou.ui
hou.ui = ui
sys.modules["hou"] = hou

print(help(cProfile))
print(dir(cProfile))


#itertools.combinations()