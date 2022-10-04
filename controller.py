from view.View import View as v
import relationship as r
import UMLClass as u
import saveload as s
import relationship as r
import attributes as a
import parameter as p


class Controller:
    def __init__(self):
        self.view = v(self)

    def main(self):
        self.view.main()

    def clickAddClassButton(self):
        num = u.addClass(root.view.className)
        if num == -1:
            root.view.inputFrame.destroy()
            root.view.makeInputFrame()
            root.view.makeAddClassFrame()
            self.view.makeMessage("Class name cannot be empty.")
        elif num == -2:
            root.view.inputFrame.destroy()
            root.view.makeInputFrame()
            root.view.makeAddClassFrame()
            self.view.makeMessage(f"\nClass \"{root.view.className}\" already exists, could not create.")            
        else:
            root.view.remake()
            root.view.makeAddClassFrame()
            self.view.makeMessage(f"\nClass \"{root.view.className}\" has been created!")

    def clickDeleteClassButton(self):
        num = u.deleteClass(root.view.className)
        if num == -1:
            root.view.remake()
            root.view.makeDeleteClassFrame()
            self.view.makeMessage(f"\nClass \"{ root.view.className}\" does not exist")
        else:
            root.view.remake()
            root.view.makeDeleteClassFrame()
            self.view.makeMessage(f"\nClass \"{root.view.className}\" has been deleted.")

    def clickRenameClassButton(self):
        num = u.renameClass(root.view.className, root.view.classNameNew)
        if num == -1:
            root.view.remake()
            root.view.makeRenameClassFrame()
            self.view.makeMessage(f"\nA class already exists with the name \"{root.view.classNameNew}\"")
        elif num == -2:
            root.view.remake()
            root.view.makeRenameClassFrame()
            self.view.makeMessage(f"\nClass \"{root.view.className}\" does not exist")
        else:
            root.view.remake()
            root.view.makeRenameClassFrame()
            self.view.makeMessage("Class renamed")
        
    def clickAddRelationButton(self):
        num = r.addRelationship( root.view.source, root.view.destination, root.view.relationshipType)
        if num == -2:
            self.view.remake()
            self.view.makeAddRelationFrame()
            self.view.makeMessage("Source and destination cannot be the same")
        elif num == -1:
            self.view.remake()
            self.view.makeAddRelationFrame()
            self.view.makeMessage("Source or destination does not exist")
        elif num == -3:
            self.view.remake()
            self.view.makeAddRelationFrame()
            self.view.makeMessage("Relationship already exists")
        else:
            self.view.remake()
            self.view.makeAddRelationFrame() 
            self.view.makeMessage("Relationship added")

    def clickUpdateTypeButton(self):
        num = r.findRelationship(root.view.source, root.view.destination)
        if num == -1:
            self.view.remake()
            self.view.makeUpdateRelationType()
            self.view.makeMessage("Relationship does not exist")
        else:
            r.relationIndex[num].editType(self.view.relationshipTypeNew)
            self.view.remake()
            self.view.makeUpdateRelationType()
            self.view.makeMessage("Relationship type updated")       
    
    def clickDeleteRelationButton(self):
        num = r.deleteRelationship( root.view.source, root.view.destination)
        if num == -1:
            self.view.remake()
            self.view.makeDeleteRelationFrame()
            self.view.makeMessage("Relationship does not exist")
        else:
            self.view.remake()
            self.view.makeDeleteRelationFrame()
            self.view.makeMessage("Relationship deleted")

    def clickAddFieldButton(self):
        num = a.addField(root.view.field, root.view.className, root.view.fieldType)
        if num == -1:
            self.view.remake()
            self.view.makeAddFieldFrame()
            self.view.makeMessage("Class does not exist")
        elif num == -2:
            self.view.remake()
            self.view.makeAddFieldFrame()
            self.view.makeMessage("Field already exists")
        else:
            self.view.remake()
            self.view.makeAddFieldFrame()
            self.view.makeMessage("Field added")

    def clickDeleteFieldButton(self):   
        num = a.deleteField(root.view.field, root.view.className)
        if num == -1:
            self.view.remake()
            self.view.makeDeleteFieldFrame()
            self.view.makeMessage("Class does not exist")
        elif num == -2:
            self.view.remake()
            self.view.makeDeleteFieldFrame()
            self.view.makeMessage("Field does not exist")
        else:
            self.view.remake()
            self.view.makeDeleteFieldFrame()
            self.view.makeMessage("Field deleted")

    def clickRenameFieldButton(self):
        num = a.renameField(root.view.field, root.view.feildNew, root.view.className)
        if num == -1:
            self.view.remake()
            self.view.makeRenameFieldFrame()
            self.view.makeMessage("Class does not exist")
        elif num == -2:
            self.view.remake()
            self.view.makeRenameFieldFrame()
            self.view.makeMessage("Field does not exists to rename")
        elif num == -3:
            self.view.remake()
            self.view.makeRenameFieldFrame()
            self.view.makeMessage("Another field already exists with that name")
        else:
            self.view.remake()
            self.view.makeDeleteFieldFrame()
            self.view.makeMessage("Field renamed")
    
    def clickAddMethodAndParamsButton(self):

        num = a.addMethod(self.view.method, self.view.className, self.view.methodReturnType)
        if num == -1:
            root.view.inputFrame.destroy()
            root.view.makeInputFrame()
            root.view.makeAddMethodFrame()
            self.view.makeMessage("Class does not exist")
        elif num == -2:
            root.view.inputFrame.destroy()
            root.view.makeInputFrame()
            root.view.makeAddMethodFrame()
            self.view.makeMessage("Method already exists")
        else:       
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeParamInputFrame()
            self.view.makeMessage("Method added, please enter parameter(s)")

    def clickAddMethodWithoutParamsButton(self):
        num = a.addMethod(self.view.method, self.view.className, self.view.methodReturnType)
        if num == -1:
            root.view.inputFrame.destroy()
            root.view.makeInputFrame()
            root.view.makeAddMethodFrame()
            self.view.makeMessage("Class does not exist")
        elif num == -2:
            root.view.inputFrame.destroy()
            root.view.makeInputFrame()
            root.view.makeAddMethodFrame()
            self.view.makeMessage("Method already exists")
        else:       
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeAddMethodFrame()
            self.view.makeMessage("Method added")

    def clickAddParamButton(self):
        if len(self.view.param) == 0:
            root.view.inputFrame.destroy()
            root.view.makeInputFrame()
            root.view.makeParamInputFrame()
            self.view.makeMessage('Parameter name cannot be empty')
            return 
        l = [(root.view.param, root.view.paramType)]
        num = p.addParameter(l, self.view.method, self.view.className)
        if num == -1:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeParamInputFrame()
            self.view.makeMessage("Class does not exist")
        elif num == -2:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeParamInputFrame()
            self.view.makeMessage("Method does not exist in class")
        elif num == -3:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeParamInputFrame()
            self.view.makeMessage("Parameter already exists in method")
        else:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeParamInputFrame()
            self.view.makeMessage("Parameter added")            

    def clickDeleteMethodButton(self):
        num = a.deleteMethod(self.view.method, self.view.className)
        if num == -1:
            self.view.remake()
            self.view.makeDeleteMethodFrame()
            self.view.makeMessage("Class does not exist")
        elif num == -2:
            self.view.remake()
            self.view.makeDeleteMethodFrame()
            self.view.makeMessage("Method does not exist")  
        else:
            self.view.remake()
            self.view.makeDeleteMethodFrame()
            self.view.makeMessage("Method Deleted")          


    def clickUpdateMethodButton(self):
        num = a.renameMethod(self.view.method, self.view.methodNew, self.view.className)
        if num == -1:    
            self.view.remake()
            self.view.makeRenameMethodFrame()
            self.view.makeMessage('Class does not exist')
        elif num == -2:    
            self.view.remake()
            self.view.makeRenameMethodFrame()
            self.view.makeMessage('Method does not exist to rename')
        elif num == -3:    
            self.view.remake()
            self.view.makeRenameMethodFrame()
            self.view.makeMessage('New method name already exists')
        else:    
            self.view.remake()
            self.view.makeRenameMethodFrame()
            self.view.makeMessage('Method renamed')

    def clickAddParamToMethodButton(self):
        num = a.findMethod(self.view.method, self.view.className)
        if num == -1:
            root.view.inputFrame.destroy()
            root.view.makeInputFrame()
            root.view.makeAddParamFrame()
            self.view.makeMessage('Class does not exist')
        elif num == -2:
            root.view.inputFrame.destroy()
            root.view.makeInputFrame()
            root.view.makeAddParamFrame()
            self.view.makeMessage('Method does not exist in class')
        else:  
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeParamInputFrame()
 
    def clickDeleteParamButton(self):
        num = a.findMethod(self.view.method, self.view.className)
        if num == -1:
            root.view.inputFrame.destroy()
            root.view.makeInputFrame()
            root.view.makeDeleteParamFrame()
            self.view.makeMessage('Class does not exist')
        elif num == -2:
            root.view.inputFrame.destroy()
            root.view.makeInputFrame()
            root.view.makeDeleteParamFrame()
            self.view.makeMessage('Method does not exist in class')
        else:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeDeleteParamInputFrame()
    
    def clickDeleteAllParamButton(self):
        num = p.deleteAllParameter(self.view.method, self.view.className)
        if num == -1:
            root.view.inputFrame.destroy()
            root.view.makeInputFrame()
            root.view.makeDeleteParamFrame()
            self.view.makeMessage('Class does not exist')
        elif num == -2:
            root.view.inputFrame.destroy()
            root.view.makeInputFrame()
            root.view.makeDeleteParamFrame()
            self.view.makeMessage('Method does not exist in class')
        else:
            root.view.inputFrame.destroy()
            root.view.makeInputFrame()
            root.view.makeDeleteParamFrame()
            self.view.makeMessage('All parameters deleted')
    
    def clickSecondDeleteParamButton(self):
        if len(self.view.param) == 0:
            root.view.inputFrame.destroy()
            root.view.makeInputFrame()
            root.view.makeDeleteParamInputFrame()
            self.view.makeMessage('Parameter does not exist')
            return
        l = [self.view.param]
        num = p.deleteParameter(l, self.view.method, self.view.className)
        if num == -1:
            root.view.inputFrame.destroy()
            root.view.makeInputFrame()
            root.view.makeDeleteParamInputFrame()
            self.view.makeMessage("Class does not exist")
        elif num == -2:
            root.view.inputFrame.destroy()
            root.view.makeInputFrame()
            root.view.makeDeleteParamInputFrame()
            self.view.makeMessage('Method does not exist in class')
        elif num == -3:
            root.view.inputFrame.destroy()
            root.view.makeInputFrame()
            root.view.makeDeleteParamInputFrame()
            self.view.makeMessage('Parameter does not exist in method')
        else:
            root.view.inputFrame.destroy()
            root.view.makeInputFrame()
            root.view.makeDeleteParamInputFrame()
            self.view.makeMessage('Parameter deleted')

    def clickChangeParamButton(self):
        num = a.findMethod(self.view.method, self.view.className)
        if num == -1:
            root.view.inputFrame.destroy()
            root.view.makeInputFrame()
            root.view.makeChangeParamFrame()
            self.view.makeMessage('Class does not exist')
        elif num == -2:
            root.view.inputFrame.destroy()
            root.view.makeInputFrame()
            root.view.makeChangeParamFrame()
            self.view.makeMessage('Method does not exist in class')
        else:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeChangeParamInputFrame()                

    def clickChangeAllParamButton(self):
        num = p.deleteAllParameter(self.view.method, self.view.className)
        if num == -1:
            root.view.inputFrame.destroy()
            root.view.makeInputFrame()
            root.view.makeChangeParamFrame()
            self.view.makeMessage('Class does not exist')
        elif num == -2:
            root.view.inputFrame.destroy()
            root.view.makeInputFrame()
            root.view.makeChangeParamFrame()
            self.view.makeMessage('Method does not exist in class')
        else:   
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeParamInputFrame()
            self.view.makeMessage('Parameters removed, add new parameter(s)') 

    def clickChangeAnotherParamButton(self):
        if len(self.view.paramNew) == 0:
            root.view.inputFrame.destroy()
            root.view.makeInputFrame()
            root.view.makeChangeParamInputFrame()
            self.view.makeMessage('New parameter name cannot be empty')
            return
        oldParam = [self.view.param]
        newParam = [(self.view.paramNew, self.view.paramTypeNew)]
        num = p.changeParameter(oldParam, newParam, self.view.method, self.view.className)
        if num == -1:
            root.view.inputFrame.destroy()
            root.view.makeInputFrame()
            root.view.makeChangeParamInputFrame()
            self.view.makeMessage('Class does not exist')
        elif num == -2:
            root.view.inputFrame.destroy()
            root.view.makeInputFrame()
            root.view.makeChangeParamInputFrame()
            self.view.makeMessage('Method does not exist in class')
        elif num == -3:
            root.view.inputFrame.destroy()
            root.view.makeInputFrame()
            root.view.makeChangeParamInputFrame()
            self.view.makeMessage('Parameter does not exist to change')
        elif num == -4:
            root.view.inputFrame.destroy()
            root.view.makeInputFrame()
            root.view.makeChangeParamInputFrame()
            self.view.makeMessage('Parameter already exists within method')            
        else:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeChangeParamInputFrame()  
            self.view.makeMessage('Parameter changed')            
    
    def clickSaveButton(self):
        self.view.save()
        message = s.saveGUI(u.classIndex, r.relationIndex, self.view.fileName)
        if message == "":
            self.view.makeMessage('Saved successfully')
        else:
            self.view.makeMessage(message)

    def clickLoadButton(self):
        self.view.load()
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


