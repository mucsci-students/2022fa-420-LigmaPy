"""
    Author(s): Trevor Bender, Christian Shepperson
    Filename: cliController.py
    Description: Basic CLI interface and commands to go along with it.
"""

import pyfiglet
import cmd2
from model.ErrorHandlers.FieldException import FieldException
from model.ErrorHandlers.MethodException import MethodException
# Local Imports
import model.UMLClass as UMLCLass
import model.attributes as attributes
import model.relationship as relationship
import model.parameter as parameter
from UMLException import UMLException, UMLSuccess
from interface.interfaceCommands import *
from model.saveload import *
from model import UMLState
from model.ErrorHandlers.UMLClassExceptions import UMLClassException
from model.ErrorHandlers.RelationException import RelationException


_intro_text = """\
{}
Type `help` for an overview `help <command>` for more details.
Type `exit` to quit.
"""

class Interface(cmd2.Cmd):
    intro = _intro_text.format(pyfiglet.figlet_format("UML Editor"))
    prompt = ">> "

    def __init__(self):
        super().__init__(allow_cli_args=False)
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
        # Save the current state
        UMLState.addUndo(UMLState.saveState())
        ret = UMLClass.addClass(arg.class_name)
        UMLState.clearRedo()

        UMLClassException(ret).throwStatus(arg.class_name, None)

    """
        Delete Class
    """
    deleteClassParser = cmd2.Cmd2ArgumentParser(description="Removes a class and all of its contents")
    deleteClassParser.add_argument('class_name', help="Name of the class to be deleted")
    @cmd2.with_argparser(deleteClassParser)
    @cmd2.with_category("Class")
    # Removes a class
    def do_deleteClass(self, arg):
        # Save the current state
        UMLState.addUndo(UMLState.saveState())
        ret = UMLClass.deleteClass(arg.class_name)
        UMLState.clearRedo()

        UMLClassException(ret).throwStatus(arg.class_name, None)
    
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
        # Save the current state
        UMLState.addUndo(UMLState.saveState())
        ret = UMLClass.renameClass(arg.class_name, arg.new_name)
        UMLState.clearRedo()

        UMLClassException(ret).throwStatus(arg.class_name, arg.new_name)

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
        # Save the current state
        UMLState.addUndo(UMLState.saveState())
        ret = relationship.addRelationship(arg.src, arg.dest, arg.type)
        UMLState.clearRedo()

        RelationException(ret).throwStatus(arg.src, arg.dest)

    """
        Delete Relationship
    """
    deleteRelationParser = cmd2.Cmd2ArgumentParser(description="Removes an existing relationship between two classes")
    deleteRelationParser.add_argument('src', help="Name of the source class")
    deleteRelationParser.add_argument('dest', help="Name of the destination class")
    @cmd2.with_category("Relationship")
    # Deletes an existing relationship between two classes
    def do_deleteRelationship(self, arg):
        # Save the current state
        UMLState.addUndo(UMLState.saveState())
        ret = relationship.deleteRelationship(arg.src, arg.dest)
        UMLState.clearRedo()

        RelationException(ret).throwStatus(arg.src, arg.dest)

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
        # Save the current state
        UMLState.addUndo(UMLState.saveState())
        relIndex = relationship.findRelationship(arg.src, arg.dest)
        relationship.relationIndex[relIndex].editType(arg.new_type)
        UMLState.clearRedo()

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
        # Save the current state
        UMLState.addUndo(UMLState.saveState())
        # Added the method with return type to the class
        ret = attributes.addMethod(arg.method_name, arg.class_name, arg.ret_type)
        MethodException(ret).throwStatus(arg.class_name, arg.method_name, None)
        # Check if optional arg 'p' was entered
        if arg.p != None:
            # Create a list of tuples containing (paramName, paramType)
            paramList = []
            for param in arg.p:
                paramName, paramType = param.split(":")
                paramList.append((paramName, paramType))
            # Add parameter list to the newly created method            
            retPar = parameter.addParameter(paramList, arg.method_name, arg.class_name)


        UMLState.clearRedo()

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
        # Save the current program state
        UMLState.addUndo(UMLState.saveState())
        # Remove method from class
        ret = attributes.deleteMethod(arg.method_name, arg.class_name)
        UMLState.clearRedo()

        MethodException(ret).throwStatus(arg.class_name, arg.method_name, None)


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
        # Save the current program state
        UMLState.addUndo(UMLState.saveState())
        # Update the name of the method in a class
        ret = attributes.renameMethod(arg.old_name, arg.new_name, arg.class_name)
        UMLState.clearRedo()

        MethodException(ret).throwStatus(arg.class_name, arg.old_name, arg.new_name)

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
        # Save the current program state
        UMLState.addUndo(UMLState.saveState())
        ret = attributes.addField(arg.field_name, arg.class_name, arg.type)
        UMLState.clearRedo()

        FieldException(ret).throwStatus(arg.class_name, arg.field_name, None)

    """
        Delete Field
    """
    deleteFieldParser = cmd2.Cmd2ArgumentParser(description="Removes an existing field from an existing class")
    deleteFieldParser.add_argument('class_name', help="Name of the pre-existing class")
    deleteFieldParser.add_argument('field_name', help="Name of the pre-existing field")
    @cmd2.with_argparser(deleteFieldParser)
    @cmd2.with_category("Field")
    def do_deleteField(self, arg):
        # Save the current program state
        UMLState.addUndo(UMLState.saveState())
        ret = attributes.deleteField(arg.field_name, arg.class_name)
        UMLState.clearRedo()

        FieldException(ret).throwStatus(arg.class_name, arg.field_name, None)

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
        # Save the current program state
        UMLState.addUndo(UMLState.saveState())
        ret = attributes.renameField(arg.name, arg.new_name, arg.class_name)
        UMLState.clearRedo()

        FieldException(ret).throwStatus(arg.class_name, arg.name, arg.new_name)

    """ PARAMETER COMMANDS """

    """
        Add Parameter(s)
    """
    addParamParser = cmd2.Cmd2ArgumentParser(description="Adds one or more parameters to a classes method", epilog="A parameter has the format name:type")
    addParamParser.add_argument('class_name', help="Name of the class containing the target method")
    addParamParser.add_argument('method_name', help="Name of the method to add the parameter(s) to")
    addParamParser.add_argument('p', nargs='+', help="Name and type of the parameter")
    @cmd2.with_argparser(addParamParser)
    @cmd2.with_category("Parameter")
    def do_addParam(self, arg):
        # Save the current program state
        UMLState.addUndo(UMLState.saveState())
        # List of parameter tuples to pass to addParameter method
        paramList = []
        for param in arg.p:
            # Split the parameter name and type
            paramName, paramType = param.split(':')
            paramList.append((paramName, paramType))
        parameter.addParameter(paramList, arg.method_name, arg.class_name)

        UMLState.clearRedo()

    """
        Delete Parameter(s)
    """
    deleteParamParser = cmd2.Cmd2ArgumentParser(description="Removes parameter(s) from a classes method")
    deleteParamParser.add_argument('class_name', help="Name of the class containing the target method")
    deleteParamParser.add_argument('method_name', help="Name of the method to remove parameter(s) from")
    deleteParamParser.add_argument('-a', action='store_true', help="Delete all parameters from the specified method")
    deleteParamParser.add_argument('-p', nargs='+', help="Name of the parameter to be deleted")
    @cmd2.with_argparser(deleteParamParser)
    @cmd2.with_category("Parameter")
    def do_deleteParam(self, arg):
        # Save the current program state
        UMLState.addUndo(UMLState.saveState())
        if arg.a:
            parameter.deleteAllParameter(arg.method_name, arg.class_name)
        else:
            parameter.deleteParameter(arg.p, arg.method_name, arg.class_name)
        UMLState.clearRedo()

    """
        Change Parameter(s)
    """
    @cmd2.with_category("Parameter")
    def do_changeParam(self, arg):
        """Usage: changeParam <class> <method> -o <old_name>... -n <new_name>:<new_type>
        
        Changes the list of parameters from <old_list> to <new_list> in <method>
        """
        # args = arg.split()
        
        print(f"Waiting to be implemented")
    
    """ SAVE/LOAD COMMANDS """

    saveParser = cmd2.Cmd2ArgumentParser(description="Saves the current program state")
    saveParser.add_argument('filename', help="Name to save JSON file to")
    @cmd2.with_argparser(saveParser)
    @cmd2.with_category("Save/Load")
    # Stores the current state to a JSON file
    def do_save(self, arg):
        save(UMLClass.classIndex, relationship.relationIndex, arg.filename)
        UMLState.clearRedo()
    
    loadParser = cmd2.Cmd2ArgumentParser(description="Loads a previously stored state")
    loadParser.add_argument('filename', help="Name of the JSON file to be loaded")
    @cmd2.with_argparser(loadParser)
    @cmd2.with_category("Save/Load")
    # Load a previous state from a JSON file
    def do_load(self, arg):
        load(arg.filename)

    """ UNDO/REDO """
    def do_undo(self, _):
        UMLState.loadState(UMLState.undo())
    
    def do_redo(self, _):
        UMLState.loadState(UMLState.redo())

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
        listClass(arg.class_name)

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
