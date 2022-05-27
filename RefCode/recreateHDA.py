# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0

import hrpyc
import hou
import os
connection,hou = hrpyc.import_remote_module()
ui = connection.modules.hou.ui

# Initialize parent node variable.
if locals().get("hou_parent") is None:
    hou_parent = hou.node("/obj/geo1")

# Code for /obj/geo1/lh_craterscatter1
hou_node = hou_parent.createNode("lh_craterscatter", "lh_craterscatter1", run_init_scripts=False, load_contents=False, exact_type_name=True)
hou_node.move(hou.Vector2(-3.21756, 1.97977))
hou_node.bypass(False)
hou_node.setDisplayFlag(True)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(True)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/lh_craterscatter1/totalpointcount parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1")
hou_parm = hou_node.parm("totalpointcount")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(3)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/variability_unifromrange parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1")
hou_parm_tuple = hou_node.parmTuple("variability_unifromrange")
hou_parm_tuple.lock((False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((5, 10))
hou_parm_tuple.setAutoscope((False, False))


# Code for /obj/geo1/lh_craterscatter1/blur parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1")
hou_parm = hou_node.parm("blur")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(5)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/distort parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1")
hou_parm = hou_node.parm("distort")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_mesh parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1")
hou_parm = hou_node.parm("make_mesh")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/mesh_material parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1")
hou_parm = hou_node.parm("mesh_material")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/resample_scale parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1")
hou_parm = hou_node.parm("resample_scale")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.5)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/polyreduce_percent parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1")
hou_parm = hou_node.parm("polyreduce_percent")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/mesh_raise parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1")
hou_parm = hou_node.parm("mesh_raise")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(2)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Update the parent node.
hou_parent = hou_node

# Code for /obj/geo1/lh_craterscatter1/Start
hou_node = hou_parent.createNode("null", "Start", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(0.0914117, 0.311138))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/lh_craterscatter1/Start/copyinput parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/Start")
hou_parm = hou_node.parm("copyinput")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/Start/cacheinput parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/Start")
hou_parm = hou_node.parm("cacheinput")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.589")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.589")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/lh_craterscatter1/output
hou_node = hou_parent.createNode("output", "output", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(0.0914117, -23.9021))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/lh_craterscatter1/output/outputidx parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/output")
hou_parm = hou_node.parm("outputidx")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.589")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.589")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/lh_craterscatter1/project_crater
hou_node = hou_parent.createNode("heightfield_project", "project_crater", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(1.54798, -2.10968))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/lh_craterscatter1/project_crater/layer parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/project_crater")
hou_parm = hou_node.parm("layer")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("height")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/project_crater/maskmode parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/project_crater")
hou_parm = hou_node.parm("maskmode")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/project_crater/maskdir parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/project_crater")
hou_parm = hou_node.parm("maskdir")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("both")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/project_crater/heightlayer parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/project_crater")
hou_parm = hou_node.parm("heightlayer")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("height")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/project_crater/maskdensity parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/project_crater")
hou_parm = hou_node.parm("maskdensity")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/project_crater/maskinvert parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/project_crater")
hou_parm = hou_node.parm("maskinvert")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/project_crater/hitfarthest parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/project_crater")
hou_parm = hou_node.parm("hitfarthest")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/project_crater/combine parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/project_crater")
hou_parm = hou_node.parm("combine")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("min")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/project_crater/maxraydist parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/project_crater")
hou_parm = hou_node.parm("maxraydist")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1000)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/project_crater/dojitter parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/project_crater")
hou_parm = hou_node.parm("dojitter")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/project_crater/sample parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/project_crater")
hou_parm = hou_node.parm("sample")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(3)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/project_crater/jitter parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/project_crater")
hou_parm = hou_node.parm("jitter")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.25)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/project_crater/jittercombine parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/project_crater")
hou_parm = hou_node.parm("jittercombine")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("median")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/project_crater/seed parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/project_crater")
hou_parm = hou_node.parm("seed")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/geo1/lh_craterscatter1/substract_crater
hou_node = hou_parent.createNode("heightfield_layer", "substract_crater", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(1.05664, -2.96667))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/lh_craterscatter1/substract_crater/mode parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/substract_crater")
hou_parm = hou_node.parm("mode")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("subtract")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/substract_crater/blend parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/substract_crater")
hou_parm = hou_node.parm("blend")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.5)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/substract_crater/layer parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/substract_crater")
hou_parm = hou_node.parm("layer")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("height")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/substract_crater/folder2 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/substract_crater")
hou_parm = hou_node.parm("folder2")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/substract_crater/masklayer parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/substract_crater")
hou_parm = hou_node.parm("masklayer")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("mask")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/substract_crater/maskweight parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/substract_crater")
hou_parm = hou_node.parm("maskweight")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/substract_crater/invertmask parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/substract_crater")
hou_parm = hou_node.parm("invertmask")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/substract_crater/folder0 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/substract_crater")
hou_parm = hou_node.parm("folder0")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/substract_crater/base_offset parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/substract_crater")
hou_parm = hou_node.parm("base_offset")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/substract_crater/base_scale parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/substract_crater")
hou_parm = hou_node.parm("base_scale")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/substract_crater/layer_offset parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/substract_crater")
hou_parm = hou_node.parm("layer_offset")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/substract_crater/layer_scale parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/substract_crater")
hou_parm = hou_node.parm("layer_scale")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/substract_crater/final_offset parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/substract_crater")
hou_parm = hou_node.parm("final_offset")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/substract_crater/final_scale parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/substract_crater")
hou_parm = hou_node.parm("final_scale")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/substract_crater/folder1 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/substract_crater")
hou_parm = hou_node.parm("folder1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/substract_crater/doclampmin parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/substract_crater")
hou_parm = hou_node.parm("doclampmin")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/substract_crater/clampmin parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/substract_crater")
hou_parm = hou_node.parm("clampmin")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/substract_crater/doclampmax parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/substract_crater")
hou_parm = hou_node.parm("doclampmax")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/substract_crater/clampmax parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/substract_crater")
hou_parm = hou_node.parm("clampmax")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/geo1/lh_craterscatter1/blur_crater
hou_node = hou_parent.createNode("heightfield_blur", "blur_crater", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(1.05664, -3.92649))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/lh_craterscatter1/blur_crater/layer parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/blur_crater")
hou_parm = hou_node.parm("layer")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("height")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/blur_crater/masklayer parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/blur_crater")
hou_parm = hou_node.parm("masklayer")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("mask")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/blur_crater/maskaware parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/blur_crater")
hou_parm = hou_node.parm("maskaware")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/blur_crater/iterations parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/blur_crater")
hou_parm = hou_node.parm("iterations")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(10)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/blur_crater/method parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/blur_crater")
hou_parm = hou_node.parm("method")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("blur")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/blur_crater/radius parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/blur_crater")
hou_parm = hou_node.parm("radius")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(5)
hou_parm.setAutoscope(False)

# Code for first keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(11.699999999999999)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("ch(\"../blur\")", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for last keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(11.699999999999999)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("ch(\"../blur\")", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(11.699999999999999)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("ch(\"../blur\")", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(11.699999999999999)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("ch(\"../blur\")", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)


