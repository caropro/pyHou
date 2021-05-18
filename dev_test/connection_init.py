#coding = utf-8
import os,sys,socket
import hrpyc
import toolutils
import soptoolutils

connection,hou = hrpyc.import_remote_module()
ui = connection.modules.hou.ui
hou.ui = ui
sys.modules["hou"] = hou











