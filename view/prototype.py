"""
Filename    : prototype.py
Description : Prototype for class labels in gui
"""



import tkinter as tk
#import UMLNotebook as notebook
from tkinter import LEFT, RIGHT, VERTICAL, Y, Canvas, OptionMenu, StringVar, ttk, Tk, Label
import view.View as v
# import model.UMLClass as u
# import model.relationship as r
# import model.attributes as a
# import model.UMLState as s
# import math


class classLabel(tk.Tk):

    def __init__(self):
        # self.view = v(self)
        self.height = 8
        self.width = 12
        self.text = "Class: \n\n    Fields:\n\n    Methods:\n\n"

    def main(self):
        self.view.main()

def makeLabel(classObject, canvas):

    newLabel = classLabel()
    p = Label(canvas, text=newLabel.text, height=newLabel.height, width=newLabel.width, borderwidth=1, relief="solid", justify=LEFT, name = classObject.name.lower())
    return p