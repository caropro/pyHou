#coding = utf-8
import hou

def run():
    node = hou.selectedNodes()[0]
    geo = node.geometry()
    primsAttr = [prim.attribValue("name") for prim in geo.prims()]
    primsAttr.remove("height")
    vex=""
    for layer in primsAttr:
        vex += "@{0} = clamp(@{0},0,1);\n".format(layer)

    parent_dir = node.parent()
    clamp_node = parent_dir.createNode("volumewrangle","LayerClamp")
    clamp_node.parm("snippet").set(vex)
    clamp_node.setInput(0, node, 0)
    hou.ui.displayMessage("Done!")
    return
