# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0

import hrpyc
connection,hou = hrpyc.import_remote_module()
ui = connection.modules.hou.ui
# try:
#     import hou
# except:
#     pass

targetNode = hou.selectedNodes()[0]
root = targetNode.parent()


MtlSub = root.createNode("subnet","MtlXConvert")

#get Textures Path
baseTex = targetNode.evalParm("basecolor_texture")
RoughTex = targetNode.evalParm("rough_texture")
NormTex = targetNode.evalParm("baseNormal_texture")
dispTex = targetNode.evalParm("dispTex_texture")

#create inputs node
# MtlSub.createNode("subinput","inputs")

#create mtlxSurface
mtlxsurface = MtlSub.createNode("mtlxstandard_surface","mtlxsurface")
surface_output = MtlSub.createNode("subnetconnector","surface_output")
surface_output.setParms({"parmtype":24})
surface_output.setInput(0,mtlxsurface)
surface_output.setParms({"connectorkind":1})
surface_output.setParms({"parmname":"surface"})
surface_output.setParms({"parmlabel":"Surface"})

#baseColor
baseReader = MtlSub.createNode("mtlximage","BaseColor")
baseReader.setParms({"file":baseTex})
mtlxsurface.setInput(1,baseReader)
#Roughness separate Channel
RoughReader = MtlSub.createNode("mtlximage","Roughness")
RoughReader.setParms({"file":RoughTex})
separate = MtlSub.createNode("mtlxseparate3c")
separate.setInput(0,RoughReader)
mtlxsurface.setInput(6,separate,0)

#Normal add mapConvert
NormReader = MtlSub.createNode("mtlximage","Normal")
NormReader.setParms({"file":NormTex})
normalmap = MtlSub.createNode("mtlxnormalmap")
normalmap.setInput(0,NormReader)
mtlxsurface.setInput(40,normalmap,0)

#create mtlxdisplacement
mtlxdisplacement = MtlSub.createNode("mtlxdisplacement","mtlxdisplacement")
displacement_output = MtlSub.createNode("subnetconnector","displacement_output")
displacement_output.setInput(0,mtlxdisplacement)
displacement_output.setParms({"connectorkind":1})
displacement_output.setParms({"parmname":"displacement"})
displacement_output.setParms({"parmlabel":"Displacement"})
displacement_output.setParms({"parmtype":25})

dispReader = MtlSub.createNode("mtlximage","Displacement")
dispReader.setParms({"file":dispTex})
Dispseparate = MtlSub.createNode("mtlxseparate3c")
Dispseparate.setInput(0,dispReader)
remap = MtlSub.createNode("mtlxremap")
remap.setInput(0,Dispseparate,0)
mtlxdisplacement.setInput(0,remap)
mtlxdisplacement.setParms({"scale":0.1})

MtlSub.layoutChildren()
MtlSub.setMaterialFlag(1)