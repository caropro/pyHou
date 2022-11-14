# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0

import hou

def setupPruneBundle(**kwargs):
   #set Color info
   pruneColor = hou.Color([0.05,0.05,0.05])
   defColor = hou.Color([0.8,0.8,0.8])
   selectedNodes = hou.selectedNodes()
   #get target bundle by name
   bundle = hou.nodeBundle("prune")

   def add_nodes(bundle,selectedNodes):
      for node in selectedNodes:
         if node not in bundle.nodes():
            bundle.addNode(node)
            node.setColor(pruneColor)
   #if bundle exist add current node to the bundle
   if bundle:
      #if only alt click , remove current selection from bundle
      if kwargs["altclick"] and not kwargs["ctrlclick"]:
         if selectedNodes:
            for node in selectedNodes:
               bundle.removeNode(node)
               node.setColor(defColor)
            return
      #if alt and ctrl click,remove the bundle
      elif kwargs["ctrlclick"] and kwargs["altclick"]:
         nodes = bundle.nodes()
         bundle.destroy()
         for node in nodes:node.setColor(defColor)
         return
      #if normal click , add nodes to bundle
      elif selectedNodes:
         add_nodes(bundle, selectedNodes)

   #if bundle does not exist, create one and add node to the bundle
   else:
      #not alt click and not ctrlclicke
      if not kwargs["altclick"] and not kwargs["ctrlclick"]:
         bundle = hou.addNodeBundle("prune")
         add_nodes(bundle, selectedNodes)
      else:
         return

#run the function
setupPruneBundle(kwargs)