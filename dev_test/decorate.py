#coding = utf-8

def print_val(func,*args):
    def wrapped(args):
        for arg in args:
            print(arg)
        return func(args)
    return wrapped

val_list = [1,2,3,4,5]

@print_val
def cal(a_list):
    sum = 0;
    for a in a_list:
        sum += a
    print("sum = %s"%sum)
    return sum



cal(val_list)