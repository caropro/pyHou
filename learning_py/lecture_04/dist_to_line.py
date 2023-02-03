# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import math
import hou
import itertools


def intersection(centerPos, PtA, PtB):
    # 点A指向点B
    AtoB = PtB.position() - PtA.position()
    # 点A指向面中心
    AtoC = centerPos - PtA.position()
    # 点A指向面中心到点A指向B方向的分量大小
    projectDist = AtoC.dot(AtoB) / AtoB.length()
    # 应当直接投射的位置（垂直与这根线或者延长线的位置）
    projectPos = PtA.position() + AtoB.normalized() * projectDist

    dirDist = math.sqrt(math.pow(AtoC.length(), 2) - math.pow(projectDist, 2))

    return dirDist, projectPos


def cook():
    current_node = hou.pwd()
    geo = current_node.geometry()

    curveNode = current_node.inputs()[1]
    curve = curveNode.geometry()
    pt_1 = curve.iterPoints()[0]
    pt_2 = curve.iterPoints()[1]

    for prim in geo.prims():
        center = prim.positionAtInterior(0.5, 0.5)
        dirDist, projectPos = intersection(center, pt_1, pt_2)
        if not dirDist:
            continue

        poly = geo.createPolygon()
        poly.setIsClosed(False)

        for pos in [center, projectPos]:
            point = geo.createPoint()
            point.setPosition(pos)
            poly.addVertex(point)


cook()










