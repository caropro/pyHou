# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import hou
def unlockChildren(node):
    for child_node in node.children():
        child_node.allowEditingOfContents(1)
        try:
            unlockChildren(child_node)
        except:
            continue

node = hou.selectedNodes()[0]
node.allowEditingOfContents(1)
unlockChildren(node)