"""
Author      : Trevor Bender
Filename    : uml.py
Description : Main driver code for the UML Editor
"""

import sys
# Local imports
from view import gui
import cliInterface

def run():
    if len(sys.argv) == 2 and sys.argv[1] == '--cli':
        cliInterface.Interface().cmdloop()
    else:
        gui.display()

if __name__=="__main__":
    run()