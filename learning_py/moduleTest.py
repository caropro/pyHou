# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import myModule
import sys
import os
import logging
from TestPackage import playModule
from PySide2 import QtHelp

currentFile = __file__
currentDir = os.path.dirname(currentFile)

print(__name__)
print(myModule.MYVAR)

playModule.run()
