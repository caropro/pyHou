# coding = utf-8
import hou
import json
import os
from collections import OrderedDict


def convert():
    tar_file = hou.ui.selectFile(title="Select json File")
    if not tar_file:
        return
    if os.path.splitext(tar_file)[-1] != ".json":
        hou.ui.displayMessage("select json file!")
    else:
        with open(tar_file, "r") as outfile:
            all_info = outfile.read()
            parm_dic = json.loads(all_info, object_pairs_hook=OrderedDict)
        curve_coords = parm_dic.get("coords").get("value")
        new_coords = ""
        for point in curve_coords.split(" "):
            if new_coords:
                new_coords = point + " " + new_coords
            else:
                new_coords = point
        parm_dic["coords"]["value"] = new_coords
        print(new_coords)
        with open(tar_file, "w+") as outfile:
            json.dump(parm_dic, outfile)
        hou.ui.displayMessage("Save!")
