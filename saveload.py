
import json
from os.path import exists
import os.path
import UMLClass as u
import relationship as r
import attribute as a
    

##################################################################

"""
saves file as filename in specified directory: open('filepath' + filename...)
currently saves in root folder

:param param1: UMLclass list 
:param param2: relationship list 
:param param3: filename specified by user
:returns: nothing
"""
def save(classes, relations, filename):
    
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


"""
loads filename from specified directory: open('filepath' + filename...)
currently loads from root folder

:param param1: the file name to load
:returns: tuple(list[UMLclass], list[relationships]) 
"""
def load(filename):
    
    #check if file exists returns original lists if not
    fileExists = os.path.exists("UMLsavefiles/" + filename + '.json')
    if not fileExists:    
        print("File not found")
        return (u.classIndex, r.listofrelationships)
    
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
        return (u.classIndex, r.listofrelationships)
 

##################################################################


#test code for storing classes in list
"""
onetwo = ('one', 'two')
threefour = ('three', 'four')
fivesix = ('five', 'six')

r = [onetwo, threefour]
listRelationships = [onetwo, threefour, fivesix]

class1 = u.UMLClass("class1")
class2 = u.UMLClass('class2') 
class3 = u.UMLClass('class3')

class attribute:
    def __init__ (self, name):
        self.name = name

a1 = attribute('attr1')
a2 = attribute('attr2')
a3 = attribute('attr3')

class1.attributes.append(a1)
class1.attributes.append(a2)
class1.attributes.append(a3)
class2.attributes.append(a1)
class2.attributes.append(a2)
class2.attributes.append(a3)
class3.attributes.append(a1)
class3.attributes.append(a2)
class3.attributes.append(a3)

c = [class1, class2]
listClass = [class1, class2, class3]


listClass = [class1, class2, class3]

onetwo = ('one', 'two')
threefour = ('three', 'four')
fivesix = ('five', 'six')

r = [onetwo, threefour]

listRelationships = [onetwo, threefour, fivesix]

#save(listClass, listRelationships, 'testfile')

tuple1 = load('testfile')

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
print(listOfClasses[0].attributes)
for each in listOfClasses[0].attributes:
    print(each.name)
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