"""
Author: Aaron Heinbaugh
Filename: saveload.py
Description: Saves and loads a user's session as a json
"""

import json
from os.path import exists
import os.path
from pathvalidate import is_valid_filename
import copy

import UMLClass as u
import relationship as r
import attributes as a
import parameter as p


##################################################################
"""
# Test code

class UMLClass:
    def __init__(self, name: str):
            self.name = name
            self.fields = []
            self.methods = []
        
class UMLMethod:
    def __init__(self, name: str, returnType = None):
        self.name = name
        self.return_type = returnType
        self.params = []

class UMLField:
    def __init__ (self, name: str , type = None):
        self.name = name
        self.type = type
    
class UMLParameters:
    def __init__ (self, name: str , type = None):
        self.name = name
        self.type = type

class UMLRelationship:
    def __init__ (self, source, destination, type):
        self.source = source
        self.destination = destination
        self.type = type

tire = UMLClass("Tire")
tiref1 = UMLField('diameter', 'float')
tiref2 = UMLField("psi", "float")
tiref3 = UMLField("brand", 'string')
tirem1 = UMLMethod('setPSI', 'void')
tirem1p1 = UMLParameters("new_psi", "string")
tirem1.params.append(tirem1p1)
tire.fields.append(tiref1)
tire.fields.append(tiref2)
tire.fields.append(tiref3)
tire.methods.append(tirem1)

car = UMLClass("Car")
carf1 = UMLField("make", 'string')
carf2 = UMLField("model", 'string')
carf3 = UMLField("year", "int")
carm1 = UMLMethod("drive", "void")
car.fields.append(carf1)
car.fields.append(carf2)
car.fields.append(carf3)
car.methods.append(carm1)

u.classIndex.append(tire)
u.classIndex.append(car)

r1 = UMLRelationship(tire, car, "composition")

r.relationIndex.append(r1)

"""

def save(classes, relations, filename):
    """
    saves file as filename in specified directory: open('filepath' + filename...)
    currently saves in root folder

    :param param1: UMLclass list 
    :param param2: relationship list 
    :param param3: filename specified by user
    :returns: (string) error message or "" if succesful
    """
    
    returnMessage = ""
    filename = filename
    
    #checks if file name is valid
    if not is_valid_filename(filename):
        returnMessage = "Invalid file name."
        print("Invalid file name")
        return returnMessage
    
    if filename.endswith('.json'):
        filename = filename[:-5]

    #checks if folder exists and creates it if it doesn't
    fileExists = os.path.exists("UMLsavefiles")
    if not fileExists:    
        print("Created directory: UMLsavefiles")
        os.mkdir("UMLsavefiles")
    
    #combines both into a dictionary
    t = {"classes": classes, "relationships": relations}
    
    #encodes tuple above to json
    jsonString = json.dumps(t, default=vars, indent=4)
    
    #saves json string to file
    with open("UMLsavefiles/" + filename + ".json", "w") as outfile:
        outfile.write(jsonString)
    
    return returnMessage


def saveGUI(classes, relations, filename):
    """
    saves file as filename in specified directory: open('filepath' + filename...)
    currently saves in root folder

    :param param1: UMLclass list 
    :param param2: relationship list 
    :param param3: filename specified by user
    :returns: (string) error message or "" if succesful
    """
    
    returnMessage = ""
    filename = filename
    
    if filename.endswith('.json'):
        filename = filename[:-5]

    #combines both into a dictionary
    t = {"classes": classes, "relationships": relations}
    
    #encodes tuple above to json
    jsonString = json.dumps(t, default=vars, indent=4)
    
    #saves json string to file
    with open(filename + ".json", "w") as outfile:
        outfile.write(jsonString)
    
    return returnMessage
#save(u.classIndex, r.relationIndex, "testfile")
##################################################################


