#coding = utf-8
def glob():
    global a
    a = 100

class Ca():
    va = 10
    def __init__(self):
        self.value = 222
    @staticmethod
    def print_test():
        print(a)
        print("Test Print")
    def print_test2(self):
        print(self.value)
    @classmethod
    def print_test3(cls):
        print(cls.va)

glob()
print(a)

Ca.print_test()

instance = Ca()
instance.value = 666
instance.print_test2()

Ca.print_test3()
