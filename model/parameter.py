"""
Author: Julia Geesaman
Filename: parameter.py
Description: Adds, deletes, and renames parameters
"""

import model.UMLClass as C
import model.attributes as A
from UMLException import UMLException, UMLSuccess

class parameter:
    def __init__(self, name:str, type:str):
        """
        Initializes parameter with name

        :param name: name of the parameter
        :param type: Type of the parameter
        """
        self.name = name
        self.type = type

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
        print(UMLException("Class error", f"{className} does not exist"))
        return -1

    # Runs if method doesn't exist within given class
    if methodIndex == -2:
        print(UMLException("Method error", f"{methodName} does not exist"))
        return -2

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

            print(UMLSuccess(f"{params[i]} added to {methodName}"))
        return 1
    
    for i, p in enumerate(paramIndex):
        if p >= 0:
            print(UMLException("Parameter error", f"{params[i]} already exists in {methodName}"))
    return -3


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
        print(UMLException("Class error", f"{className} does not exist"))
        return -1


    # Runs if method does not exist
    if methodIndex == -2:
        print(UMLException("Method error", f"{methodName} does not exist in {className}"))
        return -2
  
    paramList = C.classIndex[cIndex].methods[methodIndex].params    
    paramNames = []
    
    for par in paramList:
        paramNames.append(par.name)
    for n in name:
        if n not in paramNames:
            print(UMLException("Parameter error", f"{n} does not exist in {methodName}"))
            return -3

    for par in paramList:
        if par.name in name:
            paramList.remove(par)
            print(UMLSuccess(f"Removed {par.name} from {methodName}"))
    C.classIndex[cIndex].methods[methodIndex].params = paramList
    return 1

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
        print(f"Class \"{className}\" does not exist.")
        return -1

    # Runs if method does not exist
    if methodIndex == -2:
        print(f"Method \"{methodName}\" does not exist in class \"{className}\".")
        return -2

    C.classIndex[classIndex].methods[methodIndex].params = []
    return 1

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
        print(f"Class \"{className}\" does not exist.")
        return -1    

    if methodIndex == -2:
        print(f"Method \"{methodName}\" does not exist in class \"{className}\".")
        return -2

    paramList = C.classIndex[cIndex].methods[methodIndex].params    
    paramNames = []
    for par in paramList:
        paramNames.append(par.name)
    
    for n in oldName:
        if n not in paramNames:
            print(f"Parameter \"{n}\" does not exist in method \"{methodName}\"!")
            return -3
    
    params = list(zip(*newName))[0]
    for n in params:
        if n in paramNames:
            print(f"Parameter \"{n}\" already exists in method \"{methodName}\"!")
            return -4
    
    deleteParameter(oldName, methodName, className)
    addParameter(newName, methodName, className)
    return 1
    