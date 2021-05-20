#coding = utf-8
import hou

node = hou.pwd()
geo = node.geometry()

# Add code to modify contents of geo.
# Use drop down menu to select examples.
input_node = node.inputConnections()[1].inputNode()

geo2 = input_node.geometry()
# 设置数据字典，键为area类型，对为tile位置标号
data_dict = {}
# 设置数据字典，键为tile位置标号，值为area类型，目的在于跳过所有非标注区域
tile_dict = {}
# 设置数据列表，被标记过的tile进行记录，之后的查找会进行略过
total_tile_list = []
#设置数据字典，将当前area中所有边界tile相邻的area类型进行记录
area_seamType = {}

seam_dict = {}
area_count = input_node.parm("area_list").eval()

#split mode selection
mode = node.parm("seamType").eval()

#tile split
for i in range(area_count):
    count = i + 1
    area_code = "area_name_{}".format(count)
    area_name = input_node.parm(area_code).eval()
    tile_list_code = "tile_list_{}".format(count)
    tile_list = input_node.parm(tile_list_code).eval()
    tile_list = tile_list.split(" ")
    data_dict[area_name] = []
    for tile in tile_list:
        data_dict[area_name].append(tile)
        tile_dict[tile] = area_name


def gen_targettiles(tile):
    """
    公用数据处理，生成器
    :param tile:
    :return:
    """
    tile_x, tile_y = tile.split(",")
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            new_x = int(tile_x) + x
            new_y = int(tile_y) + y
            if new_x >= 0 and new_y >= 0:
                # 组装坐标位置
                target_tile = "{},{}".format(new_x, new_y)
                yield target_tile

#公用数据处理，生成器
def gen_targetTile(tile_list):
    for tile in tile_list:
        tile_x, tile_y = tile.split(",")
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                new_x = int(tile_x) + x
                new_y = int(tile_y) + y
                if new_x >= 0 and new_y >= 0:
                    # 组装坐标位置
                    target_tile = "{},{}".format(new_x,new_y)
                    yield target_tile,tile

def intersect_loop(start_tile,seam_dict,seam_name,tile_dict,total_tile_list,area_target,area):
    if start_tile not in total_tile_list:
        # 目标位置不在筛选列表时，添加标记
        total_tile_list.append(start_tile)
        #获取这个tile周边的tile信息
        for target_tile in gen_targettiles(start_tile):
            #所属area相同，且未经过处理，且有对外相邻
            if tile_dict.get(target_tile) == area and target_tile not in total_tile_list and area_target.get(target_tile)>1:
                #添加到当前数据中
                seam_dict[seam_name].append(target_tile)
                #进行嵌套挖掘
                seam_dict,total_tile_list = intersect_loop(target_tile,seam_dict,seam_name,tile_dict,total_tile_list,area_target,area)
            if tile_dict.get(target_tile) != None and tile_dict.get(target_tile) != area:
                # 如果判断区域非空白区时才会进行下一步
                if target_tile not in total_tile_list:
                    # 非当前area的临近tile添加标记
                    total_tile_list.append(target_tile)
                    seam_dict[seam_name].append(target_tile)
        return seam_dict,total_tile_list
    else:
        #当前tile已经过处理标注，直接返回原有数据
        return seam_dict,total_tile_list

