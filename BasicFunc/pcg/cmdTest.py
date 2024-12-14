# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import hou
import os
import threading
import operator
try:
    import pdgcmd
    import pdgjson
except ImportError:
    from pdgjob import pdgcmd
    from pdgjob import pdgjson

printlog = pdgcmd.printlog

def RunPDG(hipfile):
    # Set up PDGD
    terminate_event = threading.Event()
    printlog("Running Houdini {} with PID {}".format(
        hou.applicationVersionString(), os.getpid()))

    #Load File
    hou.hipFile.load(hipfile, suppress_save_prompt=True, ignore_load_warnings=True)

    # Get the pdg graph node
    pcgGraph = hou.node("/obj/Geo/pcgbuildingcalflow/PCGBuildingCalFlow")

    disp_node = pcgGraph.displayNode()

    printlog("Given Node '{}', Cooking Node '{}'".format(pcgGraph, disp_node),
            timestamp=True)

    # blocking cook of PDG
    disp_node.cookWorkItems(block=True)
    printlog("Finished Cook", timestamp=True)

