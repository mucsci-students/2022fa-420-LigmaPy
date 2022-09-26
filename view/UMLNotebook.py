"""
Author(s)   : Trevor Bender
Filename    : UMLNotebook.py
Description : Constructs the tkinter Notebook to switch between tabs.
"""
import tkinter as tk
from tkinter import ttk

# Local imports
import buttons as b

def createNotebook(frame : tk.Frame):
    """
        Creates a tkinter Notebook

        :param frame: Parent frame
        :return: tkinter Notebook object
    """

    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background='#c2c2c2')
    style.map("TNotebook.Tab", background=[("selected", "#bcade0")])

    tabControl = ttk.Notebook(frame)
    # Class tab
    classTab = tk.Frame(master=tabControl, bg='#bcade0')
    tabControl.add(classTab, text="Class")
    b.classTabContents(classTab)
    # Relationship tab
    relationTab = tk.Frame(master=tabControl, bg='#bcade0')
    tabControl.add(relationTab, text="Relationship")
    b.relationTabContents(relationTab)
    # Field tab
    fieldTab = tk.Frame(master=tabControl, bg='#bcade0')
    tabControl.add(fieldTab, text="Field")
    b.fieldTabContent(fieldTab)
    # Method tab
    methTab = tk.Frame(master=tabControl, bg='#bcade0')
    tabControl.add(methTab, text="Method")
    b.methodTabContent(methTab)
    # Parameter tab
    paramTab = tk.Frame(master=tabControl, bg='#bcade0')
    tabControl.add(paramTab, text="Parameter")
    b.parameterTabContents(paramTab)

    return tabControl