def load(filename): 
    """
    loads filename from specified directory: open('filepath' + filename...)
    currently loads from root folder

    :param param1: the file name to load
    :returns: tuple(list[UMLclass], list[relationships]) 
    """
    if filename.endswith('.json'):
        filename = filename[:-5]
        
    #check if file exists returns original lists if not
    fileExists = os.path.exists("UMLsavefiles/" + filename + '.json')
    if not fileExists:    
        print("File not found")
        return
        #return (u.classIndex, r.relationIndex)

    
    #creates lists to return
    returnClasses = []
    returnRelations = []
    
    #checks if file is empty and returns empty lists

    if os.stat("UMLsavefiles/" + filename + ".json").st_size == 0:
        u.classIndex = returnClasses
        r.relationIndex = returnRelations
        return
        #return(returnClasses, returnRelations)    
    
    try:
        #opens the file and save contents as a json string
        with open("UMLsavefiles/" + filename + ".json", "r") as openfile: 
            jsonObject = json.load(openfile)

        classes = jsonObject["classes"]
        relationships = jsonObject["relationships"]
        
        #creates new class object for each json class and adds them to return list
        for c in classes:
            name = c['name']
            classObj = u.UMLClass(name)
            fields = c['fields']
            for fld in fields:
                classObj.fields.append(a.field(fld['name'],fld['type']))
            methods = c['methods']
            for meth in methods:
                mName = meth["name"]
                mType = meth["return_type"]
                methodObj = a.method(mName, mType)
                mParams = meth['params']
                for par in mParams:
                    methodObj.params.append(p.parameter(par['name'],par['type']))
                classObj.methods.append(methodObj)
            returnClasses.append(classObj)
        
        #creates new relation for each json relation and adds them to return list
        for rel in relationships:
            returnRelations.append(r.UMLRelationship(rel['source'], rel['destination'], rel['type']))

        u.classIndex = returnClasses
        r.relationIndex = returnRelations       
        return 
        #return (returnClasses, returnRelations)
    
    #if error loading return original lists
    except Exception as e:
        print("Load failed")
        return
        #return (u.classIndex, r.relationIndex)
 
def loadGUI(filename): 
    """
    loads filename from specified directory: open('filepath' + filename...)
    currently loads from root folder

    :param param1: the file name to load
    :returns: tuple(list[UMLclass], list[relationships]) 
    """
    #creates lists to return
    returnClasses = []
    returnRelations = []
    message = ""
    #checks if file is empty and returns empty lists

    if os.stat(filename).st_size == 0:
        u.classIndex = returnClasses
        r.relationIndex = returnRelations
        message = "Loaded empty file"
        return message
        #return(returnClasses, returnRelations)    
    
    try:
        #opens the file and save contents as a json string
        with open(filename, "r") as openfile: 
            jsonObject = json.load(openfile)

        classes = jsonObject["classes"]
        relationships = jsonObject["relationships"]
        
        #creates new class object for each json class and adds them to return list
        for c in classes:
            name = c['name']
            classObj = u.UMLClass(name)
            fields = c['fields']
            for fld in fields:
                classObj.fields.append(a.field(fld['name'],fld['type']))
            methods = c['methods']
            for meth in methods:
                mName = meth["name"]
                mType = meth["return_type"]
                methodObj = a.method(mName, mType)
                mParams = meth['params']
                for par in mParams:
                    methodObj.params.append(p.parameter(par['name'],par['type']))
                classObj.methods.append(methodObj)
            returnClasses.append(classObj)
        
        #creates new relation for each json relation and adds them to return list
        for rel in relationships:
            returnRelations.append(r.UMLRelationship(rel['source'], rel['destination'], rel['type']))

        u.classIndex = returnClasses
        r.relationIndex = returnRelations       
        message = "Loaded successfully"
        return message
            #return (returnClasses, returnRelations)
    
    #if error loading return original lists
    
    except Exception as e:
        print("Load failed")
        message = "Load failed"
        return message
    