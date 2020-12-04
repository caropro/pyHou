# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0

import hrpyc
import hou
connection,hou = hrpyc.import_remote_module()
ui = connection.modules.hou.ui

hou.ui.displayMessage("test")


