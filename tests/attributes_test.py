"""
Author(s)   : Trevor Bender
Filename    : attributes_test.py
Description : Tests for the attributes class
"""

import UMLClass
# Class to test
import attributes

UMLClass.addClass("Tire")

"""    Add Field Tests     """
def test_add_field():
    # Test adding a field to a class
    field = attributes.addField("psi", "Tire", "float")
    assert field == 1

def test_add_to_nonexisting_class():
    # Test adding a field to a class that does not exist
    assert attributes.addField("psi", "Car", "float") == -1

def test_add_existing_field():
    # Test adding a field that already exists
    attributes.addField("psi", "Tire", "float")
    assert attributes.addField("psi", "Tire", "float") == -2

"""     Rename Field Tests    """
def test_rename_field():
    # Test renaming a field
    attributes.addField("brand", "Tire", "string")
    assert attributes.renameField("brand", "manufacturer", "Tire") == 1

"""     Delete Field Tests    """
def test_delete_nonexisting_field():
    # Test deleting a field that does not exist
    assert attributes.deleteField("creator", "Tire") == -2

def test_delete_field_nonexisting_class():
    # Test deleting a field in a class that does not exist
    attributes.addField("psi", "Tire", "float")
    assert attributes.deleteField("psi", "tire") == -1

def test_delete_field():
    # Test deleting a field
    attributes.addField("psi", "Tire", "float")
    assert attributes.deleteField("psi", "Tire") == 1

"""     Add Method Tests     """
def test_add_method():
    # Test adding a method to a class
    assert attributes.addMethod("setDiameter", "Tire", "void") == 1

"""     Rename Method Tests     """
def test_rename_method():
    # Test renaming a method
    attributes.addMethod("getBarnd", "Tire", "string")
    assert attributes.renameMethod("getBarnd", "getBrand", "Tire") == 1
"""     Delete Method Tests    """
def test_delete_method():
    # Test deleting a method from a class
    attributes.addMethod("getBrand", "Tire", "string")
    assert attributes.deleteMethod("getBrand", "Tire") == 1

def test_delete_method_nonexisting_class():
    # Test deleting a method from a class that does not exist
    assert attributes.deleteMethod("setPSI", "Car") == -1

def test_delete_nonexisting_method():
    # Test deleting a method that does not exist
    assert attributes.deleteMethod("getDiameter", "Tire") == -2

