"""
Filename: attributes.py
Description: Adds, deletes, and renames an attribute (method or field)
"""

import model.UMLClass as C
from model.ErrorHandlers.ReturnStatus import codes


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

    def toDict(self):
        """
        Converts a method to a dictionary

        :returns: A dictionary of the method
        """

        paramDict = [p.toDict() for p in self.params]

        return {"name": self.name, "return_type": self.return_type, "params": paramDict}

    def __str__(self):
        return f"{self.return_type} {self.name}({', '.join(map(str, self.params))})"

class field(attribute):
    def __init__(self, name : str, t : str):
        super().__init__(name)
        self.type = t

    def toDict(self):
        """
        Converts a field to a dictionary

        :returns: A dictionary of the field
        """
        return {"name": self.name, "type": self.type}

    def changeType(self, newName : str):
        self.name = newName

    def __str__(self):
        return f"{self.type} {self.name}"


###########################################################

# Each of these have been specialized into methods and fields. 
# We could possibly merge these into one, and require another
# parameter passed to specify which type - but this is up
# to us. Just a design thing

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

    existingMethod = findMethod(name, className)

    # Runs if attribute with given name already exists in given class
    if existingMethod >= 0:
        return codes.ADD_EXISTING_METHOD
    # Runs if attribute does not exist in given class
    elif existingMethod == -2:
        newMethod = method(name, ret_type)
        index = C.findClass(className)
        C.classIndex[index].methods.append(newMethod)
        return codes.ADDED_METHOD
    # Runs if given class does not exist
    else:
        return codes.ADD_NOT_EXISTING_CLASS

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

    existingField = findField(name, className)

    # Runs if attribute with given name already exists in given class
    if existingField >= 0:
        return codes.ADD_EXISTING_FIELD
    # Runs if attribute does not exist in given class
    elif existingField == -2:
        newField = field(name, t)
        index = C.findClass(className)
        C.classIndex[index].fields.append(newField)
        return codes.ADDED_FIELD
    # Runs if given class does not exist
    else:
        return codes.ADD_FIELD_NOT_EXISTING_CLASS


def deleteMethod(name, className):
    """
    Deletes a method object from a given class.

    :param name: name of method to be deleted
    :param className: name of class method should be deleted from
    :returns: -1 if the class does not exist
              -2 if the method does not exist
               1 on successful deletion
    """
    methIndex = findMethod(name, className)

    # Runs if given class does not exist
    if methIndex == -1:
        return codes.DELETE_METHOD_NOT_EXISTING_CLASS
    # Runs if class and attribute exist
    elif methIndex >= 0:
        classIndex = C.findClass(className)
        C.classIndex[classIndex].methods.pop(methIndex)
        return codes.DELETED_METHOD
    # Runs if class exists but method does not
    else:
        return codes.DELETE_NOT_EXISTING_METHOD

def deleteField(name, className):
    """
    Deletes a field object from a given class.

    :param name: name of field to be deleted
    :param className: name of class field should be deleted from
    :returns: -1 if the class does not exist
              -2 if the field does not exist
               1 on successful deletion
    """
    fieldIndex = findField(name, className)

    # Runs if given class does not exist
    if fieldIndex == -1:
        return codes.DELETE_FIELD_NOT_EXISTING_CLASS
    # Runs if class and attribute exist
    elif fieldIndex >= 0:
        classIndex = C.findClass(className)
        C.classIndex[classIndex].fields.pop(fieldIndex)
        return codes.DELETED_FIELD
    # Runs if class exists but field does not
    else:
        return codes.DELETE_FIELD_NOT_EXISTING_FIELD

def renameMethod(oldName, newName, className):
    """
    Renames a given method

    :param oldName: current name of method
    :param newName: new name for method
    :param className: name of class method exists within
    :returns: -1 if given class does not exist
              -2 if given method does not exist in class
              -3 if the new name is already in use in class
    """

    attIndexOld = findMethod(oldName, className)
    attIndexNew = findMethod(newName, className)

    # Runs if method exists and can be renamed to new name
    if attIndexOld >= 0 and attIndexNew < 0:
        index = C.findClass(className)
        C.classIndex[index].methods[attIndexOld].rename(newName)
        return codes.RENAMED_METHOD
    # Runs if given method does not exist in given class
    elif attIndexOld == -2:
        return codes.RENAME_METHOD_METHOD_NOT_EXIST
    # Runs if given class does not exist
    elif attIndexOld == -1:
        return codes.RENAME_METHOD_CLASS_NOT_EXIST
    # Runs if method already exists with new name in given class
    else:
        return codes.RENAME_METHOD_NEW_EXISTS

def renameField(oldName, newName, className):
    """
    Renames a given field

    :param oldName: current name of field
    :param newName: new name for field
    :param className: name of class field exists within
    :returns: -1 if given class does not exist
              -2 if given field does not exist in class
              -3 if the new name is already in use in class
    """

    attIndexOld = findField(oldName, className)
    attIndexNew = findField(newName, className)

    # Runs if field exists and can be renamed to new name
    if attIndexOld >= 0 and attIndexNew < 0:
        index = C.findClass(className)
        C.classIndex[index].fields[attIndexOld].rename(newName)
        return codes.RENAMED_FIELD
    # Runs if given field does not exist in given class
    elif attIndexOld == -2:
        return codes.RENAME_FIELD_FIELD_NOT_EXIST
    # Runs if given class does not exist
    elif attIndexOld == -1:
        return codes.RENAME_FIELD_CLASS_NOT_EXIST
    # Runs if field already exists with new name in given class
    else:
        return codes.RENAME_FIELD_NEW_EXISTS
