#coding = utf-8
import time
itertimes = 1000

def timer(func,iter = 1000 ,*args,**kwargs):
    start_time = time.clock()
    for i in range(iter):
        func(*args,**kwargs)
    timecosume = time.clock() - start_time
    return timecosume

def bestRecord(func, *args, ** kwargs):
    best = 2**50
    for i in range(50):
        timecosume = timer(func,*args,iter = 1 ,**kwargs)
        if timecosume<best:
            best = timecosume
    return best