# Code for /obj/geo1/lh_craterscatter1/blur_crater/bordertype parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/blur_crater")
hou_parm = hou_node.parm("bordertype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("streak")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/blur_crater/borderval parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/blur_crater")
hou_parm = hou_node.parm("borderval")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___toolid___", "geometry_terrain")
hou_node.setUserData("___Version___", "")
hou_node.setUserData("___toolcount___", "1")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/geo1/lh_craterscatter1/crater_landscape_ok
hou_node = hou_parent.createNode("heightfield_layer", "crater_landscape_ok", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(0.428181, -6.92431))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/lh_craterscatter1/crater_landscape_ok/mode parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/crater_landscape_ok")
hou_parm = hou_node.parm("mode")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("subtract")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/crater_landscape_ok/blend parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/crater_landscape_ok")
hou_parm = hou_node.parm("blend")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.5)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/crater_landscape_ok/layer parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/crater_landscape_ok")
hou_parm = hou_node.parm("layer")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("height")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/crater_landscape_ok/folder2 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/crater_landscape_ok")
hou_parm = hou_node.parm("folder2")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/crater_landscape_ok/masklayer parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/crater_landscape_ok")
hou_parm = hou_node.parm("masklayer")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("mask")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/crater_landscape_ok/maskweight parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/crater_landscape_ok")
hou_parm = hou_node.parm("maskweight")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/crater_landscape_ok/invertmask parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/crater_landscape_ok")
hou_parm = hou_node.parm("invertmask")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/crater_landscape_ok/folder0 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/crater_landscape_ok")
hou_parm = hou_node.parm("folder0")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/crater_landscape_ok/base_offset parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/crater_landscape_ok")
hou_parm = hou_node.parm("base_offset")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/crater_landscape_ok/base_scale parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/crater_landscape_ok")
hou_parm = hou_node.parm("base_scale")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/crater_landscape_ok/layer_offset parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/crater_landscape_ok")
hou_parm = hou_node.parm("layer_offset")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/crater_landscape_ok/layer_scale parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/crater_landscape_ok")
hou_parm = hou_node.parm("layer_scale")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/crater_landscape_ok/final_offset parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/crater_landscape_ok")
hou_parm = hou_node.parm("final_offset")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/crater_landscape_ok/final_scale parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/crater_landscape_ok")
hou_parm = hou_node.parm("final_scale")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/crater_landscape_ok/folder1 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/crater_landscape_ok")
hou_parm = hou_node.parm("folder1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/crater_landscape_ok/doclampmin parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/crater_landscape_ok")
hou_parm = hou_node.parm("doclampmin")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/crater_landscape_ok/clampmin parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/crater_landscape_ok")
hou_parm = hou_node.parm("clampmin")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/crater_landscape_ok/doclampmax parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/crater_landscape_ok")
hou_parm = hou_node.parm("doclampmax")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/crater_landscape_ok/clampmax parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/crater_landscape_ok")
hou_parm = hou_node.parm("clampmax")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/geo1/lh_craterscatter1/distort_crater
hou_node = hou_parent.createNode("heightfield_distort", "distort_crater", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(1.05664, -4.84651))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/lh_craterscatter1/distort_crater/layer parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/distort_crater")
hou_parm = hou_node.parm("layer")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("height")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/distort_crater/masklayer parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/distort_crater")
hou_parm = hou_node.parm("masklayer")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("mask")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/distort_crater/noisetype parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/distort_crater")
hou_parm = hou_node.parm("noisetype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("curl")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/distort_crater/amp parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/distort_crater")
hou_parm = hou_node.parm("amp")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)

# Code for first keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(10)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("ch(\"../distort\")", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for last keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(10)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("ch(\"../distort\")", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(10)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("ch(\"../distort\")", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(10)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("ch(\"../distort\")", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)


# Code for /obj/geo1/lh_craterscatter1/distort_crater/element_size parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/distort_crater")
hou_parm = hou_node.parm("element_size")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(100)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/distort_crater/element_scale parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/distort_crater")
hou_parm_tuple = hou_node.parmTuple("element_scale")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((1, 1, 1))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/lh_craterscatter1/distort_crater/offset parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/distort_crater")
hou_parm_tuple = hou_node.parmTuple("offset")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/lh_craterscatter1/distort_crater/rough parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/distort_crater")
hou_parm = hou_node.parm("rough")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.5)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/distort_crater/maxoctave parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/distort_crater")
hou_parm = hou_node.parm("maxoctave")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(8)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/distort_crater/steps parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/distort_crater")
hou_parm = hou_node.parm("steps")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/geo1/lh_craterscatter1/resample
hou_node = hou_parent.createNode("heightfield_resample", "resample", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(2.56493, -8.10281))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/lh_craterscatter1/resample/fixedresample parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/resample")
hou_parm = hou_node.parm("fixedresample")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/resample/resscale parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/resample")
hou_parm = hou_node.parm("resscale")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.5)
hou_parm.setAutoscope(False)

# Code for first keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(0.5)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("ch(\"../resample_scale\")", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for last keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(0.5)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("ch(\"../resample_scale\")", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(0.5)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("ch(\"../resample_scale\")", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(0.5)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("ch(\"../resample_scale\")", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)


