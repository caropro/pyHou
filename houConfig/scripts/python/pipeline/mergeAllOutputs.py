#coding = utf-8
import hou

def run():
    n = hou.selectedNodes()[0]
    parent = n.parent()
    if n!=None:
        m = parent.createNode("merge")
        outputlist = n.outputLabels()
        print(outputlist)
        index = 0
        for name in outputlist:
            print(name)
            name = name.replace(" ","_")
            outputNull = parent.createNode("null",name)
            outputNull.setInput(0,n,index)
            m.setInput(index,outputNull,0)
            index+=1
        parent.layoutChildren()