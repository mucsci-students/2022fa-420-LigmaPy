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
        self.welcomeMsg()
        while self.isRunning:
            cmd = input(">> ").split(" ")
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
        Shows a formatted welcome message to user. Only shown
        at the startup of the program.
    '''
    def welcomeMsg(self):
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
    '''
    def listClasses(self):
        pass

    '''
        Lists the contents of a specified
        class in a nice way.
    '''
    def listClass(self, name):
        pass

    '''
        Lists all of the relationships that
        exist between classes in a nice way.

        Example Output:
        [src] -> [dest]
    '''
    def listRelationships(self):
        pass

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
                # print(i['name'] + "\t" + i['desc'] + "\n")
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
            # Prints the usage and description of the specified command.
            if command is not None:
                print("Usage: " + cmd, end="")
                for option in command["args"]:
                    print(" [" + option + "]", end="")
                print("\n\n\t" + command["desc"] + "\n")
            else:
                print("Invalid command. Type 'help' for a list of commands.")
                


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
