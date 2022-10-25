"""
Author: Sam Noggle
Filename: UMLClass.py
Description: Adds, renames, and deletes a class object
"""

from typing import List
import model.relationship as relationship
from UMLException import UMLException, UMLSuccess
from model.ErrorHandlers.ReturnStatus import codes


class UMLClass:
    def __init__(self, name: str):
        self.name = name
        self.fields = []
        self.methods = []
        self.location = {'x' : 100, 'y' : 100}
        #observer list
        self.subscribers = []

    def __repr__(self):
        return f"{self.name}"

    def toDict(self):
        """
        Converts a class to a dictionary

        :returns: A dictionary of the class
        """
        fieldDict = [field.toDict() for field in self.fields]
        methodDict = [method.toDict() for method in self.methods]
        return {"name": self.name, "Fields": fieldDict, "Methods": methodDict}

    def rename(self, newName):
        self.name = newName
    
    def register(self, relationship):
        self.subscribers.append(relationship)

    def unregister(self, relationship):
        self.subscribers.pop(relationship)
    
    def dispatch(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)


def isNameUnique(name: str):
    """
    Checks classIndex for duplicate names

    :param name: a string of which name to check if it is unique
    :returns: True if the name is unique
    """
    for c in classIndex:
        if c.name.lower() == name.lower():
            return False
    return True


def findClass(name: str):
    """
    Finds a class object by name and returns it's index

    :param name: the name of which class to find 
    :returns: the index of that class in classIndex if it is found 
                or None if it was not found 
    """
    for i, c in enumerate(classIndex):
        if c.name == name:
            
            return i
    return None


def addClass(name: str):
    """
    Creates and adds a new class to the classIndex

    :param name: the name of the new class
    """
    if len(name.strip()) == 0:
        return codes.ADD_EMPTY_CLASS

    if isNameUnique(name):
        newClass = UMLClass(name)
        classIndex.append(newClass)
        return codes.ADDED_CLASS
    else:
        return codes.ADD_EXISTING_CLASS

def deleteClass(name: str):
    """ 
    Deletes a class by it's name

    :param name: the name of the class to delete
    """
    index = findClass(name)
    if index is not None:
        # uses observer to update the relationships on class deletion
        for sub in classIndex[index].subscribers:
            for relation in relationship.relationIndex:
                if sub == relation.hash():
                    relationship.deleteRelationship(relation.source, relation.destination)
                    break
        """
        for relation in relationship.relationIndex:
            if relation.source == name or relation.destination == name:
                listToDel.append(relation)
        for each in listToDel:
            relationship.deleteRelationship(each.source,each.destination)
        """
        classIndex.pop(index)
        return codes.DELETED_CLASS
    else:
        return codes.DELETE_NOT_EXISTING_CLASS


def renameClass(oldName: str, newName: str):
    """ 
    Renames a class from oldName to newName

    :param oldName: the target class's name
    :param newName: the new name for the target class
    """
    if findClass(newName) != None:
        return codes.RENAME_NEW_CLASS_EXIST
    
    if not isNameUnique(newName):
        print(UMLException("Class Rename Error", f"{newName} class already exists"))
        return codes.ADD_EXISTING_CLASS

    if len(newName.strip()) == 0:
        return codes.RENAME_CLASS_EMPTY

    index = findClass(oldName)
    if index is not None:
        classIndex[index].rename(newName)
        # uses observer to update the relationships on class rename
        for sub in classIndex[index].subscribers:
            for relation in relationship.relationIndex:
                if sub == relation.hash():
                    relation.updateRename(oldName, newName)
                    break

        return codes.RENAMED_CLASS

    else:
        return codes.RENAME_CLASS_NOT_EXIST

def clear():
    classIndex.clear()

# List of all class objects the user has created
classIndex: List[UMLClass] = []
