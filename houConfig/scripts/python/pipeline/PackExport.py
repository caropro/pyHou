# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import hou
import os
import shutil


# import hrpyc
# connection,hou = hrpyc.import_remote_module()
# ui = connection.modules.hou.ui

ui = hou.ui

def exportHDAInFile():
    # Get all HDAs in the scene
    # root
    root = hou.node("/obj")
    hda_list = []
    # iter node
    for child_node in root.allNodes():
        #print(child_node.name())
        definition = child_node.type().definition()
        if definition:
            # print(definition.libraryFilePath())
            hda_path = definition.libraryFilePath()
            hdadir = os.path.dirname(hda_path)

            if os.path.isdir(hdadir) and not "~" in hdadir and not hda_path in hda_list:
                hda_list.append(hda_path)
                print(hda_path)

    # select Export dir
    export_dir = ui.selectFile(title="Select Export Dir",file_type=hou.fileType.Directory)
    if os.path.exists(export_dir):
        for hdapath in hda_list:
            hda_name = os.path.basename(hdapath)
            # export_hda_dir = os.path.join(export_dir,hda_name)
            if not os.path.exists(export_dir):
                os.makedirs(export_dir)
            shutil.copy(hdapath,export_dir)
            print("Export %s" % hdapath)
        ui.displayMessage("Export Success!")
        os.startfile(export_dir)
    else:
        ui.displayMessage("Select Export Dir!")