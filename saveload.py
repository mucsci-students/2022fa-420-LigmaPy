
import json
from os.path import exists
import os.path
import UMLClass
import relationship

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


##################################################################


"""
loads filename from specified directory: open('filepath' + filename...)
currently loads from root folder

:param the file name to load
:returns tuple(list[UMLclass], list[relationships]) 
"""
def load(filename):
    
    #check if file exists returns original lists if not
    fileExists = os.path.exists(filename + '.json')
    if not fileExists:    
        print("File not found")
        return (UMLClass.classIndex, relationship.relationIndex)
    
    #creates lists to return
    returnClasses = []
    returnRelations = []
    
    #checks if file is empty and returns empty lists
    if os.stat(filename + ".json").st_size == 0:
        return(returnClasses, returnRelations)    
    
    try:
    #opens the file and save contents as a json string
        with open(filename + ".json", "r") as openfile: 
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
        return (UMLClass.classIndex, relationship.relationIndex)

    

##################################################################