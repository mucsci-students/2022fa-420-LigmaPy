#Author Ammanuel Amare
#9/5/22 :)
from UMLClass import *
# This list is used to store the relationships. 
relationIndex=[]
class relationship:
    # This is the constructor, you will need 3 paramaters to initialize the class
    # Every relationship has a source and destination
    def __init__(self,source,destination):
        self.destination = destination
        self.source = source

#@para source is thesource class for relationship 
#@para Destination is the destination class for relationship
# returns a string with needed information, can be a boolean value in the future. 
#  this is how you will add relationship to class
def addRelationship(source: str, destination: str):
    
    status =""
    #findclass returns index of item in golobal list 
    sourceClass = findClass(source)
    destinationClass = findClass(destination)

    if sourceClass is not None and destinationClass is not None:
        # Create tuple to later be appened to list of relationships.
        newRelationship = (source, destination)
        for item in relationIndex:
            #if we find the relationship already exists we will log a error
            if item == newRelationship:
                status = f" Error: Relationship already exists."
                return status
        relationIndex.append(newRelationship)
        status =f"Relationship for {source} & {destination} added"
        return status
    else:
        status = f" The {source} or {destination} class does not exist."
        return status

# @para source is thesource class for relationship 
# @para destination is the destination class for relationship
# @para tpe is the type of relationship defined between the classes
def deleteRelationship(source: str, destination: str):
    status =""
    # Here we will need to search the source and destination to confrim they exist 
    sourceClass = findClass(source)
    destinationClass = findClass(destination)

    if sourceClass is not None and destinationClass is not None:
        newRelationship = (source, destination)

        for item in relationIndex:

            if item == newRelationship:
                # if we find the relationship remove it.
                relationIndex.remove(newRelationship)
                status = "Successfully deleted relationship."
                return status
    else:
        status = f"The {source} or {destination} does not exist"
        return status
    
# @para source is thesource class for relationship 
# @para Destination is the destination class for relationship
# @para tpe is the type of relationship defined between the classes
# Edit a relationship, needs to be discussed if we can create on the fly relationships. 
def editRelationship(source: str, destination: str):
    status=""
# search
    sourceClass = findClass(source)
    destinationClass = findClass(destination)
    #this will be great for debugging we can remove the Exception in prod. 
    if sourceClass is not None and destinationClass is not None:
        try:
            newRelationship = (sourceClass, destinationClass)
            relationIndex.remove(newRelationship)
            addRelationship(sourceClass, destinationClass)
            status = f"Successfully edited relationship {source} & {destination}"

        except Exception as e:
            status = f"Error: The {source} or {destination} does not exist."
            # exc_type, exc_obj, exc_tb = sys.exc_info()
            # fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            # print('{} {}:{}'.format(exc_type, fname, exc_tb.tb_lineno))
            # print(e)
            return status
    else:
        status = f"Error: The {source} or {destination} does not exist."
        return status
