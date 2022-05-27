# coding = utf-8
from lister import ListInstance


class Spam(ListInstance):
    def __init__(self):
        self.data1 = "Test"


x = Spam()
print (x)
print (x.__dict__)
