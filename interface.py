"""
    Author(s): Trevor Bender, Christian Sheperdson
    Filename: interface.py
    Description: Basic CLI interface and commands to go along with it.
"""


import pyfiglet # Install: pip install pyfiglet

# Local Imports
from UMLClass import addClass, deleteClass, renameClass
from relationship import addRelationship, deleteRelationship
from interfaceCommands import *
from saveload import save, load

class Interface():
    def __init__(self):
        self.isRunning = True
        self.run()

    '''
        Main loop to run the program.
        Takes input from user and runs the 
        corresponding commands.
    '''
    def run(self):
        # Prints a unicode art using package pyfiglet
        print(pyfiglet.figlet_format("UML Editor"))
        while self.isRunning:
            cmd = input(">> ").split(" ")
            ### CLASS COMMANDS ###
            if cmd[0] == 'addClass':
                if len(cmd) == 2:
                    addClass(cmd[1])
                else:
                    print(f"Invalid syntax.\nType 'help {cmd[0]}' for correct usage.")
            elif cmd[0] == 'deleteClass':
                if len(cmd) == 2:
                    deleteClass(cmd[1])
                else:
                    print(f"Invalid syntax.\nType 'help {cmd[0]}' for correct usage.")
            elif cmd[0] == 'renameClass':
                if len(cmd) == 3:
                    renameClass(cmd[1], cmd[2])
                else:
                    print(f"Invalid syntax.\nType 'help {cmd[0]}' for correct usage.")
            ### RELATIONSHIP COMMANDS ###
            elif cmd[0] == 'addRelationship':
                if len(cmd) == 3:
                    addRelationship(cmd[1], cmd[2])
                else:
                    print(f"Invalid syntax.\nType 'help {cmd[0]}' for correct usage.")
            elif cmd[0] == 'deleteRelationship':
                if len(cmd) == 3:
                    deleteRelationship(cmd[1], cmd[2])
                else:
                    print(f"Invalid syntax.\nType 'help {cmd[0]}' for correct usage.")
            ### ATTRIBUTES COMMANDS ###
            elif cmd[0] == 'addAttribute':
                # TODO
                pass
            elif cmd[0] == 'deleteAttribute':
                # TODO
                pass
            elif cmd[0] == 'renameAttribute':
                # TODO
                pass
            ### SAVE/LOAD ###
            elif cmd[0] == 'save':
                if len(cmd) == 2:
                    save(classIndex, relationIndex, cmd[1])
                else:
                    print(f"Invalid syntax.\nType 'help {cmd[0]}' for correct usage.")                
            elif cmd[0] == 'load':
                if len(cmd) == 2:
                    load(cmd[1])
                else:
                    print(f"Invalid syntax.\nType 'help {cmd[0]}' for correct usage.") 
                pass
            ### INTERFACE COMMANDS ###
            # List all classes and contents
            elif cmd[0] == 'listClasses':
                listClasses()
            # List contents of a specified class
            elif cmd[0] == 'listClass':
                if len(cmd) == 2:
                    listClass(cmd[1])
                else:
                    print(f"Invalid syntax.\nType 'help {cmd[0]}' for correct usage.")
            # List all relationships that exist between classes
            elif cmd[0] == 'listRelationships':
                listRelationships()
            # Help with a specified command
            elif cmd[0] == 'help' and len(cmd) > 1:
                help(cmd[1])
            # Default help command
            elif cmd[0] == 'help':
                help()
            # Exit application
            elif cmd[0] == 'exit':
                self.isRunning = False
                exit()
            elif cmd[0] == '':
                pass
            else:
                print(f"Command not found: {cmd[0]}")

def main():
    app = Interface()

if __name__=="__main__":
    main()
