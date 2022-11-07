# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import math
import scipy
import pprint


a = [x for x in range(100)]
print(a)

count = len(a)
total_list=[]

for i in range(count):
    if i == (count-1):
        continue
    pairList = [(a[i],a[x]) for x in range(i+1,count)]
    total_list.append(pairList)

for pair in total_list:
    print(pair)