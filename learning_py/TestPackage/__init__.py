# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0

#init Package
print("using TesrtPackage")

import sys
import os

CurrentDir = os.path.abspath(os.path.dirname(__file__))
#append current dir
os.environ['PATH'] = CurrentDir + os.pathsep + os.environ['PATH']