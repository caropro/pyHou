#coding = utf-8
import hou
import os

#获取当前节点
node = hou.pwd()
geo = node.geometry()

target_node = node.inputs()[1]
target_geo = target_node.geometry()
target_point = target_geo.point(0)
#获取传递的名称
file_name = target_point.attribValue("Seam_name")

