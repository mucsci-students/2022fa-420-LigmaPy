"""
Author(s)   : Aaron Heinbaugh
Filename    : GuiController.py
Description : Controller that links the view and the model
"""

from view.View import UMLLines, UMLBoxes, View as v
import model.relationship as r
import model.UMLClass as u
import model.UMLState as us
import model.saveload as s
import model.attributes as a
import model.parameter as p


class Controller:
    def __init__(self):
        self.view = v(self)

    def main(self):
        self.view.main()

    """
    Each function below is called when a user clicks one of inputframe buttons
    in the lower left of the GUI or the file menu (save, load, list...).
    Each then calls the approprate function in the model and interprets the return value
    to inform the user in the lower left of the GUI 
    The function's name decribes which button was click in GUI
    Instead of commenting each function, apply the idea of comments from 
    clickChangeAnotherParamButton directly below to the others
    """
    
    #calls changeParameter in the model and return an error/success message
    #and remakes the inputframe so users can change another param if needed
    def clickChangeAnotherParamButton(self):
        #check if empty string was given and tells user not to do that
        if len(self.view.paramNew) == 0:
            #destroys base input frame and everything in it
            self.view.inputFrame.destroy()
            #creates new base input frame
            self.view.makeInputFrame()
            #creates new changeparam frame in new base frame created above
            self.view.makeChangeParamInputFrame()
            #output message to user below new changeparam frame
            self.view.makeMessage('New parameter name cannot be empty')
            return

        # saves state
        state = us.saveState()
        #creates num to hold result of changeParam call
        num = p.changeParameter(self.view.param, self.view.paramNew, self.view.method, self.view.className)
        #each conditional below recreates the changeParam frame and alerts user based on the result of changeParam call
        if num == 532:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeChangeParamInputFrame()
            self.view.makeMessage('Class does not exist')
        elif num == 533:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeChangeParamInputFrame()
            self.view.makeMessage('Method does not exist in class')
        elif num == 535:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeChangeParamInputFrame()
            self.view.makeMessage('Parameter does not exist to change')
        elif num == 534:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeChangeParamInputFrame()
            self.view.makeMessage('Parameter already exists within method')            
        else:
            # save undo
            us.addUndo(state)    
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeChangeParamInputFrame()
            self.view.printClassToCanvas(u.classIndex[u.findClass(self.view.className)])  
            self.view.makeMessage('Parameter changed')
            # clear redo
            us.clearRedo()

    def clickAddClassButton(self):
        # saves state
        state = us.saveState()
        num = u.addClass(self.view.className)
        if num == 113:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeAddClassFrame()
            self.view.makeMessage("Class name cannot be empty.")
        elif num == 112:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeAddClassFrame()
            self.view.makeMessage(f"\nClass \"{self.view.className}\" already exists, could not create.")            
        else:
            # save undo
            us.addUndo(state)    
            self.view.remake()
            self.view.makeAddClassFrame()
            self.view.printClassToCanvas(u.classIndex[u.findClass(self.view.className)])
            self.view.makeMessage(f"\nClass \"{self.view.className}\" has been created!")
            # clear redo
            us.clearRedo()

    def clickDeleteClassButton(self):
        # saves state
        state = us.saveState()
        num = u.deleteClass(self.view.className)
        if num == 122:
            self.view.remake()
            self.view.makeDeleteClassFrame()
            self.view.makeMessage(f"\nClass \"{ self.view.className}\" does not exist")
        else:
            # save undo
            us.addUndo(state)    
            self.view.remake()
            self.view.makeDeleteClassFrame()
            self.view.removeClassFromCanvas(self.view.className)
            self.view.makeMessage(f"\nClass \"{self.view.className}\" has been deleted.")
            # clear redo
            us.clearRedo()

    def clickRenameClassButton(self):
        # saves state
        state = us.saveState()
        num = u.renameClass(self.view.className, self.view.classNameNew)
        if num == 133:
            self.view.remake()
            self.view.makeRenameClassFrame()
            self.view.makeMessage(f"\nA class already exists with the name \"{self.view.classNameNew}\"")
        elif num == 132:
            self.view.remake()
            self.view.makeRenameClassFrame()
            self.view.makeMessage(f"\nClass \"{self.view.className}\" does not exist")
        elif num == 134:
            self.view.remake()
            self.view.makeRenameClassFrame()
            self.view.makeMessage(f"\nClass name cannot be empty")
        else:
            # save undo
            us.addUndo(state)    
            self.view.remake()
            self.view.makeRenameClassFrame()
            self.view.printRenamedClassToCanvas(u.classIndex[u.findClass(self.view.classNameNew)], self.view.className)            
            self.view.makeMessage("Class renamed")
            # clear redo
            us.clearRedo()
        
    def clickAddRelationButton(self):
        # saves state
        state = us.saveState()
        num = r.addRelationship( self.view.source, self.view.destination, self.view.relationshipType)
        if num == 215:
            self.view.remake()
            self.view.makeAddRelationFrame()
            self.view.makeMessage("Source and destination cannot be the same")
        elif num == 212 or num == 213:
            self.view.remake()
            self.view.makeAddRelationFrame()
            self.view.makeMessage("Source or destination does not exist")
        elif num == 216:
            self.view.remake()
            self.view.makeAddRelationFrame()
            self.view.makeMessage("Relationship already exists")
        else:
            # save undo
            us.addUndo(state)    
            self.view.remake()
            self.view.makeAddRelationFrame()
            self.view.makeLine(self.view.source, self.view.destination) 
            self.view.makeMessage("Relationship added")
            # clear redo
            us.clearRedo()

    def clickUpdateTypeButton(self):
        # saves state
        state = us.saveState()
        num = r.findRelationship(self.view.source, self.view.destination)
        if num == -1:
            self.view.remake()
            self.view.makeUpdateRelationType()
            self.view.makeMessage("Relationship does not exist")
        else:
            # save undo
            us.addUndo(state)    
            self.view.deleteLine(self.view.source, self.view.destination) 
            r.relationIndex[num].editType(self.view.relationshipTypeNew)
            self.view.remake()
            self.view.makeUpdateRelationType()
            self.view.makeLine(self.view.source, self.view.destination) 
            self.view.makeMessage("Relationship type updated") 
            # clear redo
            us.clearRedo()   
    
    def clickDeleteRelationButton(self):
        # saves state
        state = us.saveState()
        num = r.deleteRelationship( self.view.source, self.view.destination)
        if num == 222:
            self.view.remake()
            self.view.makeDeleteRelationFrame()
            self.view.makeMessage("Relationship does not exist")
        else:
            # save undo
            us.addUndo(state)    
            self.view.remake()
            self.view.makeDeleteRelationFrame()
            self.view.deleteLine(self.view.source, self.view.destination)
            self.view.makeMessage("Relationship deleted")
            # clear redo
            us.clearRedo() 

    def clickAddFieldButton(self):
        # saves state
        state = us.saveState()
        if len(self.view.field.strip()) == 0:
            self.view.remake()
            self.view.makeAddFieldFrame()
            self.view.makeMessage("Field name cannot be empty")
            return
        num = a.addField(self.view.field, self.view.className, self.view.fieldType)
        if num == 412:
            self.view.remake()
            self.view.makeAddFieldFrame()
            self.view.makeMessage("Class does not exist")
        elif num == 413:
            self.view.remake()
            self.view.makeAddFieldFrame()
            self.view.makeMessage("Field already exists")
        else:
            # save undo
            us.addUndo(state)    
            self.view.remake()
            self.view.makeAddFieldFrame()
            self.view.printClassToCanvas(u.classIndex[u.findClass(self.view.className)])
            self.view.makeMessage("Field added")
            # clear redo
            us.clearRedo() 

    def clickDeleteFieldButton(self):   
        print(self.view.field)
        print(self.view.className)
        # saves state
        state = us.saveState()
        num = a.deleteField(self.view.field, self.view.className)
        if num == 422:
            self.view.remake()
            self.view.makeDeleteFieldFrame()
            self.view.makeMessage("Class does not exist")
        elif num == 423:
            self.view.remake()
            self.view.makeDeleteFieldFrame()
            self.view.makeMessage("Field does not exist")
        else:
            # save undo
            us.addUndo(state)    
            self.view.remake()
            self.view.makeDeleteFieldFrame()
            self.view.printClassToCanvas(u.classIndex[u.findClass(self.view.className)])
            self.view.makeMessage("Field deleted")
            # clear redo
            us.clearRedo() 

    def clickRenameFieldButton(self):
        # saves state
        if len(self.view.feildNew.strip()) == 0:
            self.view.remake()
            self.view.makeRenameFieldFrame()
            self.view.makeMessage("Field name cannot be empty")
            return
        state = us.saveState()
        num = a.renameField(self.view.field, self.view.feildNew, self.view.className)
        if num == 432:
            self.view.remake()
            self.view.makeRenameFieldFrame()
            self.view.makeMessage("Class does not exist")
        elif num == 433:
            self.view.remake()
            self.view.makeRenameFieldFrame()
            self.view.makeMessage("Field does not exists to rename")
        elif num == 434:
            self.view.remake()
            self.view.makeRenameFieldFrame()
            self.view.makeMessage("Another field already exists with that name")
        else:
            # save undo
            us.addUndo(state)    
            self.view.remake()
            self.view.makeRenameFieldFrame()
            self.view.printClassToCanvas(u.classIndex[u.findClass(self.view.className)])
            self.view.makeMessage("Field renamed")
            # clear redo
            us.clearRedo() 
    
    def clickAddMethodAndParamsButton(self):
        # saves state
        if len(self.view.method.strip()) == 0:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeAddMethodFrame()
            self.view.makeMessage("Method name cannot be empty")
            return    
        state = us.saveState()
        num = a.addMethod(self.view.method, self.view.className, self.view.methodReturnType)
        if num == 312:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeAddMethodFrame()
            self.view.makeMessage("Class does not exist")
        elif num == 313:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeAddMethodFrame()
            self.view.makeMessage("Method already exists")
        else:   
            # save undo
            us.addUndo(state)        
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeParamInputFrame()
            self.view.printClassToCanvas(u.classIndex[u.findClass(self.view.className)])
            self.view.makeMessage("Method added, please enter parameter(s)")
            # clear redo
            us.clearRedo() 

    def clickAddMethodWithoutParamsButton(self):
        if len(self.view.method.strip()) == 0:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeAddMethodFrame()
            self.view.makeMessage("Method name cannot be empty") 
            return
        # saves state
        state = us.saveState()
        num = a.addMethod(self.view.method, self.view.className, self.view.methodReturnType)
        if num == 312:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeAddMethodFrame()
            self.view.makeMessage("Class does not exist")
        elif num == 313:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeAddMethodFrame()
            self.view.makeMessage("Method already exists")
        else:
            # save undo
            us.addUndo(state)               
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeAddMethodFrame()
            self.view.printClassToCanvas(u.classIndex[u.findClass(self.view.className)])
            self.view.makeMessage("Method added")
            # clear redo
            us.clearRedo()

    def clickAddParamButton(self):
        if len(self.view.param) == 0:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeParamInputFrame()
            self.view.makeMessage('Parameter name cannot be empty')
            return 

        # saves state
        state = us.saveState()
        num = p.addParameter(self.view.param, self.view.paramType, self.view.method, self.view.className)

        if num == 512:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeParamInputFrame()
            self.view.makeMessage("Class does not exist")
        elif num == 513:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeParamInputFrame()
            self.view.makeMessage("Method does not exist in class")
        elif num == 514:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeParamInputFrame()
            self.view.makeMessage("Parameter already exists in method")
        else:
            # save undo
            us.addUndo(state)        
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeParamInputFrame()
            self.view.printClassToCanvas(u.classIndex[u.findClass(self.view.className)])
            self.view.makeMessage("Parameter added")    
            # clear redo
            us.clearRedo()        

    def clickDeleteMethodButton(self):
        # saves state
        state = us.saveState()
        num = a.deleteMethod(self.view.method, self.view.className)
        if num == 322:
            self.view.remake()
            self.view.makeDeleteMethodFrame()
            self.view.makeMessage("Class does not exist")
        elif num == 323:
            self.view.remake()
            self.view.makeDeleteMethodFrame()
            self.view.makeMessage("Method does not exist")  
        else:
            # save undo
            us.addUndo(state)        
            self.view.remake()
            self.view.makeDeleteMethodFrame()
            self.view.printClassToCanvas(u.classIndex[u.findClass(self.view.className)])
            self.view.makeMessage("Method Deleted")     
            # clear redo
            us.clearRedo()     


    def clickUpdateMethodButton(self):
        if len(self.view.methodNew.strip()) == 0:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeRenameMethodFrame()
            self.view.makeMessage("Method name cannot be empty") 
            return
        # saves state
        state = us.saveState()
        num = a.renameMethod(self.view.method, self.view.methodNew, self.view.className)
        if num == 332:    
            self.view.remake()
            self.view.makeRenameMethodFrame()
            self.view.makeMessage('Class does not exist')
        elif num == 333:    
            self.view.remake()
            self.view.makeRenameMethodFrame()
            self.view.makeMessage('Method does not exist to rename')
        elif num == 334:    
            self.view.remake()
            self.view.makeRenameMethodFrame()
            self.view.makeMessage('New method name already exists')
        else:    
            # save undo
            us.addUndo(state)        
            self.view.remake()
            self.view.makeRenameMethodFrame()
            self.view.printClassToCanvas(u.classIndex[u.findClass(self.view.className)])
            self.view.makeMessage('Method renamed')
            # clear redo
            us.clearRedo()

    def clickAddParamToMethodButton(self):
        # saves state
        state = us.saveState()
        num = a.findMethod(self.view.method, self.view.className)
        if num == -1:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeAddParamFrame()
            self.view.makeMessage('Class does not exist')
        elif num == -2:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeAddParamFrame()
            self.view.makeMessage('Method does not exist in class')
        else:  
            # save undo
            us.addUndo(state)        
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeParamInputFrame()
            # clear redo
            us.clearRedo()

    def clickDeleteParamButton(self):
        # saves state
        state = us.saveState()
        num = a.findMethod(self.view.method, self.view.className)
        if num == -1:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeDeleteParamFrame()
            self.view.makeMessage('Class does not exist')
        elif num == -2:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeDeleteParamFrame()
            self.view.makeMessage('Method does not exist in class')
        else:
            # save undo
            us.addUndo(state)        
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeDeleteParamInputFrame()
            # clear redo
            us.clearRedo()

    def clickDeleteAllParamButton(self):
        # saves state
        state = us.saveState()
        num = p.deleteAllParameter(self.view.method, self.view.className)
        if num == 522:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeDeleteParamFrame()
            self.view.makeMessage('Class does not exist')
        elif num == 523:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeDeleteParamFrame()
            self.view.makeMessage('Method does not exist in class')
        else:
            # save undo
            us.addUndo(state)        
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeDeleteParamFrame()
            self.view.printClassToCanvas(u.classIndex[u.findClass(self.view.className)])
            self.view.makeMessage('All parameters deleted')
            # clear redo
            us.clearRedo()
    
    def clickSecondDeleteParamButton(self):
        if len(self.view.param) == 0:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeDeleteParamInputFrame()
            self.view.makeMessage('Parameter does not exist')
            return

        # saves state
        state = us.saveState()
        num = p.deleteParameter(self.view.param, self.view.method, self.view.className)

        if num == 522:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeDeleteParamInputFrame()
            self.view.makeMessage("Class does not exist")
        elif num == 523:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeDeleteParamInputFrame()
            self.view.makeMessage('Method does not exist in class')
        elif num == 524:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeDeleteParamInputFrame()
            self.view.makeMessage('Parameter does not exist in method')
        else:
            # save undo
            us.addUndo(state)        
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeDeleteParamInputFrame()
            self.view.printClassToCanvas(u.classIndex[u.findClass(self.view.className)])
            self.view.makeMessage('Parameter deleted')
        # clear redo
            us.clearRedo()

    def clickChangeParamButton(self):
        # saves state
        state = us.saveState()
        num = a.findMethod(self.view.method, self.view.className)
        if num == -1:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeChangeParamFrame()
            self.view.makeMessage('Class does not exist')
        elif num == -2:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeChangeParamFrame()
            self.view.makeMessage('Method does not exist in class')
        else:
            # save undo
            us.addUndo(state)        
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeChangeParamInputFrame()  
            # clear redo
            us.clearRedo()              

    def clickChangeAllParamButton(self):
        # saves state
        state = us.saveState()
        num = p.deleteAllParameter(self.view.method, self.view.className)
        if num == 522:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeChangeParamFrame()
            self.view.makeMessage('Class does not exist')
        elif num == 523:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeChangeParamFrame()
            self.view.makeMessage('Method does not exist in class')
        else:
            # save undo
            us.addUndo(state)           
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeParamInputFrame()
            self.view.printClassToCanvas(u.classIndex[u.findClass(self.view.className)])
            self.view.makeMessage('Parameters removed, add new parameter(s)') 
            # clear redo
            us.clearRedo()

    def clickUndoButton(self):
        """
        Calls model and view to undo action
        """ 
        state = us.undo()
        print(state)

        # runs if needs to print blank canvas
        if state is None:
            self.view.clearScreen()
            UMLLines.clear()
            UMLBoxes.clear()
            # prints success message
            self.view.makeMessage('Action has been undone.') 
        else:
            # load this state
            us.loadState(state)
            # clear screen
            self.view.clearScreen()
            UMLLines.clear()
            UMLBoxes.clear()
            # reprint classes to canvas
            for c in u.classIndex:
                self.view.printClassToCanvas(c)
            # reprint relationships to canvas
            for rel in r.relationIndex:
                self.view.makeLine(rel.source, rel.destination)
            # prints success message
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeMessage('Action has been undone.') 

        
    def clickRedoButton(self):
        """
        Calls model and view to redo action
        """

        # retrieve saved state
        state = us.redo()
        print(state)

        # load this state
        us.loadState(state)
        # clear screen
        # self.view.clearScreen()
        self.view.clearCanvas()
        UMLLines.clear()
        UMLBoxes.clear()
        # reprint classes to canvas
        for c in u.classIndex:
            self.view.printClassToCanvas(c)
        # reprint relationships to canvas
        for rel in r.relationIndex:
            self.view.makeLine(rel.source, rel.destination)
        # prints success method
        self.view.inputFrame.destroy()
        self.view.makeInputFrame()
        self.view.makeMessage('Action has been redone.') 
        # saves new state
        newState = us.saveState()
        # adds new state to undo stack
        us.addUndo(newState)           

        
        

    
    def clickSaveButton(self):
        self.view.save()
        if self.view.fileName == "":
            return
        message = s.saveGUI(u.classIndex, r.relationIndex, self.view.fileName)
        if message == "":
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeMessage('Saved successfully')
        else:
            self.view.inputFrame.destroy()
            self.view.makeInputFrame()
            self.view.makeMessage(message)

    def clickLoadButton(self):
        self.view.load()
        message = s.loadGUI(self.view.fileName)
        #clears the canvas and empties lines dictionary
        self.view.clearScreen()
        UMLLines.clear()
        #loops thru loaded class and relationships and makes boxes/lines for each
        for each in u.classIndex:
            self.view.printClassToCanvas(each)
        for rel in r.relationIndex:
            self.view.makeLine(rel.source, rel.destination)
        self.view.inputFrame.destroy()
        self.view.makeInputFrame()
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
            self.view.clearScreen()
            self.view.makeMessage('No classes to list')
        else:
            self.view.printAllClassesToCanvas(u.classIndex)
            self.view.remake()

    def clickListRelationsButton(self):
        self.view.remake()
        if len(r.relationIndex) == 0:
            self.view.clearScreen()
            self.view.makeMessage("No relationships to list")
        else:
            self.view.printRelationsToCanvase(r.relationIndex)
            self.view.remake()




