"""
Filename    : uml.py
Description : Main driver code for the UML Editor
"""

import sys
# Local imports
from controller.GuiController import Controller
import controller.cliController as cliController

def run():
    if len(sys.argv) == 2 and sys.argv[1] == '--cli':
        cliController.Interface().cmdloop()
    else:
        Controller().main()

if __name__=="__main__":
    run()