# Code for /obj/geo1/lh_craterscatter1/resample/divisionmode parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/resample")
hou_parm = hou_node.parm("divisionmode")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("size")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/resample/gridspacing parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/resample")
hou_parm = hou_node.parm("gridspacing")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(4)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/resample/gridsamples parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/resample")
hou_parm = hou_node.parm("gridsamples")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(256)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/resample/filter parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/resample")
hou_parm = hou_node.parm("filter")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("gauss")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/resample/filterscale parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/resample")
hou_parm = hou_node.parm("filterscale")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1.5)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/geo1/lh_craterscatter1/set_mask
hou_node = hou_parent.createNode("volumewrangle", "set_mask", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(3.50647, -5.93821))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/lh_craterscatter1/set_mask/folder01 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/set_mask")
hou_parm = hou_node.parm("folder01")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/set_mask/group parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/set_mask")
hou_parm = hou_node.parm("group")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/set_mask/bindeach parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/set_mask")
hou_parm = hou_node.parm("bindeach")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/set_mask/snippet parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/set_mask")
hou_parm = hou_node.parm("snippet")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("@mask = @height;")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/set_mask/exportlist parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/set_mask")
hou_parm = hou_node.parm("exportlist")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("mask")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/set_mask/vex_strict parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/set_mask")
hou_parm = hou_node.parm("vex_strict")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/set_mask/autobind parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/set_mask")
hou_parm = hou_node.parm("autobind")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/set_mask/bindings parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/set_mask")
hou_parm = hou_node.parm("bindings")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/set_mask/vex_geometrygenerator parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/set_mask")
hou_parm = hou_node.parm("vex_geometrygenerator")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/set_mask/vdb_signedflood parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/set_mask")
hou_parm = hou_node.parm("vdb_signedflood")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/set_mask/vex_cwdpath parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/set_mask")
hou_parm = hou_node.parm("vex_cwdpath")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(".")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/set_mask/vex_outputmask parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/set_mask")
hou_parm = hou_node.parm("vex_outputmask")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/set_mask/vex_precision parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/set_mask")
hou_parm = hou_node.parm("vex_precision")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("auto")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/geo1/lh_craterscatter1/make_mask
hou_node = hou_parent.createNode("heightfield_layer", "make_mask", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(3.50947, -9.14281))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/lh_craterscatter1/make_mask/mode parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_mask")
hou_parm = hou_node.parm("mode")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("replace")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_mask/blend parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_mask")
hou_parm = hou_node.parm("blend")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.5)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_mask/layer parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_mask")
hou_parm = hou_node.parm("layer")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("mask")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_mask/folder2 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_mask")
hou_parm = hou_node.parm("folder2")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_mask/masklayer parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_mask")
hou_parm = hou_node.parm("masklayer")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("mask")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_mask/maskweight parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_mask")
hou_parm = hou_node.parm("maskweight")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_mask/invertmask parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_mask")
hou_parm = hou_node.parm("invertmask")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_mask/folder0 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_mask")
hou_parm = hou_node.parm("folder0")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_mask/base_offset parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_mask")
hou_parm = hou_node.parm("base_offset")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_mask/base_scale parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_mask")
hou_parm = hou_node.parm("base_scale")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_mask/layer_offset parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_mask")
hou_parm = hou_node.parm("layer_offset")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_mask/layer_scale parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_mask")
hou_parm = hou_node.parm("layer_scale")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_mask/final_offset parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_mask")
hou_parm = hou_node.parm("final_offset")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_mask/final_scale parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_mask")
hou_parm = hou_node.parm("final_scale")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_mask/folder1 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_mask")
hou_parm = hou_node.parm("folder1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_mask/doclampmin parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_mask")
hou_parm = hou_node.parm("doclampmin")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_mask/clampmin parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_mask")
hou_parm = hou_node.parm("clampmin")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_mask/doclampmax parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_mask")
hou_parm = hou_node.parm("doclampmax")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_mask/clampmax parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_mask")
hou_parm = hou_node.parm("clampmax")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/geo1/lh_craterscatter1/convert_mesh
hou_node = hou_parent.createNode("convertheightfield", "convert_mesh", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(3.50947, -10.7111))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/lh_craterscatter1/convert_mesh/layer parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/convert_mesh")
hou_parm = hou_node.parm("layer")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("height")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/convert_mesh/conversion parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/convert_mesh")
hou_parm = hou_node.parm("conversion")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("poly")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/convert_mesh/surftype parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/convert_mesh")
hou_parm = hou_node.parm("surftype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("quads")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/convert_mesh/lod parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/convert_mesh")
hou_parm = hou_node.parm("lod")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/convert_mesh/bakecd parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/convert_mesh")
hou_parm = hou_node.parm("bakecd")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/convert_mesh/folder0 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/convert_mesh")
hou_parm = hou_node.parm("folder0")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/convert_mesh/doextrude parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/convert_mesh")
hou_parm = hou_node.parm("doextrude")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/convert_mesh/depth parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/convert_mesh")
hou_parm = hou_node.parm("depth")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(-1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/convert_mesh/basenormal parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/convert_mesh")
hou_parm_tuple = hou_node.parmTuple("basenormal")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 1, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/lh_craterscatter1/convert_mesh/flat parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/convert_mesh")
hou_parm = hou_node.parm("flat")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/geo1/lh_craterscatter1/separate_mask
hou_node = hou_parent.createNode("volumewrangle", "separate_mask", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(3.50647, -9.98283))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/lh_craterscatter1/separate_mask/folder01 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/separate_mask")
hou_parm = hou_node.parm("folder01")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/separate_mask/group parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/separate_mask")
hou_parm = hou_node.parm("group")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/separate_mask/bindeach parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/separate_mask")
hou_parm = hou_node.parm("bindeach")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/separate_mask/snippet parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/separate_mask")
hou_parm = hou_node.parm("snippet")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("@height = @mask*100;")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/separate_mask/exportlist parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/separate_mask")
hou_parm = hou_node.parm("exportlist")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("height")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/separate_mask/vex_strict parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/separate_mask")
hou_parm = hou_node.parm("vex_strict")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/separate_mask/autobind parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/separate_mask")
hou_parm = hou_node.parm("autobind")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/separate_mask/bindings parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/separate_mask")
hou_parm = hou_node.parm("bindings")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/separate_mask/vex_geometrygenerator parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/separate_mask")
hou_parm = hou_node.parm("vex_geometrygenerator")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/separate_mask/vdb_signedflood parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/separate_mask")
hou_parm = hou_node.parm("vdb_signedflood")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/separate_mask/vex_cwdpath parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/separate_mask")
hou_parm = hou_node.parm("vex_cwdpath")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(".")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/separate_mask/vex_outputmask parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/separate_mask")
hou_parm = hou_node.parm("vex_outputmask")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/separate_mask/vex_precision parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/separate_mask")
hou_parm = hou_node.parm("vex_precision")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("auto")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/geo1/lh_craterscatter1/remove_no_mask
hou_node = hou_parent.createNode("attribwrangle", "remove_no_mask", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(3.50647, -11.467))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/lh_craterscatter1/remove_no_mask/folder01 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/remove_no_mask")
hou_parm = hou_node.parm("folder01")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/remove_no_mask/group parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/remove_no_mask")
hou_parm = hou_node.parm("group")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/remove_no_mask/grouptype parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/remove_no_mask")
hou_parm = hou_node.parm("grouptype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("guess")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/remove_no_mask/class parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/remove_no_mask")
hou_parm = hou_node.parm("class")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("primitive")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/remove_no_mask/vex_numcount parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/remove_no_mask")
hou_parm = hou_node.parm("vex_numcount")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(10)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/remove_no_mask/vex_threadjobsize parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/remove_no_mask")
hou_parm = hou_node.parm("vex_threadjobsize")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1024)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/remove_no_mask/snippet parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/remove_no_mask")
hou_parm = hou_node.parm("snippet")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("if(@P.y<50)\n    removeprim(0,@primnum,1);")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/remove_no_mask/exportlist parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/remove_no_mask")
hou_parm = hou_node.parm("exportlist")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/remove_no_mask/vex_strict parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/remove_no_mask")
hou_parm = hou_node.parm("vex_strict")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/remove_no_mask/autobind parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/remove_no_mask")
hou_parm = hou_node.parm("autobind")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/remove_no_mask/bindings parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/remove_no_mask")
hou_parm = hou_node.parm("bindings")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/remove_no_mask/groupautobind parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/remove_no_mask")
hou_parm = hou_node.parm("groupautobind")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/remove_no_mask/groupbindings parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/remove_no_mask")
hou_parm = hou_node.parm("groupbindings")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/remove_no_mask/vex_cwdpath parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/remove_no_mask")
hou_parm = hou_node.parm("vex_cwdpath")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(".")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/remove_no_mask/vex_outputmask parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/remove_no_mask")
hou_parm = hou_node.parm("vex_outputmask")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/remove_no_mask/vex_updatenmls parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/remove_no_mask")
hou_parm = hou_node.parm("vex_updatenmls")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/remove_no_mask/vex_matchattrib parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/remove_no_mask")
hou_parm = hou_node.parm("vex_matchattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("id")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/remove_no_mask/vex_inplace parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/remove_no_mask")
hou_parm = hou_node.parm("vex_inplace")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/remove_no_mask/vex_selectiongroup parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/remove_no_mask")
hou_parm = hou_node.parm("vex_selectiongroup")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/remove_no_mask/vex_precision parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/remove_no_mask")
hou_parm = hou_node.parm("vex_precision")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("auto")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/geo1/lh_craterscatter1/make_mesh
hou_node = hou_parent.createNode("python", "make_mesh", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(2.72969, -12.5832))
hou_node.bypass(False)
hou_node.setDisplayFlag(True)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(True)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/lh_craterscatter1/make_mesh/python parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_mesh")
hou_parm = hou_node.parm("python")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("\nhf = hou.pwd().inputs()[1].geometry().prims()[0];\n\ngeo = hou.pwd().geometry()\n\nfor p in geo.points():\n    pos = p.position();\n    p.setPosition([pos[0],hf.sample(pos),pos[2]])")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.589")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.589")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/lh_craterscatter1/is_make_mesh
hou_node = hou_parent.createNode("switch", "is_make_mesh", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(0.0914117, -22.9745))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/lh_craterscatter1/is_make_mesh/input parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/is_make_mesh")
hou_parm = hou_node.parm("input")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)

# Code for first keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(0)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("ch(\"../make_mesh\")", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for last keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(0)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("ch(\"../make_mesh\")", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(0)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("ch(\"../make_mesh\")", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(0)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("ch(\"../make_mesh\")", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.589")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.589")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/lh_craterscatter1/merge_land_mesh
hou_node = hou_parent.createNode("merge", "merge_land_mesh", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(1.05549, -21.648))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)
hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.589")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.589")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/lh_craterscatter1/raise_mesh
hou_node = hou_parent.createNode("xform", "raise_mesh", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(2.9593, -20.998))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/lh_craterscatter1/raise_mesh/group parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/raise_mesh")
hou_parm = hou_node.parm("group")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/raise_mesh/grouptype parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/raise_mesh")
hou_parm = hou_node.parm("grouptype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("guess")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/raise_mesh/xOrd parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/raise_mesh")
hou_parm = hou_node.parm("xOrd")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("srt")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/raise_mesh/rOrd parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/raise_mesh")
hou_parm = hou_node.parm("rOrd")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("xyz")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/raise_mesh/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/raise_mesh")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 2, 0))
hou_parm_tuple.setAutoscope((False, False, False))

# Code for first keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(2)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("ch(\"../mesh_raise\")", hou.exprLanguage.Hscript)
hou_parm_tuple[1].setKeyframe(hou_keyframe)

# Code for last keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(2)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("ch(\"../mesh_raise\")", hou.exprLanguage.Hscript)
hou_parm_tuple[1].setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(2)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("ch(\"../mesh_raise\")", hou.exprLanguage.Hscript)
hou_parm_tuple[1].setKeyframe(hou_keyframe)


