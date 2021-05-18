#coding = utf-8
import logging
import os
import hou
import time

currenttime = time.localtime()
currenttime = time.ctime()

print(currenttime)

logging.basicConfig(filename="test.log",level=logging.INFO)
logging.info("test_log info")