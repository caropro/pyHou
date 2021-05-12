# coding = utf-8
import os
import hou

node = hou.pwd()
geo = node.geometry()

hda_path = node.parent().parent().parent().type().definition().libraryFilePath()
HDA_dir = os.path.dirname(hda_path)

parent_node = node.parent()
target_point = geo.point(0)
# Add code to modify contents of geo.
# Use drop down menu to select examples.
file_name = target_point.attribValue("Seam_name")


def getLevelName(x, y):
    if (x <= 8):
        xName = "L" + str(9 - x)
    else:
        xName = "R" + str(x - 8)
    if (y <= 8):
        yName = "U" + str(9 - y)
    else:
        yName = "D" + str(y - 8)
    return "Tile_" + xName + yName


# create Subnet
new_hda = parent_node.createNode("subnet", file_name)
create_merge_node = new_hda.createNode("merge")
output_name = "Seam_" + file_name + ".bgeo"

input_count = 0
for tile in geo.points():
    tile_data = tile.attribValue("tile")
    tile_x, tile_y = tile_data.split(",")
    tile_x = int(tile_x)
    tile_y = int(tile_y)
    tile_name = getLevelName(tile_x, tile_y)
    tile_name = tile_name + ".bgeo"

    # create pyhton node record hda_path
    python_name = "file_path_%s" % input_count
    python = new_hda.createNode("python", python_name)
    python.parm("python").set(
        '''import os\nnode = hou.pwd()\nHDAPath = node.parent().type().definition().libraryFilePath()\nGeoPath = os.path.join(os.path.dirname(HDAPath),'%s');\nOutputPath = os.path.join(os.path.dirname(HDAPath),'%s');\ngeo = node.geometry()\ngeo.addAttrib(hou.attribType.Global, "basegeo_path","")\ngeo.setGlobalAttribValue("basegeo_path",GeoPath)\ngeo.addAttrib(hou.attribType.Global, "output_path","")\ngeo.setGlobalAttribValue("output_path",OutputPath)\n''' % (
            tile_name, output_name))

    tile_full_path = os.path.normpath(os.path.join(HDA_dir, tile_name + ".bgeo"))
    fileRead = new_hda.createNode("file", tile_name)
    fileRead.setInput(0, python, 0)
    fileRead.parm("file").set('\`details(0,"basegeo_path")\`')

    record_name = new_hda.createNode("python")
    record_name.parm("python").set(
        '''import os\nnode = hou.pwd()\ninput_node = node.inputs()[0]\ninput_name = input_node.name()\n\ngeo = node.geometry()\nname_attr = geo.addAttrib(hou.attribType.Point,"Name","")\nfor point in geo.points():\n    point.setAttribValue(name_attr, input_name) ''')
    record_name.setInput(0, fileRead, 0)

    create_merge_node.setInput(input_count, record_name, 0)
    input_count += 1

# 创建数据节点
seam_data = new_hda.createNode("python", "Geo_%s" % file_name)
# 获取接缝名称
seam_data.parm("python").set(
    '''import os\nnode = hou.pwd()\nHDAPath = node.parent().type().definition().libraryFilePath()\ngeo_name = os.path.join(os.path.dirname(HDAPath),"WorldSeam.bgeo")\nGeoPath = os.path.join(os.path.dirname(HDAPath),geo_name);\ngeo = node.geometry()\ngeo.addAttrib(hou.attribType.Global, "Seam_path","")\ngeo.setGlobalAttribValue("Seam_path",GeoPath)\n''')
# 创建接缝模型读取节点
SeamRead = new_hda.createNode("file", "SeamRead")
SeamRead.setInput(0, seam_data, 0)
SeamRead.parm("file").set('\`details(0,"Seam_path")\`')
# 添加mask节点
hf_mask = new_hda.createNode("heightfield_maskbyobject", "Seam_mask")
hf_mask.parm("maxdist").set(20000)
hf_mask.setInput(1, SeamRead, 0)

# 合并tile
create_volumeSplice = new_hda.createNode("volumesplice")
create_volumeSplice.setInput(0, create_merge_node, 0)

# 进行遮罩处理
hf_mask.setInput(0, create_volumeSplice, 0)

# 添加blur节点
hf_blur = new_hda.createNode("heightfield_blur")
hf_blur.setInput(0, hf_mask, 0)
hf_blur.setInput(1, hf_mask, 0)

# 创建输出数据
output_data = new_hda.createNode("python", "Geo_%s" % file_name)
# 获取输出地址
output_data.parm("python").set(
    '''import os\nnode = hou.pwd()\nHDAPath = node.parent().type().definition().libraryFilePath()\ngeo_name = os.path.basename(HDAPath)[5:].replace(".hda",".bgeo")\nGeoPath = os.path.join(os.path.dirname(HDAPath),geo_name);\ngeo = node.geometry()\ngeo.addAttrib(hou.attribType.Global, "output_path","")\ngeo.setGlobalAttribValue("output_path",GeoPath)\n''')
output_data.setInput(0, hf_blur, 0)

create_seam_output = new_hda.createNode("rop_geometry")
create_seam_output.setInput(0, output_data, 0)
create_seam_output.parm("sopoutput").set('\`details(0,"output_path")\`')

seam2tile = new_hda.createNode("seam2tile")
seam2tile.bypass(1)
seam2tile.setInput(0, hf_blur, 0)
seam2tile.setInput(1, create_merge_node, 0)

new_hda_path = os.path.join(HDA_dir, "Seam_" + file_name + ".hda")
if os.path.exists(new_hda_path):
    os.remove(new_hda_path)
node_name = "Seam_" + file_name

hda_node = new_hda.createDigitalAsset(name=node_name, hda_file_name=new_hda_path, description=node_name,
                                      min_num_inputs=0, max_num_inputs=0)

hda_node.destroy()