# Code for /obj/geo1/lh_craterscatter1/raise_mesh/r parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/raise_mesh")
hou_parm_tuple = hou_node.parmTuple("r")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/lh_craterscatter1/raise_mesh/s parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/raise_mesh")
hou_parm_tuple = hou_node.parmTuple("s")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((1, 1, 1))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/lh_craterscatter1/raise_mesh/shear parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/raise_mesh")
hou_parm_tuple = hou_node.parmTuple("shear")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/lh_craterscatter1/raise_mesh/scale parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/raise_mesh")
hou_parm = hou_node.parm("scale")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/raise_mesh/parmgroup_pivotxform parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/raise_mesh")
hou_parm = hou_node.parm("parmgroup_pivotxform")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/raise_mesh/p parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/raise_mesh")
hou_parm_tuple = hou_node.parmTuple("p")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/lh_craterscatter1/raise_mesh/pr parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/raise_mesh")
hou_parm_tuple = hou_node.parmTuple("pr")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/lh_craterscatter1/raise_mesh/parmgroup_prexform parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/raise_mesh")
hou_parm = hou_node.parm("parmgroup_prexform")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/raise_mesh/prexform_xOrd parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/raise_mesh")
hou_parm = hou_node.parm("prexform_xOrd")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("srt")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/raise_mesh/prexform_rOrd parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/raise_mesh")
hou_parm = hou_node.parm("prexform_rOrd")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("xyz")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/raise_mesh/prexform_t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/raise_mesh")
hou_parm_tuple = hou_node.parmTuple("prexform_t")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/lh_craterscatter1/raise_mesh/prexform_r parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/raise_mesh")
hou_parm_tuple = hou_node.parmTuple("prexform_r")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/lh_craterscatter1/raise_mesh/prexform_s parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/raise_mesh")
hou_parm_tuple = hou_node.parmTuple("prexform_s")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((1, 1, 1))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/lh_craterscatter1/raise_mesh/prexform_shear parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/raise_mesh")
hou_parm_tuple = hou_node.parmTuple("prexform_shear")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/lh_craterscatter1/raise_mesh/movecentroid parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/raise_mesh")
hou_parm = hou_node.parm("movecentroid")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("0")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/raise_mesh/attribs parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/raise_mesh")
hou_parm = hou_node.parm("attribs")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/raise_mesh/updatenmls parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/raise_mesh")
hou_parm = hou_node.parm("updatenmls")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/raise_mesh/updateaffectednmls parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/raise_mesh")
hou_parm = hou_node.parm("updateaffectednmls")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/raise_mesh/vlength parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/raise_mesh")
hou_parm = hou_node.parm("vlength")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/raise_mesh/invertxform parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/raise_mesh")
hou_parm = hou_node.parm("invertxform")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/raise_mesh/addattrib parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/raise_mesh")
hou_parm = hou_node.parm("addattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/raise_mesh/outputattrib parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/raise_mesh")
hou_parm = hou_node.parm("outputattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("xform")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/raise_mesh/outputmerge parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/raise_mesh")
hou_parm = hou_node.parm("outputmerge")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("post")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.589")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.589")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/lh_craterscatter1/polyreduce
hou_node = hou_parent.createNode("polyreduce::2.0", "polyreduce", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(2.9593, -14.5832))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/lh_craterscatter1/polyreduce/group parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("group")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/polyreduce/reductiontarget parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("reductiontarget")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/polyreduce/target parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("target")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("poly_percent")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/polyreduce/percentage parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("percentage")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(100)
hou_parm.setAutoscope(False)

# Code for first keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(10)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("ch(\"../polyreduce_percent\")*100", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for last keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(10)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("ch(\"../polyreduce_percent\")*100", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(10)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("ch(\"../polyreduce_percent\")*100", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(10)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("ch(\"../polyreduce_percent\")*100", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)


