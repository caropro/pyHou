#coding = utf-8
import os,sys,socket
import hrpyc
import hou
import cProfile
import toolutils
import soptoolutils
import itertools
import logging
import json
import csv

connection,hou = hrpyc.import_remote_module()
ui = connection.modules.hou.ui
hou.ui = ui
sys.modules["hou"] = hou


def SaveConfig():
    current_node = hou.selectedNodes()[0]
    # print(current_node)
    jsonFile = current_node.parm("DataFile").eval()
    if not jsonFile or not jsonFile.endswith(".json"):
        return
    parms = {x:"" for x in ["MeshPath","MaterialPart","scatter","PosVx","PosVy"]}
    for parm_name,parm_value in parms.items():
        print(type(current_node.parm(parm_name).eval()))
        if isinstance(current_node.parm(parm_name).eval(),str):
            parms[parm_name] = current_node.parm(parm_name).rawValue()
        else:
            parms[parm_name] = float(current_node.parm(parm_name).eval())

    with open(jsonFile, "w+") as outfile:
        json.dump(parms, outfile)
    return

def LoadConfig(jsonFile = None):
    current_node = hou.selectedNodes()[0]
    # print(current_node)
    if not jsonFile:
        jsonFile = current_node.parm("DataFile").eval()
        logging.info("Current Loading : %s"%jsonFile)
    if not jsonFile or not jsonFile.endswith(".json"):
        return
    #读取数据字典
    parm_dic = {}
    with open(jsonFile, "r") as outfile:
        all_info = outfile.read()
        parm_dic = json.loads(all_info)
    current_node.setParms(parm_dic)
    return

def sim():
    current_node = hou.pwd()
    #refresh python
    Code = current_node.node("Code")
    Code.cook()
    #refresh output
    result_node = current_node.node("Output")
    result_node.cook()
    print("Done")
    #save csv
    csvFile = current_node.parm("csvFile").evalAsString()
    if not csvFile.endswith(".csv"):
        print("not csv file path")
        return

    data_geo = result_node.geometry()
    print(data_geo)
    pos_list = []
    for point in data_geo.points():
        pos = []
        pos.append(point.attribValue("P")[0] * 100)
        pos.append(point.attribValue("P")[2] * 100)
        pos.append(point.attribValue("P")[1] * 100)
        pos_list.append(pos)

    with open(csvFile, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for pos in pos_list:
            writer.writerow(pos)



def simAll():
    current_node = hou.pwd()
    # get config Dir
    configDir = current_node.parm("ConfigRoot").eval()
    csvDir = current_node.parm("CsvRoot").eval()

    jsonFiles = [jsfile for jsfile in os.listdir(configDir) if jsfile.endswith(".json")]
    # loop
    for jsonfile in jsonFiles:
        # read config file
        LoadConfig(jsonfile)


    # export csv

    return