area_target = {}
for area, tile_list in data_dict.items():
    #总的数据记录，记录每个tile相邻的area种类
    for target_tile, tile in gen_targetTile(tile_list):
        seam_area = tile_dict.get(target_tile)
        if tile_dict.get(target_tile) != None:
            #将周围所有area类型添加到当前tile的表中
            if area_seamType.get(tile):
                area_seamType[tile].append(seam_area)
            else:
                area_seamType[tile] = [area, seam_area]
    for tile, area_list in area_seamType.items():
        if area_list:
            # 去除重复
            clean_list = list(set(area_list))
            area_num = len(clean_list)
            clean_list.sort()
            area_seamType[tile] = clean_list
            area_target[tile] = area_num

    # todo 以area为核心的标注当前area所能记录的所有边界信息
    if mode == 1:  # 整体型，将当前area的边界完整标记出来
        total_tile_list = []
        # 组装分类名称
        new_name = "{}_seam".format(area)
        seam_dict[new_name] = []
        for target_tile,tile in gen_targetTile(tile_list):
            #扩展范围的添加
            if target_tile not in total_tile_list:
                total_tile_list.append(target_tile)
                if tile_dict.get(target_tile) != area and tile_dict.get(target_tile) != None:
                    seam_dict[new_name].append(target_tile)
                #自身范围的添加
                elif tile_dict.get(target_tile) == area:
                    total_tile_list.append(target_tile)
                    if area_target[target_tile] >1:
                        seam_dict[new_name].append(target_tile)

    # todo 如果当前tile附近超过两种area存在时，需要进行判断处理将所有连续的tile内容都包含进来
    elif mode == 2:#连续型，列出当前area中所有边界tile的交界数量，从最多的开始处理，如果相邻tile为当前area内部tile，则嵌套进行下一步筛查
        area_target = {}
        for target_tile,tile in gen_targetTile(tile_list):
            # 如果临近位置与当前tile属于同一块区域，跳过（只有当前tile会在边界判断时添加本area的内容）
            if tile_dict.get(target_tile) == area:
                continue
            if tile_dict.get(target_tile) != None:
                #获取当前tile临近的所有area名称
                seam_area = tile_dict.get(target_tile)
                if area_seamType.get(tile):
                    area_seamType[tile].append(seam_area)
                else:
                    area_seamType[tile] = [area,seam_area]
        for tile,area_list in area_seamType.items():
            #去除重复
            clean_list = list(set(area_list))
            area_num = len(clean_list)
            area_seamType[tile] = clean_list
            area_target[tile] = area_num
        #根据临近数量决定起始tile
        area_seamType_list = sorted(area_seamType.items(),key=lambda x:x[1])
        for start_tile,area_name in area_seamType_list:
            if start_tile not in total_tile_list and area_target.get(start_tile)>1:
                #开辟数据存储
                seam_name = "_".join(area_name)
                if not seam_dict.get(seam_name):
                    seam_dict[seam_name] = [start_tile]
                # else:
                #     seam_dict[seam_name].append(start_tile)
                #进行处理
                seam_dict,total_tile_list = intersect_loop(start_tile,seam_dict,seam_name,tile_dict,total_tile_list,area_target,area)

#获得完整数据后进程条件0的判断
if mode == 0:  # 配对型，处理一种area与另一种的交界
    #按照临近area数量进行排序，从最多的开始排除
    resort_area_target = sorted(area_target.items(),key=lambda x:x[1],reverse = 1)
    for tile,area_num in resort_area_target:
        current_name = "_".join(area_seamType[tile])
        # 如果当前tile没有被处理过，并且对外有临近area存在
        if tile not in total_tile_list and area_num>1:
            total_tile_list.append(tile)
            # 为当前seam类添加当前tile
            seam_dict[current_name] = [tile]
            #查找四周的tile
            for target_tile in gen_targettiles(tile):
                # 如果目标tile没有临近area，或与当前tile相同，跳过
                if target_tile not in total_tile_list and area_target[target_tile] > 1 and "_".join(area_seamType.get(target_tile)) == current_name:
                    seam_dict[current_name].append(target_tile)
                    total_tile_list.append(target_tile)
        else:
            #不符合条件的直接跳过
            total_tile_list.append(tile)
            continue

# #获得完整数据后进程条件0的判断
# if mode == 0:  # 配对型，处理一种area与另一种的交界
#     #按照临近area数量进行排序，从最多的开始排除
#     resort_area_target = sorted(area_target.items(),key=lambda x:x[1],reverse = 1)
#     for tile,area_num in resort_area_target:
#         current_name = "_".join(area_seamType[tile])
#         if not seam_dict.get(current_name):
#             seam_dict[current_name] = []
#         if area_num>1 and tile not in total_tile_list:
#             seam_dict[current_name].append(tile)
#             total_tile_list.append(tile)


#最后去除重复内容
for final_seam_name, final_tile_list in seam_dict.items():
    # 去除重复
    clean_list = list(set(final_tile_list))
    seam_dict[final_seam_name] = clean_list

#print(seam_dict)
tile_attr = geo.addAttrib(hou.attribType.Point, "tile",'')
name_attr = geo.addAttrib(hou.attribType.Point, "Seam_name",'')
pos_attr = geo.addAttrib(hou.attribType.Point, "Pos",0)
for seam_name,tile_list in seam_dict.items():
    for tile in tile_list:
        pt = geo.createPoint()
        pt.setAttribValue(name_attr,seam_name)
        tile_x,tile_y = tile.split(",")
        tile_x = int(tile_x)
        tile_y = int(tile_y)
        pos = (tile_x-1)*geo2.attribValue("TileDivide")+tile_y-1
        pt.setAttribValue(pos_attr,pos)
        pt.setAttribValue(tile_attr,tile)