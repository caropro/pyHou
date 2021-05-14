# coding = utf-8
import hou
import os

# target_node = hou.ui.selectNode()
# target mtl node
target_node = hou.selectedNodes()[0]
target_nodename = target_node.name()
shaders = target_node.children()


shader_node = target_node.parent().createNode("matnet", "New_%s"%target_nodename)
shader_node.moveToGoodPosition()

for shd in shaders:
    shd_type = shd.type().name()
    # print(shd.type().name())
    if shd_type == "material":
        # shadernode
        new_mtl = shader_node.createNode("materialbuilder", shd.name())
        # create_shader
        psh = new_mtl.createNode("principledshader::2.0")
        psh.parm("rough").set(1)
        psh.parm("reflect").set(0)
        # create computelight
        cpl = new_mtl.createNode("computelighting::2.0")
        # connect cpl with psh
        cpl.setInput(0, psh, 2)
        # get output node
        output = new_mtl.node("surface_output")
        # connect shd with output
        output.setInput(0, cpl, 0)
        output.setInput(1, cpl, 1)
        output.setInput(4, cpl, 2)

        #get fbx shader
        fbx_shader = shd.glob("* ^suboutput")[0]
        print fbx_shader
        # get the texture info
        texture = fbx_shader.evalParm("map1")
        if texture:
            tx_node = new_mtl.createNode("texture::2.0")
            tx_node.parm("map").set(texture)
            psh.setInput(1,tx_node,0)

        new_mtl.layoutChildren()
        shader_node.layoutChildren()


target_geo_path = hou.ui.selectNode(initial_node = target_node.parent())
if target_geo_path:
    target_geo = hou.node(target_geo_path)
    print(target_geo_path)
    print(target_geo)
    current_mtl_path = target_geo.evalParm("shop_materialpath")
    print(current_mtl_path)
    new_mtl_path = current_mtl_path.replace(target_nodename,"New_{0}".format(target_nodename))
    target_geo.parm("shop_materialpath").set(new_mtl_path)


