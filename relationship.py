"""
Author: Ammanuel Amare
Filename: relationship.py
Description: Adds, deletes, & edits relationships between classes
"""

from UMLClass import *

# This list is used to store the relationships
relationIndex = []


class relationship:
    """
    This is the constructor, you will need 3 paramaters to initialize the class
    Every relationship has a source and destination
    """
    def __init__(self, source, destination):
        self.destination = destination
        self.source = source


def addRelationship(source: str, destination: str):
    """
    Adds a relationship to a class

    :param source: the source class for relationship
    :param destination: the destination class for relationship
    :return: a string with needed information, can be a boolean value in the future
    """

    status = ""
    # findclass returns index of item in golobal list
    sourceClass = findClass(source)
    destinationClass = findClass(destination)

    if sourceClass is not None and destinationClass is not None:
        # Create tuple to later be appened to list of relationships
        newRelationship = (source, destination)
        for item in relationIndex:
            # if we find the relationship already exists we will log a error
            if item == newRelationship:
                status = f" Error: Relationship already exists."
                return status
        relationIndex.append(newRelationship)
        status = f"Relationship for {source} & {destination} added"
        return status
    else:
        status = f" The {source} or {destination} class does not exist."
        return status


def deleteRelationship(source: str, destination: str):
    """
    Deletes a relationship

    :param source: the source class for relationship
    :param destination: the destination class for relationship
    :return: A string containing the outcome of the function
    """

    status = ""
    # Here we will need to search the source and destination to confrim they exist
    sourceClass = findClass(source)
    destinationClass = findClass(destination)

    if sourceClass is not None and destinationClass is not None:
        newRelationship = (source, destination)

        for item in relationIndex:

            if item == newRelationship:
                # if we find the relationship remove it
                relationIndex.remove(newRelationship)
                status = "Successfully deleted relationship."
                return status
    else:
        status = f"The {source} or {destination} does not exist"
        return status


def editRelationship(source: str, destination: str):
    """
    Edits a relationship, needs to be discussed if we can create on the fly relationships

    :param source: the source class for relationship
    :param destination: the destination class for relationship
    :returns: A string containing the outcome of the function
    """

    status = ""
    # search
    sourceClass = findClass(source)
    destinationClass = findClass(destination)
    # this will be great for debugging we can remove the Exception in prod
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
