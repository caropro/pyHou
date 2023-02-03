# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import math
import hou


def intersection(center, PtA, PtB):
    AtoB = PtB.position() - PtA.position()
    AtoC = center - PtB.position()

    projectDist = AtoB.dot(AtoC) / AtoC.length()
    projectPos = PtA.position() + AtoB.normalized() * projectDist

    dirDist = math.sqrt(math.pow(AtoC.length(), 2) - math.pow(projectDist, 2))


def cook():
    current_node = hou.pwd()
    geo = current_node.geometry()

    curveNode = current_node.inputs()[1]
    curve = curveNode.geometry()
    pt_1 = curve.iterPoints()[0]
    pt_2 = curve.iterPoints()[1]

    for prim in geo.prims():
        center = prim.positionAtInterior(0.5, 0.5)
        intersection(center, pt_1, pt_2)










