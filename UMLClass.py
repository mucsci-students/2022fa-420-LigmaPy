'''
Samantha Noggle

Adds a class, deletes a class, & renames a class
'''

from typing import List

# List of all class objects the user has created
# classIndex = []

class UMLClass:
    def __init__(self, name: str):
        self.name = name
        self.attributes = []

    def rename(self, newName):
        print(f"\nClass \"{self.name}\" was renamed to \"{newName}\"")
        self.name = newName


def isNameUnique(name: str):
    '''
    Checks classIndex for duplicate names
    '''
    for c in classIndex:
        if c.name == name:
            return False
    return True


def findClass(name: str):
    """
    Finds a class object by name and returns it's index
    """
    for i, c in enumerate(classIndex):
        if c.name == name:
            return i
    print(f"\nClass \"{name}\" does not exist")
    return None


def addClass(name: str):
    """
    Creates and adds a new class
    """
    if isNameUnique(name):
        newClass = UMLClass(name)
        classIndex.append(newClass)
        print(f"\nClass \"{newClass.name}\" has been created!")
    else:
        print(f"\nClass \"{name}\" already exists, could not create.")


def deleteClass(name: str):
    """
    Deletes a class by it's name
    """
    index = findClass(name)
    if index is not None:
        classIndex.pop(index)
        print(f"\nClass \"{name}\" has been deleted.")
    else:
        print("Deletion failed")


def renameClass(oldName: str, newName: str):
    """
    Renames a class from oldName to newName
    """
    if findClass(newName):
        print(f"\nA class already exists with the name \"{newName}\"")
        print("Rename failed")
        return

    index = findClass(oldName)
    if index is not None:
        classIndex[index].rename(newName)
    else:
        print("Rename failed")


classIndex : List[UMLClass] = []

######################## Driver Code ########################
"""
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
                    f"\n\"{command[0]}\" is not a command or too many arguments were passed.")
                print("Type \"help\" for command syntax.")
        else:
            print("\nNot enough arguments.")
            print("Type \"help\" for command syntax.")


if __name__ == "__main__":
    main()
"""
