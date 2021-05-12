# coding = utf-8
import hou

node = hou.pwd()
geo = node.geometry()
base_node = node.parent()
data_count = base_node.parm("data_node_list").eval()

data_list = []
data_dict = {}
for node_index in range(1, data_count + 1):
    data_path = base_node.parm("data_node_%s" % node_index).eval()
    data_node = hou.node(data_path)
    data_list.append(data_node)

print(data_list)
#### create point attr
name_attr = geo.addAttrib(hou.attribType.Point, "Name", "")
CalAttr = geo.addAttrib(hou.attribType.Point, "Cal_Func", 0)
areaAttr = geo.addAttrib(hou.attribType.Point, "Area", "")
layercount_attr = geo.addAttrib(hou.attribType.Point, "LayerCount", 0)
coscount_attr = geo.addAttrib(hou.attribType.Point, "CosCount", 0)
shoredist_attr = geo.addAttrib(hou.attribType.Point, "shoredist", 0.0)
underwater_attr = geo.addAttrib(hou.attribType.Point, "UnderWater", 0.0)
seadist_attr = geo.addAttrib(hou.attribType.Point, "SeaDist", 0.0)
waterdist_attr = geo.addAttrib(hou.attribType.Point, "WaterDist", 0.0)
seadist_o_attr = geo.addAttrib(hou.attribType.Point, "SeaDist_o", 0.0)
waterdist_o_attr = geo.addAttrib(hou.attribType.Point, "WaterDist_o", 0.0)
slopemin_attr = geo.addAttrib(hou.attribType.Point, "SlopeMin", 0.0)
slopemax_attr = geo.addAttrib(hou.attribType.Point, "SlopeMax", 0.0)
density_attr = geo.addAttrib(hou.attribType.Point, "density", 0)
clusterSize_attr = geo.addAttrib(hou.attribType.Point, "ClusterSize", 0)
eleDist_attr = geo.addAttrib(hou.attribType.Point, "ele_dist", 0.0)

max_layer_count = max([data_node.parm("layer_list").eval() for data_node in data_list])

layer_dict = {}
if max_layer_count:
    for layer_index in range(1, max_layer_count + 1):
        layer_dict["%s" % layer_index] = geo.addAttrib(hou.attribType.Point, "layer_name_%s" % (layer_index), '')

cos_dict = {}
if max_layer_count:
    for cos_index in range(1, max_layer_count + 1):
        cos_dict["%s" % cos_index] = geo.addAttrib(hou.attribType.Point, "customize_layer_name_%s" % (cos_index), '')

for data_node in data_list:
    name = data_node.name()
    shoredist = data_node.parm("shore_dist").eval()
    seadist = data_node.parm("sea_distance").eval()
    waterdist = data_node.parm("water_distance").eval()
    seadist_o = data_node.parm("sea_distance_o").eval()
    waterdist_o = data_node.parm("water_distance_o").eval()
    cal = data_node.parm("function").eval()
    slope_min = data_node.parm("slope1").eval()
    slope_max = data_node.parm("slope2").eval()
    density = data_node.parm("density").eval()
    clustersize = data_node.parm("group_num").eval()
    layercount = data_node.parm("layer_list").eval()
    coscount = data_node.parm("customize_layer").eval()
    eledist = data_node.parm("group_ele_dist").eval()
    underwater = data_node.parm("underwater").eval()
    bio = geo.createPoint()
    # area
    bio.setAttribValue(areaAttr, data_node.parm("area_name").eval())
    # layer
    bio.setAttribValue(layercount_attr, layercount)
    for layer_index in range(1, 1 + layercount):
        bio.setAttribValue(layer_dict["%s" % layer_index], data_node.parm("layer_name_%s" % (layer_index)).eval())
    # cos layer
    bio.setAttribValue(coscount_attr, coscount)
    for cos_index in range(1, 1 + coscount):
        bio.setAttribValue(cos_dict["%s" % cos_index], data_node.parm("customize_layer_name_%s" % (cos_index)).eval())

    bio.setAttribValue(name_attr, name)
    bio.setAttribValue(CalAttr, cal)
    bio.setAttribValue(shoredist_attr, shoredist)
    bio.setAttribValue(underwater_attr, underwater)
    bio.setAttribValue(seadist_attr, seadist)
    bio.setAttribValue(waterdist_attr, waterdist)
    bio.setAttribValue(seadist_o_attr, seadist_o)
    bio.setAttribValue(waterdist_o_attr, waterdist_o)
    bio.setAttribValue(slopemin_attr, slope_min)
    bio.setAttribValue(slopemax_attr, slope_max)
    bio.setAttribValue(density_attr, density)
    bio.setAttribValue(clusterSize_attr, clustersize)
    bio.setAttribValue(eleDist_attr, eledist)



