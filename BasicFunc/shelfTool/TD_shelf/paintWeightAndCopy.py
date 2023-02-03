# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import hou
import toolutils

def runGen():
    currentSelected = hou.selectedNodes()[0]
    currentPath = currentSelected.path()

    #create BaseNose
    BaseNode = hou.node("/obj").createNode("geo","PaintAndCopy")
    #print child node inside BaseNode
    gridNode = BaseNode.createNode("grid","BaseGrid")
    paintNode = BaseNode.createNode("attribpaint","Paint")
    scatterNode = BaseNode.createNode("scatter::2.0","Scatter")
    copyNode = BaseNode.createNode("copytopoints::2.0","Copy")
    objMergeNode = BaseNode.createNode("object_merge","ObjMerge")

    #connect Node
    paintNode.setInput(0,gridNode)
    scatterNode.setInput(0,paintNode)
    copyNode.setInput(0,objMergeNode)
    copyNode.setInput(1,scatterNode)

    #layout node inside
    BaseNode.layoutChildren()

    #set Attr
    objMergeNode.parm("objpath1").set(currentPath)
    gridNode.setParms({"rows":20,"cols":20})
    paintNode.parm("attribname1").set("density")
    paintNode.parm("attribtype1").set(1)
    scatterNode.parm("usedensityattrib").set(1)
    #set flag
    copyNode.setDisplayFlag(1)

    #viewer
    v = toolutils.sceneViewer()
    paintNode.setCurrent(True)
    v.enterCurrentNodeState()


if not hou.selectedNodes():
    hou.ui.displayMessage("Please select at least one model to Copy!")
else:
    runGen()