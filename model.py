import relationship as relationships
import saveload as saveload
import UMLClass as UMLClass
import attributes
import os, json
import pandas as pd
#TO-DO need to remove print statments 
class Model():
    def __init__(self):
        self.data=Load_data

    def Load_data(self):
        path_to_json = 'UMLsavefiles/'
        json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
        print(json_files)  # for me this prints ['filename.json']
        return saveload.load(json_files[0])
    def Save(self, classes,relationships, filename):
        oldtime=os.path.getmtime('UMLsaefiles/') 
        #TO-DO need to test if file was created. 
        saveload.save(classes, relationships, filename)
        newtime=os.path.getmtime('UMLsaefiles/') 
        if oldtime == newtime:
            return "Failed to save (new filename)"
        else:
            return "Saved successfully!"
    
    def Add_class(self,classname):
        UMLClass.addClass(className)
        return f"Added {classname} to List of Classes"

    def Remove_class(self,classname):
        UMLClass.deleteClass(className)
        return f'Removed {classname} from List of Classes'

    def Rename_class(self,oldName, newName):
        UMLClass.renameClass(oldName,newName)
        return f'Renamed {oldName} to {newName}'

    def Find_class(self, className):
        if UMLClass.findClass(className)==True:
            return f'Found {className}'
        else:
            return f'Not Found {className}'

    def Add_relationship(self,source,destination):
        relationships.addRelationship(source, destination)
        return "TO-DO"


    def Remove_relationship(self,source,destination):
        relationships.deleteRelationship(source, destination)
        return "TO-DO"

        
    def Get_relationship(self,source, destination):
        relationships.findRelationship(source, destination)
        return "TO-DO"
