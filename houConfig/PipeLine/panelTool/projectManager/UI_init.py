# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
from hutil.Qt import QtWidgets
import os
import hou
import sys
import json
import copy

current_path = os.path.dirname(__file__)
sys.path.append(current_path)

from PySide2 import QtWidgets
from PySide2 import QtUiTools
class ProjectManager(QtWidgets.QWidget):
    def __init__(self):
        super(ProjectManager, self).__init__()
        self.projectDir = ""
        self.projectName = ""
        self.recentRecord = ""
        self.init_UI()

    def init_UI(self):
        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(os.path.join(current_path, "pm_ui.ui"))
        self.recentRecord = os.path.join(current_path,"projectRecord.json")
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.ui)
        self.setLayout(self.layout)
        self.connectSignal()
        self.loadRecent()

    def connectSignal(self):
        self.ui.ChangeBtm.clicked.connect(self.setProject)
        self.ui.FileList.doubleClicked.connect(self.openScene)
        self.ui.RefreshBtm.clicked.connect(self.refresh)

    def setProject(self,Load = False):
        if Load:
            hou.hscript("setenv JOB=" + self.projectDir)
            self.ui.ProjectPath.setText(self.projectDir)
            self.ui.ProjectName.setText(self.projectName)
            self.updateFiles()
            self.record()
        else:
            self.projectDir = hou.ui._selectFile(title="Select Project Folder",file_type=hou.fileType.Directory)
            if(self.projectDir):
                hou.hscript("setenv JOB=" + self.projectDir)
                self.projectDir = os.path.dirname(self.projectDir)
                self.projectName = self.projectDir.split("/")[-1]

                self.ui.ProjectPath.setText(self.projectDir)
                self.ui.ProjectName.setText(self.projectName)
                self.updateFiles()
                self.record()


    def updateFiles(self):
        hiplist = [file for file in os.listdir(self.projectDir) if file.endswith(".hip")]
        self.ui.FileList.clear()
        for file in hiplist:
            self.ui.FileList.addItem(file)


    def openScene(self,item):
        print(item.data())
        HipPath = os.path.join(self.projectDir,item.data())
        hou.hipFile.load(HipPath)

    def record(self):
        RecordDict = {}
        if os.path.exists(self.recentRecord):
            with open(self.recentRecord,"r") as jsonFile:
                all_info = jsonFile.read()
                RecordDict = json.loads(all_info)
                RecordDict[self.projectName] = self.projectDir
            with open(self.recentRecord, "w") as jsonFile:
                json.dump(RecordDict, jsonFile)
        else:
            with open(self.recentRecord,"w+") as jsonFile:
                RecordDict[self.projectName] = self.projectDir
                json.dump(RecordDict, jsonFile)
    def loadRecord(self):
        pass

    def refresh(self):
        self.updateFiles()

    def loadRecent(self):
        print("Recent")
        if os.path.exists(self.recentRecord):
            with open(self.recentRecord,"r") as jsonFile:
                all_info = jsonFile.read()
                RecordDict = json.loads(all_info)

            self.projectName,self.projectDir = RecordDict.popitem()
            if(os.path.exists(self.projectDir)):
                self.setProject(Load=True)
