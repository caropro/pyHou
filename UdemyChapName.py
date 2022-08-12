# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import pprint
path = r'C:\\Users\\jianx\\Desktop\\Test.txt'

data = []
with open(path,"r+") as file:
    for line in file.readlines():
        if "." in line:
            data.append(line)

#data = [x.split(".")[1] for lec in data]

for course in data:
    print(course)


