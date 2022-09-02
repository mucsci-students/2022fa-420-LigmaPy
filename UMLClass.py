'''
Samantha Noggle

Adds a class, deletes a class, & renames a class
'''

# List of all class objects the user has created
classIndex = []

class UMLClass:
    def __init__(self, name: str):
        self.name = name
        self.attributes = []

    def rename(self, newName):
        print(f"Class \"{self.name}\" was renamed to \"{newName}\"")
        self.name = newName


def isNameUnique(name: str):
    for c in classIndex:
        if c.name == name:
            return False
    return True


def findClass(name: str):
    """
    Finds a class object by name

    :param name: the name of the class to find
    :param classes: the list of all class objects

    :return: the index of the class object with the specified name
            or None if it was not found
    """
    for i, c in enumerate(classIndex):
        if c.name == name:
            return i
    print(f"Class \"{name}\" does not exist")
    return None


def addClass(name: str):
    if isNameUnique(name):
        newClass = UMLClass(name)
        classIndex.append(newClass)
        print(f"{newClass.name} has been created!")
    else:
        print(f"{name} already exists, could not create.")


def deleteClass(name: str):
    index = findClass(name)
    if index is not None:
        classIndex.pop(index)
        print(f"Class \"{name}\" has been deleted.")
    else:
        print(f"Deletion failed")


def renameClass(oldName: str, newName: str):
    index = findClass(oldName)
    if index is not None:
        classIndex[index].rename(newName)
    else:
        print(f"Rename failed")


###### Driver Code ######
def main():

    # Not yet an exit function so it'll wait for commands forever
    while(1):
        command = input("Waiting for a command...\n")
        command = command.split()

        if len(command) > 1:
            # Add a class
            if command[0] == 'addClass':
                addClass(command[1])
            # Delete a class
            elif command[0] == 'deleteClass':
                deleteClass(command[1])
            # Rename a class
            elif command[0] == 'renameClass' and len(command) == 3:
                renameClass(command[1], command[2])
            # Error
            else:
                print(
                    f"\n {command[0]} is not a command or too many arguments were passed.")
                print("Type \"help\" for command syntax.")
        else:
            print("Not enough arguments.")
            print("Type \"help\" for command syntax.")


if __name__ == "__main__":
    main()
