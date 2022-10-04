import tkinter as tk
from tkinter import ttk

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controller.guiController import GUIController

def makeInputFrame():
    inputFrame = tk.Frame()
    inputFrame.grid(row=1, column=0)
    return inputFrame

def makeAddClassFrame():
    """
        Creates imbeded frame to add a new class


    """
    inputlabel1 = tk.Label(GUIController().inputFrame, text='Enter Class name to add')
    inputlabel1.grid(row=0, columnspan=2) 
    e1 = tk.Entry(GUIController().inputFrame, width=50)
    e1.grid(row=1, columnspan=2)
    def output():
        # Error check here????
        GUIController().className = e1.get()
    ok = tk.Button(GUIController().inputFrame, text='Add Class', command=lambda: output())
    ok.grid(row=4, column=0)
    cancel = tk.Button(GUIController().inputFrame, text='Cancel', command=lambda: GUIController().wipe())
    cancel.grid(row=4, column=1)

def makeDeleteClassFrame():
    """
        Creates imbeded frame to delete a class


    """
    
    pass

def makeRenameClassFrame():
    """
        Creates imbeded frame to rename an existing class


    """
    pass

def makeAddRelationFrame():
    """
        Creates imbeded frame to create a relationship


    """
    pass

def makeDeleteRelationFrame():
    """
        Creates imbeded frame to delete an existing relationship


    """
    pass

def makeUpdateRelationType():
    """
        Creates an imbeded frame to update an existing relationship's type


    """
    pass

def makeAddFieldFrame():
    """
        Creates an imbeded frame to add a field to an existing class


    """
    pass

def makeDeleteFieldFrame():
    """
        Creates an imbeded frame to delete an existing field from an existing class


    """
    pass

def makeRenameFieldFrame():
    """
        Creates an imbeded frame to rename an existing field in an existing class


    """
    pass

def makeParamInputFrame():
    """
        Creates an imbeded frame to add parameters to a method
    """
    pass

def makeAddMethodFrame():
    """
        Creates an imbeded frame to add a method to an existing class


    """
    pass

def makeDeleteMethodFrame():
    """
        Creates an imbeded frame to delete a method from an existing class


    """
    pass

def makeRenameMethodFrame():
    """
        Creates an imbeded frame to delete a method in an existing class


    """
    pass

def makeAddParamFrame():
    """
        Creates an imbeded frame to add a parameter to an existing method


    """
    pass

def makeDeleteParamFrame():
    """
        Creates an imbeded frame to delete an existing parameter from an existing method


    """
    pass

def makeChangeParamFrame():
    """
        Creates an imbeded frame to change an existing method's parameters

    
    """
    pass