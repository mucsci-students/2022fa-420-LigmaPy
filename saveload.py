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
import attributes as a


##################################################################


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
    
    #combines both into a tuple
    t = (classes, relations)
    
    #encodes tuple above to json
    jsonString = json.dumps(t, default=vars, indent=4)
    
    #saves json string to file
    with open("UMLsavefiles/" + filename + ".json", "w") as outfile:
        outfile.write(jsonString)


##################################################################


def load(filename): 
    """
    loads filename from specified directory: open('filepath' + filename...)
    currently loads from root folder

    :param param1: the file name to load
    :returns: tuple(list[UMLclass], list[relationships]) 
    """
    
    #check if file exists returns original lists if not
    fileExists = os.path.exists("UMLsavefiles/" + filename + '.json')
    if not fileExists:    
        print("File not found")
        return (u.classIndex, r.relationIndex)

    
    #creates lists to return
    returnClasses = []
    returnRelations = []
    
    #checks if file is empty and returns empty lists

    if os.stat("UMLsavefiles/" + filename + ".json").st_size == 0:
        return(returnClasses, returnRelations)    
    
    try:
        #opens the file and save contents as a json string
        with open("UMLsavefiles/" + filename + ".json", "r") as openfile: 
            jsonObject = json.load(openfile)
        
        #divides the json string into classes/relations
        classes = jsonObject[0]
        relations = jsonObject[1]

        #loops through classes json and decodes each piece creating new objects then adds them to a list
        for eachClass in classes:
            className = str(eachClass['name'])
            attributesList = eachClass['attributes']

            className = u.UMLClass(className)
            for eachAttribute in attributesList:
                className.attributes.append(a.attribute(eachAttribute['name']))
            returnClasses.append(className)
        
        #loops through relationship json and decodes each piece creating new objects then adds them to a list
        for eachRelation in relations:    
            name = r.UMLRelationship(eachRelation['source'], eachRelation['destination'])
            returnRelations.append(name) 

        return (returnClasses, returnRelations)
    
    #if error loading return original lists
    except Exception as e:
        print("Load failed")
        return (u.classIndex, r.relationIndex)
 
