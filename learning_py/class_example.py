# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0

class Myclass():
    def __init__(self,a,b):
        self.initValue = 50
        self.a = a
        self.b = b
    def sum(self):
        print(self.a+self.b)

# class_instance = Myclass(15,20)
# class_instance.sum()

class Car():
    def __init__(self,name,engine,year):
        self.CarName = name
        self.engine = engine
        self.year = year

    def __str__(self):
        return "Current Info is %s" % self.CarName
    def print_name(self):
        print(self.CarName)
    def print_year(self):
        print(self.year)
    def print_engine(self):
        print(self.engine)

    def print_all(self):
        self.print_name()
        self.print_year()
        self.print_engine()

car_instance = Car(name="Shit Car",engine="Ruin Engine",year=55)
car_instance.print_all()

print(car_instance)