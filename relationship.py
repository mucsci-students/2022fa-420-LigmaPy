"""
Author : Ammanuel Amare, Christian Shepperson
Filename : relationship.py
Description : Adds and deletes relationships
"""
from typing import List
# Local Imports
import UMLClass

###################################################################################################

class UMLRelationship:
    def __init__(self, source: str, destination: str, type:str):
        self.source = source
        self.destination = destination
        self.type = type

        print(f"\nRelationship added: {repr(self)}")

    def __repr__(self):
        return f"[{self.source}] - [{self.destination}]"

    #changes the type of the relationship
    def editType(self, newType:str):

        self.type = newType
        return 1

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
    #search error
    return -1

def addRelationship(source: str, destination: str):
    """
        Creates a relationship between to classes.

        :param source: Name of the source class
        :param destination: Name of the destination class

        :returns: The message of the status of adding a relationship
    """
    if source == destination:
        return -2
    # Check if both source and destination classes exist
    if UMLClass.findClass(source) is not None and UMLClass.findClass(destination) is not None:
        for relation in relationIndex:
            # Check if relationship already exists
            if source == relation.source and destination == relation.destination:
                return -3
        # Append the new relationship to the relationIndex list
        newRelation = UMLRelationship(source, destination)
        relationIndex.append(newRelation)
    else:
        return -1

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

        return 1
    else:
        #source and destination do not exist
        return -1
        
###################################################################################################

relationIndex : List[UMLRelationship]= []