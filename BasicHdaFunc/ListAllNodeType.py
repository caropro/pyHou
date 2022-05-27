# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import hou
# import hrpyc

# connection,hou = hrpyc.import_remote_module()
# ui = connection.modules.hou.ui
# import hou

NodeTypeCategory_list = [x for x in dir(hou) if "NodeTypeCategory" in x]
NodeTypeCategory_list.remove("vexContextForNodeTypeCategory")
print(NodeTypeCategory_list)

count = 0
for nodetype in NodeTypeCategory_list:
    if(nodetype != "NodeTypeCategory"):
        print(nodetype)
        cateGory = getattr(hou,nodetype)
        nodecount = len(cateGory().nodeTypes())
        count+=nodecount
        print(nodecount)

print(count)
print("end")