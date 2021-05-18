#coding = utf-8
import os,sys
import toolutils
import soptoolutils
from connection_init import hou,toolutils,ui

# hrpyc.start_server()
toolutils.sceneViewer()
def setup():
    v = toolutils.sceneViewer()
    print(dir(toolutils))
    obj = v.selectObjects("Select Current Objs")
    print(obj)

setup()











