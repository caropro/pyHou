#coding = utf-8
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
