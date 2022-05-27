# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import os
import shutil

#document folder
userFolder = os.path.expanduser("~")

#version pending transfer
old_version = "houdini18.5"
new_version = "houdini19.0"

#combine path
old_path = os.path.join(userFolder,old_version)
new_path = os.path.join(userFolder,new_version)

#target folder or file
otl_folder = "otls"
desktop_folder = "desktop"
PipeLine_folder = "PipeLine"
presets_folder = "presets"
scripts_folder = "scripts"
toolbar = "toolbar"
houdini_env = "houdini_env"

#make folder list
Pending_list = [otl_folder,desktop_folder,PipeLine_folder,presets_folder,scripts_folder,toolbar]

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
            absPath = filePath.replace(fileDir,moveTo)
            targetFilePath = os.path.normpath(absPath)
            #record pair info
            pairInfo[filePath] = targetFilePath
            print("\n{}\n{}".format(filePath,targetFilePath))

    print(pairInfo)

    if os.path.exists(moveTo):
        for sourcefile,targetfile in pairInfo.items():
            shutil.copy2(sourcefile,targetfile)
        # shutil.rmtree(targetDir)
        # shutil.copytree(currentDir, targetDir)
        print("OverWrite Copy")
    else:
        shutil.copytree(targetPath, moveTo)
        print("New Copy")