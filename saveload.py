"""
Author: Aaron Heinbaugh
Filename: saveload.py
Description: Saves and loads a user's session as a json
"""

import json
from os.path import exists
import os.path
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

    fileExists = os.path.exists("UMLsavefiles")
    if not fileExists:    
        print("Created directory: UMLsavefiles")
        os.mkdir("UMLsavefiles")
    

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
        print("File Saved.")

# maybe return filename or flag?

##################################################################


def load(filename): 
    """
    loads filename from specified directory: open('filepath' + filename...)
    currently loads from root folder

    :param param1: the file name to load
    :returns: tuple(list[UMLclass], list[relationships]) 
    """

:param the file name to load
:returns tuple(list[UMLclass], list[relationships]) 
"""
def load(filename):
    # find the file if not we will fail
    try :
        dir_path = os.path.dirname(os.path.realpath(filename))
        os.chdir(dir_path)
        fileExists = True

    #used to print exception 
    except Exception as e:
        print(f"Error: The {filename} does not exist.")
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print('{} {}:{}'.format(exc_type, fname, exc_tb.tb_lineno))
        print(e)
        return (UMLClass.classIndexx(), relationship.Listofrelationships())
    # if not fileExists:    
        # print("File not found")
        # return (UMLClass.classIndexx(), relationship.Listofrelationships())

    
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

        #loops through classes json and decodes each piece creating new objects then adds them to a dictionary
        for eachClass in classes:
            className = str(eachClass['name'])
            attributesList = eachClass['attributes']

            className = u.UMLClass(className)
            for eachAttribute in attributesList:
                className.attributes.append(a.attribute(eachAttribute['name']))

            returnClasses.append(className)
        
        #loops through relationship json and decodes each piece creating new tuples then adds them to a list
        for eachRelation in relations:
            eachRelationTuple = (eachRelation[0], eachRelation[1])
            returnRelations.append(eachRelationTuple)

            #code below is for returning relationship objects 
            """
            #name = (str(eachRelation['source']) + str(eachRelation['destination'])) #I just concat SourceNameDestName to name the relationship object (can change to match how interface does it)  
            #name = relationship(eachRelation['source'], eachRelation['destination'])
            #returnRelations.append(name) 
            """ 

        return (returnClasses, returnRelations)
    
    #if error loading return original lists
    except Exception as e:
        print("Load failed")
        return (u.classIndex, r.relationIndex)
 




#test code for loading classes in dictionary 
"""
onetwo = relationship('one', 'two')
threefour = relationship('three', 'four')
fivesix = relationship('five', 'six')

dict1 = {'class1' : UMLClass("class1"), 'class2' : UMLClass('class2'), 'class3' : UMLClass('class3')}
dict1['class1'].addAttribute('attr1')
dict1['class1'].addAttribute('attr2')
dict1['class1'].addAttribute('attr3')
dict1['class2'].addAttribute('attr1')
dict1['class2'].addAttribute('attr2')
dict1['class2'].addAttribute('attr3')
dict1['class3'].addAttribute('attr1')
dict1['class3'].addAttribute('attr2')
dict1['class3'].addAttribute('attr3')

list1 = [onetwo, threefour, fivesix]

#t1 = load('testfile')
#print(t1)
#json_s = json.dumps(t1, default=vars)
#print(json_s)

