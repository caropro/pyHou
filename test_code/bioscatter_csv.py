import csv
import os
import hou


def EXport_csv():
    Folder = hou.pwd().parm("output_folder").evalAsString()
    if not os.path.exists(Folder):
        os.makedirs(Folder)

    data_node = hou.pwd().node("Export_csv")
    data_geo = data_node.geometry()
    point_dict = {}
    for point in data_geo.points():
        filename = point.attribValue("name")
        if not point_dict.get(filename):
            point_dict[filename] = []
        pos = []
        pos.append(point.attribValue("P")[0] * 100)
        pos.append(point.attribValue("P")[2] * 100)
        pos.append(point.attribValue("P")[1] * 100)
        point_dict[filename].append(pos)

    for name, points in point_dict.items():
        csv_path = Folder + name + ".csv"
        with open(csv_path, 'wb') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for pos in points:
                writer.writerow(pos)
