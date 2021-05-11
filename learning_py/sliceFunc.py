#coding = utf-8



class test:
    data = [1,2,3,4]
    def __getitem__(self, index):
        print("Input Value: " , index)
        return self.data[index]
    def __index__(self):
        return 222

class cus_iter:
    def __init__(self,start,end):
        self.value = start - 1
        self.end = end
    def __iter__(self):
        return self

# t = test()
# t[2:]
# print t.__index__()
#
# for item in t:
#     print item