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

def test_delete_class_does_not_exist():
    # Test deleting a parameter from a class that does not exist
    assert parameter.addParameter("idNum", "string", "setPSI", "Tire") == codes.ADDED_PARAM
    assert parameter.deleteParameter("idNum", "setPSI", "Car") == codes.DELETE_PARAM_CLASS_NOT_EXIST

def test_delete_method_does_not_exist():
    # Test deleting a parameter from a method that does not exist
    assert parameter.addParameter("id", "int", "setPSI", "Tire") == codes.ADDED_PARAM
    assert parameter.deleteParameter("id", "new", "Tire") == codes.DELETE_PARAM_METHOD_NOT_EXIST

def test_delete_param_does_not_exist():
    # Test deleting a parameter that does not exist
    assert parameter.deleteParameter("new", "setPSI", "Tire") == codes.DELETE_PARAM_NOT_EXIST

def test_delete_all_class_does_not_exist():
    # Test deleting all parameters when class does not exist
    assert parameter.deleteAllParameter("getQuality", "Car") == codes.DELETE_PARAM_CLASS_NOT_EXIST

def test_delete_all_method_does_not_exist():
    # Test deleting all parameters when method does not exist
    assert parameter.deleteAllParameter("new", "Tire") == codes.DELETE_PARAM_METHOD_NOT_EXIST


"""     Change Parameter Tests     """
def test_change_parameters():
    # Test Changing the name of a parameter
    assert parameter.addParameter("band", "string", "setPSI", "Tire") == codes.ADDED_PARAM
    assert parameter.changeParameter("band", "brand", "setPSI", "Tire") == codes.CHANGED_PARAM

def test_change_class_does_not_exist():
    # Test changing the name of a parameter when the class does not exist
    assert parameter.addParameter("band", "string", "setPSI", "Tire") == codes.ADDED_PARAM
    assert parameter.changeParameter("band", "brand", "setPSI", "Car") == codes.CHANGE_PARAM_CLASS_NOT_EXIST

def test_change_method_does_not_exist():
    # Test changing the name of a parameter when the class does not exist
    assert parameter.addParameter("drum", "string", "setPSI", "Tire") == codes.ADDED_PARAM
    assert parameter.changeParameter("drum", "guitar", "new", "Tire") == codes.CHANGE_PARAM_METHOD_NOT_EXIST
    
def test_change_param_does_not_exist():
    # Test changing the name of a parameter that does not exist
    assert parameter.changeParameter("one", "four", "setPSI", "Tire") == codes.CHANGE_PARAM_PARAM_NOT_EXIST

def test_change_param_already_exists():
    # Test changing the name of a parameter to the name of an existing parameter
    assert parameter.addParameter("one", "int", "getQuality", "Tire") == codes.ADDED_PARAM
    assert parameter.addParameter("two", "int", "getQuality", "Tire") == codes.ADDED_PARAM
    assert parameter.changeParameter("one", "two", "getQuality", "Tire") == codes.CHANGE_PARAM_ALREADY_EXISTS
    

# """     Test param class     """
def test_toDict():
    assert parameter.addParameter("three", "int", "getQuality", "Tire") == codes.ADDED_PARAM
    classInd = UMLClass.findClass("Tire")
    methodInd = attributes.findMethod("getQuality", "Tire")
    paramInd = parameter.findParameter("three", methodInd, classInd)
    assert UMLClass.classIndex[classInd].methods[methodInd].params[paramInd].toDict() == {"name": "three", "type": "int"}

def test_str():
    assert parameter.addParameter("four", "int", "getQuality", "Tire") == codes.ADDED_PARAM
    classInd = UMLClass.findClass("Tire")
    methodInd = attributes.findMethod("getQuality", "Tire")
    paramInd = parameter.findParameter("four", methodInd, classInd)
    assert UMLClass.classIndex[classInd].methods[methodInd].params[paramInd].__str__() == "int four"
