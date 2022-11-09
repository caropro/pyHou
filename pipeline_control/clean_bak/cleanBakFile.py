# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import os

targetFolder = r"E:\BigOne"
filedata = os.walk(targetFolder)

for dir_path,folders,filelist in filedata:
    bakList = [bakfile for bakfile in filelist if "_bak" in bakfile]
    if bakList:
        print(bakList)
        bakFilePathList = [os.path.normpath(os.path.join(dir_path,bakfile)) for bakfile in bakList]
        for bakFilePath in bakFilePathList:
            os.remove(bakFilePath)
