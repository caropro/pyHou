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

targetMtl = hou.node("/mat")

NameList=[]
index = 0
for node in root.children():
    try:
        if node.type().name() == "material":
            mtl_name = node.parm("shop_materialpath1").eval().split("/")[-1]
            mtl = targetMtl.node(mtl_name)
            if mtl:
                node.parm("shop_materialpath1").set(mtl.path())
            else:
                print("Lack Mtl %s" % mtl)
    except:
        print(node.name())