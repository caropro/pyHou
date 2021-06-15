import os
import sys

filepath = __file__
targetPath = os.path.dirname(filepath)
sys.path.append(targetPath)

print("Running!!!!!!!")
import init_tool

print("Hello PipeLine")
