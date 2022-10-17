"""
Author(s)   : Trevor Bender, Sam Noggle
Filename    : UMLState.py
Description : Takes a snapshot of the current program state
"""

from queue import LifoQueue

from model import UMLClass, relationship

undoStack = LifoQueue(maxsize=50)

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
    undoStack.put(UMLState(dict))

def loadState(state : UMLState):
    pass
    

def undo():
    pass

