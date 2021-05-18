#coding = utf-8
import time

def timer(func):
    def start_count(*args):
        current_time = time.time()
        try:
            return func(*args)
        finally:
            end_time = time.time()
            time_consume = end_time - current_time
            print(time_consume)
    return start_count

data_list = range(100000)

@timer
def cal(data):
    sum = 0
    for num in data:
        sum += num
    print("sum is : %s"% sum)
    return sum

cal(data_list)



