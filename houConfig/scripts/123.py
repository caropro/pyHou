
import os
import hou
ProjectPath = "G:/REF/Art" #注意，这个路径应该是你项目的Art路径，请更换！
for fpathe,dirs,fs in os.walk(ProjectPath+"/HouLand/OperatorHDAs"):
    for f in fs:
        HDAPath = os.path.join(fpathe,f)
        if(HDAPath.endswith(".hda")):
            hou.hda.installFile(HDAPath)
