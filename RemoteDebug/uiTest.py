# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import hrpyc
import toolutils
import sys

connection,hou = hrpyc.import_remote_module()
ui = connection.modules.hou.ui
hou.ui = ui
toolutils.hou.ui = hou.ui
sys.modules["hou"] = hou


#
# vp = toolutils.sceneViewer()
# print(vp)