"""
Author(s)   : Trevor Bender
Filename    : class_test.py
Description : Tests for the UMLClass class
"""
# Class to test
import model.UMLClass as UMLClass

"""     Add Class Tests     """
def test_add_class():
    # Test adding a class
    UMLClass.addClass("Foo")
    assert UMLClass.findClass("Foo") != None

def test_add_existing_class_name():
    # Test adding a class that already exists
    UMLClass.addClass("Foo")
    assert UMLClass.addClass("Foo") == -2

def test_empty_class_name():
    # Test adding a class with no name
    assert UMLClass.addClass("") == -1

"""     Rename Class Tests     """
def test_rename_class():
    # Test renaming a class
    UMLClass.addClass("Foo")
    UMLClass.renameClass("Foo", "Bar")
    assert UMLClass.findClass("Foo") == None and UMLClass.findClass != None

def test_rename_nonexisting_class():
    # Test renaming a class that does not exist
    UMLClass.addClass("Foo")
    UMLClass.addClass("Bar")
    assert UMLClass.renameClass("Baz", "Far") == -2

def test_rename_existing_new_class():
    # Test renaming a class to an already existing class
    UMLClass.addClass("Foo")
    UMLClass.addClass("Bar")
    assert UMLClass.renameClass("Bar", "Foo") == -1

"""     Delete Class Tests     """
def test_delete_class():
    # Test deleting a class
    UMLClass.addClass("Foo")
    UMLClass.addClass("Bar")
    assert UMLClass.deleteClass("Foo") == 1

def test_delete_class_not_existing():
    # Test deleting a class that does not exist
    assert UMLClass.deleteClass("Baz") == -1

