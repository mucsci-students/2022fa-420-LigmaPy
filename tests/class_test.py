"""
Filename    : class_test.py
Description : Tests for the UMLClass class
"""
# Class to test
import model.UMLClass as UMLClass
import model.relationship as r
from model.ErrorHandlers.ReturnStatus import codes

"""     Add Class Tests     """
def test_add_class():
    # Test adding a class
    ret = UMLClass.addClass("Foo")
    assert ret == codes.ADDED_CLASS

def test_add_existing_class_name():
    # Test adding a class that already exists
    UMLClass.addClass("Foo")
    assert UMLClass.addClass("Foo") == codes.ADD_EXISTING_CLASS

def test_empty_class_name():
    # Test adding a class with no name
    assert UMLClass.addClass("") == codes.ADD_EMPTY_CLASS

"""     Rename Class Tests     """
def test_rename_class():
    # Test renaming a class
    UMLClass.addClass("Foo")
    ret = UMLClass.renameClass("Foo", "Bar")
    assert ret == codes.RENAMED_CLASS

def test_rename_nonexisting_class():
    # Test renaming a class that does not exist
    UMLClass.addClass("Foo")
    UMLClass.addClass("Bar")
    assert UMLClass.renameClass("Baz", "Far") == codes.RENAME_CLASS_NOT_EXIST
    
def test_rename_nonunique():
    # Test renaming a class to an already existing class
    UMLClass.addClass("Pizza")
    UMLClass.addClass("Bacon")
    assert UMLClass.renameClass("Bacon", "Pizza") == codes.ADD_EXISTING_CLASS

def test_rename_emptyname():
    # Test renaming a class to an empty string
    UMLClass.addClass("Soda")
    assert UMLClass.renameClass("Soda", "") == codes.RENAME_CLASS_EMPTY
 

"""     Delete Class Tests     """
def test_delete_class():
    # Test deleting a class
    UMLClass.addClass("Foo")
    UMLClass.addClass("Bar")
    assert UMLClass.deleteClass("Foo") == codes.DELETED_CLASS

def test_delete_class_not_existing():
    # Test deleting a class that does not exist
    assert UMLClass.deleteClass("Baz") == codes.DELETE_NOT_EXISTING_CLASS

"""     String Test    """

def test_repr():
    UMLClass.addClass("Peanut")
    testClass = UMLClass.classIndex[UMLClass.findClass("Peanut")]
    s = testClass.__repr__()
    assert s == testClass.name




   
