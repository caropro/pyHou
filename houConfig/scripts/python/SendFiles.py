# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0

import os
import shutil
import copy


targetDir = r"C:\Users\wujianxuan\Documents\houdini20.0\scripts\python\pipeline"

file = "pipeline/ImportFbx.py"

currentFile = os.path.abspath(__file__)
currentDir = os.path.dirname(currentFile)
filepath = os.path.normpath(os.path.join(currentDir, file))
print(filepath)


#copy file to target directory overwriting the file if it exists
shutil.copy(filepath, targetDir)