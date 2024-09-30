# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import json
import csv
import os



def retrieveData(DataItem):
    Name = DataItem.get("Name")
    AssetPath = DataItem.get("Asset")
    BuildingType = [typename for typename in DataItem.get("BuildingType").keys() if DataItem.get("BuildingType")[typename]]
    if BuildingType:
        BuildingType = BuildingType[0]
    else:
        BuildingType = ""

    # get bound info
    bbx = DataItem.get("BoundingSize").get("X")
    bbx = bbx / 100
    # swap y and z
    bby = DataItem.get("BoundingSize").get("Z")
    bby = bby / 100
    bbz = DataItem.get("BoundingSize").get("Y")
    bbz = bbz / 100

    # get Extend info
    ExtendX = DataItem.get("ExtendSize").get("X")
    ExtendX = ExtendX / 100
    # swap y and z
    ExtendY = DataItem.get("ExtendSize").get("Z")
    ExtendY = ExtendY / 100
    ExtendZ = DataItem.get("ExtendSize").get("Y")
    ExtendZ = ExtendZ / 100

    res = DataItem.get("Zyzh").get("Res")
    res_sw = res.get("switch")
    res_percentage = res.get("percentage")

    com = DataItem.get("Zyzh").get("Commercial")
    com_sw = com.get("switch")
    com_percentage = com.get("percentage")

    cbd = DataItem.get("Zyzh").get("CBD")
    cbd_sw = cbd.get("switch")
    cbd_percentage = res.get("percentage")

    print(f"Name: {Name}")
    print(f"AssetPath: {AssetPath}")
    print(f"BuildingType: {BuildingType}")
    print(f"X:{bbx} \nY:{bby} \nZ:{bbz}")
    print(f"Extend: X:{ExtendX} Y:{ExtendY} Z:{ExtendZ}")
    print(f"Res:{res_sw}--{res_percentage}%\nCom:{com_sw}--{com_percentage}%\nCBS:{cbd_sw}--{cbd_percentage}%")


# json version
def ReadFromJson(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data_dict = json.loads(file.read())

    if not data_dict:
        print("Blank File")
        return

    for data in data_dict:
        retrieveData(data)


def ReadFromCSV(csv_file_path):
    pass


ReadFromJson('BuildingConfig.json')