# Code for /obj/geo1/lh_craterscatter1/polyreduce/finalcount parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("finalcount")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1000)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/polyreduce/reducepassedtarget parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("reducepassedtarget")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/polyreduce/qualitytolerance parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("qualitytolerance")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1.0000000000000001e-05)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/polyreduce/outputgeo parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("outputgeo")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/polyreduce/originalpoints parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("originalpoints")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/polyreduce/preservequads parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("preservequads")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/polyreduce/equalizelengths parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("equalizelengths")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1e-10)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/polyreduce/stiffen parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("stiffen")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/polyreduce/boundaryweight parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("boundaryweight")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/polyreduce/vattribseamweight parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("vattribseamweight")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/polyreduce/seamattribs parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("seamattribs")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("* ^N")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/polyreduce/features parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("features")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/polyreduce/hardfeaturepoints parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("hardfeaturepoints")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/polyreduce/hardfeatureedges parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("hardfeatureedges")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/polyreduce/softfeaturepoints parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("softfeaturepoints")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/polyreduce/softfeaturepointweight parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("softfeaturepointweight")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/polyreduce/softfeatureedges parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("softfeatureedges")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/polyreduce/softfeatureedgeweight parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("softfeatureedgeweight")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/polyreduce/retentioncontrol parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("retentioncontrol")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/polyreduce/useretainattrib parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("useretainattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/polyreduce/retainattrib parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("retainattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("retention")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/polyreduce/retainattribweight parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("retainattribweight")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/polyreduce/viewbasedretentioncontrol parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("viewbasedretentioncontrol")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/polyreduce/silhouetteweight parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("silhouetteweight")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/polyreduce/usesilhouettefalloff parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("usesilhouettefalloff")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/polyreduce/silhouettefalloffdist parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("silhouettefalloffdist")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/polyreduce/frontfacingweight parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("frontfacingweight")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/polyreduce/usefrontfacingfalloff parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("usefrontfacingfalloff")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/polyreduce/frontfacingfalloffdist parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("frontfacingfalloffdist")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/polyreduce/experimental parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("experimental")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/polyreduce/decimationcontrol parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("decimationcontrol")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/polyreduce/controlattribs parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/polyreduce")
hou_parm = hou_node.parm("controlattribs")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.589")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.589")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/lh_craterscatter1/avoid_out
hou_node = hou_parent.createNode("heightfield_project", "avoid_out", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(1.28625, -16.6396))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/lh_craterscatter1/avoid_out/layer parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/avoid_out")
hou_parm = hou_node.parm("layer")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("height")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/avoid_out/maskmode parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/avoid_out")
hou_parm = hou_node.parm("maskmode")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/avoid_out/maskdir parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/avoid_out")
hou_parm = hou_node.parm("maskdir")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("both")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/avoid_out/heightlayer parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/avoid_out")
hou_parm = hou_node.parm("heightlayer")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("height")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/avoid_out/maskdensity parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/avoid_out")
hou_parm = hou_node.parm("maskdensity")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/avoid_out/maskinvert parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/avoid_out")
hou_parm = hou_node.parm("maskinvert")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/avoid_out/hitfarthest parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/avoid_out")
hou_parm = hou_node.parm("hitfarthest")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/avoid_out/combine parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/avoid_out")
hou_parm = hou_node.parm("combine")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("min")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/avoid_out/maxraydist parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/avoid_out")
hou_parm = hou_node.parm("maxraydist")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1000)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/avoid_out/dojitter parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/avoid_out")
hou_parm = hou_node.parm("dojitter")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/avoid_out/sample parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/avoid_out")
hou_parm = hou_node.parm("sample")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(3)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/avoid_out/jitter parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/avoid_out")
hou_parm = hou_node.parm("jitter")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.25)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/avoid_out/jittercombine parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/avoid_out")
hou_parm = hou_node.parm("jittercombine")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("median")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/avoid_out/seed parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/avoid_out")
hou_parm = hou_node.parm("seed")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/geo1/lh_craterscatter1/create_edge
hou_node = hou_parent.createNode("groupcreate", "create_edge", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(2.9593, -15.7665))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(True)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/lh_craterscatter1/create_edge/groupname parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("groupname")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("edge")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/create_edge/grouptype parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("grouptype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("edge")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/create_edge/mergeop parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("mergeop")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("replace")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/create_edge/folder0 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("folder0")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/create_edge/groupbase parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("groupbase")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/create_edge/basegroup parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("basegroup")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/create_edge/ordered parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("ordered")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/create_edge/geotype parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("geotype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("all")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/create_edge/switcher3 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("switcher3")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/create_edge/groupbounding parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("groupbounding")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/create_edge/boundtype parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("boundtype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("usebbox")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/create_edge/size parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm_tuple = hou_node.parmTuple("size")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((1, 1, 1))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/lh_craterscatter1/create_edge/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/lh_craterscatter1/create_edge/includenotwhollycontained parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("includenotwhollycontained")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/create_edge/iso parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("iso")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/create_edge/invertvolume parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("invertvolume")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/create_edge/switcher4 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("switcher4")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/create_edge/groupnormal parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("groupnormal")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/create_edge/camerapath parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("camerapath")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/create_edge/nonplanar parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("nonplanar")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/create_edge/nonplanartol parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("nonplanartol")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.001)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/create_edge/dir parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm_tuple = hou_node.parmTuple("dir")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 1))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/lh_craterscatter1/create_edge/angle parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("angle")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(180)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/create_edge/switcher5 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("switcher5")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/create_edge/groupedges parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("groupedges")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/create_edge/dominedgeangle parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("dominedgeangle")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/create_edge/minedgeangle parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("minedgeangle")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(20)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/create_edge/domaxedgeangle parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("domaxedgeangle")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/create_edge/maxedgeangle parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("maxedgeangle")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(20)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/create_edge/edgeanglebetweenedges parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("edgeanglebetweenedges")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/create_edge/dominedgelen parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("dominedgelen")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/create_edge/minedgelen parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("minedgelen")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/create_edge/domaxedgelen parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("domaxedgelen")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/create_edge/maxedgelen parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("maxedgelen")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/create_edge/dodepth parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("dodepth")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/create_edge/edgestep parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("edgestep")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/create_edge/edgeptgrp parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("edgeptgrp")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("0")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/create_edge/unshared parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("unshared")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/create_edge/boundarygroups parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/create_edge")
hou_parm = hou_node.parm("boundarygroups")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.589")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.589")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/lh_craterscatter1/make_edge_vertex_color_black
hou_node = hou_parent.createNode("attribwrangle", "make_edge_vertex_color_black", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(2.9563, -16.7774))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/lh_craterscatter1/make_edge_vertex_color_black/folder01 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_edge_vertex_color_black")
hou_parm = hou_node.parm("folder01")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_edge_vertex_color_black/group parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_edge_vertex_color_black")
hou_parm = hou_node.parm("group")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("edge")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_edge_vertex_color_black/grouptype parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_edge_vertex_color_black")
hou_parm = hou_node.parm("grouptype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("guess")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_edge_vertex_color_black/class parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_edge_vertex_color_black")
hou_parm = hou_node.parm("class")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("point")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_edge_vertex_color_black/vex_numcount parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_edge_vertex_color_black")
hou_parm = hou_node.parm("vex_numcount")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(10)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_edge_vertex_color_black/vex_threadjobsize parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_edge_vertex_color_black")
hou_parm = hou_node.parm("vex_threadjobsize")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1024)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_edge_vertex_color_black/snippet parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_edge_vertex_color_black")
hou_parm = hou_node.parm("snippet")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("@Cd = set(0,0,0);")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_edge_vertex_color_black/exportlist parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_edge_vertex_color_black")
hou_parm = hou_node.parm("exportlist")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_edge_vertex_color_black/vex_strict parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_edge_vertex_color_black")
hou_parm = hou_node.parm("vex_strict")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_edge_vertex_color_black/autobind parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_edge_vertex_color_black")
hou_parm = hou_node.parm("autobind")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_edge_vertex_color_black/bindings parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_edge_vertex_color_black")
hou_parm = hou_node.parm("bindings")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_edge_vertex_color_black/groupautobind parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_edge_vertex_color_black")
hou_parm = hou_node.parm("groupautobind")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_edge_vertex_color_black/groupbindings parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_edge_vertex_color_black")
hou_parm = hou_node.parm("groupbindings")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_edge_vertex_color_black/vex_cwdpath parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_edge_vertex_color_black")
hou_parm = hou_node.parm("vex_cwdpath")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(".")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_edge_vertex_color_black/vex_outputmask parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_edge_vertex_color_black")
hou_parm = hou_node.parm("vex_outputmask")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_edge_vertex_color_black/vex_updatenmls parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_edge_vertex_color_black")
hou_parm = hou_node.parm("vex_updatenmls")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_edge_vertex_color_black/vex_matchattrib parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_edge_vertex_color_black")
hou_parm = hou_node.parm("vex_matchattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("id")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_edge_vertex_color_black/vex_inplace parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_edge_vertex_color_black")
hou_parm = hou_node.parm("vex_inplace")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_edge_vertex_color_black/vex_selectiongroup parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_edge_vertex_color_black")
hou_parm = hou_node.parm("vex_selectiongroup")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_edge_vertex_color_black/vex_precision parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_edge_vertex_color_black")
hou_parm = hou_node.parm("vex_precision")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("auto")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/geo1/lh_craterscatter1/make_vertex_normal
hou_node = hou_parent.createNode("normal", "make_vertex_normal", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(2.9593, -17.8153))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/lh_craterscatter1/make_vertex_normal/group parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_vertex_normal")
hou_parm = hou_node.parm("group")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_vertex_normal/grouptype parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_vertex_normal")
hou_parm = hou_node.parm("grouptype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("guess")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_vertex_normal/overridenormal parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_vertex_normal")
hou_parm = hou_node.parm("overridenormal")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_vertex_normal/normalattrib parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_vertex_normal")
hou_parm = hou_node.parm("normalattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("N")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_vertex_normal/construct parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_vertex_normal")
hou_parm = hou_node.parm("construct")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_vertex_normal/docompute parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_vertex_normal")
hou_parm = hou_node.parm("docompute")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_vertex_normal/type parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_vertex_normal")
hou_parm = hou_node.parm("type")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("typepoint")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_vertex_normal/cuspangle parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_vertex_normal")
hou_parm = hou_node.parm("cuspangle")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(60)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_vertex_normal/method parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_vertex_normal")
hou_parm = hou_node.parm("method")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_vertex_normal/origifzero parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_vertex_normal")
hou_parm = hou_node.parm("origifzero")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_vertex_normal/modify parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_vertex_normal")
hou_parm = hou_node.parm("modify")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_vertex_normal/normalize parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_vertex_normal")
hou_parm = hou_node.parm("normalize")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/make_vertex_normal/reverse parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/make_vertex_normal")
hou_parm = hou_node.parm("reverse")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.589")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.589")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/lh_craterscatter1/set_uv
hou_node = hou_parent.createNode("attribwrangle", "set_uv", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(2.9563, -18.9601))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/lh_craterscatter1/set_uv/folder01 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/set_uv")
hou_parm = hou_node.parm("folder01")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/set_uv/group parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/set_uv")
hou_parm = hou_node.parm("group")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/set_uv/grouptype parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/set_uv")
hou_parm = hou_node.parm("grouptype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("guess")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/set_uv/class parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/set_uv")
hou_parm = hou_node.parm("class")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("point")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/set_uv/vex_numcount parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/set_uv")
hou_parm = hou_node.parm("vex_numcount")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(10)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/set_uv/vex_threadjobsize parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/set_uv")
hou_parm = hou_node.parm("vex_threadjobsize")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1024)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/set_uv/snippet parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/set_uv")
hou_parm = hou_node.parm("snippet")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("@uv = set(@P.x,@P.z);")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/set_uv/exportlist parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/set_uv")
hou_parm = hou_node.parm("exportlist")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/set_uv/vex_strict parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/set_uv")
hou_parm = hou_node.parm("vex_strict")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/set_uv/autobind parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/set_uv")
hou_parm = hou_node.parm("autobind")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/set_uv/bindings parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/set_uv")
hou_parm = hou_node.parm("bindings")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/set_uv/groupautobind parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/set_uv")
hou_parm = hou_node.parm("groupautobind")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/set_uv/groupbindings parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/set_uv")
hou_parm = hou_node.parm("groupbindings")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/set_uv/vex_cwdpath parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/set_uv")
hou_parm = hou_node.parm("vex_cwdpath")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(".")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/set_uv/vex_outputmask parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/set_uv")
hou_parm = hou_node.parm("vex_outputmask")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/set_uv/vex_updatenmls parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/set_uv")
hou_parm = hou_node.parm("vex_updatenmls")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/set_uv/vex_matchattrib parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/set_uv")
hou_parm = hou_node.parm("vex_matchattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("id")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/set_uv/vex_inplace parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/set_uv")
hou_parm = hou_node.parm("vex_inplace")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/set_uv/vex_selectiongroup parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/set_uv")
hou_parm = hou_node.parm("vex_selectiongroup")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/set_uv/vex_precision parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/set_uv")
hou_parm = hou_node.parm("vex_precision")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("auto")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/geo1/lh_craterscatter1/unreal_material
hou_node = hou_parent.createNode("attribcreate::2.0", "unreal_material", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(2.95585, -19.998))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/lh_craterscatter1/unreal_material/group parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/unreal_material")
hou_parm = hou_node.parm("group")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/unreal_material/grouptype parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/unreal_material")
hou_parm = hou_node.parm("grouptype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("guess")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/unreal_material/encodenames parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/unreal_material")
hou_parm = hou_node.parm("encodenames")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/unreal_material/numattr parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/unreal_material")
hou_parm = hou_node.parm("numattr")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/unreal_material/enable1 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/unreal_material")
hou_parm = hou_node.parm("enable1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/unreal_material/name1 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/unreal_material")
hou_parm = hou_node.parm("name1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("unreal_material")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/unreal_material/existing1 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/unreal_material")
hou_parm = hou_node.parm("existing1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("better")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/unreal_material/createvarmap1 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/unreal_material")
hou_parm = hou_node.parm("createvarmap1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/unreal_material/varname1 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/unreal_material")
hou_parm = hou_node.parm("varname1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/unreal_material/class1 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/unreal_material")
hou_parm = hou_node.parm("class1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("primitive")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/unreal_material/savetoinfo1 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/unreal_material")
hou_parm = hou_node.parm("savetoinfo1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/unreal_material/type1 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/unreal_material")
hou_parm = hou_node.parm("type1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("index")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/unreal_material/typeinfo1 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/unreal_material")
hou_parm = hou_node.parm("typeinfo1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("guess")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/unreal_material/precision1 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/unreal_material")
hou_parm = hou_node.parm("precision1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("32")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/unreal_material/size1 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/unreal_material")
hou_parm = hou_node.parm("size1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/unreal_material/default1v parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/unreal_material")
hou_parm_tuple = hou_node.parmTuple("default1v")
hou_parm_tuple.lock((False, False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False, False))


