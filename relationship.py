#Author Ammanuel Amare
#9/1/22
# we will need to inherit from the class module/class 
# from classes import classmodel 

class relationship:
    def __init__(self,type,source,destination):
        self.type = type
        self.destination = destination
        self.source = source
        self.listofrelationships = []


def Add_relationship(source: str, destination: str, type: str):
    status =""
# currently waiting for the ability to search for a class given name 
    sourceclass = source
    destinationclass = destination
    if sourceclass is not None and destinationclass is not None:
        #listofrelationships is just a placeholder for the list of class relationships
        for item in sourceclass.listofrelationships:
            if item.destination == destinationclass.name:
                status = f" Error: Relationship already exists."
                return status
        updated_class = sourceclass.listofrelationships.append(updated_relationship)
        status =f"Relationship for {source} & {destination} added"
    else:
        status = f" The {source} or {destination} class does not exist."
        return status

def Delete_relationship(source: str, destination: str, type: str):
    status =""
    res = None
    #again we need a way to search based on class name this will not work 
    sourceclass = source
    destinationclass = destination 
    if sourceclass is not None and destinationclass is not None:
        for item in sourceclass.listofrelationships:
            if item.destination == destination:
                
                updated_class = sourceclass.listofrelationships.remove(item)
                status = "Successfully deleted relationship."
                return status
    else:
        status = f"The {source} or {destination} does not exist"
        return status
    

def Edit_relationship(source: str, destination: str, type: str):
    status=""
# gotta do the search here too 
    sourceclass = source
    destinationclass = destination
    if sourceclass is not None and destinationclass is not None:
        for item in sourceclass.listofrelationships:
            if item.destination == destination:
                #to-do add logic for checking duplicate items
                Add_relationship(source, destination, item.type, type)
                status = f"Successfully edited relationship {source} & {destination}"
                return status
        status = f"Error: Relationship does not exist."
        return status
    else:
        status = f"Error: The {source} or {destination} does not exist."
        return status