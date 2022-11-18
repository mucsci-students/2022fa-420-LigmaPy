"""
Filename    : attributes_test.py
Description : Tests for the attributes class
"""

from model.ErrorHandlers.ReturnStatus import codes

import model.UMLClass as UMLClass
# Class to test
import model.attributes as attributes

import model.parameter as p

UMLClass.addClass("Tire")

"""    Add Field Tests     """
def test_add_field():
    # Test adding a field to a class
    field = attributes.addField("psi", "Tire", "float")
    assert field == codes.ADDED_FIELD
    UMLClass.classIndex[0].fields[0].changeType("int")
    assert UMLClass.classIndex[0].fields[0].name == "int"

def test_toDict():
    attributes.addMethod("psi", "Tire", "int")
    p.addParameter('stuff', 'string', 'psi', 'Tire')
    assert UMLClass.classIndex[0].methods[0].toDict() == UMLClass.classIndex[0].methods[0].toDict() 
    assert UMLClass.classIndex[0].methods[0].__str__() == UMLClass.classIndex[0].methods[0].__str__()


def test_add_to_nonexisting_class():
    # Test adding a field to a class that does not exist
    assert attributes.addField("psi", "Van", "float") == codes.ADD_FIELD_NOT_EXISTING_CLASS
    assert attributes.addMethod("new", "Nope", "int") == codes.ADD_NOT_EXISTING_CLASS

def test_add_existing_field():
    # Test adding a field that already exists
    attributes.addField("psi", "Tire", "float")
    assert attributes.addField("psi", "Tire", "float") == codes.ADD_EXISTING_FIELD

"""     Rename Field Tests    """
def test_rename_field():
    # Test renaming a field
    attributes.addField("brand", "Tire", "string")
    attributes.addField("Exists", "Tire", "string")
    assert attributes.renameField("brand", "manufacturer", "Tire") == codes.RENAMED_FIELD
    assert attributes.renameField("Nope", "manufacturer", "Tire") == codes.RENAME_FIELD_FIELD_NOT_EXIST
    assert attributes.renameField("manufacturer", "what", "Nope") == codes.RENAME_FIELD_CLASS_NOT_EXIST
    assert attributes.renameField("manufacturer", "Exists", "Tire") == codes.RENAME_FIELD_NEW_EXISTS


"""     Delete Field Tests    """
def test_delete_nonexisting_field():
    # Test deleting a field that does not exist
    assert attributes.deleteField("creator", "Tire") == codes.DELETE_FIELD_NOT_EXISTING_FIELD

def test_delete_field_nonexisting_class():
    # Test deleting a field in a class that does not exist
    attributes.addField("psi", "Tire", "float")
    assert attributes.deleteField("psi", "tire") == codes.DELETE_FIELD_NOT_EXISTING_CLASS

def test_delete_field():
    # Test deleting a field
    attributes.addField("psi", "Tire", "float")
    assert attributes.deleteField("psi", "Tire") == codes.DELETED_FIELD

"""     Add Method Tests     """
def test_add_method():
    # Test adding a method to a class
    assert attributes.addMethod("setDiameter", "Tire", "void") == codes.ADDED_METHOD

"""     Rename Method Tests     """
def test_rename_method():
    # Test renaming a method
    attributes.addMethod("getBarnd", "Tire", "string")
    attributes.addMethod("Exists", "Tire", "string")
    assert attributes.renameMethod("getBarnd", "getBrand", "Tire") == codes.RENAMED_METHOD
    assert attributes.renameMethod("Nope", "yep", "Tire") == codes.RENAME_METHOD_METHOD_NOT_EXIST
    assert attributes.renameMethod("getBrand", "yep", "nope") == codes.RENAME_METHOD_CLASS_NOT_EXIST
    assert attributes.renameMethod("getBrand", "Exists", "Tire") == codes.RENAME_METHOD_NEW_EXISTS

"""     Delete Method Tests    """
def test_delete_method():
    # Test deleting a method from a class
    attributes.addMethod("getBrand", "Tire", "string")
    assert attributes.deleteMethod("getBrand", "Tire") == codes.DELETED_METHOD

def test_delete_method_nonexisting_class():
    # Test deleting a method from a class that does not exist
    assert attributes.deleteMethod("setPSI", "Van") == codes.DELETE_METHOD_NOT_EXISTING_CLASS

def test_delete_nonexisting_method():
    # Test deleting a method that does not exist
    assert attributes.deleteMethod("getDiameter", "Tire") == codes.DELETE_NOT_EXISTING_METHOD