# Code for /obj/geo1/lh_craterscatter1/unreal_material/writevalues1 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/unreal_material")
hou_parm = hou_node.parm("writevalues1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/unreal_material/uselocal1 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/unreal_material")
hou_parm = hou_node.parm("uselocal1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/unreal_material/value1v parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/unreal_material")
hou_parm_tuple = hou_node.parmTuple("value1v")
hou_parm_tuple.lock((False, False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False, False))


# Code for /obj/geo1/lh_craterscatter1/unreal_material/string1 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/unreal_material")
hou_parm = hou_node.parm("string1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("`chs(\"../mesh_material\")`")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.589")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.589")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/lh_craterscatter1/meteorite
hou_node = hou_parent.createNode("sphere", "meteorite", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(6.81103, 3.22409))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/lh_craterscatter1/meteorite/type parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/meteorite")
hou_parm = hou_node.parm("type")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("prim")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/meteorite/surftype parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/meteorite")
hou_parm = hou_node.parm("surftype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("quads")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/meteorite/rad parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/meteorite")
hou_parm_tuple = hou_node.parmTuple("rad")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((1, 1, 1))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/lh_craterscatter1/meteorite/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/meteorite")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/lh_craterscatter1/meteorite/r parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/meteorite")
hou_parm_tuple = hou_node.parmTuple("r")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/geo1/lh_craterscatter1/meteorite/scale parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/meteorite")
hou_parm = hou_node.parm("scale")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/meteorite/orient parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/meteorite")
hou_parm = hou_node.parm("orient")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("y")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/meteorite/freq parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/meteorite")
hou_parm = hou_node.parm("freq")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(2)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/meteorite/rows parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/meteorite")
hou_parm = hou_node.parm("rows")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(13)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/meteorite/cols parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/meteorite")
hou_parm = hou_node.parm("cols")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(24)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/meteorite/orderu parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/meteorite")
hou_parm = hou_node.parm("orderu")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(4)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/meteorite/orderv parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/meteorite")
hou_parm = hou_node.parm("orderv")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(4)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/meteorite/imperfect parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/meteorite")
hou_parm = hou_node.parm("imperfect")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/meteorite/upole parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/meteorite")
hou_parm = hou_node.parm("upole")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/meteorite/accurate parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/meteorite")
hou_parm = hou_node.parm("accurate")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/meteorite/triangularpoles parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/meteorite")
hou_parm = hou_node.parm("triangularpoles")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.589")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.589")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/lh_craterscatter1/curve_input
hou_node = hou_parent.createNode("curve", "curve_input", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(3.80274, 3.75022))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(True)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/lh_craterscatter1/curve_input/type parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/curve_input")
hou_parm = hou_node.parm("type")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("nurbs")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/curve_input/method parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/curve_input")
hou_parm = hou_node.parm("method")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("breakpoints")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/curve_input/coords parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/curve_input")
hou_parm = hou_node.parm("coords")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("143.015,3.4187,-93.0784 141.752,-191.546,93.2571 -30.5598,-63.656,123.996 -103.914,116.999,-91.8599 ")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/curve_input/stdswitcher1 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/curve_input")
hou_parm = hou_node.parm("stdswitcher1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/curve_input/close parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/curve_input")
hou_parm = hou_node.parm("close")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/curve_input/reverse parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/curve_input")
hou_parm = hou_node.parm("reverse")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/curve_input/normalize parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/curve_input")
hou_parm = hou_node.parm("normalize")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/curve_input/order parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/curve_input")
hou_parm = hou_node.parm("order")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(4)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/curve_input/param parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/curve_input")
hou_parm = hou_node.parm("param")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("uniform")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/curve_input/tolerance parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/curve_input")
hou_parm = hou_node.parm("tolerance")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.01)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/curve_input/smooth parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/curve_input")
hou_parm = hou_node.parm("smooth")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/curve_input/csharp parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/curve_input")
hou_parm = hou_node.parm("csharp")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/curve_input/keepgeo parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/curve_input")
hou_parm = hou_node.parm("keepgeo")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.589")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.589")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1
hou_node = hou_parent.createNode("heightfield_scatter::2.0", "heightfield_scatter1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(3.80274, -1.41344))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/tag parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("tag")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("$OS")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/scattermethod parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("scattermethod")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("totalpointcount")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/folder1 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("folder1")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/layer parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("layer")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("mask")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/coverage parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("coverage")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.5)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/density parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("density")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.0001)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/totalpointcount parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("totalpointcount")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(3)
hou_parm.setAutoscope(False)

# Code for first keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(3)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("ch(\"../totalpointcount\")", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for last keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(3)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("ch(\"../totalpointcount\")", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(3)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("ch(\"../totalpointcount\")", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(3)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("ch(\"../totalpointcount\")", hou.exprLanguage.Hscript)
hou_parm.setKeyframe(hou_keyframe)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/sourcetag parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("sourcetag")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/perpointcount_method parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("perpointcount_method")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("poissondist")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/perpointcount_exactnumber parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("perpointcount_exactnumber")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(10)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/perpointcount_poissonrange parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm_tuple = hou_node.parmTuple("perpointcount_poissonrange")
hou_parm_tuple.lock((False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 20))
hou_parm_tuple.setAutoscope((False, False))


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/positioning_method parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("positioning_method")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("offset")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/positioning_origin parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm_tuple = hou_node.parmTuple("positioning_origin")
hou_parm_tuple.lock((False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 10))
hou_parm_tuple.setAutoscope((False, False))


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/positioning_offset parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm_tuple = hou_node.parmTuple("positioning_offset")
hou_parm_tuple.lock((False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0, 10))
hou_parm_tuple.setAutoscope((False, False))


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/positioning_ratio parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm_tuple = hou_node.parmTuple("positioning_ratio")
hou_parm_tuple.lock((False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((1, 2))
hou_parm_tuple.setAutoscope((False, False))


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/outerradius parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("outerradius")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/falloff parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("falloff")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.5)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/folder2 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("folder2")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/variability_method parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("variability_method")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("uniformdist")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/variability_exactscale parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("variability_exactscale")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/variability_unifromrange parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm_tuple = hou_node.parmTuple("variability_unifromrange")
hou_parm_tuple.lock((False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((5, 10))
hou_parm_tuple.setAutoscope((False, False))

# Code for first keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(5)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("ch(\"../variability_unifromrangemin\")", hou.exprLanguage.Hscript)
hou_parm_tuple[0].setKeyframe(hou_keyframe)

# Code for last keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(5)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("ch(\"../variability_unifromrangemin\")", hou.exprLanguage.Hscript)
hou_parm_tuple[0].setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(5)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("ch(\"../variability_unifromrangemin\")", hou.exprLanguage.Hscript)
hou_parm_tuple[0].setKeyframe(hou_keyframe)

# Code for first keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(10)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("ch(\"../variability_unifromrangemax\")", hou.exprLanguage.Hscript)
hou_parm_tuple[1].setKeyframe(hou_keyframe)

# Code for last keyframe.
# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(10)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("ch(\"../variability_unifromrangemax\")", hou.exprLanguage.Hscript)
hou_parm_tuple[1].setKeyframe(hou_keyframe)

# Code for keyframe.
hou_keyframe = hou.Keyframe()
hou_keyframe.setTime(0)
hou_keyframe.setValue(10)
hou_keyframe.useValue(False)
hou_keyframe.setSlope(0)
hou_keyframe.useSlope(False)
hou_keyframe.setAccel(0)
hou_keyframe.useAccel(False)
hou_keyframe.setExpression("ch(\"../variability_unifromrangemax\")", hou.exprLanguage.Hscript)
hou_parm_tuple[1].setKeyframe(hou_keyframe)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/variability_normalrange parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm_tuple = hou_node.parmTuple("variability_normalrange")
hou_parm_tuple.lock((False, False))
hou_parm_tuple.deleteAllKeyframes()
hou_parm_tuple.set((0.5, 1.5))
hou_parm_tuple.setAutoscope((False, False))


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/variability_normalspread parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("variability_normalspread")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.5)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/folder0 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("folder0")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/relax_points parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("relax_points")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/relax_selfoverlap parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("relax_selfoverlap")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/relax_avoidtag parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("relax_avoidtag")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/relax_maskcutoff parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("relax_maskcutoff")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.25)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/relax_iterations parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("relax_iterations")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(10)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/relax_removingrate parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("relax_removingrate")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.10000000000000001)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/relax_stepratio parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("relax_stepratio")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.75)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/relax_allowoutofbounds parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("relax_allowoutofbounds")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/relax_pointremovalmethod parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("relax_pointremovalmethod")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("remove")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/keepscatterpoints parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("keepscatterpoints")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/keepterrain parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("keepterrain")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/matchnormalterrain parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("matchnormalterrain")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/matchslopeterrain parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("matchslopeterrain")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/randomup parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("randomup")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/randomyaw parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("randomyaw")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/instancenewpoints parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("instancenewpoints")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/piecemode parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("piecemode")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("connectivity")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/pieceattrib parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("pieceattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("class")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/quant parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("quant")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.01)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/seed parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("seed")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(8853)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/useemergencylimit parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("useemergencylimit")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/heightfield_scatter1/emergencylimit parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/heightfield_scatter1")
hou_parm = hou_node.parm("emergencylimit")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1000000)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/geo1/lh_craterscatter1/project_mask
hou_node = hou_parent.createNode("heightfield_project", "project_mask", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(3.50947, -0.106026))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/lh_craterscatter1/project_mask/layer parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/project_mask")
hou_parm = hou_node.parm("layer")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("mask")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/project_mask/maskmode parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/project_mask")
hou_parm = hou_node.parm("maskmode")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/project_mask/maskdir parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/project_mask")
hou_parm = hou_node.parm("maskdir")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("both")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/project_mask/heightlayer parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/project_mask")
hou_parm = hou_node.parm("heightlayer")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("height")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/project_mask/maskdensity parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/project_mask")
hou_parm = hou_node.parm("maskdensity")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/project_mask/maskinvert parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/project_mask")
hou_parm = hou_node.parm("maskinvert")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/project_mask/hitfarthest parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/project_mask")
hou_parm = hou_node.parm("hitfarthest")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/project_mask/combine parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/project_mask")
hou_parm = hou_node.parm("combine")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("max")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/project_mask/maxraydist parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/project_mask")
hou_parm = hou_node.parm("maxraydist")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1000)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/project_mask/dojitter parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/project_mask")
hou_parm = hou_node.parm("dojitter")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/project_mask/sample parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/project_mask")
hou_parm = hou_node.parm("sample")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(3)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/project_mask/jitter parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/project_mask")
hou_parm = hou_node.parm("jitter")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0.25)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/project_mask/jittercombine parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/project_mask")
hou_parm = hou_node.parm("jittercombine")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("median")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/project_mask/seed parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/project_mask")
hou_parm = hou_node.parm("seed")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/geo1/lh_craterscatter1/pointwrangle1
hou_node = hou_parent.createNode("attribwrangle", "pointwrangle1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(3.79974, 2.53116))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/lh_craterscatter1/pointwrangle1/folder01 parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/pointwrangle1")
hou_parm = hou_node.parm("folder01")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/pointwrangle1/group parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/pointwrangle1")
hou_parm = hou_node.parm("group")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/pointwrangle1/grouptype parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/pointwrangle1")
hou_parm = hou_node.parm("grouptype")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("guess")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/pointwrangle1/class parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/pointwrangle1")
hou_parm = hou_node.parm("class")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("point")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/pointwrangle1/vex_numcount parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/pointwrangle1")
hou_parm = hou_node.parm("vex_numcount")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(10)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/pointwrangle1/vex_threadjobsize parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/pointwrangle1")
hou_parm = hou_node.parm("vex_threadjobsize")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1024)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/pointwrangle1/snippet parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/pointwrangle1")
hou_parm = hou_node.parm("snippet")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("@P.y = 1;\n")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/pointwrangle1/exportlist parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/pointwrangle1")
hou_parm = hou_node.parm("exportlist")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/pointwrangle1/vex_strict parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/pointwrangle1")
hou_parm = hou_node.parm("vex_strict")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/pointwrangle1/autobind parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/pointwrangle1")
hou_parm = hou_node.parm("autobind")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/pointwrangle1/bindings parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/pointwrangle1")
hou_parm = hou_node.parm("bindings")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/pointwrangle1/groupautobind parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/pointwrangle1")
hou_parm = hou_node.parm("groupautobind")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/pointwrangle1/groupbindings parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/pointwrangle1")
hou_parm = hou_node.parm("groupbindings")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/pointwrangle1/vex_cwdpath parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/pointwrangle1")
hou_parm = hou_node.parm("vex_cwdpath")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(".")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/pointwrangle1/vex_outputmask parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/pointwrangle1")
hou_parm = hou_node.parm("vex_outputmask")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/pointwrangle1/vex_updatenmls parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/pointwrangle1")
hou_parm = hou_node.parm("vex_updatenmls")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/pointwrangle1/vex_matchattrib parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/pointwrangle1")
hou_parm = hou_node.parm("vex_matchattrib")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("id")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/pointwrangle1/vex_inplace parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/pointwrangle1")
hou_parm = hou_node.parm("vex_inplace")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/pointwrangle1/vex_selectiongroup parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/pointwrangle1")
hou_parm = hou_node.parm("vex_selectiongroup")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/pointwrangle1/vex_precision parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/pointwrangle1")
hou_parm = hou_node.parm("vex_precision")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("auto")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/geo1/lh_craterscatter1/resample1
hou_node = hou_parent.createNode("resample", "resample1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(3.80274, 1.69185))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/geo1/lh_craterscatter1/resample1/group parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/resample1")
hou_parm = hou_node.parm("group")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/resample1/maintainprimorder parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/resample1")
hou_parm = hou_node.parm("maintainprimorder")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/resample1/lod parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/resample1")
hou_parm = hou_node.parm("lod")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/resample1/edge parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/resample1")
hou_parm = hou_node.parm("edge")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/resample1/method parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/resample1")
hou_parm = hou_node.parm("method")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("dist")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/resample1/measure parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/resample1")
hou_parm = hou_node.parm("measure")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("arc")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/resample1/dolength parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/resample1")
hou_parm = hou_node.parm("dolength")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/resample1/length parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/resample1")
hou_parm = hou_node.parm("length")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(20)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/resample1/dosegs parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/resample1")
hou_parm = hou_node.parm("dosegs")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/resample1/segs parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/resample1")
hou_parm = hou_node.parm("segs")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(10)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/resample1/useattribs parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/resample1")
hou_parm = hou_node.parm("useattribs")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/resample1/allequal parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/resample1")
hou_parm = hou_node.parm("allequal")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/resample1/last parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/resample1")
hou_parm = hou_node.parm("last")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/resample1/randomshift parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/resample1")
hou_parm = hou_node.parm("randomshift")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/resample1/onlypoints parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/resample1")
hou_parm = hou_node.parm("onlypoints")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/resample1/treatpolysas parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/resample1")
hou_parm = hou_node.parm("treatpolysas")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("straight")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/resample1/outputsubdpoly parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/resample1")
hou_parm = hou_node.parm("outputsubdpoly")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/resample1/doptdistattr parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/resample1")
hou_parm = hou_node.parm("doptdistattr")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/resample1/ptdistattr parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/resample1")
hou_parm = hou_node.parm("ptdistattr")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("ptdist")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/resample1/dotangentattr parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/resample1")
hou_parm = hou_node.parm("dotangentattr")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/resample1/tangentattr parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/resample1")
hou_parm = hou_node.parm("tangentattr")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("tangentu")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/resample1/docurveuattr parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/resample1")
hou_parm = hou_node.parm("docurveuattr")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/resample1/curveuattr parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/resample1")
hou_parm = hou_node.parm("curveuattr")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("curveu")
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/resample1/docurvenumattr parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/resample1")
hou_parm = hou_node.parm("docurvenumattr")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/geo1/lh_craterscatter1/resample1/curvenumattr parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/lh_craterscatter1/resample1")
hou_parm = hou_node.parm("curvenumattr")
hou_parm.lock(False)
hou_parm.deleteAllKeyframes()
hou_parm.set("curvenum")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "19.0.589")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("19.0.589")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code to establish connections for /obj/geo1/lh_craterscatter1/Start
hou_node = hou_parent.node("Start")
if len(hou_parent.indirectInputs()) > 0:
    hou_node.setInput(0, hou_parent.indirectInputs()[0])
