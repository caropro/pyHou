import os
import hou
node = hou.pwd()
geo = node.geometry()
tileAttr = geo.addAttrib(hou.attribType.Point, "tilename", "x")
parent = node.inputs()[1]
try:
    HDAPath = node.parent().type().definition().libraryFilePath()
    GeoPath = os.path.join(HDAPath.split("OperatorHDAs")[0], "LandscapeHDAs");

    TileName = node.parent().parent().parent().parent().name()
    if "R" in TileName:
        tile_x = 8 + int(TileName[-3])
    else:
        tile_x = 9 - int(TileName[-3])
    if "U" in TileName:
        tile_y = 8 + int(TileName[-1])
    else:
        tile_y = 9 - int(TileName[-1])

    locator_list = [(x, y) for y in [tile_y, tile_y + 1, tile_y - 1] for x in [tile_x, tile_x + 1, tile_x - 1]]
    print(locator_list)

    for loc in locator_list:
        xName = ""
        yName = ""
        x, y = loc
        if (x <= 8):
            xName = "L" + str(9 - x)
        else:
            xName = "R" + str(x - 8)
        if (y <= 8):
            yName = "D" + str(9 - y)
        else:
            yName = "U" + str(y - 8)

        tilename = "Tile_{}{}.bgeo".format(xName, yName)
        seamname = "Seamed_%s" % tilename
        tile_path = os.path.normpath(os.path.join(GeoPath, tilename))
        seam_path = os.path.normpath(os.path.join(GeoPath, seamname))
        point = geo.createPoint()
        if (os.path.exists(seam_path)):
            point.setAttribValue(tileAttr, seam_path)
        else:
            point.setAttribValue(tileAttr, tile_path)
except:
    pass