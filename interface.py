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
import relationship
from interface.interfaceCommands import *
from saveload import *


_intro_text = """\
{}
Type `help` for an overview `help <command>` for more details.
Type `exit` to quit.
"""

class Interface(cmd.Cmd):
    intro = _intro_text.format(pyfiglet.figlet_format("UML Editor"))
    prompt = ">> "

    """
        Commmand listeners
    """
    # Creates a uniquely named class
    def do_addClass(self, arg):
        """Usage: addClass <name>
        
        Creates and adds a new class with name <name>.
        """
        UMLClass.addClass(arg)
    # Removes a class
    def do_deleteClass(self, arg):
        """Usage: deleteClass <name>
        
        Deletes a class by it's <name>.
        """
        UMLClass.deleteClass(arg)
    # Changes the name of a class
    def do_renameClass(self, arg):
        """Usage: renameClass <name> <newName>

        Renames a class from <name> to <newName>.
        """
        names = arg.split()
        if len(names) == 2:
            UMLClass.renameClass(names[0], names[1])
        else:
            print(f"Argument error")
    # Creates a relationship between two classes
    def do_addRelationship(self, arg):
        """Usage addRelationship <source> <destination>
        
        Creates a relationship between the <source> and <destination> classes.
        """
        classes = arg.split()
        if len(classes) == 2:
            relationship.addRelationship(classes[0], classes[1])
        else:
            print(f"Argument error")
    # Deletes an existing relationship between two classes
    def do_deleteRelationship(self, arg):
        """Usage: deleteRelationship <source> <destination>
        
        Removes an existing relationship between the <source> and <destination> classes.
        """
        classes = arg.split()
        if len(classes) == 2:
            relationship.deleteRelationship(classes[0], classes[1])
        else:
            print(f"Argument error")
    # Creates an attribute for the specified class
    def do_addAttribute(self, arg):
        """Usage: addAttribute <name> <class>
        
        Creates a new attribute named <name> in <class>.
        """
        args = arg.split()
        if len(args) == 2:
            attributes.addAttribute(args[0], args[1])
        else:
            print(f"Argument error")
    # Removes attribute from specified class
    def do_deleteAttribute(self, arg):
        """Usage: deleteAttribute <name> <class>
        
        Removes the <name> attribute from <class>.
        """
        args = arg.split()
        if len(args) == 2:
            attributes.deleteAttribute(args[0], args[1])
        else:
            print(f"Argument error")
    # Renames an attribute
    def do_renameAttribute(self, arg):
        """Usage: renameAttribute <name> <newName> <class>
        
        Renames the <name> attribute in <class> to <newName>.
        """
        args = arg.split()
        if len(args) == 3:
            attributes.renameAttribute(args[0], args[1], args[2])
        else:
            print(f"Argument error")
    # Stores the current state to a JSON file
    def do_save(self, arg):
        """Usage: save <filename>
        
        Saves the current program state to <filename>.json.
        """
        save(UMLClass.classIndex, relationship.relationIndex, arg)
    # Load a previous state from a JSON file
    def do_load(self, arg):
        """Usage: load <filename>
        
        Loads a previously saved state from <filename>.json.
        """
        UMLClass.classIndex, relationship.relationIndex = load(arg)
    # List all classes and their contents
    def do_listClasses(self, arg):
        """Usage: listClasses
        
        Lists all existing classes and their contents.
        """
        listClasses()
    # Lists the contents of a specified class
    def do_listClass(self, arg):
        """Usage: listClass <name>
        
        Lists the contents of class <name>.
        """
        listClass(arg)
    # Lists all existing relationships
    def do_listRelationships(self, arg):
        """Usage: listRelationships
        
        Lists all existing relationships between classes.
        """
        listRelationships()
    # Exits the program
    def do_exit(self, arg):
        """Usage: exit
        
        Exits the program.
        """
        exit(UMLClass.classIndex, relationship.relationIndex)
    # Overrides the emptyline method to avoid repetition of previous command
    def emptyline(self):
        pass

def main():
    Interface().cmdloop()

if __name__=="__main__":
    main()
