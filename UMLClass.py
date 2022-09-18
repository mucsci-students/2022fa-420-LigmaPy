"""
Author: Sam Noggle
Filename: UMLClass.py
Description: Adds, renames, and deletes a class object
"""

from typing import List
import relationship


class UMLClass:
    def __init__(self, name: str):
        self.name = name
        self.attributes = []

    def rename(self, newName):
        print(f"\nClass \"{self.name}\" was renamed to \"{newName}\"")
        self.name = newName


def isNameUnique(name: str):
    """
    Checks classIndex for duplicate names

    :param name: a string of which name to check if it is unique
    :returns: True if the name is unique
    """
    for c in classIndex:
        if c.name == name:
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
        print("Class name cannot be empty.")
        return
    if isNameUnique(name):
        newClass = UMLClass(name)
        classIndex.append(newClass)
        print(f"\nClass \"{newClass.name}\" has been created!")
    else:
        print(f"\nClass \"{name}\" already exists, could not create.")


def deleteClass(name: str):
    """ 
    Deletes a class by it's name

    :param name: the name of the class to delete
    """
    index = findClass(name)
    if index is not None:
        listToDel = []
        # Remove relationships 
        for relation in relationship.relationIndex:
            if relation.source == name or relation.destination == name:
                listToDel.append(relation)
                #relationship.deleteRelationship(relation.source, relation.destination)
        for each in listToDel:
            relationship.deleteRelationship(each.source,each.destination)
        classIndex.pop(index)
        print(f"\nClass \"{name}\" has been deleted.")
    else:
        print(f"\nClass \"{name}\" does not exist")
        print("Deletion failed")


def renameClass(oldName: str, newName: str):
    """ 
    Renames a class from oldName to newName

    :param oldName: the target class's name
    :param newName: the new name for the target class
    """
    if findClass(newName):
        print(f"\nA class already exists with the name \"{newName}\"")
        print("Rename failed")
        return

    index = findClass(oldName)
    if index is not None:
        classIndex[index].rename(newName)
        
        # Update it's relationships
        for i, relation in enumerate(relationship.relationIndex):
            # Check source
            if relation.source == oldName:
                relationship.relationIndex[i].source = newName
            # Check destination
            elif relation.destination == oldName:
                relationship.relationIndex[i].destination = newName
    else:
        print(f"\nClass \"{oldName}\" does not exist")
        print("Rename failed")


# List of all class objects the user has created
classIndex: List[UMLClass] = []
