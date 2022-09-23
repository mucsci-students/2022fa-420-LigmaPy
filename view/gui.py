import tkinter as tk
from tkinter import ttk

# Local imports
import UMLNotebook as notebook

def display():
    root = tk.Tk()
    frame = tk.Frame(root)
    # Gets the width and height of the screen
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    # Sets the size of the window
    root.geometry(f"{screenWidth}x{screenHeight}")
    
    pane = notebook.createNotebook(frame)
    pane.pack()
    
    # Adds menubar to the root window
    root.config(menu=menubar(root))
    frame.pack()
    root.mainloop()

def menubar(root : tk.Tk):
    menubar = tk.Menu(root)
    # File menu
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=None)
    filemenu.add_command(label="Open", command=None)
    filemenu.add_command(label="Save", command=None)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    return menubar

if __name__=="__main__":
    display()