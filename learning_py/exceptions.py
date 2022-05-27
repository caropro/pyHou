# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
a = {"a":1}
try:
    a["test"]
except KeyError as e:
    print("Error")
    raise e
