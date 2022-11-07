#coding = utf-8
import time
import sys
itertimes = 1000

def timer(func):
    def wraped(*args,**kwargs):
        start_time = time.time()
        try:
            return func(*args,**kwargs)
        finally:
            runtime = time.time() - start_time
            print("time consume is : %f" % runtime)
            print("Func: {}".format(func.__name__))
    return  wraped

def bestRecord(func, *args, ** kwargs):
    best = 2**50
    for i in range(50):
        timecosume = timer(func,*args,iter = 1 ,**kwargs)
        if timecosume<best:
            best = timecosume
    return best

@timer
def calTest():
    for i in range(1000000):
        print(i)
    return None
#
# calTest()