# Code to establish connections for /obj/geo1/lh_craterscatter1/output
hou_node = hou_parent.node("output")
if hou_parent.node("is_make_mesh") is not None:
    hou_node.setInput(0, hou_parent.node("is_make_mesh"), 0)
# Code to establish connections for /obj/geo1/lh_craterscatter1/project_crater
hou_node = hou_parent.node("project_crater")
if hou_parent.node("Start") is not None:
    hou_node.setInput(0, hou_parent.node("Start"), 0)
if hou_parent.node("heightfield_scatter1") is not None:
    hou_node.setInput(1, hou_parent.node("heightfield_scatter1"), 0)
# Code to establish connections for /obj/geo1/lh_craterscatter1/substract_crater
hou_node = hou_parent.node("substract_crater")
if hou_parent.node("Start") is not None:
    hou_node.setInput(0, hou_parent.node("Start"), 0)
if hou_parent.node("project_crater") is not None:
    hou_node.setInput(1, hou_parent.node("project_crater"), 0)
# Code to establish connections for /obj/geo1/lh_craterscatter1/blur_crater
hou_node = hou_parent.node("blur_crater")
if hou_parent.node("substract_crater") is not None:
    hou_node.setInput(0, hou_parent.node("substract_crater"), 0)
# Code to establish connections for /obj/geo1/lh_craterscatter1/crater_landscape_ok
hou_node = hou_parent.node("crater_landscape_ok")
if hou_parent.node("Start") is not None:
    hou_node.setInput(0, hou_parent.node("Start"), 0)
