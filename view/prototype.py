"""
Filename    : prototype.py
Description : Prototype for class labels in gui
"""

import tkinter as tk
from tkinter import LEFT, RIGHT, VERTICAL, Y, Canvas, OptionMenu, StringVar, ttk, Tk, Label
import view.View as v


class classLabel(tk.Tk):
    """
    Prototype design pattern implementation. 
    Creates classLabel object
    """

    def __init__(self):
        self.height = 8
        self.width = 12
        self.text = "Class: \n\n    Fields:\n\n    Methods:\n\n"

    def main(self):
        self.view.main()

def makeLabel(classObject, canvas):
    """
    Creates label when new class is added.
    @param classObject: new class that is being added
    @param canvas: current canvas label should be printed on
    """
    newLabel = classLabel()
    p = Label(canvas, text=newLabel.text, height=newLabel.height, width=newLabel.width, borderwidth=1, relief="solid", justify=LEFT, name = classObject.name.lower())
    return p