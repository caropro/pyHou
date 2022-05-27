# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0

def dec(func):
    # first layer import func as var
    print("Dec Running")
    def wrap(*args,**kwargs):
        print("Running import Func")
        #second layer return that func
        return func(*args,**kwargs)
    print("Use Wrap")
    return wrap

def dec_2(func,*args,**kwargs):
    # first layer import func as var
    print("Dec Running")
    def wrap(data):
        print("Running import Func")
        print(data)
        #second layer return that func
        return func(data)
    print("Use Wrap")
    return wrap


#装饰器，会吧被装饰的function作为参数传进装饰器函数中
#所以装饰器，在完成自己的执行任务的同时，需要返回被装饰的函数
@dec_2
def testFunc(test_var):
    print("Running Test Function")
    #print(test_var)

testFunc(9999)