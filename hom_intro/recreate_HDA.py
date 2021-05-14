#coding = utf-8
import hou,os

def hda_recreate():
    #select tar node
    target_node = hou.selectedNodes()[0]
    root_tar = target_node.parent().path()
    print root_tar

    #create blank subnet node
    temp_node = hou.node(root_tar).createNode("subnet")

    hda_node = temp_node.createDigitalAsset()
