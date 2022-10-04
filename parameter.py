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

    def __str__(self):
        return f"{self.type} {self.name}"

    def __repr__(self):
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
        print(f"Class \"{className}\" does not exist.")
        return -1

    # Runs if method doesn't exist within given class
    if methodIndex == -2:
        print(f"Method \"{methodName}\" does not exist in class \"{className}\".")
        return -2

    
    # Separates list name into list of params and list of types
    params = list(zip(*name))[0]
    types = list(zip(*name))[1]
    #params, types = zip(*name)
    paramIndex = []

    for i, n in enumerate(params):
        #paramIndex[i] = findParameter(n, methodIndex, classIndex)
        paramIndex.append(findParameter(n, methodIndex, classIndex))
    
    # Runs if none of the given parameters already exist in given method
    if paramIndex[0] == -1 and all(ele == paramIndex[0] for ele in paramIndex):
        for i, p in enumerate(paramIndex):
            newParameter = parameter(params[i], types[i])

            C.classIndex[classIndex].methods[methodIndex].params.append(newParameter)

            print(f"Successfully added parameter \"{str(params[i])}\" to method \"{methodName}\"!")
        return 
    
    for i, p in enumerate(paramIndex):
        if p > 0:
            print(f"Parameter \"{params[i]}\" already exists in method \"{methodName}\".")
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
        print(f"Class \"{className}\" does not exist.")
        return -1


    # Runs if method does not exist
    if methodIndex == -2:
        print(f"Method \"{methodName}\" does not exist in class \"{className}\".")
        return -2
  
    paramList = C.classIndex[cIndex].methods[methodIndex].params    
    paramNames = []
    
    for par in paramList:
        paramNames.append(par.name)
    for n in name:
        if n not in paramNames:
            print(f"Parameter \"{n}\" does not exist in method \"{methodName}\"!")
            return -3

    for par in paramList:
        if par.name in name:
            paramList.remove(par)
            print(f"Successfully removed parameter \"{par.name}\" from method \"{methodName}\"!")
    C.classIndex[cIndex].methods[methodIndex].params = paramList


"""    
    # Separates list name into list of param names
    params = list(zip(*name))[0]
    
    paramIndex = []

    #for i, n in enumerate(params):
    for i, n in enumerate(params):
        #paramIndex[i] = findParameter(n, classIndex, methodIndex)
        paramIndex.append(findParameter(n, classIndex, methodIndex))

    # Runs if any given parameters do not exist
    if -1 in paramIndex:
        for i, p in enumerate(paramIndex):
            if p == -1:
                print(f"Parameter \"{param[i]}\" does not exist within method \"{methodName}\".")

        return -3

    for i, param in enumerate(paramIndex):  
        C.classIndex[classIndex].methods[methodIndex].params.pop(param)
        print(f"Successfully removed parameter \"{param[i]}\" from method \"{methodName}\"!")
    return 
""" 
def deleteAllParameter(methodName:str, className:str):
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


def changeParam(className:str, methodName:str, oldParams:list, newParams:list):
    cIndex = C.findClass(className)
    methodIndex = A.findMethod(methodName, className)

    if cIndex is None:
        # Class does not exist
        return -1

    if methodIndex == -2:
        # Method does not exist
        return -2

    paramList = C.classIndex[cIndex].methods[methodIndex].params
    paramNames = [par.name for par in paramList]
    # removedParams = []


    print(f"Parameter List: {C.classIndex[cIndex].methods[methodIndex].params}")


    # Loop through list of parameters to replace
    for p in oldParams:
        # Check if parameter exists (has an index > -1)
        paramIndex = findParameter(p, methodIndex, cIndex)
        if paramIndex == -1:
            print(f"{methodName} does not contain method {p}")
            paramList.pop(paramIndex)
        # Pop the parameter from paramList and append it to removedParams list
        # removedParams.append(paramList.pop(paramIndex))

    

    deleteParameter(oldParams, methodName, className)

    # print(f"Removed Parameter(s): {removedParams}")
    C.classIndex[cIndex].methods[methodIndex].params = paramList
    print(f"Parameter List After: {C.classIndex[cIndex].methods[methodIndex].params}")

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
   
   # for par in paramList:
    #    if par.name in name:
     #       paramList.remove(par)
      #      print(f"Successfully removed parameter \"{par.name}\" from method \"{methodName}\"!")
    #C.classIndex[cIndex].methods[methodIndex].params = paramList



"""

    # Separates list name into list of params and list of types
    oldParams = list(zip(*oldName))[0]
    newParams = list(zip(*newName))[0]

    oldParamIndex = []
    newParamIndex = []

    for i, n in enumerate(oldName):

        #oldParamIndex[i] = findParameter(n, classIndex, methodIndex)
        oldParamIndex.append(findParameter(n, classIndex, methodIndex))

    for i, n in enumerate(newName):
        #newParamIndex[i] = findParameter(n, classIndex, methodIndex)
        newParamIndex.append(findParameter(n, classIndex, methodIndex))

    
    # Runs if any old parameters do not exist
    if -1 in oldParamIndex:
        for i, p in enumerate(oldParamIndex):
            if p == -1:
                print(f"Parameter \"{oldName[i]}\" does not exist within method \"{methodName}\".")

        return -3


    # Runs if any new parameters already exist
    if -1 in newParamIndex:
        for i, p in enumerate(newParamIndex):
            if p == -1:
                print(f"Parameter \"{newName[i]}\" already exists within method \"{methodName}\".")
        return -4
"""
    # Runs if able to rename parameters
    #deleteParameter(oldName, methodName, className)
    #addParameter(newName, methodName, className)

    