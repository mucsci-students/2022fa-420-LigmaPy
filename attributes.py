"""
Authors: Julia Geesaman, Sam Noggle
Filename: attributes.py
Description: Adds, deletes, and renames an attribute (method or field)
"""

import UMLClass as C


class attribute():
    """
    This is the attribute super class.
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

class method(attribute):
    def __init__(self, name : str, retType : str):
        super().__init__(name)
        self.return_type = retType
        self.params = []
    
    def findParam(self, paramName : str):
        """
        Searches the method's parameter list for a parameter by name

        :param paramName: The name of the parameter to find
        :return: The index of where that parameter is in the list
        """
        for i, param in enumerate(self.params):
            if param.name == paramName:
                return i

class field(attribute):
    def __init__(self, name : str, t : str):
        super().__init__(name)
        self.type = t

    def changeType(self, newName : str):
        self.name = newName


###########################################################

def findMethod(name, className):
    """
    Finds whether the given method exists in a class

    :param name: name of the method
    :param className: class method is part of

    :returns: -1 if given class does not exist
            -2 if method does not exist in given class
            i index of method, if method and class exist
    """

    classIndex = C.findClass(className)

    # runs if class not found
    if classIndex is None:
        return -1

    for i, a in enumerate(C.classIndex[classIndex].methods):
        if a.name == name:
            return i
    return -2

def findField(name, className):
    """
    Finds whether the given field exists in a class

    :param name: name of the field
    :param className: class field is part of

    :returns: -1 if given class does not exist
              -2 if field does not exist in given class
               i index of field, if field and class exist
    """

    classIndex = C.findClass(className)

    # runs if class not found
    if classIndex is None:
        return -1

    for i, a in enumerate(C.classIndex[classIndex].fields):
        if a.name == name:
            return i
    return -2



def addMethod(name : str, className : str, ret_type : str):
    """
    Creates a new method object and inserts it into given class' list of methods

    :param name: name of the method
    :param className: name of class method should be added to
    :param ret_type: The type that the method will return
    :returns: -1 if the class does not exist
              -2 if the method already exists
               1 on successful add
    """

    existingMethod = findMethod(name, className, ret_type)

    # Runs if attribute with given name already exists in given class
    if existingMethod >= 0:
        return -2
    # Runs if attribute does not exist in given class
    elif existingMethod == -2:
        newMethod = method(name, ret_type)
        index = C.findClass(className)
        C.classIndex[index].methods.append(newMethod)
        return 1
    # Runs if given class does not exist
    else:
        return -1

def addField(name, className, t):
    """
    Creates a new field object and inserts it into given class' list of fields

    :param name: name of the field
    :param className: name of class field should be added to
    :param t: The type of the field
    :returns: -1 if the class does not exist
              -2 if the field already exists
               1 on successful add
    """

    existingField = findField(name, className, t)

    # Runs if attribute with given name already exists in given class
    if existingField >= 0:
        return -2
    # Runs if attribute does not exist in given class
    elif existingField == -2:
        newField = field(name, t)
        index = C.findClass(className)
        C.classIndex[index].fields.append(newField)
        return 1
    # Runs if given class does not exist
    else:
        return -1


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
