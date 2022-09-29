from view.View import View as v
import relationship as r
import UMLClass as u
import saveload as s
import relationship as r

class Controller:
    def __init__(self):
        self.view = v(self)

    def main(self):
        self.view.main()

    def clickAddClassButton(self):
        self.view.makeMessage("call addClass with: " + root.view.className)

    def clickDeleteClassButton(self):
        self.view.makeMessage("call deleteClass with: " + root.view.className)

    def clickRenameClassButton(self):
        print("do rename class stuff")
        self.view.makeMessage("call rename class with: " + root.view.className + " " + root.view.classNameNew)

    def clickAddRelationButton(self):
        print("do add relationship stuff")
        self.view.makeMessage("call addRelation with: " + root.view.source + " " + root.view.destination + " " + root.view.relationshipType )

    def clickUpdateTypeButton(self):
        self.view.makeMessage("update relation type w/ " + root.view.source + " " + root.view.destination + " " + root.view.relationshipTypeNew)

    def clickDeleteRelationButton(self):
        print("do add relationship stuff")
        self.view.makeMessage("call deleteRelation with: " + root.view.source + " " + root.view.destination  )

    def clickAddFieldButton(self):
        print("do add feild stuff")
        self.view.makeMessage("call add field with: " + root.view.className + " " + root.view.field + " " + root.view.fieldType)

    def clickDeleteFieldButton(self):   
        print("do delete feild stuff")
        self.view.makeMessage('call deleteField with ' + root.view.className + " " + root.view.field )

    def clickRenameFieldButton(self):
        print("do rename fields stuff")
        self.view.makeMessage("call renameField with " + root.view.className + " " + root.view.field + " " + root.view.feildNew)

    def clickAddMethodAndParamsButton(self):
        print("add method with no params")
        #error checking example (doesnt actually error check)
        #its just an example of how to remake the window and send error message if input is faulty
        if root.view.className == "error":
            #remake window and send error message
            root.view.inputFrame.destroy()
            root.view.makeInputFrame()
            root.view.makeAddMethodFrame()
            self.view.makeMessage('test entered cant proceed')
            return
        #otherwise make param window to add params 
        # and send success message     
        self.view.inputFrame.destroy()
        self.view.makeInputFrame()
        self.view.makeParamInputFrame()
        self.view.makeMessage('call addMethod with:' + self.view.className + " " + self.view.method + " " + self.view.methodReturnType)

    def clickAddMethodWithoutParamsButton(self):
        self.view.makeMessage('call addMethod with:' + self.view.className + " " + self.view.method + " " + self.view.methodReturnType)

    def clickAddParamButton(self):
        print("add params ")
        self.view.inputFrame.destroy()
        self.view.makeInputFrame()
        self.view.makeParamInputFrame()
        self.view.makeMessage("call addParam with " + root.view.className + " " + root.view.method + " " + root.view.param + " " + root.view.paramType )

    def clickDeleteMethodButton(self):
        print("do delete method stuff")
        self.view.makeMessage("call deleteMethod w/ " + self.view.className + " " + self.view.method)

    def clickUpdateMethodButton(self):
        print("do update method stuff")
        self.view.makeMessage('call renameMethod w/ ' + self.view.className + " " + self.view.method + " " + self.view.methodNew)

    def clickAddParamToMethodButton(self):
        #error checking 
        if root.view.className == "error":
            #remake window and send error message
            root.view.inputFrame.destroy()
            root.view.makeInputFrame()
            root.view.makeAddParamFrame()
            self.view.makeMessage('error entered cant proceed')
            return
        #otherwise make param window to add params 
        # and send success message     
        self.view.inputFrame.destroy()
        self.view.makeInputFrame()
        self.view.makeParamInputFrame()
        self.view.makeMessage('add params to :' + self.view.className + " " + self.view.method )
    
    def clickDeleteParamButton(self):
        #error checking 
        if root.view.className == "error":
            #remake window and send error message
            root.view.inputFrame.destroy()
            root.view.makeInputFrame()
            root.view.makeDeleteParamFrame()
            self.view.makeMessage('error entered cant proceed')
            return
        #otherwise make param window to add params 
        # and send success message     
        self.view.inputFrame.destroy()
        self.view.makeInputFrame()
        self.view.makeDeleteParamInputFrame()
        self.view.makeMessage('call deleteParam on: ' + self.view.className + " " + self.view.method )
    
    def clickDeleteAllParamButton(self):
        print('delete param')
        self.view.makeMessage('call deleteAll on: ' + self.view.className + " " + self.view.method)

    def clickSecondDeleteParamButton(self):
        print('delete param')
        self.view.makeMessage("call deleteParam on: " + self.view.className + " " + self.view.method + " " + self.view.param )

    def clickChangeParamButton(self):
        print("delete the param then add new param")
        #error checking 
        if root.view.className == "error":
            #remake window and send error message
            root.view.inputFrame.destroy()
            root.view.makeInputFrame()
            root.view.makeChangeParamFrame()
            self.view.makeMessage('error entered cant proceed')
            return
        #otherwise make param window to add params 
        # and send success message     
        self.view.inputFrame.destroy()
        self.view.makeInputFrame()
        self.view.makeChangeParamInputFrame()
        self.view.makeMessage('call deleteParam on: ' + self.view.className + " " + self.view.method )
    

    def clickChangeAllParamButton(self):
        print("delete the param then add new param")
        #error checking 
        if root.view.className == "error":
            #remake window and send error message
            root.view.inputFrame.destroy()
            root.view.makeInputFrame()
            root.view.makeChangeParamFrame()
            self.view.makeMessage('error entered cant proceed')
            return
        #otherwise make param window to add params 
        # and send success message     
        self.view.inputFrame.destroy()
        self.view.makeInputFrame()
        self.view.makeParamInputFrame()
        self.view.makeMessage('call deleteAllParam on: ' + self.view.className + " " + self.view.method )
    
    def clickChangeAnotherParamButton(self):
        self.view.inputFrame.destroy()
        self.view.makeInputFrame()
        self.view.makeChangeParamInputFrame()
        self.view.makeMessage('call deleteParam on: ' + self.view.className + " " + self.view.method + " " + self.view.param + " call addparam on: "  + self.view.className + " " + self.view.method + ' ' + self.view.paramNew + " " + self.view.paramType)

    #button not made yet
    def clickListAllClasses(self):
        print("print all classes")
        self.view.makeMessage()
    
    #button not made yet
    def clickListClass(self):
        print("list the class")
        self.view.makeMessage()

    #button not made yet
    def clickListRelationships(self):
        print("List the relationships")
        self.view.makeMessage()

    def clickSaveButton(self):
        print("call save")
        self.view.save()
        message = s.saveGUI(u.classIndex, r.relationIndex, self.view.fileName)
        #self.view.inputFrame.destroy()
        #self.view.makeInputFrame()
        #self.view.save()
        if message == "":
            self.view.makeMessage('Saved successfully')
        else:
            self.view.makeMessage(message)


    def clickLoadButton(self):
        print("call load")
        self.view.load()
        print(self.view.fileName)
        message = s.loadGUI(self.view.fileName)
        self.view.makeMessage(message)

root = Controller()
root.main()