# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import os
if os.environ.get("DEVMODE"):
    print("Current In Dev Mode")
else:
    import hou

    