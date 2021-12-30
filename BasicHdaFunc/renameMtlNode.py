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

NameList=[]
index = 0
for node in root.children():
    if node.type().name() == "material":
        mtl_name = node.parm("shop_materialpath1").eval().split("/")[-1]
        print(mtl_name)
        index = NameList.count(mtl_name)
        node.setName("%s_%s"%(mtl_name,index))
        NameList.append(mtl_name)