"""
Author(s)   : Trevor Bender
Filename    : relationship_test.py
Description : Tests for the relationship class
"""

import UMLClass
# Class to test
import relationship

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

"""     Edit Relationship Type Tests     """
def test_edit_relationship_type():
    # Test changing the type of an existing relationship
    pass

"""     Delete Relationship Tests"""
def test_delete_nonexisting_relationship():
    # Test deleting a relationship that does not exist
    assert relationship.deleteRelationship("Tire", "Car") == -1

def test_delete_relationship():
    # Test deleting a relationship
    assert relationship.deleteRelationship("Car", "Tire") == 1
