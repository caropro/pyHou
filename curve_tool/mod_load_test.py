import os
import sys

#get current hda path
current_dir = os.path.dirname(kwargs["node"].type().definition().libraryFilePath())
parent_dir = os.path.dirname(current_dir)
tar_dir = os.path.join(parent_dir,"scripts/python_modules")
sys.path.append(tar_dir)
import parmFunc
