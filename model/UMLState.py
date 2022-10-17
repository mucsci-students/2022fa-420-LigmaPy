"""
Author(s)   : Trevor Bender, Sam Noggle
Filename    : UMLState.py
Description : Takes a snapshot of the current program state
"""

from queue import LifoQueue

from model import UMLClass, relationship, attributes, parameter

undoStack = LifoQueue(maxsize=5)

class UMLState():
    def __init__(self, state):
        self.stateDict = state

    
def saveState():
    """
    Saves the current program state to a stack
    """
    classDict = [c.toDict() for c in UMLClass.classIndex]
    relationDict = [relation.toDict() for relation in relationship.relationIndex]
    dict = {"classes": classDict, "relationships": relationDict}
    if undoStack.full():
        print("UNDO FULL")
        test = undoStack.get()
        print(test.stateDict)
        return
    undoStack.put(UMLState(dict))

def loadState(state : UMLState):
    """
        TODO Reset classIndex and relationIndex
    
    """


    print(state.stateDict.items())

    UMLClass.clear()
    relationship.clear()
    # Add all classes and their contents 
    for c in state.stateDict['classes']:
        # Add the class
        UMLClass.addClass(c['name'])
        # Add the fields to the class
        for field in c['Fields']:
            attributes.addField(field['name'], c['name'], field['type'])
        # Add the methods to the class
        for meth in c['Methods']:
            attributes.addMethod(meth['name'], c['name'], meth['return_type'])
            # Add parameters to the method
            for param in meth['params']:
                parameter.addParameter([(param['name'], param['type'])], meth['name'], c['name'])

def undo() -> UMLState:
    return undoStack.get()

