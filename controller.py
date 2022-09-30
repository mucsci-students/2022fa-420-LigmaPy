from view.View import View as v
import relationship as r
import UMLClass as u
import saveload as s
import relationship as r

# Test code since nothing is hooked up
"""
class UMLClass:
    def __init__(self, name: str):
            self.name = name
            self.fields = []
            self.methods = []
        
class UMLMethod:
    def __init__(self, name: str, returnType = None):
        self.name = name
        self.return_type = returnType
        self.params = []

class UMLField:
    def __init__ (self, name: str , type = None):
        self.name = name
        self.type = type
    
class UMLParameters:
    def __init__ (self, name: str , type = None):
        self.name = name
        self.type = type

class UMLRelationship:
    def __init__ (self, source, destination, type):
        self.source = source
        self.destination = destination
        self.type = type

tire = UMLClass("Tire")
tiref1 = UMLField('diameter', 'float')
tiref2 = UMLField("psi", "float")
tiref3 = UMLField("brand", 'string')
tirem1 = UMLMethod('setPSI', 'void')
tirem1p1 = UMLParameters("new_psi", "string")
tirem1.params.append(tirem1p1)
tire.fields.append(tiref1)
tire.fields.append(tiref2)
tire.fields.append(tiref3)
tire.methods.append(tirem1)

car = UMLClass("Car")
carf1 = UMLField("make", 'string')
carf2 = UMLField("model", 'string')
carf3 = UMLField("year", "int")
carm1 = UMLMethod("drive", "void")
car.fields.append(carf1)
car.fields.append(carf2)
car.fields.append(carf3)
car.methods.append(carm1)

u.classIndex.append(tire)
u.classIndex.append(car)

r1 = UMLRelationship(tire, car, "composition")
r2 = UMLRelationship(car, tire, "Whatever")

r.relationIndex.append(r1)
r.relationIndex.append(r2)
"""

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

    def clickSaveButton(self):
        print("call save")
        self.view.save()
        message = s.saveGUI(u.classIndex, r.relationIndex, self.view.fileName)
        print(u.classIndex)
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

    def clickListClassButton(self):
        name = self.view.className
        index = u.findClass(name)
        if index == None:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeListClassFrame()
            self.view.makeMessage('Class does not exist')
        else:
            self.view.printClassToCanvas(u.classIndex[index])
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeListClassFrame()

    def clickListAllClassesButton(self):
        self.view.remake()
        if len(u.classIndex) == 0:
            self.view.makeMessage('No classes to list')
        else:
            self.view.printAllClassesToCanvas(u.classIndex)
            self.view.remake()

    def clickListRelationsButton(self):
        self.view.remake()
        if len(r.relationIndex) == 0:
            self.view.makeMessage("No relationships to list")
        else:
            self.view.printRelationsToCanvase(r.relationIndex)
            self.view.remake()

root = Controller()
root.main()


