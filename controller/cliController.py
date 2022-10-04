"""
    Author(s): Trevor Bender, Christian Shepperson
    Filename: cliInterface.py
    Description: Basic CLI interface and commands to go along with it.
"""

import pyfiglet
import cmd
# Local Imports
import UMLClass
import attributes
import relationship
import parameter
import UMLException
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
        """Usage: renameClass <name> <new_name>

        Renames a class from <name> to <new_name>.
        """
        names = arg.split()
        if len(names) == 2:
            UMLClass.renameClass(names[0], names[1])
        else:
            print(f"Argument error")
    # Creates a relationship between two classes
    def do_addRelationship(self, arg):
        """Usage addRelationship <source> <destination> <type>
        
        Creates a relationship of <type> between the <source> and <destination> classes.
        """
        classes = arg.split()
        if len(classes) == 3:
            relationship.addRelationship(classes[0], classes[1], classes[2])
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

    def do_changeRelType(self, arg):
        """Usage: changeRelType
        
        """
        pass

    # Creates a new method for the specified class
    def do_addMethod(self, arg):
        """Usage: addMethod <class> <name> <return_type> [-p <name>:<type>...]
        
        Adds the method <name> with <return_type> to <class>
        """
        args = arg.split()
        if len(args) == 3:
            attributes.addMethod(args[1], args[0], args[2])
        elif len(args) > 4:
            if args[3] != "-p":
                return
            # parse the parameter lists into a list of tuples
            paramList = []
            for param in args[4:]:
                paramName, paramType = param.split(":")
                paramList.append((paramName, paramType))

            attributes.addMethod(args[1], args[0], args[2])
            parameter.addParameter(paramList, args[1], args[0])

    # Removes the method from the specified class
    def do_deleteMethod(self, arg):
        """Usage: deleteMethod <class> <method>

        Removes <method> from <class>
        """
        args = arg.split()
        if len(args) == 2:
            attributes.deleteMethod(args[1], args[0])
        else:
            print(f"Wrong")
    # Renames the specified method in the specified class
    def do_renameMethod(self, arg):
        """Usage: renameMethod <class> <old_name> <new_name>
        
        Changes the name of a method from <old_name> to <new_name> in <class>
        """
        args = arg.split()
        if len(args) == 3:
            ret = attributes.renameMethod(args[1], args[2], args[0])
        else:
            print(UMLException("Argument error", "BLAH"))

    def do_addField(self, arg):
        """Usage: addField <class> <name> <type>
        
        Adds the field <name> with <type> to <class>
        """
        args = arg.split()

        if len(args) == 3:
            ret = attributes.addField(args[1], args[0], args[2])

            if ret == -1:
                print(UMLException("Class error", f"{args[0]} does not exist"))
            elif ret == -2:
                print(UMLException("Field error", f"{args[1]} already exists"))
        else:
            print("Incorrect amount of arguments")

    def do_deleteField(self, arg):
        """Usage: deleteField <class> <field>
        
        Removes the <field> from <class>
        """
        args = arg.split()
        if len(args) == 2:
            ret = attributes.deleteField(args[1], args[0])
            if ret == -1:
                print(UMLException("Class error", f"{args[0]} does not exist"))
            elif ret == -2:
                print(UMLException("Field error", f"{args[1]} does not exist"))
        else:
            print("ARGUMENT ERROR")

    def do_renameField(self, arg):
        """Usage: renameField <class> <old_name> <new_name>

        Updates the name of a field from <old_name> to <new_name>
        """
        args = arg.split()
        if len(args) == 3:
            ret = attributes.renameField(args[1], args[2], args[0])
        else:
            print(UMLException("Argument error", f"expected 3, given {len(args)}"))

    def do_addParam(self, arg):
        """Usage: addParam <class> <method> <name>:<type>...
        
        Adds a list of parameters to <method> in <class>
        """
        args = arg.split()
        if len(args) > 2:
            paramList = []
            for param in args[4:]:
                paramName, paramType = param.split(":")
                paramList.append((paramName, paramType))

            ret = parameter.addParameter(paramList, args[1], args[0])
        else:
            print(UMLException("Argument error", f"not enough args"))

    def do_deleteParam(self, arg):
        """Usage: deleteParam <class> <method> [-a] [<name>...]
        
        Removes parameter(s) from <method>
        """
        args = arg.split()
        if len(args) == 3:
            if args[2] == "-a":
                parameter.deleteAllParameter(args[1], args[0])
            else:
                parameter.deleteParameter(args[2:], args[1], args[0])
        else:
            print()

    def do_changeParam(self, arg):
        """Usage: changeParam <class> <method> -o <old_name>... -n <new_name>:<new_type>
        
        Changes the list of parameters from <old_list> to <new_list> in <method>
        """
        args = arg.split()

        print(f"Waiting to be implemented")

        # parameter.changeParameter(args[3:], args[0], args[1], args[0])
        # parameter.changeParam(args[0], args[1], args[3:], args[0])
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
        load(arg)
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
        print(listRelationships())
    # Exits the program
    def do_exit(self, arg):
        """Usage: exit
        
        Exits the program.
        """
        exit(UMLClass.classIndex, relationship.relationIndex)
    # Overrides the emptyline method to avoid repetition of previous command
    def emptyline(self):
        pass