"""
Author: Julia Geesaman
Filename: parameter.py
Description: Adds, deletes, and renames parameters
"""

import UMLClass as C
import attributes as A


class parameter:

    def __init__(self, name:str, type:str):
        """
        Initializes parameter with name

        :param name: name of the parameter
        """
        self.name = name
        self.type = type




def findParameter(name, methodIndex, classIndex):
    """
    Finds whether a parameter exists within a method

    :param name: name(s) of parameter(s) to be found
    :param methodName: name of method to be searched
    :param className: name of class to be searched for method

    :returns: -1 if parameter does not exist within given method
              i: index of parameter, if parameter exists within given method within given class 
    """

    for i, p in enumerate(C.classIndex[classIndex].attributes[methodIndex].params):
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
    methodIndex = A.findAttribute(methodName, className)

    # Runs if class doesn't exist
    if classIndex == None:
        print(f"Class \"{className}\" does not exist.")
        return -1

    # Runs if method doesn't exist within given class
    if methodIndex == -2:
        print(f"Method \"{methodName}\" does not exist in class \"{className}\".")
        return
    
    # Separates list name into list of params and list of types
    params = list(zip(*name))[0]
    types = list(zip(*name))[1]

    paramIndex = []

    for i, n in enumerate(params):
        paramIndex[i] = findParameter(n, methodIndex, classIndex)

    # Runs if none of the given parameters already exist in given method
    if paramIndex[0] == -1 and all(ele == paramIndex[0] for ele in paramIndex):
        for i, p in enumerate(paramIndex):
            newParameter = parameter(params[i], types[i])
            C.classIndex[classIndex].attributes[methodIndex].params.append(newParameter)
            print(f"Successfully added parameter \"{params[i]}\" to method \"{methodName}\"!")
        return 
    
    for i, p in enumerate(paramIndex):
        if p > 0:
            print(f"Parameter \"{params[i]}\" already exists in method \"{methodName}\".")
    return 


def deleteParameter(name:list, methodName:str, className:str):
    """
    Removes parameter from a specified method in specified class

    :param name: name(s) of the parameter(s) to be removed
    :param methodName: name of the method parameter should be removed from
    :param className: name of class containing the method the parameters will be removed from
    """

    classIndex = C.findClass(className)
    methodIndex = A.findAttribute(methodName, className)

    # Runs if class does not exist
    if classIndex == None:
        print(f"Class \"{className}\" does not exist.")
        return

    # Runs if method does not exist
    if methodIndex == -2:
        print(f"Method \"{methodName}\" does not exist in class \"{className}\".")
        return
    
    # Separates list name into list of param names
    params = list(zip(*name))[0]

    paramIndex = []

    for i, n in enumerate(params):
        paramIndex[i] = findParameter(n, classIndex, methodIndex)

    # Runs if any given parameters do not exist
    if -1 in paramIndex:
        for i, p in enumerate(paramIndex):
            if p == -1:
                print(f"Parameter \"{param[i]}\" does not exist within method \"{methodName}\".")
        return

    for i, param in enumerate(paramIndex):  
        C.classIndex[classIndex].attributes[methodIndex].params.pop(param)
        print(f"Successfully removed parameter \"{param[i]}\" from method \"{methodName}\"!")
    return
    

def changeParameter(oldName:list, newName:list, methodName:str, className:str):
    """
    Changes and replaces parameter(s) to specified method in specified class

    :param oldName: name of the parameter to be replaced
    :param newName: name of parameter replacing other parameter
    :param methodName: name of the method parameter should be added to
    :param className: name of class containing the method the parameters will be added to
    """
    classIndex = C.findClass(className)
    methodIndex = A.findAttribute(methodName, className)

    if classIndex == None:
        print(f"Class \"{className}\" does not exist.")
        return     

    if methodIndex == -2:
        print(f"Method \"{methodName}\" does not exist in class \"{className}\".")
        return

    # Separates list name into list of params and list of types
    oldParams = list(zip(*oldName))[0]
    newParams = list(zip(*newName))[0]

    oldParamIndex = []
    newParamIndex = []

    for i, n in enumerate(oldName):
        oldParamIndex[i] = findParameter(n, classIndex, methodIndex)

    for i, n in enumerate(newName):
        newParamIndex[i] = findParameter(n, classIndex, methodIndex)
    
    # Runs if any old parameters do not exist
    if -1 in oldParamIndex:
        for i, p in enumerate(oldParamIndex):
            if p == -1:
                print(f"Parameter \"{oldName[i]}\" does not exist within method \"{methodName}\".")
        return

    # Runs if any new parameters already exist
    if -1 in newParamIndex:
        for i, p in enumerate(newParamIndex):
            if p == -1:
                print(f"Parameter \"{newName[i]}\" already exists within method \"{methodName}\".")
        return

    # Runs if able to rename parameters
    deleteParameter(oldName, methodName, className)
    addParameter(newName, methodName, className)
    