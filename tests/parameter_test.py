import UMLClass
import attributes
# Class to test
import parameter

UMLClass.addClass("Tire")
attributes.addMethod("setPSI", "Tire", "void")
attributes.addMethod("getQuality", "Tire", "string")

def test_add_parameter():
    assert parameter.addParameter([("new_psi", "string")], "setPSI", "Tire") == 1

def test_add_multiple_parameters():
    assert parameter.addParameter([("currentTread", "Float"), ("illegalTread", "Float")], "getQuality", "Tire") == 1

def test_add_duplicate_parameters():
    parameter.addParameter([("new_psi", "string")], "setPSI", "Tire")
    assert parameter.addParameter([("new_psi", "string")], "setPSI", "Tire") == -3

def test_method_does_not_exist():
    assert parameter.addParameter([("velocity", "float")], "getRotation", "Tire") == -2

def test_class_does_not_exist():
    assert parameter.addParameter([("currentTread", "Float")], "getQuality", "Engine") == -1

def test_delete_single_parameter():
    parameter.addParameter([("fudge", "long")], "setPSI", "Tire")
    assert parameter.deleteParameter(["fudge"], "setPSI", "Tire") == 1

def test_delete_multiple_parameters():
    parameter.addParameter([("new_psi", "string"), ("blaahhh", "string")], "setPSI", "Tire")
    assert parameter.deleteParameter(["new_psi", "blaahhh"], "setPSI", "Tire") == 1

def test_delete_all_parameters():
    parameter.addParameter([("bus", "string"), ("earned", "int"), ("idNum", "string")], "getQuality", "Tire")
    assert parameter.deleteAllParameter("getQuality", "Tire") == 1

def test_change_parameters():
    parameter.addParameter([("new_pis", "float")], "setPSI", "Tire")
    changed = parameter.changeParameter([("new_pis")], [("new_psi")], "setPSI", "Tire")
    assert changed ==  1

def test_change_multiple_parameters():
    parameter.addParameter([("new_pis", "float"), ("max_pis", "float"), ("diameter", "float")], "setPSI", "Tire")
    changed = parameter.changeParameter([("new_pis"), ("max_pis")], [("new_psi"), ("max_psi")], "setPSI", "Tire")
    assert changed == 1