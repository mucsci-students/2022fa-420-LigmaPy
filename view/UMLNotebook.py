import tkinter as tk
from tkinter import ttk

# Local imports
import buttons as b

def createNotebook(frame : tk.Frame):
    tabControl = ttk.Notebook(frame)
    # Class tab
    classTab = tk.Frame(master=tabControl)
    tabControl.add(classTab, text="Class")
    b.classTabContents(classTab)
    # tabControl.insert(0, classTab)
    # Relationship tab
    relationTab = tk.Frame(master=tabControl)
    tabControl.add(relationTab, text="Relationship")
    b.relationTabContents(relationTab)
    # tabControl.insert(1, relationTab)
    # Field tab
    fieldTab = tk.Frame(master=tabControl)
    tabControl.add(fieldTab, text="Field")
    b.fieldTabContent(fieldTab)
    # tabControl.insert(2, fieldTab)
    # Method tab
    methTab = tk.Frame(master=tabControl)
    tabControl.add(methTab, text="Method")
    b.methodTabContent(methTab)
    # Parameter tab
    paramTab = tk.Frame(master=tabControl)
    tabControl.add(paramTab, text="Parameter")
    b.parameterTabContents(paramTab)

    # tabControl.pack(expand=1, fill="y")

    return tabControl