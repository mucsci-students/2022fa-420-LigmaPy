"""
Author: Julia Geesaman
Filename: parameter.py
Description: Adds, deletes, and renames parameters
"""

import model.UMLClass as C
import model.attributes as A
from UMLException import UMLException, UMLSuccess
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


def addParameter(name:list, methodName:str, className:str):
    """
    Adds parameter to specified method in specified class

    :param name: name(s) of the parameter(s) to be added
    :param methodName: name of the method parameter should be added to
    :param className: name of class containing the method the parameters will be added to
    """
    
    classIndex = C.findClass(className)
    methodIndex = A.findMethod(methodName, className)

    # Runs if class doesn't exist
    if classIndex == None:
        # print(UMLException("Class error", f"{className} does not exist"))
        return codes.ADD_PARAM_CLASS_NOT_EXIST

    # Runs if method doesn't exist within given class
    if methodIndex == -2:
        # print(UMLException("Method error", f"{methodName} does not exist"))
        return codes.ADD_PARAM_METHOD_NOT_EXIST

    # Separates list name into list of params and list of types
    params = list(zip(*name))[0]
    types = list(zip(*name))[1]
    paramIndex = []

    for i, n in enumerate(params):
        paramIndex.append(findParameter(n, methodIndex, classIndex))
    
    # Runs if none of the given parameters already exist in given method
    if paramIndex[0] == -1 and all(ele == paramIndex[0] for ele in paramIndex):
        for i, p in enumerate(paramIndex):
            newParameter = parameter(params[i], types[i])

            C.classIndex[classIndex].methods[methodIndex].params.append(newParameter)

            # print(UMLSuccess(f"{params[i]} added to {methodName}"))
        return codes.ADDED_PARAM
    
    for i, p in enumerate(paramIndex):
        if p >= 0:
            print(UMLException("Parameter error", f"{params[i]} already exists in {methodName}"))
    return codes.ADD_PARAM_ALREADY_EXISTS


def deleteParameter(name:list, methodName:str, className:str):
    """
    Removes parameter from a specified method in specified class

    :param name: name(s) of the parameter(s) to be removed
    :param methodName: name of the method parameter should be removed from
    :param className: name of class containing the method the parameters will be removed from
    """

    cIndex = C.findClass(className)
    methodIndex = A.findMethod(methodName, className)

    # Runs if class does not exist
    if cIndex == None:
        # print(UMLException("Class error", f"{className} does not exist"))
        return codes.DELETE_PARAM_CLASS_NOT_EXIST


    # Runs if method does not exist
    if methodIndex == -2:
        # print(UMLException("Method error", f"{methodName} does not exist in {className}"))
        return codes.DELETE_PARAM_METHOD_NOT_EXIST
  
    paramList = C.classIndex[cIndex].methods[methodIndex].params    
    paramNames = []
    
    for par in paramList:
        paramNames.append(par.name)
    for n in name:
        if n not in paramNames:
            # print(UMLException("Parameter error", f"{n} does not exist in {methodName}"))
            return codes.DELETE_PARAM_NOT_EXIST

    for par in paramList:
        if par.name in name:
            paramList.remove(par)
            print(UMLSuccess(f"Removed {par.name} from {methodName}"))
    C.classIndex[cIndex].methods[methodIndex].params = paramList
    return codes.DELETED_PARAM

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
        print(f"Class \"{className}\" does not ex?ist.")
        return codes.DELETE_PARAM_CLASS_NOT_EXIST

    # Runs if method does not exist
    if methodIndex == -2:
        # print(f"Method \"{methodName}\" does not exist in class \"{className}\".")
        return codes.DELETE_PARAM_METHOD_NOT_EXIST

    C.classIndex[classIndex].methods[methodIndex].params = []
    return codes.DELETED_PARAM

def changeParameter(oldName:list, newName:list, methodName:str, className:str):
    """
    Changes and replaces parameter(s) to specified method in specified class

    :param oldName: name of the parameter to be replaced
    :param newName: name of parameter replacing other parameter
    :param methodName: name of the method parameter should be added to
    :param className: name of class containing the method the parameters will be added to
    """

    cIndex = C.findClass(className)
    methodIndex = A.findMethod(methodName, className)

    if cIndex == None:
        # print(f"Class \"{className}\" does not exist.")
        return codes.CHANGE_PARAM_CLASS_NOT_EXIST 

    if methodIndex == -2:
        # print(f"Method \"{methodName}\" does not exist in class \"{className}\".")
        return codes.CHANGE_PARAM_METHOD_NOT_EXIST

    paramList = C.classIndex[cIndex].methods[methodIndex].params    
    paramNames = []
    for par in paramList:
        paramNames.append(par.name)
    
    for n in oldName:
        if n not in paramNames:
            # print(f"Parameter \"{n}\" does not exist in method \"{methodName}\"!")
            return codes.CHANGE_PARAM_PARAM_NOT_EXIST
    
    params = list(zip(*newName))[0]
    for n in params:
        if n in paramNames:
            # print(f"Parameter \"{n}\" already exists in method \"{methodName}\"!")
            return codes.CHANGE_PARAM_ALREADY_EXISTS
    
    deleteParameter(oldName, methodName, className)
    addParameter(newName, methodName, className)
    return codes.CHANGED_PARAM
    