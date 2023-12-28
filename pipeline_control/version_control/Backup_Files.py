# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import os
import shutil

#document folder
userFolder = os.path.expanduser("~")

#version pending transfer
old_version = "houdini19.5"
new_version = "houdini20.0"

#combine path
old_path = os.path.join(userFolder,"Documents",old_version)
new_path = os.path.join(userFolder,"Documents",new_version)

#target folder or file
otl_folder = "otls"
dso_folder = "dso"
hdk_folder = "hdk"
help_folder = "help"
desktop_folder = "desktop"
PipeLine_folder = "PipeLine"
packages_folder = "packages"
presets_folder = "presets"
scripts_folder = "scripts"
toolbar = "toolbar"
houdini_env = "houdini.env"
MainMenuCommon="MainMenuCommon.xml"
OPmenu="OPmenu.xml"
display = "display.pref"
Visualizers = "Visualizers"

#make folder list
Pending_list = [otl_folder,dso_folder,hdk_folder,help_folder,desktop_folder,packages_folder,presets_folder,scripts_folder
                ,toolbar,houdini_env,MainMenuCommon,OPmenu]

Pending_list = [scripts_folder]
#folder loop
for targetFolder in Pending_list:
    targetPath = os.path.normpath(os.path.join(old_path,targetFolder))
    moveTo = os.path.normpath(os.path.join(new_path,targetFolder))
    pairInfo = {}
    for packinfo in os.walk(targetPath):
        fileDir = packinfo[0]
        for fileName in packinfo[2]:
            #get source path info
            filePath = os.path.join(fileDir,fileName)
            filePath = os.path.normpath(filePath)
            #cal target path info
            absPath = filePath.replace(targetPath,moveTo)
            targetFilePath = os.path.normpath(absPath)
            #record pair info
            pairInfo[filePath] = targetFilePath

    if os.path.exists(moveTo):
        # for sourcefile,targetfile in pairInfo.items():
        #     shutil.copy2(sourcefile,targetfile)
        # shutil.rmtree(targetDir)
        # shutil.copytree(currentDir, targetDir)
        print("OverWrite Copy")
    else:
        # shutil.copytree(targetPath, moveTo)
        print("New Copy")