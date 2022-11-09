# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import os
import subprocess
import sys
import time

#set env path
HOUDINI_USER_PREF_DIR = ""
HOUDINI_PATH = ""

#PATH append to sys
current_env = os.environ
env_HPATH = current_env["HOUDINI_PATH"]
env_HPATH ="{}{}&".format(env_HPATH[:-1],HOUDINI_PATH)
current_env["HOUDINI_PATH"] = env_HPATH
#USERDir
UserDIR = current_env["HOUDINI_USER_PREF_DIR"]
UserDIR ="{}{}&".format(UserDIR[:-1],HOUDINI_USER_PREF_DIR)
current_env["HOUDINI_USER_PREF_DIR"] = UserDIR

#get latest houdini
pwd = os.path.dirname(os.path.abspath(__file__))
houdini_install_dir = r"C:\Program Files\Side Effects Software"
max_Version = max([x for x in os.listdir(houdini_install_dir) if "Houdini 1" in x or "Houdini 2" in x])


houdini_exe = os.path.normpath(os.path.join(houdini_install_dir,max_Version,"bin","houdini.exe"))
print(houdini_exe)
subprocess.Popen(houdini_exe)
