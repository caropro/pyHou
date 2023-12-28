import os
import logging
import json
import csv
import time
import hou

# 保存当前面板配置
def saveConfig():
    current_node = hou.pwd()
    jsonFile = current_node.parm("DataFile").eval()
    if not jsonFile or not jsonFile.endswith(".json"):
        return
    # 获取当前面板数据
    parms = {x: "" for x in ["MeshPath", "MaterialPart", "scatter", "PosVx", "PosVy"]}
    for parm_name, parm_value in parms.items():
        print(type(current_node.parm(parm_name).eval()))
        if isinstance(current_node.parm(parm_name).eval(), str):
            parms[parm_name] = current_node.parm(parm_name).rawValue()
        else:
            parms[parm_name] = float(current_node.parm(parm_name).eval())
    # 输出json文件
    with open(jsonFile, "w+") as outfile:
        json.dump(parms, outfile)
    return


# 从文件更新面板数据
def LoadConfig(jsonFile=None):
    current_node = hou.pwd()
    # print(current_node)
    if not jsonFile:
        jsonFile = current_node.parm("DataFile").eval()
        logging.info("get Config Path : %s\n" % jsonFile)

    if not jsonFile or not jsonFile.endswith(".json"):
        return

    logging.info("Current Loading : %s\n" % jsonFile)
    # 读取数据字典
    print("Read json:  %s" % jsonFile)
    parm_dic = {}
    with open(jsonFile, "r") as outfile:
        all_info = outfile.read()
        parm_dic = json.loads(all_info)
    current_node.setParms(parm_dic)
    logging.info("Parms Set\n")
    return


def sim(csvFile=None):
    current_node = hou.pwd()
    # refresh python
    Code = current_node.node("Code")
    Code.cook()
    # refresh output
    result_node = current_node.node("Output")
    result_node.cook()
    print("Done")
    # save csv
    if not csvFile:
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

    if not pos_list:
        logging.error("no points in current calculation")
        logging.error("Error filename is :%s" % csvFile)
        return
    with open(csvFile, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for pos in pos_list:
            writer.writerow(pos)
    logging.info("Save csv filename :%s" % csvFile)


def simAll():
    current_node = hou.pwd()
    currentDate = time.asctime().replace(" ", "_").replace(":", "_")
    logPath = os.path.join(os.path.expanduser("~"), "%s.log" % currentDate)
    logging.basicConfig(filename=logPath, level=logging.INFO)
    # get config Dir
    configDir = current_node.parm("ConfigRoot").eval()
    csvDir = current_node.parm("CsvRoot").eval()

    jsonFiles = [jsfile for jsfile in os.listdir(configDir) if jsfile.endswith(".json")]
    if not jsonFiles:
        logging.info("No Json Files in selected Dir")
        return

    # loop
    for jsonfile in jsonFiles:
        jsonPath = os.path.join(configDir, jsonfile)
        # read config file
        LoadConfig(jsonPath)
        csvFile = jsonfile.replace(".json", ".csv")
        csvPath = os.path.join(configDir, csvFile)
        print(csvPath)
        # export csv
        sim(csvPath)

    hou.ui.displayMessage("Done")
    return
