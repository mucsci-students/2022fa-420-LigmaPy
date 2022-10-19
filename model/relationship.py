"""
Author : Christian Shepperson
Filename : relationship.py
Description : Adds, deletes and updates the type of relationships
"""
from typing import List
# Local Imports
import model.UMLClass as UMLClass
from UMLException import UMLException, UMLSuccess

###################################################################################################

class UMLRelationship:
    def __init__(self, source: str, destination: str, type:str):
        self.source = source
        self.destination = destination
        self.type = type

        print(f"\nRelationship added: {self}")

    def __repr__(self):
        return f"[{self.source}] - [{self.destination}] <{self.type}>"

    #changes the type of the relationship
    def editType(self, newType:str):
        self.type = newType
        print(UMLSuccess(f"Changed type to {newType}"))
        return 1

    def hash(self):
        return hash(self)
    """
    updates the relationship class
    """
    
    def updateRename(self, oldName:str, newName:str):
        if self.source == oldName:
            self.source = newName
        else: 
            self.destination = newName
    


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

def addRelationship(source: str, destination: str, type: str):
    """
        Creates a relationship between to classes.

        :param source: Name of the source class
        :param destination: Name of the destination class

        :returns: The message of the status of adding a relationship
    """
    if source == destination:
        print(UMLException("Relationship Error", f"Source class cannot be the same as destination class"))
        return -2
    # Check if both source and destination classes exist
    if UMLClass.findClass(source) is not None and UMLClass.findClass(destination) is not None:
        for relation in relationIndex:
            # Check if relationship already exists
            if source == relation.source and destination == relation.destination:
                print(UMLException("Add Relationship Error", f"{relation} already exists"))
                return -3
        # Append the new relationship to the relationIndex list
        newRelation = UMLRelationship(source, destination, type)
        relationIndex.append(newRelation)
        UMLClass.classIndex[UMLClass.findClass(source)].register(newRelation.hash())
        UMLClass.classIndex[UMLClass.findClass(destination)].register(newRelation.hash())
        return 1
    else:
        print(UMLException("Class Error", f"Source or Destination class does not exist"))
        return -1

def deleteRelationship(source: str, destination: str):
    """
        Removes an existing relationship between two classes.

        :param source: Name of the source class
        :param destination: Name of the destination class

        :returns: The status of the relationship deletion
    """
    # Check if source and destination class exist
    if UMLClass.findClass(source) != None and UMLClass.findClass(destination) != None:

        index = findRelationship(source, destination)
        if index > -1:
            print(UMLSuccess(f"Removed relationship {relationIndex.pop(index)}"))
            return 1
        else:
            # Relationship does not exist
            print(UMLException("Relationship Error", f"Relationship does not exist"))
            return -1
    else:
        #source and destination do not exist
        print(UMLException("Class Error", f"Source or Destination class does not exist"))
        return -2
        
###################################################################################################

relationIndex : List[UMLRelationship]= []