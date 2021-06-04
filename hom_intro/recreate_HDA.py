#coding = utf-8
import hou


def hda_recreate():
    #select tar node
    target_node = hou.selectedNodes()[0]
    root_tar = target_node.parent().path()

    #create blank subnet node
    temp_node = hou.node(root_tar).createNode("subnet")

    hda_node = temp_node.createDigitalAsset()
