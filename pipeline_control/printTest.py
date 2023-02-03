# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import hou
import math

def intersection(orgPoint,pointA,pointB):
    vector_u = pointA.position() - pointB.position()
    vector_v = orgPoint - pointB.position()

    project = vector_u.dot(vector_v)/vector_v.length()
    dist = math.sqrt(math.pow(vector_u.length(),2) - math.pow(project,2))
    intersect = pointB.position() + vector_u.normalized() * project
    return intersect , dist

def dist_to_line():
    node = hou.pwd()
    geo = node.geometry()
    try:
        curve_input = node.inputs()[1].geometry()
    except IndexError:
        raise hou.InvalidInput("Need Curve Data!")
    
    clr_attr = geo.addAttrib(hou.attribType.Point,"Cd",(0,1,0))
    dist_attr = geo.addAttrib(hou.attribType.Prim,"dist",0.0)

    line_group = geo.createPrimGroup("lines")
    base_group = geo.createPrimGroup("base")

    #set vt clr
    #set grp
    for prim in geo.prims():
        for vt in prim.vertices():
            vt.point().setAttribValue(clr_attr,(1,1,1))
        base_group.add(prim)

    curve_pts = curve_input.iterPoints()

    for prim in base_group.prims():
        org_pos = prim.positionAtInterior(0.5,0.5)
        intersect_pt , dist = intersection(org_pos,curve_pts[0],curve_pts[1])

        poly =geo.createPolygon()
        poly.setIsClosed(False)

        for pos in [org_pos,intersect_pt]:
            point = geo.createPoint()
            point.setPosition(pos)
            poly.addVertex(point)
            line_group.add(poly)






