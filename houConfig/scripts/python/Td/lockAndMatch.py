# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import hou


def lockChildren(node):
    for child_node in node.children():
        child_node.matchCurrentDefinition(0)
        try:
            lockChildren(child_node)
        except:
            continue


node = hou.selectedNodes()[0]
lockChildren(node)
node.matchCurrentDefinition(0)
