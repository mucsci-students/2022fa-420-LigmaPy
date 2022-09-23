from tkinter import ttk

def classTabContents(frame : ttk.Frame):
    ttk.Button(frame, text="Add class", command=None).grid(row=0, column=0)
    ttk.Button(frame, text="Delete class", command=None).grid(row=1, column=0)
    ttk.Button(frame, text="Rename class", command=None).grid(row=2, column=0)

def relationTabContents(frame : ttk.Frame):
    ttk.Button(frame, text="Add relationship", command=None).grid(row=0, column=0)
    ttk.Button(frame, text="Delete relationship", command=None).grid(row=1, column=0)
    ttk.Button(frame, text="Update type", command=None).grid(row=2, column=0)

def fieldTabContent(frame : ttk.Frame):
    ttk.Button(frame, text="Add field", command=None).grid(row=0, column=0)
    ttk.Button(frame, text="Delete field", command=None).grid(row=1, column=0)
    ttk.Button(frame, text="Rename field", command=None).grid(row=2, column=0)

def methodTabContent(frame : ttk.Frame):
    ttk.Button(frame, text="Add method", command=None).grid(row=0, column=0)
    ttk.Button(frame, text="Delete method", command=None).grid(row=1, column=0)
    ttk.Button(frame, text="Update method", command=None).grid(row=2, column=0)

def parameterTabContents(frame : ttk.Frame):
    ttk.Button(frame, text="Add parameter(s)", command=None).grid(row=0, column=0)
    ttk.Button(frame, text="Delete parameter(s)", command=None).grid(row=1, column=0)
    ttk.Button(frame, text="Change parameter(s)", command=None).grid(row=2, column=0)
