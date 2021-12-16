# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0

import Timer
print(Timer)

def genTest():
    for i in range(100):
        yield i

gen = genTest()

for i in gen:
    print(i)