# coding = utf-8
import hou
import time
import random


class LayerData(object):
    pass

tree_Density = bush_Density = 0
node = hou.pwd()
geo = node.geometry()

parent_node = node.inputs()[0]


#### create point attr
# Seed attr
clusterSeed_attr = geo.addAttrib(hou.attribType.Point, "ClusterSeed", 0)
scatterSeed_attr = geo.addAttrib(hou.attribType.Point, "ScatterSeed", 0)
# cluster attribute
clusterSize_attr = geo.addAttrib(hou.attribType.Point, "ClusterSize", 0.0)
clustershrink_attr = geo.addAttrib(hou.attribType.Point, "ClusterShrink", 0.0)
fluctuation_attr = geo.addAttrib(hou.attribType.Point, "Fluctuation", 0.0)
deleterate_attr = geo.addAttrib(hou.attribType.Point, "delete_rate", 0.0)
# growth condition
set_attr = geo.addAttrib(hou.attribType.Point, "set", "")
area_attr = geo.addAttrib(hou.attribType.Point, "area", "")
specificMask_attr = geo.addAttrib(hou.attribType.Point, "specificMask", "")
path_attr = geo.addAttrib(hou.attribType.Point, "path", "")
type_attr = geo.addAttrib(hou.attribType.Point, "Type", "")
level_attr = geo.addAttrib(hou.attribType.Point, "level", 0)
ratio_attr = geo.addAttrib(hou.attribType.Point, "ratio", 0.0)
viaRad_attr = geo.addAttrib(hou.attribType.Point, "viaRad", 0.0)
occRad_attr = geo.addAttrib(hou.attribType.Point, "occRad", 0.0)
seed_attr = geo.addAttrib(hou.attribType.Point, "seed", 0.0)
# rand attribute
along_normal_intensity = geo.addAttrib(hou.attribType.Point, "along_normal", 0.0)
scale_max_attr = geo.addAttrib(hou.attribType.Point, "scale_max", 0.0)
scale_min_attr = geo.addAttrib(hou.attribType.Point, "scale_min", 0.0)
rotate_max_attr = geo.addAttrib(hou.attribType.Point, "rotate_max", 0.0)
rotate_min_attr = geo.addAttrib(hou.attribType.Point, "rotate_min", 0.0)
# basic Attr
density = geo.addAttrib(hou.attribType.Point, "density", 0)
total_density_attr = geo.addAttrib(hou.attribType.Point, "total_density", 0)
altitude_min_attr = geo.addAttrib(hou.attribType.Point, "altitude_min", 0.0)
altitude_max_attr = geo.addAttrib(hou.attribType.Point, "altitude_max", 0.0)
longitude_min_attr = geo.addAttrib(hou.attribType.Point, "longitude_min", 0.0)
longitude_max_attr = geo.addAttrib(hou.attribType.Point, "longitude_max", 0.0)
latitude_min_attr = geo.addAttrib(hou.attribType.Point, "latitude_min", 0.0)
latitude_max_attr = geo.addAttrib(hou.attribType.Point, "latitude_max", 0.0)
slope_min_attr = geo.addAttrib(hou.attribType.Point, "slope_min", 0.0)
slope_max_attr = geo.addAttrib(hou.attribType.Point, "slope_max", 0.0)
Sunlight_min_attr = geo.addAttrib(hou.attribType.Point, "Sunlight_min", 0.0)
Sunlight_max_attr = geo.addAttrib(hou.attribType.Point, "Sunlight_max", 0.0)
wetness_min_attr = geo.addAttrib(hou.attribType.Point, "wetness_min", 0.0)
wetness_max_attr = geo.addAttrib(hou.attribType.Point, "wetness_max", 0.0)
ref_attr = geo.addAttrib(hou.attribType.Point, "ref", "")
layer_count_attr = geo.addAttrib(hou.attribType.Point, "layer_count", 0)
# grass_attr
grass_attr = geo.addAttrib(hou.attribType.Point, "grass", "")


# init
data_list = []
data_dict = {}

# get data nodes
for n in parent_node.children():
    if n.type().name() == "UHouLandFoliageCircle":
        data_list.append(n)

