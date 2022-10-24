"""
Author: Julia Geesaman
Filename: parameter.py
Description: Adds, deletes, and renames parameters
"""

import model.UMLClass as C
import model.attributes as A
from model.ErrorHandlers.ReturnStatus import codes

class parameter:
    def __init__(self, name:str, type:str):
        """
        Initializes parameter with name

        :param name: name of the parameter
        :param type: Type of the parameter
        """
        self.name = name
        self.type = type

    def toDict(self):
        """
        Converts a parameter to a dictionary
        
        :returns: A dictionary of the parameter
        """
        return {"name": self.name, "type": self.type}

    # Called when printing a parameter object with print()
    def __str__(self):
        return f"{self.type} {self.name}"

def findParameter(name, methodIndex, classIndex):
    """
    Finds whether a parameter exists within a method

    :param name: name(s) of parameter(s) to be found
    :param methodName: name of method to be searched
    :param className: name of class to be searched for method
    :returns: -1 if parameter does not exist within given method
              i: index of parameter, if parameter exists within given method within given class 
    """
    for i, p in enumerate(C.classIndex[classIndex].methods[methodIndex].params):
        # If name is found, return its index
        if p.name == name:
            return i
    return -1


def addParameter(paramName:str, paramType:str, methodName:str, className:str):
    """
    Adds parameter to specified method in specified class

    :param paramName: name of the parameter to be added
    :param paramType: type of the parameter to be added
    :param methodName: name of the method parameter should be added to
    :param className: name of class containing the method the parameters will be added to
    """
    
    classIndex = C.findClass(className)
    methodIndex = A.findMethod(methodName, className)

    # Runs if class doesn't exist
    if classIndex == None:
        return codes.ADD_PARAM_CLASS_NOT_EXIST

    # Runs if method doesn't exist within given class
    if methodIndex == -2:
        return codes.ADD_PARAM_METHOD_NOT_EXIST
    # Check if parameter already exists in the method
    if findParameter(paramName, methodIndex, classIndex) == -1:
        C.classIndex[classIndex].methods[methodIndex].params.append(parameter(paramName, paramType))
        return codes.ADDED_PARAM
    else:
        return codes.ADD_PARAM_ALREADY_EXISTS


def deleteParameter(paramName:str, methodName:str, className:str):
    """
    Removes parameter from a specified method in specified class

    :param paramName: name of the parameter to be removed
    :param methodName: name of the method parameter should be removed from
    :param className: name of class containing the method the parameters will be removed from
    """

    cIndex = C.findClass(className)
    methodIndex = A.findMethod(methodName, className)

    # Runs if class does not exist
    if cIndex == None:
        return codes.DELETE_PARAM_CLASS_NOT_EXIST

    # Runs if method does not exist
    if methodIndex == -2:
        return codes.DELETE_PARAM_METHOD_NOT_EXIST

    pIndex = findParameter(paramName, methodIndex, cIndex)

    if pIndex > -1:
        C.classIndex[cIndex].methods[methodIndex].params.pop(pIndex)
        return codes.DELETED_PARAM
    else:
        return codes.DELETE_PARAM_NOT_EXIST

def deleteAllParameter(methodName:str, className:str):
    """
    Removes ALL parameters from the given method in the given class

    :param methodName:  Name of the method to delete parameters from
    :param className:   Name of the class containing the method
    """
    classIndex = C.findClass(className)
    methodIndex = A.findMethod(methodName, className)

    # Runs if class does not exist
    if classIndex == None:
        return codes.DELETE_PARAM_CLASS_NOT_EXIST

    # Runs if method does not exist
    if methodIndex == -2:
        return codes.DELETE_PARAM_METHOD_NOT_EXIST

    C.classIndex[classIndex].methods[methodIndex].params.clear()
    return codes.DELETED_PARAM

def changeParameter(oldName:str, newName:str, methodName:str, className:str):
    """
    Changes and replaces parameter(s) to specified method in specified class

    :param oldName: name of the parameter to be replaced
    :param newName: name of parameter replacing other parameter
    :param methodName: name of the method parameter should be added to
    :param className: name of class containing the method the parameters will be added to
    """

    cIndex = C.findClass(className)
    methodIndex = A.findMethod(methodName, className)
    # Check if class exists
    if cIndex == None:
        return codes.CHANGE_PARAM_CLASS_NOT_EXIST 
    # Check if method exists
    if methodIndex == -2:
        return codes.CHANGE_PARAM_METHOD_NOT_EXIST

    pIndex = findParameter(oldName, methodIndex, cIndex)
    # Check if the parameter does not exist
    if pIndex == -1:
        return codes.CHANGE_PARAM_PARAM_NOT_EXIST
    # Check if the new parameter already exists
    if findParameter(newName, methodIndex, cIndex) > -1:
        return codes.CHANGE_PARAM_ALREADY_EXISTS
    
    oldType = C.classIndex[cIndex].methods[methodIndex].params[pIndex].type

    deleteParameter(oldName, methodName, className)
    addParameter(newName, oldType, methodName, className)
    return codes.CHANGED_PARAM
    