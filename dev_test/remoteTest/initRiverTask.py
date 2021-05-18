#coding = utf-8
import hou
import os,sys
import hrpyc



data_path = r"E:\REF\Art\HouLand\LandscapeHDAs"
connection,hou = hrpyc.import_remote_module()
# ui = connection.modules.hou.ui
# hou.ui = ui
# sys.modules["hou"] = hou

obstacles = [file for file in os.listdir(data_path) if "Obstacle" in file]
print(obstacles)
tileDict = {tile:"%s_cache.hda"%tile.replace("Obstacle_","").replace(".bgeo","") for tile in obstacles}
print(tileDict)

node = hou.selectedNodes()[0]
hda_container = node.node("RiverCombine")
hda_container_ls = node.node("LakeAndSeaCombine")
obstacles_container = node.node("Obstacle")
if(hda_container.children()):
    for del_node in hda_container.children():del_node.destroy()
if(hda_container_ls.children()):
    for del_node in hda_container_ls.children():
        del_node.destroy()
if (obstacles_container.children()):
    for del_node in obstacles_container.children():
        del_node.destroy()

hda_list = []
obfile_list = []
ls_hda_list = []
for obstacleCache,hda in tileDict.items():
    #create hda
    HDAPath = os.path.join(data_path,hda)
    hou.hda.installFile(HDAPath)
    hda = hda.split(".")[0]
    hda_node = hda_container.createNode(hda)
    ls_hda_node = hda_container_ls.createNode(hda)
    #create Cache file
    filenode = obstacles_container.createNode("file")
    obstacleCachePath = os.path.join(data_path,obstacleCache)
    filenode.parm("file").set(obstacleCachePath)
    #print obstacleCache
    hda_list.append(hda_node)
    obfile_list.append(filenode)
    ls_hda_list.append(ls_hda_node)

#create merge node
hdamerge_node =hda_container.createNode("merge")
for hda in hda_list:
    hdamerge_node.setInput(len(hdamerge_node.inputs()), hda, 0)
hdamerge_node.setDisplayFlag(1)

obsmerge_node =obstacles_container.createNode("merge")
for obscacle in obfile_list:
    obsmerge_node.setInput(len(obsmerge_node.inputs()), obscacle, 0)
obsmerge_node.setDisplayFlag(1)
#lake and sea value
hda_lakemerge_node =hda_container_ls.createNode("merge")
for hda in ls_hda_list:
    hda.allowEditingOfContents(1)
    hda.node("mod_Water_mesh_cache").setDisplayFlag(1)
    hda_lakemerge_node.setInput(len(hda_lakemerge_node.inputs()), hda, 0)
hda_lakemerge_node.setDisplayFlag(1)