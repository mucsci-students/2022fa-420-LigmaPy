import UMLClass
# Class to test
import attributes

UMLClass.addClass("Tire")

"""
    Field Tests
"""
def test_add_field():
    field = attributes.addField("psi", "Tire", "float")
    assert field == 1

def test_add_to_nonexisting_class():
    assert attributes.addField("psi", "Car", "float") == -1

def test_add_existing_field():
    attributes.addField("psi", "Tire", "float")
    assert attributes.addField("psi", "Tire", "float") == -2

def test_rename_field():
    attributes.addField("brand", "Tire", "string")
    assert attributes.renameField("brand", "manufacturer", "Tire") == 1

def test_delete_nonexisting_field():
    assert attributes.deleteField("manufacturer", "Tire") == -2

def test_delete_field_nonexisting_class():
    attributes.addField("psi", "Tire", "float")
    assert attributes.deleteField("psi", "tire") == -1

def test_delete_field():
    attributes.addField("psi", "Tire", "float")
    assert attributes.deleteField("psi", "Tire") == 1

"""
    Method Tests
"""
def test_add_method():
    assert attributes.addMethod("setPSI", "Tire", "void") == 1

def test_rename_method():
    attributes.addMethod("getBarnd", "Tire", "string")
    assert attributes.renameMethod("getBarnd", "getBrand", "Tire") == 1

def test_delete_method():
    assert attributes.deleteMethod("getBrand", "Tire") == 1

