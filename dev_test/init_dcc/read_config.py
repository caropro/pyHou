#coding = utf-8
import json

with open("config_file.json","r+") as config:
    data = json.loads(config.read())
    hfs = data.get("customize_hfs")
    h_path = data.get("SoftWare_Path")


print(hfs)
print(h_path)