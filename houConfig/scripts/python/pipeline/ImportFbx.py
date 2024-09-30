# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0

import os
import hou


def importFbxfiles():
    searchDir = hou.ui.selectFile(file_type=hou.fileType.Directory)
    files = os.listdir(searchDir)
    fbxfiles = [file for file in files if file.endswith('.fbx')]
    if(len(fbxfiles) == 0):
        hou.ui.displayMessage("No fbx files found in the directory")
        return

    layout = hou.ui.displayMessage("Do you want to layout the fbx files?", buttons=("Yes", "No"))
    print(layout)
    currentNode = hou.node('/obj').createNode('geo', "ReadFbx")
    offset = 0
    for fbxfile in fbxfiles:
        filepath = os.path.join(searchDir, fbxfile)
        fileNode = currentNode.createNode('file', fbxfile)
        fileNode.parm('file').set(filepath)
        packNode = currentNode.createNode('pack')
        packNode.setInput(0, fileNode)
        if layout == 0:
            bounds = fileNode.geometry().boundingBox()
            x_size = bounds.sizevec()[0]
            xform = currentNode.createNode('xform')
            xform.setInput(0, packNode)
            xform.setDisplayFlag(True)
            xform.setParms({'tx': offset})
            offset += x_size*0.5+5

    hou.ui.displayMessage("Import fbx files successed")