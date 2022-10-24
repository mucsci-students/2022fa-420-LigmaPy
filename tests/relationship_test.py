"""
Author(s)   : Trevor Bender
Filename    : relationship_test.py
Description : Tests for the relationship class
"""

from model.ErrorHandlers.ReturnStatus import codes
import model.UMLClass as UMLClass
# Class to test
import model.relationship as relationship

"""     Add Relationship Tests     """
def test_add_relationship():
    # Test adding a relationship
    UMLClass.addClass("Tire")
    UMLClass.addClass("Car")
    assert relationship.addRelationship("Car", "Tire", "Composition") == codes.ADDED_RELATIONSHIP

def test_add_same_src_dest_relationship():
    # Test adding a relationship with the same class as source and destination
    assert relationship.addRelationship("Car", "Car", "Composition") == codes.ADD_SAME_SRC_DEST

def test_add_duplicate_relationship():
    # Test adding an already existing relationship
    assert relationship.addRelationship("Car", "Tire", "Composition") == codes.ADD_EXISTING_RELATIONSHIP

def test_add_nonexisting_class():
    # Test adding a relationship with non-existing source class
    assert relationship.addRelationship("NotCar", "Tire", "Aggregation") == codes.ADD_SRC_NOT_EXIST


"""     Edit Relationship Type Tests     """
def test_edit_relationship_type():
    # Test changing the type of an existing relationship
    assert relationship.relationIndex[0].editType("Aggregation") == 1
    assert relationship.relationIndex[0].type == "Aggregation"

"""     Delete Relationship Tests"""
def test_delete_nonexisting_relationship():
    # Test deleting a relationship that does not exist
    assert relationship.deleteRelationship("Tire", "Car") == codes.DELETE_NOT_EXISTING_RELATIONSHIP

def test_delete_relationship():
    # Test deleting a relationship
    assert relationship.deleteRelationship("Car", "Tire") == codes.DELETED_RELATIONSHIP

def test_delete_nonexistant_s_and_d():
    # Tst deleting a nonexistan relation
    assert relationship.deleteRelationship("help", "Tire") == codes.DELETE_NOT_EXISTING_SRC

"""     Find Relationship Tests     """

def test_find_relation_exists():
    # Test finding and existing relation
    assert relationship.findRelationship("Car", "Tire") == 0

    # Test not finding a non existing relation
def test_find_relation_exists():
    assert relationship.findRelationship("Car", "Fire") == -1    