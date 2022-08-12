# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
########################################################################
# Replace the sample code below with your own to create a
# PyQt5 or PySide2 interface.  Your code must define an
# onCreateInterface() function that returns the root widget of
# your interface.
#
# The 'hutil.Qt' is for internal-use only.
# It is a wrapper module that enables the sample code below to work with
# either a Qt4 or Qt5 environment for backwards-compatibility.
#
# When developing your own Python Panel, import directly from PySide2
# or PyQt5 instead of from 'hutil.Qt'.
########################################################################

#
# SAMPLE CODE
#
from hutil.Qt import QtWidgets
import os
import hou
import sys

projectDir = r"D:/Top_PDG"

def openScene(item):
    HipPath = os.path.join(projectDir,item.data())
    print(item.data())
    hou.hipFile.load(HipPath)

def init_UI():
    widget = QtWidgets.QListWidget()
    hip_list = [file for file in os.listdir(projectDir) if file.endswith(".hip")]
    for hip_file in hip_list:
        widget.addItem(hip_file)

    widget.doubleClicked.connect(openScene)
    return widget
