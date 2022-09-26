"""
Author(s)   : Trevor Bender, Aaron Heinbaugh
Filename    : gui.py
Description : Constructs and displays the gui
"""

import tkinter as tk
# Local imports
import UMLNotebook as notebook
import UMLOutput as can

def display():
    """
        Constructs and displays the GUI
    """
    root = tk.Tk()
    root.title("UML Editor")

    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.columnconfigure(1, weight=1)

    inputFrame = tk.Frame(root)
    # Gets the width and height of the screen
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    # Sets the size of the window
    root.geometry(f"{screenWidth}x{screenHeight}")
    # Create the notebook (tabs) for UML modifications
    pane = notebook.createNotebook(inputFrame)

    inputFrame.grid(row=0, column=0, sticky="nsew", rowspan=2)
    inputFrame.rowconfigure(0, weight=1)
    inputFrame.columnconfigure(1, weight=1)
    pane.grid(row=0, column=0, sticky="nsew", rowspan=2)
    # Create another frame for holding output components
    outputFrame = tk.Frame(root)
    # Create canvas for ouput
    canvas = can.createCanvas(outputFrame)
    # Configure canvas position and layout
    outputFrame.grid(row=0, column=1, sticky="nswe", rowspan=2)
    outputFrame.rowconfigure(0, weight=1)
    outputFrame.columnconfigure(1, weight=1)

    canvas.pack(fill=tk.BOTH, expand=1)

    canvas.grid(row=0, column=1, sticky="nswe", rowspan=2)

    # Adds menubar to the root window
    root.config(menu=menubar(root))
    root.mainloop()

def menubar(root : tk.Tk):
    """
        Creates the menu bar at the top of the gui

        :param root: The root of the GUI
        :return: tkinter Menu object
    """
    menubar = tk.Menu(root)
    # File menu
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=None)
    filemenu.add_command(label="Open", command=None)
    filemenu.add_command(label="Save", command=None)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    # Help menu
    helpmenu = tk.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Commands", command=None)
    menubar.add_cascade(label="Help", menu=helpmenu)

    return menubar

if __name__=="__main__":
    display()