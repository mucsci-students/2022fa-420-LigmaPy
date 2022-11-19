"""
Filename    : undoRedo_test.py
Description : Tests the functionality of undo/redo
"""

from model.ErrorHandlers.ReturnStatus import codes
import model.UMLClass as UMLClass
import model.UMLState as UMLState
import model.relationship as relationship
import model.attributes as attributes
import model.parameter as p


def test_empty():
    assert UMLState.undo() == None
    assert UMLState.redo() == None
    UMLState.loadState(UMLState.undo()) 
    UMLState.addRedo(UMLState.undo())
    assert UMLState.redoStack.get() == None

# Test undo command
def test_undo():
    relationship.clear()
    UMLClass.clear()
    UMLState.addUndo(UMLState.saveState())
    assert UMLClass.addClass("Tire") == codes.ADDED_CLASS
    UMLState.addUndo(UMLState.saveState())
    assert UMLClass.addClass("Car") == codes.ADDED_CLASS
    UMLState.addUndo(UMLState.saveState())
    assert relationship.addRelationship("Tire", "Car", "composition") == codes.ADDED_RELATIONSHIP
    assert relationship.findRelationship("Tire", "Car") > -1
    UMLState.loadState(UMLState.undo())
    assert relationship.findRelationship("Tire", "Car") == -1
    assert UMLState.saveState().__repr__() == UMLState.saveState().__repr__()

# Test multiple runs of undo back to back
def test_multi_undo():
    UMLState.addUndo(UMLState.saveState())
    assert relationship.addRelationship("Tire", "Car", "composition") == codes.ADDED_RELATIONSHIP
    UMLState.addUndo(UMLState.saveState())
    assert attributes.addField("psi", "Tire", "float") == codes.ADDED_FIELD
    assert (relationship.findRelationship("Tire", "Car") > -1) and (attributes.findField("psi", "Tire") > -1)
    UMLState.loadState(UMLState.undo())
    UMLState.loadState(UMLState.undo())
    assert (relationship.findRelationship("Tire", "Car") == -1) and (attributes.findField("psi", "Tire") < 0)

# Test redo command
def test_redo():
    UMLState.loadState(UMLState.redo())
    assert relationship.findRelationship("Tire", "Car") > -1

# Test clearing redo stack when command is run after undo
def test_command_after_undo():
    assert not UMLState.redoStack.empty()
    UMLState.clearRedo()
    assert UMLState.redoStack.empty()

def test_load():
    UMLClass.addClass("Hi")
    attributes.addField("Hi", "Hi", "Hi")
    attributes.addMethod("Hi", "Hi", 'Hi')
    p.addParameter('Hi', "Hi", "Hi", "Hi")
    s = len(UMLClass.classIndex)
    UMLClass.loadState(UMLClass.saveState())
    s1 = len(UMLClass.classIndex)
    assert s == s1



