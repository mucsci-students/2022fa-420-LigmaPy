"""
    Author(s): Trevor Bender, Christian Shepperson
    Filename: interfaceCommands.py
    Description: Commands to be used with the interface class
"""

# Imports
import os.path
import sys
import json
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
            print(c.name + ":")
            for attr in c.attributes:
                print(f"\t{attr.name}")
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
    if index is not None and len(UMLClass.classIndex[index].attributes) > 0:
        print(f"\n {name} Attributes")
        # Loop to print bottom border with
        # length len(name) + len("Attributes") + 2
        for i in range((len(name) + 13)):
            print("*", end="")
        print()
        # Loop through all attributes of the class
        for attr in UMLClass.classIndex[index].attributes:
            print(f" {attr.name}")
    else:
        print(f"\nClass \"{name}\" has no attributes")

def listRelationships():
    """
        Lists all existing relationships between classes
    """
    print()
    if len(relationship.relationIndex) > 0:
        # List all relationships in relationIndex
        table = PrettyTable(['Source', 'Destination'])
        # Left align the table
        table.align = 'l'
        for relation in relationship.relationIndex:
            # Add relationship to table
            table.add_row([relation.source, relation.destination])
        # Display table
        print(table)
    else:
        print("No relationships found.")

def help(cmd=None):
    """
        Lists how to use the application without leaving
        :param cmd: Name of the command to show usage of. Default is None
    """
    data = open('interface/commands.json')
    cmds = json.load(data)
    # Default help command - prints list of commands
    #   and their descriptions.
    if(cmd is None):
        print('{:<20}{:<12}'.format('Command', 'Description'))
        print("***************************************************************************************")
        for i in cmds['commands']:
            newLine = '{:<20}{:<12}'.format(i['name'], i['desc'])
            print(newLine)
        print("***************************************************************************************")
    else:
        command = None
        # Loops through list off commands and checks if the
        #   input matches one of the existing commands.
        # If there is no match, print message stating so.
        for name in cmds["commands"]:
            if cmd == name["name"]:
                command = name
                break
        # Prints the usage and description of the specified command.
        if command is not None:
            # Displays the syntax of the command
            print("Usage: " + cmd, end="")
            for option in command["args"]:
                print(f" [{option['name']}]", end="")
            print(f"\n\n\t{command['desc']}\n")
            # Displays the arguments and their descriptions
            for option in command["args"]:
                print('{:<12}{:<12}'.format(option['name'], option['desc']))
        else:
 #           print(f"Command not found: {cmd}\nType 'help' for a list of commands.")
            print(UMLException.UMLException("Command not found", f"{cmd}"))

def exit(classIndex, relationIndex):
    """
        Exits the application
    """

    # Check if there was a file loaded or previously saved, then check for modifications

    # Get input from user if they want to save
    exitChoice = input("Save progress? (Y/n) ")
    if exitChoice.lower() == 'y' or exitChoice == '':
        file = input("type file to save to: ")
        save(classIndex, relationIndex, file)
        print(os.path.realpath(file+".json"))
        sys.exit()
    elif exitChoice.lower() == 'n':
        print("Exiting")
        sys.exit()
    else:
        print(UMLException.UMLException("Invalid option"))
#        print("Invalid OPTION")