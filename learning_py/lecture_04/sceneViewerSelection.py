# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import hrpyc
import hou
import sys

connection,hou = hrpyc.import_remote_module()
ui = connection.modules.hou.ui
hou.ui = ui

sys.modules["hou"] = hou

import toolutils
import soptoolutils
if False:
    import hou
    print(hou)

vp = toolutils.sceneViewer()
current = vp.selectObjects()
print(vp)

# r = soptoolutils.genericTool({},"color","MyColor",allow_obj_sel=False)
# r.parmTuple("color").set([1,0,0])



