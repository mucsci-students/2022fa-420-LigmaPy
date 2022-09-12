"""
    Author(s): Trevor Bender, Christian Shepperson
    Filename: interface.py
    Description: Basic CLI interface and commands to go along with it.
"""


import pyfiglet
import cmd
# Local Imports
import UMLClass
import attributes
# from attributes import addAttribute, deleteAttribute, renameAttribute
import relationship
from interface.interfaceCommands import *
from saveload import *

class Interface(cmd.Cmd):
    # Welcome message
    intro = pyfiglet.figlet_format("UML Editor")
    prompt = ">> "
    # Creates a uniquely named class
    def do_addClass(self, arg):
        UMLClass.addClass(arg)
    # Removes a class
    def do_deleteClass(self, arg):
        UMLClass.deleteClass(arg)
    # Changes the name of a class
    def do_renameClass(self, arg):
        names = arg.split()
        if len(names) == 2:
            UMLClass.renameClass(names[0], names[1])
        else:
            print(f"Argument error")
    # Creates a relationship between two classes
    def do_addRelationship(self, arg):
        classes = arg.split()
        if len(classes) == 2:
            relationship.addRelationship(classes[0], classes[1])
        else:
            print(f"Argument error")
    # Deletes an existing relationship between two classes
    def do_deleteRelationship(self, arg):
        classes = arg.split()
        if len(classes) == 2:
            relationship.deleteRelationship(classes[0], classes[1])
        else:
            print(f"Argument error")
    # Creates an attribute for the specified class
    def do_addAttribute(self, arg):
        args = arg.split()
        if len(args) == 2:
            attributes.addAttribute(args[0], args[1])
        else:
            print(f"Argument error")
    # Removes attribute from specified class
    def do_deleteAttribute(self, arg):
        args = arg.split()
        if len(args) == 2:
            attributes.deleteAttribute(args[0], args[1])
        else:
            print(f"Argument error")
    # Renames an attribute
    def do_renameAttribute(self, arg):
        args = arg.split()
        if len(args) == 3:
            attributes.renameAttribute(args[0], args[1], args[2])
        else:
            print(f"Argument error")
    # Stores the current state to a JSON file
    def do_save(self, arg):
        save(UMLClass.classIndex, relationship.listofrelationships, arg)
    # Load a previous state from a JSON file
    def do_load(self, arg):
        UMLClass.classIndex, relationship.listofrelationships = load(arg)
    # List all classes and their contents
    def do_listClasses(self, arg):
        listClasses()
    # Lists the contents of a specified class
    def do_listClass(self, arg):
        listClass(arg)
    # Lists all existing relationships
    def do_listRelationships(self, arg):
        listRelationships()
    # Prints a help message
    def do_help(self, arg):
        if len(arg) == 0:
            help()
        elif len(arg) == 1:
            help(arg)
        else:
            print(f"Argument error")
    # Exits the program
    def do_exit(self, arg):
        exit(UMLClass.classIndex, relationship.relationIndex)
    # Overrides the emptyline method to avoid repetition of previous command
    def emptyline(self):
        pass

def main():
    Interface().cmdloop()

if __name__=="__main__":
    main()
