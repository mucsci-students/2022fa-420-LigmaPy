"""
Author(s)   : Trevor Bender
Filename    : parameter_test.py
Description : Tests for the parameter class
"""

import UMLClass
import attributes
# Class to test
import parameter

UMLClass.addClass("Tire")
attributes.addMethod("setPSI", "Tire", "void")
attributes.addMethod("getQuality", "Tire", "string")

"""     Add Parameter Tests     """
def test_add_parameter():
    # Test adding a parameter
    assert parameter.addParameter([("new_psi", "string")], "setPSI", "Tire") == 1

def test_add_multiple_parameters():
    # Test adding multiple parameters at once
    assert parameter.addParameter([("currentTread", "Float"), ("illegalTread", "Float")], "getQuality", "Tire") == 1

def test_add_duplicate_parameters():
    # Test adding a parameter that already exists
    parameter.addParameter([("new_psi", "string")], "setPSI", "Tire")
    assert parameter.addParameter([("new_psi", "string")], "setPSI", "Tire") == -3

def test_method_does_not_exist():
    # Test adding parameters to a method that does not exist
    assert parameter.addParameter([("velocity", "float")], "getRotation", "Tire") == -2

def test_class_does_not_exist():
    # Test adding a parameter to a method when the class does not exist
    assert parameter.addParameter([("currentTread", "Float")], "getQuality", "Engine") == -1

"""     Delete Parameter Tests     """
def test_delete_single_parameter():
    # Test deleting a single parameter
    parameter.addParameter([("fudge", "long")], "setPSI", "Tire")
    assert parameter.deleteParameter(["fudge"], "setPSI", "Tire") == 1

def test_delete_all_parameters():
    # Test deleting all parameters at once
    parameter.addParameter([("bus", "string"), ("earned", "int"), ("idNum", "string")], "getQuality", "Tire")
    assert parameter.deleteAllParameter("getQuality", "Tire") == 1

"""     Change Parameter Tests     """
def test_change_parameters():
    # Test Changing the name of a parameter
    parameter.addParameter([("new_pis", "float")], "setPSI", "Tire")
    changed = parameter.changeParameter([("new_pis")], [("new_psi")], "setPSI", "Tire")
    assert changed ==  1
