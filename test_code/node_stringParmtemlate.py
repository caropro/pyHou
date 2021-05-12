# coding = utf-8
import hou

# Initialize parent node variable.
if locals().get("hou_parent") is None:
    hou_parent = hou.node("/obj/geo1")
# Code for /obj/geo1/Test
hou_node = hou_parent.createNode("null", "Test", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(-17.0728, -11.5878))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(True)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)
hou_parm_template_group = hou.ParmTemplateGroup()
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("copyinput", "Copy Input (Note: Input will be still cooked if disabled)",
                                           default_value=True)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.ToggleParmTemplate("cacheinput", "Cache Input", default_value=False)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("a", "a", 1, default_value=([0]), min=0, max=10, min_is_strict=False,
                                          max_is_strict=False, look=hou.parmLook.Regular,
                                          naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.StringParmTemplate("parm", "Label", 1, default_value=([""]),
                                           naming_scheme=hou.parmNamingScheme.Base1,
                                           string_type=hou.stringParmType.Regular, menu_items=(["ss"]),
                                           menu_labels=(["s"]), icon_names=([]), item_generator_script="",
                                           item_generator_script_language=hou.scriptLanguage.Python,
                                           menu_type=hou.menuType.Normal)
hou_parm_template_group.append(hou_parm_template)
hou_node.setParmTemplateGroup(hou_parm_template_group)
# Code for /obj/geo1/Test/copyinput parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/Test")
    hou_parm = hou_node.parm("copyinput")
    hou_parm.lock(False)
    hou_parm.set(1)
    hou_parm.setAutoscope(False)
# Code for /obj/geo1/Test/cacheinput parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/Test")
    hou_parm = hou_node.parm("cacheinput")
    hou_parm.lock(False)
    hou_parm.set(0)
    hou_parm.setAutoscope(False)
    # Code for /obj/geo1/Test/a parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/Test")
    hou_parm = hou_node.parm("a")
    hou_parm.lock(False)
    hou_parm.set(0)
    hou_parm.setAutoscope(False)
    # Code for /obj/geo1/Test/parm parm
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/geo1/Test")
    hou_parm = hou_node.parm("parm")
    hou_parm.lock(False)
    hou_parm.set("")
    hou_parm.setAutoscope(False)
    hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("17.0.506")
