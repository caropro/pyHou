#coding = utf-8
num_list = [1,2,[4,5],[6,7,8]]

def cal_numlist(L):
    sum = 0
    for ele in L:
        if not isinstance(ele,list):
            sum+=ele
        else:
            sum+=cal_numlist(ele)
    return sum

# print cal_numlist(num_list)
#
# print(dir(cal_numlist))
#
# print(cal_numlist.func_code)
#
# print(cal_numlist.__code__.co_varnames)

print filter((lambda x:x>5),[2,3,4,5,1,6,7,0])




