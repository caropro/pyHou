#coding = utf-8
import os
import sys


class testStr():
    def __repr__(self):
        return "Repr"
    def __str__(self):
        return "Str"

a = testStr()
print(a)

class callTest():
    def __call__(self, *args, **kwargs):
        print "Call {}".format(args,kwargs)

b = callTest()
b(1,2,3,4,5,{"a":1})

# print str(a)
# print repr(a)