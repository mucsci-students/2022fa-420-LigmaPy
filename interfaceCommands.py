"""
    Trevor Bender and Christian Sheperdson

    Commands to be used with the interface class
"""
import json
from UMLClass import classIndex, findClass

def listClasses():
    """
        Lists all classes and their contents
    """
    # Check if at least one class exists
    if len(classIndex) > 0:
        print()
        # print each classes name and attributes
        for c in classIndex:
            print(c.name + ":")
            for attr in c.attributes:
                print("\t" + attr)
    else:
        print("\nNo classes have been added")

def listClass(name: str):
    """
        Lists a specified classes contents
    """
    # Get index of class with name in classIndex list
    index = findClass(name)
    # Check that the class exists and it has at least one attribute
    if index is not None and len(classIndex[index].attributes) > 0:
        print(f"\n {name} Attributes")
        # Loop to print bottom border with 
        # length len(name) + len("Attributes") + 2
        for i in range((len(name) + 13)):
            print("*", end="")
        print()
        # Loop through all attributes of the class
        for attr in classIndex[index].attributes:
            print(attr)
    else:
        print(f"\nClass \"{name}\" has no attributes")

def listRelationships():
    """
        Lists all existing relationships between classes
    """
    # Placeholder
    print("[src 1] -> [dest 1]")
    print("[src 2] -> [dest 2]")
    print("...")
    print("[src n] -> [dest n]")

def help(cmd=None):
    """
        Lists how to use the application without leaving
    """
    data = open('commands.json')
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
            print(f"Command not found: {cmd}\nType 'help' for a list of commands.")

def exit():
    """
        Exits the application
    """
    # Set isRunning to false to stop the loop
    # self.isRunning = False
    # Get input from user if they want to save
    exitChoice = input("Save progress? (Y/n)")
    if exitChoice.lower() == 'y' or exitChoice == '':
        print("SAVE PLACEHOLDER")
    elif exitChoice.lower() == 'n':
        print("Exiting")
    else:
        print("Invalid OPTION")