# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import os
import subprocess
import sys

HOUDINI_USER_PREF_DIR = ""
HOUDINI_PATH = ""

current_env = os.environ
env_HPATH = current_env["HOUDINI_PATH"]
env_HPATH.append(HOUDINI_PATH)
current_env["HOUDINI_PATH"] = env_HPATH

pwd = os.path.dirname(os.path.abspath(__file__))


hfs = r"C:\Program Files\Side Effects Software\Houdini 18.5.696\bin"
houdini_exe = os.path.join(hfs,"houdini.exe")

subprocess.Popen(houdini_exe)