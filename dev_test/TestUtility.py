#coding = utf-8
import os,sys
import toolutils
import soptoolutils
from connection_init import hou,toolutils,ui

def currentTime():
    currentFrame = hou.frame()
    currentTime = hou.frameToTime(currentFrame)
    print("{}f---{}s".format(currentFrame,currentTime))

currentTime()
