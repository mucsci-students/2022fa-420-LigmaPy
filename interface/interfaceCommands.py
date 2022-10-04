"""
    Author(s): Trevor Bender, Christian Shepperson
    Filename: interfaceCommands.py
    Description: Commands to be used with the interface class
"""

# Imports
import os.path
import sys
from prettytable import PrettyTable
# Local Imports
import UMLClass
import relationship
from saveload import save
import UMLException

def listClasses():
    """
        Lists all classes and their contents
    """
    # Check if at least one class exists
    if len(UMLClass.classIndex) > 0:
        print()
        # print each classes name and attributes
        for c in UMLClass.classIndex:
            print("Class: " + c.name)
            print("\tFields:")
            for field in c.fields:
                print(f"\t\t{field}")
            print("\tMethods:")
            for method in c.methods:
                print(f"\t\t{method}")
    else:
        print("\nNo classes have been added")

def listClass(name: str):
    """
        Lists a specified classes contents
        :param name: Name of the class to display contents of
    """
    # Get index of class with name in classIndex list
    index = UMLClass.findClass(name)
    # Check that the class exists and it has at least one attribute
    if index is not None:
        print(f"\n {name}")
        # Loop to print bottom border with
        # length len(name) + len("Attributes") + 2
        for _ in range((len(name) + 13)):
            print("*", end="")
        print()
        print(" Fields:")

        for _ in range((len(name) + 13)):
            print("*", end="")
        print()
        """
            LIST CLASS FIELDS HERE
        """
        for field in UMLClass.classIndex[index].fields:
            print(f"\t{field}")
        print(" Methods:")
        for _ in range((len(name) + 13)):
            print("*", end="")
        print()
        """
            LIST CLASS METHODS HERE
        """
        for method in UMLClass.classIndex[index].methods:
            print(f"\t{method}")
        # Loop through all attributes of the class
        # for attr in UMLClass.classIndex[index].attributes:
        #     print(f" {attr.name}")
    else:
        print(f"\nClass \"{name}\" does not exist")

def listRelationships():
    """
        Lists all existing relationships between classes
    """
    print()
    if len(relationship.relationIndex) > 0:
        # List all relationships in relationIndex
        table = PrettyTable(['Source', 'Destination', 'Type'])
        # Left align the table
        table.align = 'l'
        for relation in relationship.relationIndex:
            # Add relationship to table
            table.add_row([relation.source, relation.destination, relation.type])
        # Display table
        # print(table)
        return table
    else:
        print("No relationships found.")

"""
    help Command handled by cmd Module.
"""

def exit():
    """
        Exits the application
    """
    print(f"\nExiting...")
    sys.exit()
    # Get input from user if they want to save
    # exitChoice = input("Save progress? (Y/n) ")
    # if exitChoice.lower() == 'y' or exitChoice == '':
    #     file = input("type file to save to: ")
    #     save(classIndex, relationIndex, file)
    #     print(os.path.realpath(file+".json"))
    #     sys.exit()
    # elif exitChoice.lower() == 'n':
    #     print("Exiting")
    #     sys.exit()
    # else:
    #     print(UMLException.UMLException("Invalid option"))