
import json
from os.path import exists
import os.path
from UMLClass import *
from relationship import *
from pathlib import Path

##################################################################

"""
saves file as filename in specified directory: open('filepath' + filename...)
currently saves in root folder

:param param1 UMLclass list 
:param param2 relationship list 
:param param3 filename specified by user
:returns nothing
"""
def save(classes, relations, filename):
    
    #combines both into a tuple
    t = (classes, relations)
    
    #encodes tuple above to json
    jsonString = json.dumps(t, default=vars)
    
    #saves json string to file
    with open(filename + ".json", "w") as outfile:
        outfile.write(jsonString)
        print("File Saved.")

# maybe return filename or flag?

##################################################################


"""
loads filename from specified directory: open('filepath' + filename...)
currently loads from root folder

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
    if os.stat(filename).st_size == 0:
        return(returnClasses, returnRelations)    
    
    try:
    #opens the file and save contents as a json string
        with open(filename, "r") as openfile: 
            jsonObject = json.load(openfile)
        
        #divides the json string into classes/relations
        classes = jsonObject[0]
        relations = jsonObject[1]

        #loops through classes json and decodes each piece creating new objects then adds them to a dictionary
        for eachClass in classes:
            className = str(eachClass['name'])
            attributesList = eachClass['attributes']
            className = UMLClass(className)
            for eachAttribute in attributesList:
                className.attributes.append(str(eachAttribute))
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
        return (UMLClass.classIndex, relationship.listofrelationships)

    

##################################################################


#test code for storing classes in list

"""
onetwo = ('one', 'two')
threefour = ('three', 'four')
fivesix = ('five', 'six')

r = [onetwo, threefour]
listRelationships = [onetwo, threefour, fivesix]

class1 = UMLClass.UMLClass("class1")
class2 = UMLClass.UMLClass('class2') 
class3 = UMLClass.UMLClass('class3')
class1.attributes.append('attr1')
class1.attributes.append('attr2')
class1.attributes.append('attr3')
class2.attributes.append('attr1')
class2.attributes.append('attr2')
class2.attributes.append('attr3')
class3.attributes.append('attr1')
class3.attributes.append('attr2')
class3.attributes.append('attr3')

c = [class1, class2]
listClass = [class1, class2, class3]


listClass = [class1, class2, class3]

onetwo = ('one', 'two')
threefour = ('three', 'four')
fivesix = ('five', 'six')

r = [onetwo, threefour]

listRelationships = [onetwo, threefour, fivesix]

save(listClass, listRelationships, 'testfile')

tuple1 = load('tesftfile')

print()
print("objects are of type:")
print(tuple1) 
print()
json_s = json.dumps(tuple1, default=vars)
print("converted back to json to show it is equivalent to testfile:")
print(json_s + "\n")
listOfClasses = tuple1[0]
listOfRelations = tuple1[1]
print("Print .getName() to show objects act like objects")
print(listOfClasses[0].name)
print(type(listOfClasses[0]))
print(type(listOfRelations[1]))
"""

##################################################################


#dictionary load method
"""
loads filename from file 
:param the file name to load
:returns tuple(dict{classes}, list[relationships])     
"""
"""
def load(filename):
    #opens the file and save contents as a json string
    with open(filename + ".json", "r") as openfile: 
        jsonObject = json.load(openfile)
    #divides the json string into classes/relations
    classes = jsonObject[0]
    relations = jsonObject[1]
    returnClasses = {}
    returnRelations = []
    #loops through classes json and decodes each peice creating new objects then adds them to a dictionary
    for eachClass in classes:
        className = str(eachClass)
        attributesList = (classes[className]['attributes'])
        eachClass = UMLClass(classes[className]['name'])
        for attr in attributesList:
            eachClass.addAttribute(str(attr)) #method name addAttribue will have to match whatever the attibute file uses to add attributes
        returnClasses[className] = eachClass
    #loops through relationship json and decodes each peice creating new objects then adds them to a list
    for eachRelation in relations:
        name = (str(eachRelation['source']) + str(eachRelation['destination'])) #I just concat SourceNameDestName to name the relationship object (can change to match how interface does it)  
        name = relationship(eachRelation['source'], eachRelation['destination'])
        returnRelations.append(name) 
    return (returnClasses, returnRelations)
"""


##################################################################


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
"""
