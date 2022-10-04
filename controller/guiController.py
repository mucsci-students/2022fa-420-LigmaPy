import tkinter as tk
import view.imbededFrames as iFrame

class GUIController:
    def __init__(self):
        self.className = None
        self.classNameNew = None
        self.source = None
        self.destination = None
        self.relationshipType = None
        self.relationshipTypeNew = None
        self.field = None
        self.feildNew = None
        self.fieldType = None
        self.method = None
        self.methodReturnType = None
        self.methodNew = None
        self.param = None
        self.paramNew = None
        self.paramType = None
        self.paramTypeNew = None

        self.inputFrame = iFrame.makeInputFrame()

    def clear(self):
        self.className = None
        self.classNameNew = None
        self.source = None
        self.destination = None
        self.relationshipType = None
        self.relationshipTypeNew = None
        self.field = None
        self.feildNew = None
        self.fieldType = None
        self.method = None
        self.methodReturnType = None
        self.methodNew = None
        self.param = None
        self.paramNew = None
        self.paramType = None
        self.paramTypeNew = None

    def wipe(self):
        """
            Destroys the imbedded frame


        """
        self.inputFrame.destroy()
        self.inputFrame = iFrame.makeInputFrame()

    def addClassFrame(self):
        self.wipe()
        iFrame.makeAddClassFrame()

    def deleteClassFrame(self):
        self.wipe()
        iFrame.makeDeleteClassFrame()

    def renameClassFrame(self):
        self.wipe()
        iFrame.makeRenameClassFrame()

    def addRelationFrame(self):
        self.wipe()
        iFrame.makeAddRelationFrame()

    def deleteRelationFrame(self):
        self.wipe()
        iFrame.makeDeleteRelationFrame()

    def updateRelationType(self):
        self.wipe()
        iFrame.makeUpdateRelationType()

    def addFieldFrame(self):
        self.wipe()
        iFrame.makeAddFieldFrame()

    def deleteFieldFrame(self):
        self.wipe()
        iFrame.makeDeleteFieldFrame()

    def renameFieldFrame(self):
        self.wipe()
        iFrame.makeRenameFieldFrame()

    def addMethodFrame(self):
        self.wipe()
        iFrame.makeAddMethodFrame()

    def deleteMethodFrame(self):
        self.wipe()
        iFrame.makeDeleteMethodFrame()

    def renameMethodFrame(self):
        self.wipe()
        iFrame.makeRenameMethodFrame()

    def addParamFrame(self):
        self.wipe()
        iFrame.makeAddParamFrame()

    def deleteParamFrame(self):
        self.wipe()
        iFrame.makeDeleteParamFrame()

    def changeParamFrame(self):
        self.wipe()
        iFrame.makeChangeParamFrame()


