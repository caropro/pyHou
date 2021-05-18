# coding = utf-8
import itertools


def gen():
    for x in range(100):
        yield x


test = gen()
for i in test:
    print(i)
