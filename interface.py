"""
    Trevor Bender & Christian Sheperdson

    Basic CLI interface and commands to go
    along with it.
"""

import json

class Interface():
    def __init__(self):
        self.isRunning = True
        self.run()

    '''
        Main loop to run the program.
        Taks input from user and runs the 
        corresponding commands.
    '''
    def run(self):
        self.__welcomeMsg()
        while self.isRunning:
            cmd = input(">> ").split(" ")
            # List all classes and contents
            if cmd[0] == 'listClasses':
                self.listClasses()
            # List contents of a specified class
            if cmd[0] == 'listClass':
                if len(cmd) < 2:
                    print(f"Not enough arguments.\nType 'help' {cmd[0]} for correct usage.")
                    continue
                elif len(cmd) > 2:
                    print(f"Too many arguments.\n Type 'help' {cmd[0]} for correct usage.")
                    continue
                self.listClass(cmd[1])
            # List all relationships that exist between classes
            if cmd[0] == 'listRelationships':
                self.listRelationships()
            # Help with a specified command
            if cmd[0] == 'help' and len(cmd) > 1:
                self.help(cmd[1])
            # Default help command
            elif cmd[0] == 'help':
                self.help()
            # Exit application
            if cmd[0] == 'exit':
                self.exit()

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

    '''
        Lists all of the classes and contents
        of the classes in a nice way.

        Example Output:

        Class Name:
            Attribute
            Attribute
            ...
    '''
    def listClasses(self):
        # Placeholder
        print("ClassName:")
        print("\tAttribute\n\tAttribute")

        print("ClassName:")
        print("\tAttribute\n\tAttribute")

    '''
        Lists the contents of a specified
        class in a nice way.
    '''
    def listClass(self, name):
        print(f"\n {name} Attributes")
        # Loop to print bottom border with 
        # length len(name) + len("Attributes") + 2
        for i in range((len(name) + 13)):
            print("*", end="")
        # Placeholder
        print("\nAttribute 1\nAttribute 2\n...\nAttribute n\n")

    '''
        Lists all of the relationships that
        exist between classes in a nice way.

        Example Output:
        [src] -> [dest]
    '''
    def listRelationships(self):
        # Placeholder
        print("[src 1] -> [dest 1]")
        print("[src 2] -> [dest 2]")
        print("...")
        print("[src n] -> [dest n]")

    '''
        Lists how to use the application without
        leaving the program.
    '''
    def help(self, cmd=None):
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
                print("Usage: " + cmd, end="")
                for option in command["args"]:
                    print(f" [{option}]", end="")
                print(f"\n\n\t{command['desc']}\n")
            else:
                print("Command not found. Type 'help' for a list of commands.")
                


    '''
        Exits the program
    '''
    def exit(self):
        # Set isRunning to false to stop the loop
        self.isRunning = False
        # Get input from user if they want to save
        exitChoice = input("Save progress? (Y/n)")
        if exitChoice.lower() == 'y' or exitChoice == '':
            print("SAVE PLACEHOLDER")
        elif exitChoice.lower() == 'n':
            print("Exiting")
        else:
            print("Invalid OPTION")

def main():
    app = Interface()

if __name__=="__main__":
    main()
