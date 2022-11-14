# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import hou
#record stageNode
sourceNode = hou.selectedNodes()[0]

targetNodePath = hou.ui.selectNode()
targetNode = hou.node(targetNodePath)

matnet = [node for node in targetNode.children() if node.type().name()=="matnet"][0]
print(matnet)
mtl = matnet.children()[0]

#copy Node
hou.copyNodesTo((mtl,),sourceNode)
sourceNode.layoutChildren()
hou.ui.displayMessage("Done")



