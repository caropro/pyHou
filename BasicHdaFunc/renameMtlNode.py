# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0

import hrpyc
connection,hou = hrpyc.import_remote_module()
ui = connection.modules.hou.ui
#import hou

selectedNode = hou.selectedNodes()[0]
root = selectedNode.parent()

for node in root.children():
    if node.type().name() == "material":
        print(node)