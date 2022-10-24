"""
Author : Christian Shepperson
Filename : relationship.py
Description : Adds, deletes and updates the type of relationships
"""
from typing import List
# Local Imports
import model.UMLClass as UMLClass
from UMLException import UMLException, UMLSuccess
from model.ErrorHandlers.ReturnStatus import codes
from view.printColors import colors

###################################################################################################

class UMLRelationship:
    def __init__(self, source: str, destination: str, type:str):
        self.source = source
        self.destination = destination
        self.type = type

    def toDict(self):
        """
        Converts a relationship to a dictionary

        :returns: A dictionary of the relationship
        """
        return {"source": self.source, "destination": self.destination, "type": self.type}

    def __repr__(self):
        return f"{colors.bold}[{self.source}] - [{self.destination}] <{self.type}>{colors.reset}"

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
    srcClass = UMLClass.findClass(source)
    destClass = UMLClass.findClass(destination)
    # Check if the source class exists
    if srcClass is None:
        return codes.ADD_SRC_NOT_EXIST
    # Check if the destination class exists
    if destClass is None:
        return codes.ADD_DEST_NOT_EXIST

    if source == destination:
        return codes.ADD_SAME_SRC_DEST

    for relation in relationIndex:
        # Check if relationship already exists
        if source == relation.source and destination == relation.destination:
            return codes.ADD_EXISTING_RELATIONSHIP
    # Append the new relationship to the relationIndex list
    newRelation = UMLRelationship(source, destination, type)
    relationIndex.append(newRelation)
    UMLClass.classIndex[UMLClass.findClass(source)].register(newRelation.hash())
    UMLClass.classIndex[UMLClass.findClass(destination)].register(newRelation.hash())
    return codes.ADDED_RELATIONSHIP

def deleteRelationship(source: str, destination: str):
    """
        Removes an existing relationship between two classes.

        :param source: Name of the source class
        :param destination: Name of the destination class

        :returns: The status of the relationship deletion
    """
    srcClass = UMLClass.findClass(source)
    destClass = UMLClass.findClass(destination)

    if srcClass is None:
        return codes.DELETE_NOT_EXISTING_SRC
    if destClass is None:
        return codes.DELETE_NOT_EXISTING_DEST

    # Check if source and destination class exist

    index = findRelationship(source, destination)
    if index > -1:
        relationIndex.pop(index)
        return codes.DELETED_RELATIONSHIP
    else:
        # Relationship does not exist
        return codes.DELETE_NOT_EXISTING_RELATIONSHIP
        
###################################################################################################

def clear():
    """
    Clears the list of relationships
    """
    relationIndex.clear()

relationIndex : List[UMLRelationship]= []