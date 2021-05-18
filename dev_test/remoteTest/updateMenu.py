#coding = utf-8
import os,sys
import toolutils
import soptoolutils
from connection_init import hou,toolutils,ui

node = hou.selectedNodes()[0]
parm_template = node.parmTemplateGroup()

target_menu = node.parm("MenuData").parmTemplate()
target_menu.setMenuLabels(["a","b","c"])
target_menu.setMenuItems(["a","b","c"])
parm_template.replace("MenuData", target_menu)
node.setParmTemplateGroup(parm_template)
hou.ui.displayMessage("Done!!")

