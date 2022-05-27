#coding = utf-8
import time
itertimes = 1000

def timer(func):
    def wraped(*args,**kwargs):
        start_time = time.time()
        try:
            return func(*args,**kwargs)
        finally:
            runtime = time.time() - start_time
            print("time consume is : %f" % runtime)
    return  wraped

def bestRecord(func, *args, ** kwargs):
    best = 2**50
    for i in range(50):
        timecosume = timer(func,*args,iter = 1 ,**kwargs)
        if timecosume<best:
            best = timecosume
    return best

