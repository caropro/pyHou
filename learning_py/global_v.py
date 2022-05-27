#coding = utf-8
# import global_vb
# print global_vb.X
# global_vb.set(999)
# print global_vb.X
#
# import sys
# print(sys.modules["global_vb"])



def func_a(x):
    a =100
    def func_b(c=x):
        z = a+c
        print(z)
    return func_b

# test = func_a(111)
# test()
# test(222)
# 

def func_local():
    test_value = 100
    def n_local():
        global test_value
        test_value = 222
    return n_local

test = func_local()
test()