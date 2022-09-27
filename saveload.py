"""
Author: Aaron Heinbaugh
Filename: saveload.py
Description: Saves and loads a user's session as a json
"""

import json
from os.path import exists
import os.path
from pathvalidate import is_valid_filename

import UMLClass as u
import relationship as r
import methods as m
import fields as f
import params as p


##################################################################

# Test code
"""
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
    :returns: nothing
    """
    filename = filename
    
    #checks if file name is valid
    if not is_valid_filename(filename):
        print("Invalid file name.")
        return
    
    if filename.endswith('.json'):
        filename = filename[:-5]

    #checks if folder exists and creates it if it doesn't
    fileExists = os.path.exists("UMLsavefiles")
    if not fileExists:    
        print("Created directory: UMLsavefiles")
        os.mkdir("UMLsavefiles")
    
    #converts each relation class object to just the name
    for each in relations:
        each.source = each.source.name
        each.destination = each.destination.name
    
    #combines both into a dictionary
    t = {"classes": classes, "relationships": relations}
    
    #encodes tuple above to json
    jsonString = json.dumps(t, default=vars, indent=4)
    
    #saves json string to file
    with open("UMLsavefiles/" + filename + ".json", "w") as outfile:
        outfile.write(jsonString)

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
                classObj.fields.append(f.UMLField(fld['name'],fld['type']))
            methods = c['methods']
            for meth in methods:
                mName = meth["name"]
                mType = meth["return_type"]
                methodObj = m.UMLMethod(mName, mType)
                mParams = meth['params']
                for p in mParams:
                    methodObj.params.append(p.UMLParameters(p['name'],p['type']))
                classObj.methods.append(methodObj)
            returnClasses.append(classObj)
        

        #loops through relationship json and decodes each piece creating new objects then adds them to a list
        for eachRelation in relations:    
            name = r.UMLRelationship(eachRelation['source'], eachRelation['destination'])
            returnRelations.append(name) 
            
        #apapend global lists
        r.relationIndex.append(returnRelations)
        u.classIndex.append(returnClasses)
        return (returnClasses, returnRelations)

    
    #if error loading return original lists
    except Exception as e:
        print("Load failed")
        return
        #return (u.classIndex, r.relationIndex)
 
