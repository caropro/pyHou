#coding = utf-8
import traceback
a = 1
try:
    a/0
except ZeroDivisionError as er:
    print (er)
    print (ZeroDivisionError("Zero Error!"))
finally:
    print ("Turn over")

