# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0


class vector3(object):
    def __init__(self,*args):
        if isinstance(args[0],list):
            self.x = args[0][0]
            self.y = args[0][1]
            self.z = args[0][2]
        elif isinstance(args[0],vector3):
            self.x = args[0].x
            self.y = args[1].y
            self.z = args[2].z
        else:
            self.x = args[0]
            self.y = args[1]
            self.z = args[2]

    def __str__(self):
        return "Value of Vector is {0},{1},{2}".format(self.x,self.y,self.z)

    def __add__(self, other):
        result_x = self.x + other.x
        result_y = self.y + other.y
        result_z = self.z + other.z
        return(vector3(result_x,result_y,result_z))

    def __sub__(self, other):
        result_x = self.x + other.x
        result_y = self.y + other.y
        result_z = self.z + other.z
        return(vector3(result_x,result_y,result_z))

    def __mul__(self, other):
        result_x = self.x * other.x
        result_y = self.y * other.y
        result_z = self.z * other.z
        return (vector3(result_x, result_y, result_z))

    def __truediv__ (self, other):
        result_x = self.x / other.x
        result_y = self.y / other.y
        result_z = self.z / other.z
        return (vector3(result_x, result_y, result_z))

    def __getitem__(self, item):
        if item == 0:
            print(self.x)
        elif item ==1 :
            print(self.y)
        elif item == 2:
            print(self.z)
        else:
            raise IndexError("Index does not exist for current vector3 .")

    def __setitem__(self, key, value):
        if key == 0:
            self.x = value
        elif key ==1 :
            self.y = value
        else:
            self.z = value

a = vector3(1,2,3)
b = vector3(3,2,1)

print(a)
print(a/b)
print(a+b)