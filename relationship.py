#Author Ammanuel Amare
#9/5/22 :)
from UMLClass import *
# This list is used to store the relationships. 
listofrelationships=[]
class relationship:
    # This is the constructor, you will need 3 paramaters to initialize the class
    # Every relationship has a source ,destination, and a type
    def __init__(self,type,source,destination):
        self.type = type
        self.destination = destination
        self.source = source

#@para source is thesource class for relationship 
#@para Destination is the destination class for relationship
#@para tpe is the type of relationship defined between the classes
# returns a string with needed information, can be a boolean value in the future. 
#this is how you will add relationship to class
    def Add_relationship(self,source: str, destination: str, type: str):
        
        status =""
        #findclass returns index of item in golobal list 
        sourceclass = findClass(source)
        destinationclass = findClass(destination)
        #both lists will be needed for testing.
        # this will take the second item of the tuple and convert it into a list 
#        listofdestinationclasses =(list(list(zip(*listofrelationships))[1]))
        
        # this will take the first item of the tuple and convert it into a list 
#        listofsourceclasses =(list(list(zip(*listofrelationships))[0]))

        if sourceclass is not None and destinationclass is not None:
            # Create tuple to later be appened to list of relationships.
            newrelationship = (source, destination,type)
            for item in listofrelationships:
                #if we find the relationship already exists we will log a error
                if item == newrelationship:
                    status = f" Error: Relationship already exists."
                    return status
            listofrelationships.append(newrelationship)
            status =f"Relationship for {source} & {destination} added"
        else:
            status = f" The {source} or {destination} class does not exist."
            return status

    #@para source is thesource class for relationship 
    #@para destination is the destination class for relationship
    #@para tpe is the type of relationship defined between the classes
    def Delete_relationship(self,source: str, destination: str, type: str):
        status =""
        #Here we will need to search the source and destination to confrim they exist 
        sourceclass = findClass(source)
        destinationclass = findClass(destination)

        if sourceclass is not None and destinationclass is not None:
            newrelationship = (source, destination,type)

            for item in listofrelationships:

                if item == newrelationship:
                    # if we find the relationship remove it.
                    listofrelationships.remove(newrelationship)
                    status = "Successfully deleted relationship."
                    return status
        else:
            status = f"The {source} or {destination} does not exist"
            return status
        
    #@para source is thesource class for relationship 
    #@para Destination is the destination class for relationship
    #@para tpe is the type of relationship defined between the classes
    # Edit a relationship, needs to be discussed if we can create on the fly relationships. 
    def Edit_relationship(self,source: str, destination: str, type: str):
        status=""
    # search
        sourceclass = findClass(source)
        destinationclass = findclass(destination)
        #this will be great for debugging we can remove the Exception in prod. 
        if sourceclass is not None and destinationclass is not None:
            try:
                newrelationship = (sourceclass, destinationclass,type)
                listofrelationships.remove(newrelationship)
                Add_relationship(sourceclass, destinationclass, type)
                status = f"Successfully edited relationship {source} & {destination}"

            except Exception as e:
                status = f"Error: The {source} or {destination} does not exist."
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print('{} {}:{}'.format(exc_type, fname, exc_tb.tb_lineno))
                print(e)
                return status
        else:
            status = f"Error: The {source} or {destination} does not exist."
            return status
    #returns the list of all relationships type: list[typle(str,str,str)]
    def Listofrelationships():
        return listofrelationships
