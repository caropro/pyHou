#coding = utf-8
import sys
import os
import subprocess
import json
current_dir = os.path.dirname(__file__)
#default_value
h_path = r"F:/Program Files/Side Effects Software/Houdini 18.0.416/bin"
customize_hfs = r"F:\dcc_houdini"

config_file = os.path.join(current_dir,"config_file.json")
#read config file
with open(config_file,"r+") as config:
    data = json.loads(config.read())
    customize_hfs = data.get("customize_hfs")
    h_path = data.get("SoftWare_Path")
    H_M = data.get("H_M")

print(customize_hfs)
print(h_path)
print(H_M)

#customize env setting
# test = r"C:\Users\Administrator\Documents\houdini18.0"
# os.environ["HOUDINI_USER_PREF_DIR"] =test + ";" +os.environ["HOUDINI_USER_PREF_DIR"]
os.environ['HOUDINI_PATH'] = customize_hfs+";" + os.environ['HOUDINI_PATH']
os.environ['H_M'] = H_M
#sys.path.append(customize_hfs)

#cmd
cmd = "{0}/houdini.exe".format(h_path)
#open app
print(subprocess.Popen(cmd))