import csv
import os

node = hou.pwd()
geo = node.geometry()
parent = node.parent().parent().parent()
# get file dir

setting_area = geo.point(0).attribValue("Area")

current_dir = os.path.dirname(parent.type().definition().libraryFilePath())
data_dir = os.path.join(current_dir.split("HouLand")[0], "HouLand\PublicDataHDAs\FoliageCluster_data", setting_area)

if (os.path.exists(data_dir)):
    flist = [f for f in os.listdir(data_dir) if f.endswith("csv")]

    init = 1;
    for file_data in flist:
        file_path = os.path.join(data_dir, file_data)
        data = []
        with open(file_path, "r") as datafile:
            d_Reader = csv.DictReader(datafile)
            reader = 1
            while reader:
                try:
                    reader = d_Reader.next()
                    data.append(reader)
                except:
                    reader = 0

        if data and init:
            # add parm
            geo.addAttrib(hou.attribType.Point, "rot", (0.0, 0.0, 0.0))
            geo.addAttrib(hou.attribType.Point, "scale", 0.0)
            geo.addAttrib(hou.attribType.Point, "Path", "")
        init = 0
        point_list = []
        for dataitem in data:
            exec ('pos = %s' % dataitem.get("Pos"))
            exec ('rot = %s' % dataitem.get("Rot"))
            p = geo.createPoint()
            point_list.append(p)
            p.setPosition(pos)
            p.setAttribValue("rot", rot)
            p.setAttribValue("Path", "StaticMesh'%s'" % dataitem.get("geoPath"))
            p.setAttribValue("scale", float(dataitem.get("scale")))

        poly = geo.createPolygon()
        for pt in point_list:
            poly.addVertex(pt)