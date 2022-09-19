"""
Author: Julia Geesaman
Filename: attributes.py
Description: Adds, deletes, and renames an attribute
"""

import UMLClass as C


class attribute:
    """
    This is the attribute class.
    """

    def __init__(self, name):
        """
        :param name: name of the attribute
        """

        self.name = name

    def rename(self, newName):
        """
        :param newName: new name for the attribute
        """

        self.name = newName


def findAttribute(name, className):
    """
    This method finds whether the given class and attribute exist.

    :param name: name of the attribute
    :param className: class attribute is part of

    :returns: -1 if given class does not exist
            -2 if attribute does not exist in given class
            i index of attribute, if attribute and class exist
    """

    classIndex = C.findClass(className)

    # runs if class not found
    if classIndex is None:
        return -1

    for i, a in enumerate(C.classIndex[classIndex].attributes):
        if a.name == name:
            return i
    return -2


def addAttribute(name, className):
    """
    Creates a new attribute object and inserts it into given class' list of attributes

    :param name: name of the attribute
    :param className: name of class attribute should be added to
    """

    attributeIndex = findAttribute(name, className)

    # Runs if attribute with given name already exists in given class
    if attributeIndex >= 0:
        print(f'Attribute \"{name}\" already exists in \"{className}\" class.')
    # Runs if attribute does not exist in given class
    elif attributeIndex == -2:
        newAttribute = attribute(name)
        index = C.findClass(className)
        C.classIndex[index].attributes.append(newAttribute)
        print(f'\"{name}\" attribute has been added to the \"{className}\" class!')
    # Runs if given class does not exist
    else:
        print(f"\nClass \"{className}\" does not exist")
        return


def deleteAttribute(name, className):
    """
    Deletes an attribute object from a given class.

    :param name: name of attribute to be deleted
    :param className: name of class atrribute should be deleted from
    """
    attributeIndex = findAttribute(name, className)

    # Runs if given class does not exist
    if attributeIndex == -1:
        print(f"\nClass \"{className}\" does not exist")
        return
    # Runs if class and attribute exist
    elif attributeIndex >= 0:
        classIndex = C.findClass(className)
        C.classIndex[classIndex].attributes.pop(attributeIndex)
        print(f'\"{name}\" attribute has been deleted from \"{className}\" class!')
    # Runs if class exists but attribute does not
    else:
        print(f'\"{name}\" attribute does not exist in \"{className}\" class.')


def renameAttribute(oldName, newName, className):
    """
    Renames a given attribute

    :param oldName: current name of attribute
    :param newName: new name for attribute
    :param className: name of class attribute exists within
    """

    attIndexOld = findAttribute(oldName, className)
    attIndexNew = findAttribute(newName, className)

    # Runs if attribute exists and can be renamed to new name
    if attIndexOld >= 0 and attIndexNew < 0:
        index = C.findClass(className)
        C.classIndex[index].attributes[attIndexOld].rename(newName)
        print(f'\"{oldName}\" attribute has been renamed to \"{newName}\" in the \"{className}\" class!')
    # Runs if given attribute does not exist in given class
    elif attIndexOld == -2:
        print(
            f'\"{oldName}\" attribute does not exist in the \"{className}\" class.')
    # Runs if given class does not exist
    elif attIndexOld == -1:
        print(f"\nClass \"{className}\" does not exist")
        return
    # Runs if attribute already exists with new name in given class
    else:
        print(f'\"{newName}\" is the name of an existing attribute in the \"{className}\" class.')
