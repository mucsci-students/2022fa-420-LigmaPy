"""
Filename    : parameter_test.py
Description : Tests for the parameter class
"""

from model.ErrorHandlers.ReturnStatus import codes

import model.UMLClass as UMLClass
import model.attributes as attributes
# Class to test
import model.parameter as parameter

UMLClass.addClass("Tire")
attributes.addMethod("setPSI", "Tire", "void")
attributes.addMethod("getQuality", "Tire", "string")

"""     Add Parameter Tests     """
def test_add_parameter():
    # Test adding a parameter
    assert parameter.addParameter("new_psi", "float", "setPSI", "Tire") == codes.ADDED_PARAM

def test_add_multiple_parameters():
    # Test adding multiple parameters at once
    assert parameter.addParameter("currentTread", "Float", "getQuality", "Tire") == codes.ADDED_PARAM
    assert parameter.addParameter("illegalTread", "boolean", "getQuality", "Tire") == codes.ADDED_PARAM

def test_add_duplicate_parameters():
    # Test adding a parameter that already exists
    assert parameter.addParameter("new_psi", "string", "setPSI", "Tire") == codes.ADD_PARAM_ALREADY_EXISTS

def test_method_does_not_exist():
    # Test adding parameters to a method that does not exist
    assert parameter.addParameter("velocity", "float", "getRotation", "Tire") == codes.ADD_PARAM_METHOD_NOT_EXIST

def test_class_does_not_exist():
    # Test adding a parameter to a method when the class does not exist
    assert parameter.addParameter("currentTread", "Float", "getQuality", "Engine") == codes.ADD_PARAM_CLASS_NOT_EXIST

"""     Delete Parameter Tests     """
def test_delete_single_parameter():
    # Test deleting a single parameter
    assert parameter.addParameter("fudge", "long", "setPSI", "Tire") == codes.ADDED_PARAM
    assert parameter.deleteParameter("fudge", "setPSI", "Tire") == codes.DELETED_PARAM

def test_delete_all_parameters():
    # Test deleting all parameters at once
    assert parameter.addParameter("idNum", "string", "getQuality", "Tire") == codes.ADDED_PARAM
    assert parameter.addParameter("bus", "string", "getQuality", "Tire") == codes.ADDED_PARAM
    assert parameter.addParameter("earned", "int", "getQuality", "Tire") == codes.ADDED_PARAM
    assert parameter.deleteAllParameter("getQuality", "Tire") == codes.DELETED_PARAM


"""     Change Parameter Tests     """
def test_change_parameters():
    # Test Changing the name of a parameter
    assert parameter.addParameter("new_pis", "float", "setPSI", "Tire") == codes.ADDED_PARAM
    changed = parameter.changeParameter("new_pis", "new_psi", "setPSI", "Tire") == codes.CHANGED_PARAM
