# coding = utf-8
import hou
def print_tree(node, indent=0):
    for child in node.children():
        print(" "* indent +child.name())
        print_tree(child,indent+3)

