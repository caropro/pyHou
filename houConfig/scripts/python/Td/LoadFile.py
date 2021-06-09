# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0

#file节点加载文件夹内的所有文件，逐个10个单位位置偏移
import hou
import os
#read file dir
tar_dir = hou.ui.selectFile(title="Select obj File Folder", file_type=hou.fileType.Directory)
tar_dir = tar_dir.replace("\\", "/")
filelist = os.listdir(tar_dir)
pre_boundx = 0
if tar_dir:
    root_node = hou.node("/obj").createNode("geo", "Loader")

    m_node = root_node.createNode("merge")
    for file in filelist:
        filename = os.path.splitext(file)[0]
        # create file node
        filenode = root_node.createNode("file", filename)
        # add path to file parm
        filepath = os.path.join(tar_dir, file)
        filenode.parm("file").set(filepath)

        # add transfrom node
        current_boundx = abs(filenode.geometry().boundingBox().minvec()[0])
        current_boundx_len = filenode.geometry().boundingBox().maxvec()[0]
        current_posx = current_boundx + pre_boundx + 10
        if pre_boundx == 0:
            pre_boundx = current_boundx_len
            m_node.setNextInput(filenode)
            continue
        trans = root_node.createNode("xform", "%s_trans" % filename)
        trans.parm("tx").set(current_posx)
        trans.setFirstInput(filenode)
        # after loop merge together
        m_node.setNextInput(trans)
        pre_boundx = current_posx + current_boundx_len

    m_node.moveToGoodPosition()
    root_node.layoutChildren()