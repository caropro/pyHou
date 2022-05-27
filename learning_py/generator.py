# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import measureTime

@measureTime.timer
def genTest():
    l = []
    for i in range(1000000):
        l.append(i)
    return l

genTest()

import string
def getAllPairs():
    all_letters = string.ascii_letters
    result = [{x:all_letters.find(x)} for x in all_letters]
    return result

print(getAllPairs())


class iterTest(object):
    def __iter__(self):
        return self
    def __next__(self):
        return 0