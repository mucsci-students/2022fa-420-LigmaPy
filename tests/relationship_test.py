import UMLClass
# Class to test
import relationship

def test_add_relationship():
    UMLClass.addClass("Tire")
    UMLClass.addClass("Car")
    assert relationship.addRelationship("Car", "Tire", "Composition") == 1

def test_add_same_src_dest_relationship():
    assert relationship.addRelationship("Car", "Car", "Composition") == -2

def test_add_duplicate_relationship():
    assert relationship.addRelationship("Car", "Tire", "Composition") == -3

def test_edit_relationship_type():
    pass

def test_delete_nonexisting_relationship():
    assert relationship.deleteRelationship("Tire", "Car") == -1

def test_delete_relationship():
    assert relationship.deleteRelationship("Car", "Tire") == 1