max_layer_count = max([data_node.parm("ExcludeLayers").eval() for data_node in data_list])
layer_dict = {}
if max_layer_count:
    for layer_index in range(max_layer_count):
        layer_dict["%s" % layer_index] = geo.addAttrib(hou.attribType.Point, "exlayer_%s" % (layer_index), '')

for data_node in data_list:
    # data construct
    data_name = data_node.name()
    data_path = data_node.path()
    data_dict[data_name] = {}
    # pack growth condition
    area = data_node.parm("Area").eval().split(":")[-1]
    specificMask = data_node.parm("SpecificMask").eval()
    # Seed value
    clusterseed = data_node.parm("ClusterSeed").eval()
    scatterseed = data_node.parm("ScatterSeed").eval()

    # cluster area measure
    clusterSize = data_node.parm("ClusterSize").eval()
    clusterShrink = data_node.parm("ClusterShrink").eval()
    fluctuation = data_node.parm("Fluctuation").eval()
    # tree
    tree_along_normal = data_node.parm("TreeAloneNormal").eval()
    tree_scale_min = data_node.parm("TreeScaleRangex").eval()
    tree_scale_max = data_node.parm("TreeScaleRangey").eval()
    tree_rotate_min = data_node.parm("TreeRotateRangex").eval()
    tree_rotate_max = data_node.parm("TreeRotateRangey").eval()
    # bush
    bush_along_normal = data_node.parm("BushAloneNormal").eval()
    bush_scale_min = data_node.parm("BushScaleRangex").eval()
    bush_scale_max = data_node.parm("BushScaleRangey").eval()
    bush_rotate_min = data_node.parm("BushRotateRangex").eval()
    bush_rotate_max = data_node.parm("BushRotateRangey").eval()
    # altitude range
    altitude_min = data_node.parm("AltitudeRangemin").eval()
    altitude_max = data_node.parm("AltitudeRangemax").eval()
    # longitude range
    longitude_min = data_node.parm("LongitudeRangemin").eval()
    longitude_max = data_node.parm("LongitudeRangemax").eval()
    # latitude range
    latitude_min = data_node.parm("LatitudeRangemin").eval()
    latitude_max = data_node.parm("LatitudeRangemax").eval()
    # slope range
    slope_min = data_node.parm("SlopeRangemin").eval()
    slope_max = data_node.parm("SlopeRangemax").eval()
    # wetness range
    wetness_min = data_node.parm("WetnessRangemin").eval()
    wetness_max = data_node.parm("WetnessRangemax").eval()
    # sunlight range
    Sunlight_min = data_node.parm("SunlightRangemin").eval()
    Sunlight_max = data_node.parm("SunlightRangemax").eval()
    # get num of tree type
    tree_count = data_node.parm("Trees").eval()
    # get num of bush type
    bush_count = data_node.parm("Bushes").eval()
    # grass type
    grasstype = data_node.parm("GrassTypeObject").eval()

    del_rate = data_node.parm("DeleteRate").eval()
    layer_count = data_node.parm("ExcludeLayers").eval()
    exlayerdict = {}
    for layer_index in range(layer_count):
        exlayerdict["%s" % layer_index] = data_node.parm("ExcludeLayers_%s" % (layer_index + 1)).eval()

    tree_total_ratio = 0
    if tree_count:
        data_dict[data_name]["Tree"] = {}
        tree_cpLevel = data_node.parm("TreeCompetitionLevel").eval()
        tree_Density = data_node.parm("TreeDensity").eval()
        for tree_num in range(tree_count):
            tree_num += 1
            tree_path = data_node.parm("Trees_%s_MeshPath" % tree_num).eval()
            tree_ratio = data_node.parm("Trees_%s_Percent" % tree_num).eval()
            tree_viabilityRadius = data_node.parm("Trees_%s_ViabilityRadius" % tree_num).eval()
            tree_occupiedRadius = data_node.parm("Trees_%s_OccupiedRadius" % tree_num).eval()
            tree_total_ratio += tree_ratio
            tree_ref_path = data_path+"/Trees_%s_MeshPath_mesh" % tree_num
            # init tree_num dic
            data_dict[data_name]["Tree"]["Tree_%s" % tree_num] = {}
            data_dict[data_name]["Tree"]["Tree_%s" % tree_num] = {"path": tree_path, "tree_ratio": tree_ratio,
                                                                  "viaRad": tree_viabilityRadius,
                                                                  "occRad": tree_occupiedRadius,
                                                                  "level": tree_cpLevel,
                                                                  "density": int(tree_Density),
                                                                  "ref_path":tree_ref_path}
    bush_total_ratio = 0
    if bush_count:
        data_dict[data_name]["Bush"] = {}
        for bush_num in range(bush_count):
            bush_num += 1
            bush_cpLevel = data_node.parm("BushCompetitionLevel").eval()
            bush_Density = data_node.parm("BushDensity").eval()
            bush_path = data_node.parm("Bushes_%s_MeshPath" % bush_num).eval()
            bush_ratio = data_node.parm("Bushes_%s_Percent" % bush_num).eval()
            bush_occupiedRadius = data_node.parm("Bushes_%s_OccupiedRadius" % bush_num).eval()
            bush_ref_path = data_path + "/Bushes_%s_MeshPath_mesh" % bush_num
            bush_total_ratio += bush_ratio
            data_dict[data_name]["Bush"]["Bush_%s" % bush_num] = {}
            data_dict[data_name]["Bush"]["Bush_%s" % bush_num] = {"path": bush_path, "bush_ratio": bush_ratio,
                                                                  "occRad": bush_occupiedRadius,
                                                                  "level": bush_cpLevel,
                                                                  "density": int(bush_Density),
                                                                  "ref_path":bush_ref_path}
    total_density = int(tree_Density + bush_Density)
    if tree_count:
        for rubbish, treeattri in data_dict[data_name]["Tree"].items():
            seed = random.random() * 10
            tree = geo.createPoint()
            tree.setAttribValue(area_attr, area)
            tree.setAttribValue(specificMask_attr, specificMask)
            tree.setAttribValue(type_attr, "Tree")
            tree.setAttribValue(path_attr, treeattri.get("path", ""))
            tree.setAttribValue(ref_attr,treeattri.get("ref_path"))
            tree.setAttribValue(altitude_max_attr, altitude_max)
            tree.setAttribValue(altitude_min_attr, altitude_min)
            tree.setAttribValue(longitude_max_attr, longitude_max)
            tree.setAttribValue(longitude_min_attr, longitude_min)
            tree.setAttribValue(latitude_min_attr, latitude_min)
            tree.setAttribValue(latitude_max_attr, latitude_max)
            tree.setAttribValue(slope_min_attr, slope_min)
            tree.setAttribValue(slope_max_attr, slope_max)
            tree.setAttribValue(Sunlight_min_attr, Sunlight_min)
            tree.setAttribValue(Sunlight_max_attr, Sunlight_max)
            tree.setAttribValue(wetness_min_attr, wetness_min)
            tree.setAttribValue(wetness_max_attr, wetness_max)

            tree.setAttribValue(level_attr, treeattri.get("level"))
            tree.setAttribValue(viaRad_attr, treeattri.get("viaRad"))
            tree.setAttribValue(occRad_attr, treeattri.get("occRad"))
            tree.setAttribValue(density, treeattri.get("density"))
            tree.setAttribValue(total_density_attr, total_density)
            tree.setAttribValue(ratio_attr, treeattri.get("tree_ratio") / tree_total_ratio)
            tree.setAttribValue(clusterSize_attr, clusterSize)
            tree.setAttribValue(clustershrink_attr, clusterShrink)
            tree.setAttribValue(fluctuation_attr, fluctuation)

            tree.setAttribValue(set_attr, data_name)

            # tree rand attri setting
            tree.setAttribValue(along_normal_intensity, tree_along_normal)
            tree.setAttribValue(scale_max_attr, tree_scale_max)
            tree.setAttribValue(scale_min_attr, tree_scale_min)
            tree.setAttribValue(rotate_max_attr, tree_rotate_max)
            tree.setAttribValue(rotate_min_attr, tree_rotate_min)
            tree.setAttribValue(seed_attr, seed)
            tree.setAttribValue(layer_count_attr, layer_count)

            tree.setAttribValue(deleterate_attr, del_rate)
            # set seed
            tree.setAttribValue(clusterSeed_attr, clusterseed)
            tree.setAttribValue(scatterSeed_attr, scatterseed)

            for layer_index in range(layer_count):
                tree.setAttribValue(layer_dict["%s" % layer_index], exlayerdict["%s" % layer_index])

    if bush_count:
        for rubbish, bushattri in data_dict[data_name]["Bush"].items():
            seed = random.random() * 10
            bush = geo.createPoint()
            bush.setAttribValue(area_attr, area)
            bush.setAttribValue(specificMask_attr, specificMask)
            bush.setAttribValue(type_attr, "Bush")
            bush.setAttribValue(path_attr, bushattri.get("path", ""))
            bush.setAttribValue(ref_attr, bushattri.get("ref_path"))
            bush.setAttribValue(altitude_max_attr, altitude_max)
            bush.setAttribValue(altitude_min_attr, altitude_min)
            bush.setAttribValue(longitude_max_attr, longitude_max)
            bush.setAttribValue(longitude_min_attr, longitude_min)
            bush.setAttribValue(latitude_min_attr, latitude_min)
            bush.setAttribValue(latitude_max_attr, latitude_max)
            bush.setAttribValue(slope_min_attr, slope_min)
            bush.setAttribValue(slope_max_attr, slope_max)
            bush.setAttribValue(Sunlight_min_attr, Sunlight_min)
            bush.setAttribValue(Sunlight_max_attr, Sunlight_max)
            bush.setAttribValue(wetness_min_attr, wetness_min)
            bush.setAttribValue(wetness_max_attr, wetness_max)

            bush.setAttribValue(level_attr, bushattri.get("level"))
            bush.setAttribValue(occRad_attr, bushattri.get("occRad"))
            bush.setAttribValue(density, bushattri.get("density"))
            bush.setAttribValue(total_density_attr, total_density)
            bush.setAttribValue(ratio_attr, bushattri.get("bush_ratio") / bush_total_ratio)

            bush.setAttribValue(set_attr, data_name)
            bush.setAttribValue(clusterSize_attr, clusterSize)
            bush.setAttribValue(clustershrink_attr, clusterShrink)
            bush.setAttribValue(fluctuation_attr, fluctuation)

            # tree rand attri setting
            bush.setAttribValue(along_normal_intensity, bush_along_normal)
            bush.setAttribValue(scale_max_attr, bush_scale_max)
            bush.setAttribValue(scale_min_attr, bush_scale_min)
            bush.setAttribValue(rotate_max_attr, bush_rotate_max)
            bush.setAttribValue(rotate_min_attr, bush_rotate_min)

            bush.setAttribValue(seed_attr, seed)
            bush.setAttribValue(layer_count_attr, layer_count)
            bush.setAttribValue(deleterate_attr, del_rate)

            # set seed
            bush.setAttribValue(clusterSeed_attr, clusterseed)
            bush.setAttribValue(scatterSeed_attr, scatterseed)
            for layer_index in range(layer_count):
                bush.setAttribValue(layer_dict["%s" % layer_index], exlayerdict["%s" % layer_index])

    grass = geo.createPoint()
    # set grass
    grass.setAttribValue(type_attr, "grass")
    grass.setAttribValue(area_attr, area)
    grass.setAttribValue(slope_min_attr, slope_min)
    grass.setAttribValue(slope_max_attr, slope_max)
    grass.setAttribValue(grass_attr, grasstype)
    grass.setAttribValue(altitude_max_attr, altitude_max)
    grass.setAttribValue(altitude_min_attr, altitude_min)
    grass.setAttribValue(specificMask_attr, specificMask)
    for layer_index in range(layer_count):
        grass.setAttribValue(layer_count_attr, layer_count)
        grass.setAttribValue(layer_dict["%s" % layer_index], exlayerdict["%s" % layer_index])