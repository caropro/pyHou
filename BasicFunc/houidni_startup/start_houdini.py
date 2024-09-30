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

#get info by query the reg info
houdini_info = os.popen('''reg query "HKLM\Software\Side Effects Software\Houdini"''')
str_info = houdini_info.read()
versionlist = str_info.splitlines()
versionlist = [info for info in versionlist if "REG_SZ" in info and "LicenseServer" not in info]

filter_versionList = {}
for version in versionlist:
    ver = version.split("REG_SZ")
    ver = [ info.strip() for info in ver]
    filter_versionList[ver[0]] = ver[1]

print(filter_versionList)

#get latest houdini
pwd = os.path.dirname(os.path.abspath(__file__))
max_Version = max(filter_versionList.keys())
houdini_install_dir = filter_versionList[max_Version]

houdini_exe = os.path.normpath(os.path.join(houdini_install_dir,"bin","houdini.exe"))
print(houdini_exe)
#subprocess.Popen(houdini_exe)
