import numpy
from math import sqrt
import hou

node = hou.pwd()
geo = node.geometry()
# refgeo
node1 = node.inputs()[1]
geo1 = node1.geometry()
node2 = node.inputs()[2]
geo2 = node2.geometry()

dist = 20;


def vectorDis(v1, v2):
    dist = sqrt(pow(v1[0] - v2[0], 2) + pow(v1[1] - v2[1], 2) + pow(v1[2] - v2[2], 2))
    if dist < 3:
        return 1
    else:
        return 0


pts = geo1.iterPoints()
pts2 = geo2.iterPoints()
pos_list = [p.position() for p in pts]
pos_list2 = [p.position() for p in pts2]

poscreate = [(x, y) for x in pos_list for y in pos_list2 if vectorDis(x, y)]

geo.addAttrib(hou.attribType.Point, "Cd", (0, 1, 0))
for pos in poscreate:
    x, y = pos
    apt = geo.createPoint()
    apt.setPosition(x)
    bpt = geo.createPoint()
    bpt.setPosition(y)
    poly = geo.createPolygon()
    poly.setIsClosed(False)
    poly.addVertex(apt)
    poly.addVertex(bpt)