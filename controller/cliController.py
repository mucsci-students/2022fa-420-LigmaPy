"""
    Author(s): Trevor Bender, Christian Shepperson
    Filename: cliInterface.py
    Description: Basic CLI interface and commands to go along with it.
"""

import pyfiglet
import cmd2
# Local Imports
import UMLClass
import attributes
import relationship
import parameter
from UMLException import UMLException, UMLSuccess
from interface.interfaceCommands import *
from saveload import *


_intro_text = """\
{}
Type `help` for an overview `help <command>` for more details.
Type `exit` to quit.
"""

class Interface(cmd2.Cmd):
    intro = _intro_text.format(pyfiglet.figlet_format("UML Editor"))
    prompt = ">> "

    def __init__(self):
        super().__init__()
        # Remove built-in commands from cmd2.Cmd
        del cmd2.Cmd.do_edit
        del cmd2.Cmd.do_shell
        del cmd2.Cmd.do_set
        del cmd2.Cmd.do_shortcuts
        del cmd2.Cmd.do_run_script
        del cmd2.Cmd.do_run_pyscript
        del cmd2.Cmd.do_alias
        del cmd2.Cmd.do_macro
        del cmd2.Cmd.do_quit

    """
        Commmand listeners
    """

    """ CLASS COMMANDS """

    """
        Add Class
    """
    addClassParser = cmd2.Cmd2ArgumentParser(description="Adds a new class")
    addClassParser.add_argument('class_name', help="Name for the new class")
    @cmd2.with_argparser(addClassParser)
    @cmd2.with_category("Class")
    # Creates a uniquely named class
    def do_addClass(self, arg):
        
        print("\033[97m Color testing \033[00m")
        UMLClass.addClass(arg.class_name)
    
    """
        Delete Class
    """
    deleteClassParser = cmd2.Cmd2ArgumentParser(description="Removes a class and all of its contents")
    deleteClassParser.add_argument('class_name', help="Name of the class to be deleted")
    @cmd2.with_argparser(deleteClassParser)
    @cmd2.with_category("Class")
    # Removes a class
    def do_deleteClass(self, arg):

        UMLClass.deleteClass(arg)
    
    """ 
        Rename Class
    """
    renameClassParser = cmd2.Cmd2ArgumentParser(description="Changes the name of an existing class")
    renameClassParser.add_argument('class_name', help="Name of the class to update")
    renameClassParser.add_argument('new_name', help="Name to change the class to")
    @cmd2.with_argparser(renameClassParser)
    @cmd2.with_category("Class")
    # Changes the name of a class
    def do_renameClass(self, arg):

        names = arg.split()
        if len(names) == 2:
            UMLClass.renameClass(names[0], names[1])
        else:
            print(f"Argument error")

    """ RELATIONSHIP COMMANDS """

    # List of Relationship types
    relationTypes = ['aggregation', 'composition', 'inheritance', 'realization']

    """
        Add Relationship
    """
    addRelationParser = cmd2.Cmd2ArgumentParser(description="Adds a relationship between two existing classes")
    addRelationParser.add_argument('src', help="Name of the source class")
    addRelationParser.add_argument('dest', help="Name of the destination class")
    addRelationParser.add_argument('type', help="Type of relationship between the source and destination classes", choices=relationTypes)
    @cmd2.with_argparser(addRelationParser)
    @cmd2.with_category("Relationship")
    # Creates a relationship between two classes
    def do_addRelationship(self, arg):

        classes = arg.split()
        if len(classes) == 3:
            relationship.addRelationship(classes[0], classes[1], classes[2])
        else:
            print(f"Argument error")

    """
        Delete Relationship
    """
    deleteRelationParser = cmd2.Cmd2ArgumentParser(description="Removes an existing relationship between two classes")
    deleteRelationParser.add_argument('src', help="Name of the source class")
    deleteRelationParser.add_argument('dest', help="Name of the destination class")
    @cmd2.with_category("Relationship")
    # Deletes an existing relationship between two classes
    def do_deleteRelationship(self, arg):

        classes = arg.split()
        if len(classes) == 2:
            relationship.deleteRelationship(classes[0], classes[1])
        else:
            print(f"Argument error")

    """
        Change Relationship Type
    """
    changeRelTypeParser = cmd2.Cmd2ArgumentParser(description="Change the type of an existing relationship")
    changeRelTypeParser.add_argument('src', help="Name of the source class")
    changeRelTypeParser.add_argument('dest', help="Name of the destination class")
    changeRelTypeParser.add_argument('new_type', help="New type for the relationship", choices=relationTypes)
    @cmd2.with_argparser(changeRelTypeParser)
    @cmd2.with_category("Relationship")
    def do_changeRelType(self, arg):

        args = arg.split()
        if len(args) == 3:
            relIndex = relationship.findRelationship(args[0], args[1])
            relationship.relationIndex[relIndex].editType(args[2])
        else:
            print("wrong number of arguments")

    """ METHOD COMMANDS """

    """
        Add Method
    """
    # Argument Parser for addMethod
    addMethodParser = cmd2.Cmd2ArgumentParser(description="Adds a method to the specified class")
    addMethodParser.add_argument('class_name', help="Name of target class")
    addMethodParser.add_argument('method_name', help="Name of method to be added")
    addMethodParser.add_argument('ret_type', help="Return type of the new method")
    addMethodParser.add_argument('-p', nargs='+', help="List of parameters to add in the format <name>:<type>")
    @cmd2.with_category("Method")
    @cmd2.with_argparser(addMethodParser)
    # Creates a new method for the specified class
    def do_addMethod(self, arg):
        # Added the method with return type to the class
        attributes.addMethod(arg.method_name, arg.class_name, arg.ret_type)
        # Check if optional arg 'p' was entered
        if arg.p != None:
            # Create a list of tuples containing (paramName, paramType)
            paramList = []
            for param in arg.p:
                paramName, paramType = param.split(":")
                paramList.append((paramName, paramType))
            # Add parameter list to the newly created method            
            parameter.addParameter(paramList, arg.method_name, arg.class_name)

    """
        Delete Method
    """
    deleteMethodParser = cmd2.Cmd2ArgumentParser(description="Removes an existing method from an existing class")
    deleteMethodParser.add_argument('class_name', help="Class containing the method to be removed")
    deleteMethodParser.add_argument('method_name', help="Name of the method to be removed")
    @cmd2.with_argparser(deleteMethodParser)
    @cmd2.with_category("Method")
    # Removes the method from the specified class
    def do_deleteMethod(self, arg):
        # Remove method from class
        attributes.deleteMethod(arg.method_name, arg.class_name)



        # args = arg.split()
        # if len(args) == 2:
        #     ret = attributes.deleteMethod(args[1], args[0])
        #     if ret == 1:
        #         print(UMLSuccess(f"Removed {args[1]} from {args[0]}"))
        #     elif ret == -1:
        #         print(UMLException("Class error", f"{args[0]} does not exist"))
        #     elif ret == -2:
        #         print(UMLException("Method error", f"{args[1]} does not exist in {args[0]}"))
        # else:
        #     print(f"Wrong")

    """
        Rename Method
    """
    renameMethodParser = cmd2.Cmd2ArgumentParser()
    renameMethodParser.add_argument('class_name', help="Class containing the method to rename")
    renameMethodParser.add_argument('old_name', help="Current name of the method to be renamed")
    renameMethodParser.add_argument('new_name', help="New name for method")
    @cmd2.with_argparser(renameMethodParser)
    @cmd2.with_category("Method")
    # Renames the specified method in the specified class
    def do_renameMethod(self, arg):
        # Update the name of the method in a class
        attributes.renameMethod(arg.old_name, arg.new_name, arg.class_name)

        # args = arg.split()
        # if len(args) == 3:
        #     ret = attributes.renameMethod(args[1], args[2], args[0])
        #     if ret == 1:
        #         print(UMLSuccess(f"Renamed {args[0]} to {args[1]}"))
        #     elif ret == -1:
        #         print(UMLException("Class error", f"{args[2]} does not exist"))
        #     elif ret == -2:
        #         print(UMLException("Method error", f"{args[0]} does not exist in {args[2]}"))
        #     elif ret == -3:
        #         print(UMLException("Method error", f"{args[1]} already exists in {args[2]}"))
        # else:
        #     print(UMLException("Argument error", "BLAH"))

    """ FIELD COMMANDS """

    """
        Add Field
    """
    addFieldParser = cmd2.Cmd2ArgumentParser(description="Adds a new field to an existing class")
    addFieldParser.add_argument('class_name', help="Name of class to add field to")
    addFieldParser.add_argument('field_name', help="Name of field to add")
    addFieldParser.add_argument('type', help="Type of the new field")
    @cmd2.with_argparser(addFieldParser)
    @cmd2.with_category("Field")
    def do_addField(self, arg):

        attributes.addField(arg.field_name, arg.class_name, arg.type)

        # args = arg.split()

        # if len(args) == 3:
        #     ret = attributes.addField(args[1], args[0], args[2])

        #     if ret == -1:
        #         print(UMLException("Class error", f"{args[0]} does not exist"))
        #     elif ret == -2:
        #         print(UMLException("Field error", f"{args[1]} already exists"))
        # else:
        #     print("Incorrect amount of arguments")

    """
        Delete Field
    """
    deleteFieldParser = cmd2.Cmd2ArgumentParser(description="Removes an existing field from an existing class")
    deleteFieldParser.add_argument('class_name', help="Name of the pre-existing class")
    deleteFieldParser.add_argument('field_name', help="Name of the pre-existing field")
    @cmd2.with_argparser(deleteFieldParser)
    @cmd2.with_category("Field")
    def do_deleteField(self, arg):

        attributes.deleteField(arg.field_name, arg.class_name)

        # args = arg.split()
        # if len(args) == 2:
        #     ret = attributes.deleteField(args[1], args[0])
        #     if ret == -1:
        #         print(UMLException("Class error", f"{args[0]} does not exist"))
        #     elif ret == -2:
        #         print(UMLException("Field error", f"{args[1]} does not exist in {args[0]}"))
        # else:
        #     print("ARGUMENT ERROR")

    """
        Rename Field
    """
    renameFieldParser = cmd2.Cmd2ArgumentParser(description="Updates the name of an existing field")
    renameFieldParser.add_argument('class_name', help="Name of a pre-existing class")
    renameFieldParser.add_argument('name', help="Current name of an existing field")
    renameFieldParser.add_argument('new_name', help="Name to change the field to")
    @cmd2.with_argparser(renameFieldParser)
    @cmd2.with_category("Field")
    def do_renameField(self, arg):

        attributes.renameField(arg.name, arg.new_name, arg.class_name)

        # args = arg.split()
        # if len(args) == 3:
        #     ret = attributes.renameField(args[1], args[2], args[0])
        #     if ret == 1:
        #         print(UMLSuccess(f"Renamed {args[0]} to {args[1]}"))
        #     elif ret == -1:
        #         print(UMLException("Class error", f"{args[2]} does not exist"))
        #     elif ret == -2:
        #         print(UMLException("Field error", f"{args[0]} does not exist in {args[2]}"))
        #     elif ret == -3:
        #         print(UMLException("Field error", f"{args[1]} already exists in {args[2]}"))
        # else:
        #     print(UMLException("Argument error", f"expected 3 args, but was given {len(args)}"))


    """ PARAMETER COMMANDS """

    """
        Add Parameter(s)
    """
    @cmd2.with_category("Parameter")
    def do_addParam(self, arg):
        """Usage: addParam <class> <method> <name>:<type>...
        
        Adds a list of parameters to <method> in <class>
        """
        args = arg.split()
        if len(args) > 2:
            paramList = []
            for param in args[2:]:
                paramName, paramType = param.split(":")
                paramList.append((paramName, paramType))

            parameter.addParameter(paramList, args[1], args[0])
        else:
            print(UMLException("Argument error", f"not enough args"))

    """
        Delete Parameter(s)
    """
    @cmd2.with_category("Parameter")
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

    """
        Change Parameter(s)
    """
    @cmd2.with_category("Parameter")
    def do_changeParam(self, arg):
        """Usage: changeParam <class> <method> -o <old_name>... -n <new_name>:<new_type>
        
        Changes the list of parameters from <old_list> to <new_list> in <method>
        """
        args = arg.split()

        print(f"Waiting to be implemented")

        # parameter.changeParameter(args[3:], args[0], args[1], args[0])
        # parameter.changeParam(args[0], args[1], args[3:], args[0])
    
    """ SAVE/LOAD COMMANDS """

    saveParser = cmd2.Cmd2ArgumentParser(description="Saves the current state")
    saveParser.add_argument('filename', help="Name to save JSON file to")
    @cmd2.with_argparser(saveParser)
    @cmd2.with_category("Save/Load")
    # Stores the current state to a JSON file
    def do_save(self, arg):
        """Usage: save <filename>
        
        Saves the current program state to <filename>.json.
        """
        save(UMLClass.classIndex, relationship.relationIndex, arg)
    
    loadParser = cmd2.Cmd2ArgumentParser(description="Loads a previously stored state")
    loadParser.add_argument('filename', help="Name of the JSON file to be loaded")
    @cmd2.with_argparser(loadParser)
    @cmd2.with_category("Save/Load")
    # Load a previous state from a JSON file
    def do_load(self, arg):
        """Usage: load <filename>
        
        Loads a previously saved state from <filename>.json.
        """
        load(arg)
    
    """ LIST COMMANDS """
    @cmd2.with_category("Lists")
    # List all classes and their contents
    def do_listClasses(self, _):
        """Usage: listClasses
        
        Lists all existing classes and their contents.
        """
        listClasses()
    
    listClassParser = cmd2.Cmd2ArgumentParser(description="Lists the fields and methods of a class")
    listClassParser.add_argument('class_name', help="Name of the class to list")
    @cmd2.with_argparser(listClassParser)
    @cmd2.with_category("Lists")
    # Lists the contents of a specified class
    def do_listClass(self, arg):
        """Usage: listClass <name>
        
        Lists the contents of class <name>.
        """
        # ANSI COLORS
        # ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'light_gray', 'dark_gray', 'light_red',
        #  'light_green', 'light_yellow', 'light_blue', 'light_magenta', 'light_cyan', 'white', 'reset']

        output_str = cmd2.ansi.style(f"arguments: {arg}", fg=cmd2.Fg.RED)
        print(output_str)
        listClass(arg)

    @cmd2.with_category("Lists")
    # Lists all existing relationships
    def do_listRelationships(self, _):
        """Usage: listRelationships
        
        Lists all existing relationships between classes.
        """
        print(listRelationships())
    
    """ EXIT COMMAND """
    @cmd2.with_category("Exit")
    # Exits the program
    def do_exit(self, _):
        """Usage: exit
        
        Exits the program.
        """
        exit()
    # Overrides the emptyline method to avoid repetition of previous command
    def emptyline(self):
        pass
