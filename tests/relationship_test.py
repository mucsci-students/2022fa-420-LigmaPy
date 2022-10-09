"""
Author(s)   : Trevor Bender
Filename    : relationship_test.py
Description : Tests for the relationship class
"""

import model.UMLClass as UMLClass
# Class to test
import model.relationship as relationship

"""     Add Relationship Tests     """
def test_add_relationship():
    # Test adding a relationship
    UMLClass.addClass("Tire")
    UMLClass.addClass("Car")
    assert relationship.addRelationship("Car", "Tire", "Composition") == 1

def test_add_same_src_dest_relationship():
    # Test adding a relationship with the same class as source and destination
    assert relationship.addRelationship("Car", "Car", "Composition") == -2

def test_add_duplicate_relationship():
    # Test adding an already existing relationship
    assert relationship.addRelationship("Car", "Tire", "Composition") == -3

def test_add_nonexisting_class():
    # Test adding a class that doesnt exist
    assert relationship.addRelationship("NotCar", "Tire", "Aggregation") == -1

"""     Edit Relationship Type Tests     """
def test_edit_relationship_type():
    # Test changing the type of an existing relationship
    assert relationship.relationIndex[0].editType("Aggregation") == 1
    assert relationship.relationIndex[0].type == "Aggregation"

"""     Delete Relationship Tests"""
def test_delete_nonexisting_relationship():
    # Test deleting a relationship that does not exist
    assert relationship.deleteRelationship("Tire", "Car") == -1

def test_delete_relationship():
    # Test deleting a relationship
    assert relationship.deleteRelationship("Car", "Tire") == 1

def test_delete_nonexistant_s_and_d():
    # Tst deleting a nonexistan relation
    assert relationship.deleteRelationship("help", "me") == -2

"""     Find Relationship Tests     """

def test_find_relation_exists():
    # Test finding and existing relation
    assert relationship.findRelationship("Car", "Tire") == 0

    # Test not finding a non existing relation
def test_find_relation_exists():
    assert relationship.findRelationship("Car", "Fire") == -1    