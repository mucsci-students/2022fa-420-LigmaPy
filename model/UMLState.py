"""
Filename    : UMLState.py
Description : Takes a snapshot of the current program state
"""

from queue import LifoQueue

from model import UMLClass, relationship, attributes, parameter

undoStack = LifoQueue()
redoStack = LifoQueue()

class UMLState():
    def __init__(self, state):
        self.stateDict = state

    def __repr__(self):
        return f"{self.stateDict}"
    
def saveState() -> UMLState:
    """
    Saves the current program state to a stack

    :returns: The state that was saved
    """
    classDict = [c.toDict() for c in UMLClass.classIndex]
    relationDict = [relation.toDict() for relation in relationship.relationIndex]
    dict = {"classes": classDict, "relationships": relationDict}
    return UMLState(dict)

def addUndo(state : UMLState):
    """
    Appends the current state to the undoStack
    """
    undoStack.put(state)

def addRedo(state : UMLState):
    """
    Appends the current state to the redoStack
    """
    redoStack.put(state)

def loadState(state : UMLState):
    """
    Loads a UMLState object

    :param state: The UMLState object that should be loaded
    """
    # If there is no state, return
    if state is None:
        return
    # Clear the class and relationship lists
    UMLClass.clear()
    relationship.clear()
    # Add all classes and their contents 
    for c in state.stateDict['classes']:
        # Add the class
        UMLClass.addClass(c['name'])
        # Adds location to class
        # for x in c['x']:
        # print(c['x'])
        # print(c['name'])
        w = UMLClass.classIndex[UMLClass.findClass(c['name'])]
        w.location['x'] = c['x']
        w.location['y'] = c['y']
        # Add the fields to the class
        for field in c['Fields']:
            attributes.addField(field['name'], c['name'], field['type'])
        # Add the methods to the class
        for meth in c['Methods']:
            attributes.addMethod(meth['name'], c['name'], meth['return_type'])
            # Add parameters to the method
            for param in meth['params']:
                parameter.addParameter(param['name'], param['type'], meth['name'], c['name'])
    
    for rel in state.stateDict['relationships']:
        relationship.addRelationship(rel['source'], rel['destination'], rel['type'])

def undo() -> UMLState:
    """
    Pops the last state from the undoStack and puts it on the redoStack

    :returns: None if stack is empty otherwise the popped item from the stack
    """
    if undoStack.empty():
        return None

    redoStack.put(saveState())
    return undoStack.get()

def redo() -> UMLState:
    """
    Pops the last state from the redoStack and puts it on the undoStack

    :returns: None if the stack is empty otherwise the popped item from the stack
    """
    if redoStack.empty():
        return None

    undoStack.put(saveState())
    state = redoStack.get()

    print(state)

    return state
def clearRedo():
    while not redoStack.empty():
        print(redoStack.get())

