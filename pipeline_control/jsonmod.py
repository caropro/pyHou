#coding = utf-8
import os
import sys
import json

path = "E:\REF\Art\HouLand\PublicDataHDAs\FoliageRegion_data"
for jsfile in os.listdir(path):
    if jsfile.endswith("json"):
        js_path = os.path.join(path,jsfile)
        #print(js_path)
        with open(js_path,"r+") as f:
            data = f.read()
            data = data.replace("Filter","filter")
            print(data)
        with open(js_path,"w+") as f:
            f.write(data)
