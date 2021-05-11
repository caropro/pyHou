#coding = utf-8
class person():
    def __init__(self,name="",age=0,salary=0):
        self.name = name
        self.age = age
        self.salary = salary
    def setAge(self,age):
        self.age = age
    def setSalary(self,salary):
        self.salary = salary
    def __str__(self):
        return "Name:{}\nAge:{}\nSalary:{}\n".format(self.name,self.age,self.salary)

class b(person):
    def __init__(self):
        person.__init__(self)

a = person("Jonathon")
a.setAge(43)
a.setSalary(45555)

print(a.__class__)

c = b()
print(c.__class__)