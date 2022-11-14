# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
#use current value set as param's default value
import hou
#get node
nodes = hou.selectedNodes()

for node in nodes:
    # get definition
    defination = node.type().definition()
    # get ptg
    ptg = defination.parmTemplateGroup()
    parms = node.parms()
    if len(parms)>0 :
        # get param
        for parm in parms:
            parm_name = parm.name()
            parm_value = parm.eval()
            # get template
            #parTemp = ptg.find(parm_name)
            parTemp = parm.parmTemplate()
            # set param default value
            parTemp.setDefaultValue((parm_value,))
            # replace templateGrp
            ptg.replace(ptg.find(parm_name),parTemp)

        defination.setParmTemplateGroup(ptg)







