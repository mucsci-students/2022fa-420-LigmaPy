"""
    Filename: cliController.py
    Description: Basic CLI interface and commands to go along with it.
"""

import pyfiglet
import cmd2
from model.ErrorHandlers.FieldException import FieldException
from model.ErrorHandlers.MethodException import MethodException
from model.ErrorHandlers.ParamException import ParamException
from typing import List
# Local Imports
import model.UMLClass as UMLCLass
import model.attributes as attributes
import model.relationship as relationship
import model.parameter as parameter
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
        self.classNameChoices = []

    def all_class_names(self) -> List[str]:
        """
        Fetches a list of names of every class for tab completion
        """
        # Clear her
        self.classNameChoices = []
        # Update her with the string names
        for c in UMLClass.classIndex : self.classNameChoices.append(c.name)
        
        return self.classNameChoices

    def relationSources(self) -> List[str]:
        """
        Fetches a list of names of every class that is a relationship source
        """
        self.sourceClasses = []

        for source in relationship.relationIndex : self.sourceClasses.append(source.source)

        return self.sourceClasses

    def relationDestinations(self) -> List[str]:
        """
        Fetches a list of names of every class that is a relationship destination
        """
        self.destinationClass = []

        for dest in relationship.relationIndex : self.destinationClass.append(dest.destination)

        return self.destinationClass

    def classMethodNames(self):
        """
        Fetches a list of names of every method name
        """
        self.methodNames = []

        # TODO

        return self.methodNames

    

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
    deleteClassParser.add_argument('class_name', help="Name of the class to be deleted", choices_provider=all_class_names, metavar="class_name")
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
    renameClassParser.add_argument('class_name', help="Name of the class to update", choices_provider=all_class_names, metavar="class_name")
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
    addRelationParser.add_argument('src', help="Name of the source class", choices_provider=all_class_names, metavar="src")
    addRelationParser.add_argument('dest', help="Name of the destination class", choices_provider=all_class_names, metavar="dest")
    addRelationParser.add_argument('type', help="Type of relationship between the source and destination classes", choices=relationTypes, metavar="type")
    @cmd2.with_argparser(addRelationParser)
    @cmd2.with_category("Relationship")
    # Creates a relationship between two classes
    def do_addRelationship(self, arg):
        # Save the current state
        UMLState.addUndo(UMLState.saveState())
        ret = relationship.addRelationship(arg.src, arg.dest, arg.type)
        UMLState.clearRedo()

        RelationException(ret).throwStatus(arg.src, arg.dest, arg.type)

    """
        Delete Relationship
    """

    deleteRelationParser = cmd2.Cmd2ArgumentParser(description="Removes an existing relationship between two classes")
    deleteRelationParser.add_argument('src', help="Name of the source class", choices_provider=relationSources, metavar="src")
    deleteRelationParser.add_argument('dest', help="Name of the destination class", choices_provider=relationDestinations, metavar="dest")
    @cmd2.with_argparser(deleteRelationParser)
    @cmd2.with_category("Relationship")
    # Deletes an existing relationship between two classes
    def do_deleteRelationship(self, arg):
        # Save the current state
        UMLState.addUndo(UMLState.saveState())
        relType = relationship.relationIndex[relationship.findRelationship(arg.src, arg.dest)].type
        ret = relationship.deleteRelationship(arg.src, arg.dest)
        UMLState.clearRedo()

        RelationException(ret).throwStatus(arg.src, arg.dest, relType)

    """
        Change Relationship Type
    """
    changeRelTypeParser = cmd2.Cmd2ArgumentParser(description="Change the type of an existing relationship")
    changeRelTypeParser.add_argument('src', help="Name of the source class", choices_provider=relationSources, metavar="src")
    changeRelTypeParser.add_argument('dest', help="Name of the destination class", choices_provider=relationDestinations, metavar="dest")
    changeRelTypeParser.add_argument('new_type', help="New type for the relationship", choices=relationTypes, metavar="type")
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
    addMethodParser.add_argument('class_name', help="Name of target class", choices_provider=all_class_names, metavar="class_name")
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
            # loop through contents of p
            for param in arg.p:
                paramName, paramType = param.split(":")
                ret = parameter.addParameter(paramName, paramType, arg.method_name, arg.class_name)
                ParamException(ret).throwStatus(arg.class_name, arg.method_name, paramName, None)
        # Clear the redo stack
        UMLState.clearRedo()

    """
        Delete Method
    """
    deleteMethodParser = cmd2.Cmd2ArgumentParser(description="Removes an existing method from an existing class")
    deleteMethodParser.add_argument('class_name', help="Class containing the method to be removed", choices_provider=UMLClass.classIndex)
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
    renameMethodParser.add_argument('class_name', help="Class containing the method to rename", choices_provider=all_class_names)
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
    addFieldParser.add_argument('class_name', help="Name of class to add field to", choices_provider=all_class_names)
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
    deleteFieldParser.add_argument('class_name', help="Name of the pre-existing class", choices_provider=all_class_names)
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
    renameFieldParser.add_argument('class_name', help="Name of a pre-existing class", choices_provider=all_class_names)
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
    addParamParser.add_argument('class_name', help="Name of the class containing the target method", choices_provider=all_class_names)
    addParamParser.add_argument('method_name', help="Name of the method to add the parameter(s) to")
    addParamParser.add_argument('p', nargs='+', help="Name and type of the parameter")
    @cmd2.with_argparser(addParamParser)
    @cmd2.with_category("Parameter")
    def do_addParam(self, arg):
        # Save the current program state
        UMLState.addUndo(UMLState.saveState())
        for param in arg.p:
            # Split the parameter name and type
            paramName, paramType = param.split(':')
            ret = parameter.addParameter(paramName, paramType, arg.method_name, arg.class_name)
            ParamException(ret).throwStatus(arg.class_name, arg.method_name, paramName, None)
        UMLState.clearRedo()
    """
        Delete Parameter(s)
    """
    deleteParamParser = cmd2.Cmd2ArgumentParser(description="Removes parameter(s) from a classes method")
    deleteParamParser.add_argument('class_name', help="Name of the class containing the target method", choices_provider=all_class_names)
    deleteParamParser.add_argument('method_name', help="Name of the method to remove parameter(s) from")
    deleteParamParser.add_argument('-a', action='store_true', help="Delete all parameters from the specified method")
    deleteParamParser.add_argument('-p', nargs='+', help="Name of the parameter to be deleted")
    @cmd2.with_argparser(deleteParamParser)
    @cmd2.with_category("Parameter")
    def do_deleteParam(self, arg):
        # Save the current program state
        UMLState.addUndo(UMLState.saveState())
        if arg.a:
            ret = parameter.deleteAllParameter(arg.method_name, arg.class_name)
            ParamException(ret).throwStatus(arg.class_name, arg.method_name, None, None)
        else:
            for param in arg.p:
                ret = parameter.deleteParameter(param, arg.method_name, arg.class_name)
                ParamException(ret).throwStatus(arg.class_name, arg.method_name, param)
        UMLState.clearRedo()

        # ParamException(ret).throwStatus(arg.class_name, arg.method_name, )

    """
        Change Parameter(s)
    """
    changeParamParser = cmd2.Cmd2ArgumentParser(description="Changes parameter list of a classes method")
    changeParamParser.add_argument('class_name', help="Name of the class containing the target method", choices_provider=all_class_names)
    changeParamParser.add_argument('method_name', help="Name of the method to have its parameter(s) changed")
    changeParamParser.add_argument('-o', nargs='+', help="Parameter(s) to be changed")
    changeParamParser.add_argument('-n', nargs='+', help="Parameter(s) to change to")
    @cmd2.with_argparser(changeParamParser)
    @cmd2.with_category("Parameter")
    def do_changeParam(self, arg):
        # Loop through new and old list at the same time
        for i in range(0, len(arg.o)):
            ret = parameter.changeParameter(arg.o[i], arg.n[i], arg.method_name, arg.class_name)
            ParamException(ret).throwStatus(arg.class_name, arg.method_name, arg.o[i], arg.n[i])
    
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

    """
    TODO: 
        - Export current state to an image file
        - Add argument parser
    """

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
    listClassParser.add_argument('class_name', help="Name of the class to list", choices_provider=all_class_names)
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
        print(relationship.getSource())
        print(relationship.getDestinaitons("Tire"))
        print(listRelationships())
    
    """ EXIT COMMAND """
    @cmd2.with_category("Exit")
    # Exits the program
    def do_exit(self, _):
        """Usage: exit
        
        Exits the program.
        """
        exit()
