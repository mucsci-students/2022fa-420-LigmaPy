"""
Filename    : buttons.py
Description : Functions to add buttons to the gui
"""
from tkinter import ttk

def classTabContents(frame : ttk.Frame):
    """
        Adds buttons for class commands to parent "frame"
    """
    ttk.Button(frame, width=20, text="Add class", command=None).grid(row=0, column=0, pady=10, padx=5)
    ttk.Button(frame, width=20, text="Delete class", command=None).grid(row=0, column=1, pady=10)
    ttk.Button(frame, width=20, text="Rename class", command=None).grid(row=0, column=2, pady=10, padx=5)

def relationTabContents(frame : ttk.Frame):
    """
        Adds buttons for relationship commands to parent "frame"
    """
    ttk.Button(frame, width=20, text="Add relationship", command=None).grid(row=0, column=0, pady=10, padx=5)
    ttk.Button(frame, width=20, text="Delete relationship", command=None).grid(row=0, column=1, pady=10)
    ttk.Button(frame, width=20, text="Update type", command=None).grid(row=0, column=2, pady=10, padx=5   )

def fieldTabContent(frame : ttk.Frame):
    """
        Adds buttons for field commands to parent "frame"
    """
    ttk.Button(frame, width=20, text="Add field", command=None).grid(row=0, column=0, pady=10, padx=5)
    ttk.Button(frame, width=20, text="Delete field", command=None).grid(row=0, column=1, pady=10)
    ttk.Button(frame, width=20, text="Rename field", command=None).grid(row=0, column=2, pady=10, padx=5)

def methodTabContent(frame : ttk.Frame):
    """
        Adds buttons for method commands to parent "frame"
    """
    ttk.Button(frame, width=20, text="Add method", command=None).grid(row=0, column=0, pady=10, padx=5)
    ttk.Button(frame, width=20, text="Delete method", command=None).grid(row=0, column=1, pady=10)
    ttk.Button(frame, width=20, text="Update method", command=None).grid(row=0, column=2, pady=10, padx=5)

def parameterTabContents(frame : ttk.Frame):
    """
        Adds buttons for parameter commands to parent "frame"
    """
    ttk.Button(frame, width=20, text="Add parameter(s)", command=None).grid(row=0, column=0, pady=10, padx=5)
    ttk.Button(frame, width=20, text="Delete parameter(s)", command=None).grid(row=0, column=1, pady=10)
    ttk.Button(frame, width=20, text="Change parameter(s)", command=None).grid(row=0, column=2, pady=10, padx=5)
