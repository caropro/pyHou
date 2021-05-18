# coding = utf-8
from __future__ import division
import math
import copy


class Vector3(object):
    def __init__(self, *args):
        if isinstance(args[0],(tuple,list)):
            self.x = args[0][0]
            self.y = args[0][1]
            self.z = args[0][2]
        elif isinstance(args[0], Vector3):
            self.x = args[0].x
            self.y = args[0].y
            self.z = args[0].z
        else:
            self.x = args[0]
            self.y = args[1]
            self.z = args[2]

    @classmethod
    def info(Vector3):
        print("version-0.0.1")
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_z = self.z + other.z
        return Vector3(new_x, new_y, new_z)

    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        new_z = self.z - other.z
        return Vector3(new_x, new_y, new_z)

    def __mul__(self, other):
        new_x = self.x * other.x
        new_y = self.y * other.y
        new_z = self.z * other.z
        return Vector3(new_x, new_y, new_z)

    def __div__(self, other):
        new_x = self.x / other.x
        new_y = self.y / other.y
        new_z = self.z / other.z
        return Vector3(new_x, new_y, new_z)

    def cross(self, other):
        new_x = self.y * other.z - self.z * other.y
        new_y = self.z * other.x - self.x * other.z
        new_z = self.x * other.y - self.y * other.z
        return Vector3(new_x, new_y, new_z)

    def dot(self, other):
        new_x = self.x * other.x
        new_y = self.y * other.y
        new_z = self.z * other.z
        return (new_x + new_y + new_z)

    def lenght(self):
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))

    def __repr__(self):
        return ("<{},{},{}>".format(self.x, self.y, self.z))

    def __getitem__(self, item):
        if (item == 0):
            return self.x
        elif (item == 1):
            return self.y
        elif (item == 2):
            return self.z
        else:
            raise IndexError("Out of the Size of the vector!")

    def __setitem__(self, key, value):
        if (key == 0):
            self.x = value
        elif (key == 1):
            self.y = value
        elif (key == 2):
            self.z = value
        else:
            raise IndexError("Out of the Size of the vector!")


v1 = Vector3(1, 2, 3)
v2 = Vector3(2, 4, 3)
# print(v1 + v2)
# print(v1 - v2)
# print(v1 * v2)
# copy.deepcopy()
# print(v1[2])
# v1[1] = 10
# print(v1)
# v3=Vector3(v1)
# print(v3)
# print("%s----%s"%(id(v1),id(v3)))
# print v1.dot(v2)
# print v1.cross(v2)
# print v1.lenght()


Vector3.info()