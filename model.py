import relationship as relationships
import saveload as saveload
import UMLClass as UMLClass
import attributes
import os, json
import pandas as pd
#TO-DO need to remove print statments 
class Model():
    def __init__(self):
        self.data=[]

    def Load_data(self, file):
        save= saveload.load(filename=file)
        classes=save[0]
        relationships=save[1]
        cleanclasses=[]
        cleanrel=[]
        for items in classes:
            cleanclasses.append(items.name)
        for items in relationships:
            cleanrel.append(items.__repr__())
            
        returnstring=(cleanclasses.__str__(),cleanrel.__str__())
        return returnstring
        # if no filename is given we can find the most recent file and load it 
        # try:
        #     path_to_json = 'UMLsavefiles/'
        #     json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
        #     print(json_files)  # this is the most recent json file in the directory
        #     return saveload.load(json_files[0].strip('.json'))
        # except ValueError: 
        #     return "No Recent Save Files Found"
        
    
    def Save_data(self, file):
        saveload.save(classes=UMLClass.classIndex,relations=relationships.relationIndex,filename=file)
        return "Saved Data"
        # oldtime=os.path.getmtime('UMLsaefiles/') 
        # #TO-DO need to test if file was created. 
        # saveload.save(UMLClass.classIndex, relationships.relationIndex, filename)
        # newtime=os.path.getmtime('UMLsaefiles/') 
        # if oldtime == newtime:
        #     return "Failed to save (new filename)"
        # else:
        #     return "Saved successfully!"
    
    def Add_class(self,classname):
        UMLClass.addClass(classname)
        return f"Added {classname} to List of Classes"

    def Remove_class(self,classname):
        UMLClass.deleteClass(classname)
        return f'Removed {classname} from List of Classes'

    def Rename_class(self,oldName, newName):
        UMLClass.renameClass(oldName,newName)
        return f'Renamed {oldName} to {newName}'

    def Find_class(self, className):
        if UMLClass.findClass(className)!=None:
            return f'Found {className}'
        elif UMLClass.findClass(className)==None:
            return f' {className} Not Found'

    def Add_relationship(self,source,destination,reltype):
        relationships.addRelationship(source, destination, reltype)
        return "f'Relationship created between {source} and {destination}'"


    def Remove_relationship(self,source,destination):
        relationships.deleteRelationship(source, destination)
        return "f'Deleted relationship between {source} and {destination}'"

        
    def Get_relationship(self,source, destination):
        relationships.findRelationship(source, destination)
        return f'Relationship found between {source} and {destination}'

    def List_relationships(self):
        return relationships.relationIndex

    def List_classes(self):
        return UMLClass.classIndex
    
    