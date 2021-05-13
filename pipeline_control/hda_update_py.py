#coding = utf-8
import hou
#get hda nodes
hda_nodes = hou.selectedNodes()

#get hda code
python_node = hou.node(hou.ui.selectNode())
python_code = python_node.parm("python").eval()

for hda_node in hda_nodes:
    hda_path = hda_node.type().definition().libraryFilePath()
    hda = hda_node.type().definition()

    python_module = hda.sections()["PythonModule"]
    python_module.setContents(python_code)
    hda.save(hda_path)
