"""
Julia Geesaman

Attribute Class

Adds an attribute, deletes an attribute, and renames an attribute
"""

import UMLClass as C

class attribute:
    
    def __init__ (self, name):
        self.name = name

    def rename(self, newName):
        self.name = newName


def findAttribute(name, className):

    classIndex = C.findClass(className)

    """ 
    if classIndex returns None, class doesn't exist
    can't proceed
    """
    if classIndex is None:
        return -1
    """
    if classIndex returns anything but None, class does exist
    can proceed
    Need to look through class's attributes
    If attribute is found in the list, return True
        --> we can delete or rename an attribute
    If attribute is not found in the list, return False
        --> we can add an attribute
    """
    for i, a in enumerate(C.classIndex[classIndex].attributes):
        if a.name == name:
            return i
    return -2


def addAttribute(name, className):
    """
    if findAttribute returns false then attribute does not exist and we can continue 
    with adding the attribute

    Create new attribute object
    Add that attribute to list of attributes in class
    """
    if findAttribute(name) >= 0:
        print('Attribute ', name, ' already exists in ', className, ' class.')
    elif findAttribute(name) == -2:
        newAttribute = attribute(name)
        index = C.findClass(className)
        C.classIndex[index].attributes.append(newAttribute)
        print(name, 'attribute has been added to the', className, 'class!')
    else: 
        print(className, ' class does not exist.')


def deleteAttribute(name, className):
    """
    if findAttribute returns true then attribute does exist and we can continue
    deleting the attribute
    """
    attributeIndex = findAttribute(name)

    if attributeIndex == -1:
        print(className, ' class does not exist.')
    elif attributeIndex >= 0:
        classIndex = C.findClass(className)
        C.classIndex[classIndex].attribute.pop(attributeIndex)
        print(name, "attribute has been deleted from", className, "class!")
    else:
        print(name, "attribute does not exist in", className, "class.")


def renameAttribute(oldName, newName, className):
    """
    if findAttribute returns true then attribute does exist and we can continue
    renaming the attribute
    However, must check findAttribute again to see if new name already exists. 
    if findAttribute
    """
    if findAttribute(oldName) is True and findAttribute(newName) is False:
        oldName.rename(newName)
        print(oldName, 'attribute has been renamed to', newName, 'in the', className, 'class!')
    elif findAttribute(oldName):
        print(oldName, 'attribute does not exist in the', className, 'class.')
    else:
        print(newName, 'is the name of an existing attribute in the', className, 'class.')


##################################### Driver Code ##############################################
""""
def main():

    while(1):

        userCommand = input("Waiting for a command...")
        userCommand = userCommand.split()

        if len(userCommand) > 1:

            # Add an Attribute
            if userCommand[0] == 'addAttribute':
                # Check number of arguments
                if len(userCommand) == 3:
                    addAttribute(userCommand[1], userCommand[2])
                elif len(userCommand) < 3:
                    print('Not enough arguments passed to add an attribute. Type \"help\" for proper syntax.')
                else:
                    print('Too many arguments passed to add an attribute. Type \"help\" for proper syntax.')

            # Delete an Attribute
            elif userCommand[0] == 'deleteAttribute':
                # Check number of arguments
                if len(userCommand) == 3:
                    deleteAttribute(userCommand[1], userCommand[2])
                elif len(userCommand) < 3:
                    print('Not enough arguments passed to delete an attribute. Type \"help\" for proper syntax.')
                else:
                    print('Too many arguments passed to delete an attribute. Type \"help\" for proper syntax.')                

            # Rename an Attribute
            elif userCommand[0] == 'renameAttribute':
                # Check number of arguments
                if len(userCommand) == 4:
                    renameAttribute(userCommand[1], userCommand[2], userCommand[3])
                elif len(userCommand) < 4:
                    print('Not enough arguments passed to rename an attribute. Type \"help\" for proper syntax.')
                elif len(userCommand) > 4:
                    print('Too many arguments passed to rename an attribute. Type \"help\" for proper syntax.')

        else:
            print('Invalid command. Type \"help\" for list of valid commands.')
"""