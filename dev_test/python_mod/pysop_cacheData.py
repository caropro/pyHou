#coding = utf-8
import hou
node = hou.pwd()
geo = node.geometry()

from random import uniform,seed
#create variable
null_pos = hou.Vector3()
def testCook():
    geoFromCache = None
    use_cache = hou.evalParm("use_cache")
    seed(hou.evalParm("seed"))
    npoints = hou.evalParm("npts")
    scale = hou.evalParm("scale")

    geo.addAttrib(hou.attribType.Point,"Cd",{0,0,0})
    for i in range(npoints):
        pt = geo.createPoint()
        pp = hou.Vector3(uniform(-1,1),0,uniform(-1,1))
        pt.setPosition(pp*scale)

    for pt in geo.iterPoints():
        dist = pt.position().distanceTo(null_pos)
        if dist>1.0:
            pt.setAttribValue("Cd",(0,0,0))
            continue
        dist_color = 1 - hou.hmath.smooth(dist,0.0,1.0)
        pt.setAttribValue("Cd",(dist_color,0,0))

testCook()





