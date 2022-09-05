"""
    Trevor Bender & Christian Sheperdson

    Basic CLI interface and commands to go
    along with it.
"""


import pyfiglet # Install: pip install pyfiglet

# Local Imports
from UMLClass import addClass, deleteClass, renameClass
from relationship import addRelationship, deleteRelationship
from interfaceCommands import *

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

    '''
        Private
        Shows a formatted welcome message to user. Only shown
        at the startup of the program.
    '''
    def __welcomeMsg(self):
        print("\t*****************************************")
        print("\t*\t\t\t\t\t*")
        print("\t*\t\tUML Editor\t\t*")
        print("\t*\t\t Ligma Py\t\t*")
        print("\t*\t\t\t\t\t*")
        print("\t*****************************************")
        print("\t    Type 'help' for a list of commands")
        print("\t\t   Type 'exit' to quit\n")

def main():
    app = Interface()

if __name__=="__main__":
    main()
