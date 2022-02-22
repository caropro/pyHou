# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import os
import sys
import shutil

#get current path
currentFile =  __file__
currentDir = os.path.normpath(os.path.dirname(currentFile))

#get targetPath defaultpath is document folder
userFolder = os.path.expanduser("~")
houdiniPaths = [ file for file in os.listdir(userFolder) if file.startswith("houdini")]
latestVersion = max(houdiniPaths);
targetDir = os.path.normpath(os.path.join(userFolder,latestVersion))
print(targetDir)

pairInfo = {}
for packinfo in os.walk(currentDir):
    fileDir = packinfo[0]
    for fileName in packinfo[2]:
        #get source path info
        filePath = os.path.join(fileDir,fileName)
        filePath = os.path.normpath(filePath)
        #cal target path info
        absPath = filePath.replace(currentDir,"")
        targetFilePath = os.path.normpath(targetDir + absPath)
        #record pair info
        pairInfo[filePath] = targetFilePath

print(pairInfo)

# if os.path.exists(targetDir):
#     for sourcefile,targetfile in pairInfo.items():
#         shutil.copy2(sourcefile,targetfile)
#     # shutil.rmtree(targetDir)
#     # shutil.copytree(currentDir, targetDir)
#     print("OverWrite Copy")
# else:
#     shutil.copytree(currentDir, targetDir)
#     print("New Copy")