if hou_parent.node("distort_crater") is not None:
    hou_node.setInput(1, hou_parent.node("distort_crater"), 0)
# Code to establish connections for /obj/geo1/lh_craterscatter1/distort_crater
hou_node = hou_parent.node("distort_crater")
if hou_parent.node("blur_crater") is not None:
    hou_node.setInput(0, hou_parent.node("blur_crater"), 0)
# Code to establish connections for /obj/geo1/lh_craterscatter1/resample
hou_node = hou_parent.node("resample")
if hou_parent.node("crater_landscape_ok") is not None:
    hou_node.setInput(0, hou_parent.node("crater_landscape_ok"), 0)
# Code to establish connections for /obj/geo1/lh_craterscatter1/set_mask
hou_node = hou_parent.node("set_mask")
if hou_parent.node("distort_crater") is not None:
    hou_node.setInput(0, hou_parent.node("distort_crater"), 0)
# Code to establish connections for /obj/geo1/lh_craterscatter1/make_mask
hou_node = hou_parent.node("make_mask")
if hou_parent.node("resample") is not None:
    hou_node.setInput(0, hou_parent.node("resample"), 0)
if hou_parent.node("set_mask") is not None:
    hou_node.setInput(1, hou_parent.node("set_mask"), 0)
# Code to establish connections for /obj/geo1/lh_craterscatter1/convert_mesh
hou_node = hou_parent.node("convert_mesh")
if hou_parent.node("separate_mask") is not None:
    hou_node.setInput(0, hou_parent.node("separate_mask"), 0)
# Code to establish connections for /obj/geo1/lh_craterscatter1/separate_mask
hou_node = hou_parent.node("separate_mask")
if hou_parent.node("make_mask") is not None:
    hou_node.setInput(0, hou_parent.node("make_mask"), 0)
# Code to establish connections for /obj/geo1/lh_craterscatter1/remove_no_mask
hou_node = hou_parent.node("remove_no_mask")
if hou_parent.node("convert_mesh") is not None:
    hou_node.setInput(0, hou_parent.node("convert_mesh"), 0)
# Code to establish connections for /obj/geo1/lh_craterscatter1/make_mesh
hou_node = hou_parent.node("make_mesh")
if hou_parent.node("remove_no_mask") is not None:
    hou_node.setInput(0, hou_parent.node("remove_no_mask"), 0)
if hou_parent.node("resample") is not None:
    hou_node.setInput(1, hou_parent.node("resample"), 0)
# Code to establish connections for /obj/geo1/lh_craterscatter1/is_make_mesh
hou_node = hou_parent.node("is_make_mesh")
if hou_parent.node("crater_landscape_ok") is not None:
    hou_node.setInput(0, hou_parent.node("crater_landscape_ok"), 0)
if hou_parent.node("merge_land_mesh") is not None:
    hou_node.setInput(1, hou_parent.node("merge_land_mesh"), 0)
# Code to establish connections for /obj/geo1/lh_craterscatter1/merge_land_mesh
hou_node = hou_parent.node("merge_land_mesh")
if hou_parent.node("avoid_out") is not None:
    hou_node.setInput(0, hou_parent.node("avoid_out"), 0)
if hou_parent.node("raise_mesh") is not None:
    hou_node.setInput(1, hou_parent.node("raise_mesh"), 0)
# Code to establish connections for /obj/geo1/lh_craterscatter1/raise_mesh
hou_node = hou_parent.node("raise_mesh")
if hou_parent.node("unreal_material") is not None:
    hou_node.setInput(0, hou_parent.node("unreal_material"), 0)
# Code to establish connections for /obj/geo1/lh_craterscatter1/polyreduce
hou_node = hou_parent.node("polyreduce")
if hou_parent.node("make_mesh") is not None:
    hou_node.setInput(0, hou_parent.node("make_mesh"), 0)
# Code to establish connections for /obj/geo1/lh_craterscatter1/avoid_out
hou_node = hou_parent.node("avoid_out")
if hou_parent.node("crater_landscape_ok") is not None:
    hou_node.setInput(0, hou_parent.node("crater_landscape_ok"), 0)
if hou_parent.node("polyreduce") is not None:
    hou_node.setInput(1, hou_parent.node("polyreduce"), 0)
# Code to establish connections for /obj/geo1/lh_craterscatter1/create_edge
hou_node = hou_parent.node("create_edge")
if hou_parent.node("polyreduce") is not None:
    hou_node.setInput(0, hou_parent.node("polyreduce"), 0)
# Code to establish connections for /obj/geo1/lh_craterscatter1/make_edge_vertex_color_black
hou_node = hou_parent.node("make_edge_vertex_color_black")
if hou_parent.node("create_edge") is not None:
    hou_node.setInput(0, hou_parent.node("create_edge"), 0)
# Code to establish connections for /obj/geo1/lh_craterscatter1/make_vertex_normal
hou_node = hou_parent.node("make_vertex_normal")
if hou_parent.node("make_edge_vertex_color_black") is not None:
    hou_node.setInput(0, hou_parent.node("make_edge_vertex_color_black"), 0)
# Code to establish connections for /obj/geo1/lh_craterscatter1/set_uv
hou_node = hou_parent.node("set_uv")
if hou_parent.node("make_vertex_normal") is not None:
    hou_node.setInput(0, hou_parent.node("make_vertex_normal"), 0)
# Code to establish connections for /obj/geo1/lh_craterscatter1/unreal_material
hou_node = hou_parent.node("unreal_material")
if hou_parent.node("set_uv") is not None:
    hou_node.setInput(0, hou_parent.node("set_uv"), 0)
# Code to establish connections for /obj/geo1/lh_craterscatter1/heightfield_scatter1
hou_node = hou_parent.node("heightfield_scatter1")
if hou_parent.node("project_mask") is not None:
    hou_node.setInput(0, hou_parent.node("project_mask"), 0)
if hou_parent.node("project_mask") is not None:
    hou_node.setInput(1, hou_parent.node("project_mask"), 0)
if hou_parent.node("meteorite") is not None:
    hou_node.setInput(2, hou_parent.node("meteorite"), 0)
# Code to establish connections for /obj/geo1/lh_craterscatter1/project_mask
hou_node = hou_parent.node("project_mask")
if hou_parent.node("Start") is not None:
    hou_node.setInput(0, hou_parent.node("Start"), 0)
if hou_parent.node("resample1") is not None:
    hou_node.setInput(1, hou_parent.node("resample1"), 0)
# Code to establish connections for /obj/geo1/lh_craterscatter1/pointwrangle1
hou_node = hou_parent.node("pointwrangle1")
if hou_parent.node("curve_input") is not None:
    hou_node.setInput(0, hou_parent.node("curve_input"), 0)
# Code to establish connections for /obj/geo1/lh_craterscatter1/resample1
hou_node = hou_parent.node("resample1")
if hou_parent.node("pointwrangle1") is not None:
    hou_node.setInput(0, hou_parent.node("pointwrangle1"), 0)

# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()


