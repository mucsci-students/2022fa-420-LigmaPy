"""
Author: Julia Geesaman
Filename: attributes.py
Description: Adds, deletes, and renames an attribute
"""

import UMLClass as C


"""
This is the attribute class.
"""
class attribute:
    
    """
    param name: name of the attribute
    """
    def __init__ (self, name):
        self.name = name

    """
    param newName: new name for the attribute
    """
    def rename(self, newName):
        self.name = newName

"""
This method finds whether the given class and attribute exist.

param name: name of the attribute
param className: class attribute is part of

returns: -1 if given class does not exist
         -2 if attribute does not exist in given class
          i index of attribute, if attribute and class exist
"""
def findAttribute(name, className):

    classIndex = C.findClass(className)

    # runs if class not found
    if classIndex is None:
        return -1
    
    for i, a in enumerate(C.classIndex[classIndex].attributes):
        if a.name == name:
            return i
    return -2

"""
Creates a new attribute object and inserts it into given class' list of attributes

param name: name of the attribute
param className: name of class attribute should be added to
"""
def addAttribute(name, className):

    attributeIndex = findAttribute(name, className)

    # Runs if attribute with given name already exists in given class
    if attributeIndex >= 0:
        print(f'Attribute \"{name}\" already exists in \"{className}\" class.')
    # Runs if attribute does not exist in given class
    elif attributeIndex == -2:
        newAttribute = attribute(name)
        index = C.findClass(className)
        C.classIndex[index].attributes.append(newAttribute)
        print(f'\"{name}\" attribute has been added to the \"{className}\" class!')
    # Runs if given class does not exist
    else: 
        return

"""
Deletes an attribute object from a given class.

param name: name of attribute to be deleted
param className: name of class atrribute should be deleted from
"""
def deleteAttribute(name, className):
   
    attributeIndex = findAttribute(name, className)

    # Runs if given class does not exist
    if attributeIndex == -1:
        return
    # Runs if class and attribute exist
    elif attributeIndex >= 0:
        classIndex = C.findClass(className)
        C.classIndex[classIndex].attributes.pop(attributeIndex)
        print(f'\"{name}\" attribute has been deleted from \"{className}\" class!')
    # Runs if class exists but attribute does not
    else:
        print(f'\"{name}\" attribute does not exist in \"{className}\" class.')

"""
Renames a given attribute

param oldName: current name of attribute
param newName: new name for attribute
param className: name of class attribute exists within
"""
def renameAttribute(oldName, newName, className):
    
    attIndexOld = findAttribute(oldName, className)
    attIndexNew = findAttribute(newName, className)

    # Runs if attribute exists and can be renamed to new name
    if attIndexOld >= 0 and attIndexNew < 0:
        index = C.findClass(className)
        C.classIndex[index].attributes[attIndexOld].rename(newName)
        print(f'\"{oldName}\" attribute has been renamed to \"{newName}\" in the \"{className}\" class!')
    # Runs if given attribute does not exist in given class
    elif attIndexOld == -2:
        print(f'\"{oldName}\" attribute does not exist in the \"{className}\" class.')
    # Runs if given class does not exist
    elif attIndexOld == -1:
        return
    # Runs if attribute already exists with new name in given class
    else:
        print(f'\"{newName}\" is the name of an existing attribute in the \"{className}\" class.')


##################################### Driver Code ##############################################

def main():

    while(1):

        print("enter a command")
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

if __name__=="__main__":
    main()
