"""
Author : Ammanuel Amare
Filename : relationship.py
Description : Adds and deletes relationships
"""
from typing import List
# Local Imports
import UMLClass

###################################################################################################

class UMLRelationship:
    def __init__(self, source: str, destination: str):
        self.source = source
        self.destination = destination

        print(f"\nRelationship added: {repr(self)}")

    def __repr__(self):
        return f"[{self.source}] - [{self.destination}]"

###################################################################################################

def findRelationship(source: str, destination: str):

    """
        Searches for Relationship (source, destination) in relationIndex

        :param source: Source class of the relationship
        :param destination: Destination class of the relationship

        :returns: Index of the relationship in relationIndex if it exists, otherwise -1
    """

    relationLoc = 0
    # Search for relationship in relationIndex
    for relation in relationIndex:
        if source == relation.source and destination == relation.destination:
            return relationLoc
        relationLoc+=1
    return -1

def addRelationship(source: str, destination: str):
    """
        Creates a relationship between to classes.

        :param source: Name of the source class
        :param destination: Name of the destination class

        :returns: The message of the status of adding a relationship
    """
    if source == destination:
        print("Source class cannot be the same a destination class.")
        return
    # Check if both source and destination classes exist
    if UMLClass.findClass(source) is not None and UMLClass.findClass(destination) is not None:
        for relation in relationIndex:
            # Check if relationship already exists
            if source == relation.source and destination == relation.destination:
                print(f"Error: Relationship already exists.")
                return
        # Append the new relationship to the relationIndex list
        newRelation = UMLRelationship(source, destination)
        relationIndex.append(newRelation)
    else:
        print(f"The {source} or {destination} class does not exist.")

def deleteRelationship(source: str, destination: str):
    """
        Removes an existing relationship between two classes.

        :param source: Name of the source class
        :param destination: Name of the destination class

        :returns: The status of the relationship deletion
    """
    # Check if source and destination class exist
    if UMLClass.findClass(source) is not None and UMLClass.findClass(destination) is not None:

        index = findRelationship(source, destination)
        deletedRelation = relationIndex[index]
        if index > -1:
            relationIndex.pop(index)

        print(f"\nDeleted Relationship: {repr(deletedRelation)}")
    else:
        print(f"Relationship does not exist: [{source}] - [{destination}]")

###################################################################################################

relationIndex : List[UMLRelationship]= []