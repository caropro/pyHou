# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import sys
import os
import logging


logging.basicConfig(filename=r"Log.txt",filemode="a", level=logging.INFO)
# logging.basicConfig(level=logging.INFO)
#global var
MYVAR = 10

def blank_function():
    pass

if __name__ == "__main__":
    logging.log(20, "Running Current Module As File")
else:
    # {50: 'CRITICAL', 40: 'ERROR', 30: 'WARNING', 20: 'INFO', 10: 'DEBUG', 0: 'NOTSET'}
    logging.log(20, "Import myModule.")