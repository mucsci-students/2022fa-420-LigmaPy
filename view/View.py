"""
Author(s)   : Trevor Bender and Aaron Heinbaugh
Filename    : View.py
Description : Constructs and displays the gui
"""

import tkinter as tk
#import UMLNotebook as notebook
import UMLOutput as can
from tkinter import ttk

class View(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.className = None
        self.classNameNew = None
        self.source = None
        self.destination = None
        self.relationshipType = None
        self.relationshipTypeNew = None
        self.field = None
        self.feildNew = None
        self.fieldType = None
        self.method = None
        self.methodReturnType = None
        self.methodNew = None
        self.param = None
        self.paramNew = None
        self.paramType = None
        self.paramTypeNew = None
        self.geometry("800x600")
        self.title("UML Editor")
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        # Sets the size of the window
        self.geometry(f"{screenWidth}x{screenHeight}")
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        self.makeButtonFrame()
        self.makeInputFrame()
        #self.makeButtons()
        self.makeMenu()
        

    def clear(self):
        self.className = None
        self.classNameNew = None
        self.source = None
        self.destination = None
        self.relationshipType = None
        self.field = None
        self.feildNew = None
        self.fieldType = None
        self.method = None
        self.methodReturnType = None
        self.methodNew = None
        self.param = None
        self.paramNew = None
        self.paramType = None
        self.paramTypeNew = None

    def main(self):
        self.mainloop()
    
    def makeMenu(self):
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command= lambda : print("Call load function"))
        filemenu.add_command(label="Save", command= lambda : print("Call save function"))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        # Help menu
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Commands", command=None)
        menubar.add_cascade(label="File", menu=filemenu)
        self.config(menu=menubar)

    def makeButtonFrame(self):
        self.buttonFrame = tk.Frame(self)
        
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
            tabControl.add(classTab, text=f'{"Class":^20s}')
            
            def classTabContents(frame : ttk.Frame):
                """
                    Adds buttons for class commands to parent "frame"
                """
                ttk.Button(frame, width=20, text="Add class", command=lambda : addClassFrame()).grid(row=0, column=0, pady=10, padx=5)
                ttk.Button(frame, width=20, text="Delete class", command= lambda : deleteClassFrame()).grid(row=0, column=1, pady=10)
                ttk.Button(frame, width=20, text="Rename class", command=lambda : renameClassFrame()).grid(row=0, column=2, pady=10, padx=5)
            
            classTabContents(classTab)
            # Relationship tab
            relationTab = tk.Frame(master=tabControl, bg='#bcade0')
            tabControl.add(relationTab, text=f'{"Relationship":^20s}')
            
            
            def relationTabContents(frame : ttk.Frame):
                """
                    Adds buttons for relationship commands to parent "frame"
                """
                ttk.Button(frame, width=20, text="Add relationship", command= lambda : addRelationFrame()).grid(row=0, column=0, pady=10, padx=5)
                ttk.Button(frame, width=20, text="Delete relationship", command= lambda : deleteRelationFrame()).grid(row=0, column=1, pady=10)
                ttk.Button(frame, width=20, text="Update type", command= lambda : updateRelationType()).grid(row=0, column=2, pady=10, padx=5)   
            
            relationTabContents(relationTab)
            # Field tab
            fieldTab = tk.Frame(master=tabControl, bg='#bcade0')
            tabControl.add(fieldTab, text=f'{"Field":^20s}')
            
            def fieldTabContent(frame : ttk.Frame):
                """
                    Adds buttons for field commands to parent "frame"
                """
                ttk.Button(frame, width=20, text="Add field", command= lambda : addFieldFrame()).grid(row=0, column=0, pady=10, padx=5)
                ttk.Button(frame, width=20, text="Delete field", command= lambda : deleteFieldFrame()).grid(row=0, column=1, pady=10)
                ttk.Button(frame, width=20, text="Rename field", command= lambda : renameFieldFrame()).grid(row=0, column=2, pady=10, padx=5)
            
            fieldTabContent(fieldTab)
            # Method tab
            methTab = tk.Frame(master=tabControl, bg='#bcade0')
            tabControl.add(methTab, text=f'{"Method":^20s}')
            
            def methodTabContent(frame : ttk.Frame):
                """
                    Adds buttons for method commands to parent "frame"
                """
                ttk.Button(frame, width=20, text="Add method", command= lambda : addMethodFrame()).grid(row=0, column=0, pady=10, padx=5)
                ttk.Button(frame, width=20, text="Delete method", command= lambda : deleteMethodFrame()).grid(row=0, column=1, pady=10)
                ttk.Button(frame, width=20, text="Update method", command= lambda : renameMethodFrame()).grid(row=0, column=2, pady=10, padx=5)
            
            methodTabContent(methTab)
            # Parameter tab
            paramTab = tk.Frame(master=tabControl, bg='#bcade0')
            tabControl.add(paramTab, text=f'{"Parameter":^20s}')
            
            def parameterTabContents(frame : ttk.Frame):
                """
                    Adds buttons for parameter commands to parent "frame"
                """
                ttk.Button(frame, width=20, text="Add parameter(s)", command= lambda : addParamFrame()).grid(row=0, column=0, pady=10, padx=5)
                ttk.Button(frame, width=20, text="Delete parameter(s)", command= lambda : deleteParamFrame()).grid(row=0, column=1, pady=10)
                ttk.Button(frame, width=20, text="Change parameter(s)", command= lambda : changeParamFrame()).grid(row=0, column=2, pady=10, padx=5) 
            
            parameterTabContents(paramTab)

            return tabControl

        self.pane = createNotebook(self.buttonFrame)
        self.pane.enable_traversal()
        self.buttonFrame.grid(row=0, column=0, sticky="nsew", rowspan=2)
        # Configure the buttonInputFrame grid
        self.buttonFrame.rowconfigure(0, weight=1)
        self.buttonFrame.columnconfigure(1, weight=1)
        self.pane.grid(row=0, column=0, sticky="nsew", rowspan=2)
    
    #creates input frame on bottom right to put in input fields 
    def makeInputFrame(self):
        self.inputFrame = tk.Frame(self)
        self.inputFrame.grid(row = 1, column=0)

    #creates canvase for output on right side
    def makeOutputFrame(self):
        self.outputFrame = tk.Frame(self)
        canvas = can.createCanvas(self.outputFrame)
        self.outputFrame.grid(row=0, column=1, sticky="nswe", rowspan=2)
        self.outputFrame.rowconfigure(0, weight=1)
        self.outputFrame.columnconfigure(1, weight=1)
        canvas.pack(fill=tk.BOTH, expand=1)
        canvas.grid(row=0, column=1, sticky="nswe", rowspan=2)
    
    #creates the add class frame upon clicking add class
    def makeAddClassFrame(self):
        inputlabel1 = tk.Label(self.inputFrame, text='Enter Class name to add')
        inputlabel1.grid(row=0, columnspan=2) 
        e1 = tk.Entry(self.inputFrame, width=50)
        e1.grid(row=1, columnspan=2)
        def output():
            # Error check here????
            self.className = e1.get()
            print(self.className)
        ok = tk.Button(self.inputFrame, text='Add Class', command=lambda: output())
        ok.grid(row=4, column=0)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: remake())
        cancel.grid(row=4, column=1)

    #creates the frame to update relations after clicking said button
    def makeUpdateRelationType(self):
        inputlabel1 = tk.Label(self.inputFrame, text='Enter source name:')
        inputlabel1.grid(row=0, columnspan=2) 
        e1 = tk.Entry(self.inputFrame, width=50)
        e1.grid(row=1, columnspan=2)
        inputlabel2 = tk.Label(self.inputFrame, text='Enter destination name:')
        inputlabel2.grid(row=2, columnspan=2) 
        e2 = tk.Entry(self.inputFrame, width=50)
        e2.grid(row=3, columnspan=2)
        inputlabel3 = tk.Label(self.inputFrame, text='Enter new relationship type:')
        inputlabel3.grid(row=4, columnspan=2) 
        e3 = tk.Entry(self.inputFrame, width=50)
        e3.grid(row=5, columnspan=2)
        def output():
            # Error check here????
            self.source = e1.get()
            self.destination = e2.get()
            self.relationshipTypeNew = e3.get()
            print(self.source + " " + self.destination + " " + self.relationshipTypeNew)
        ok = tk.Button(self.inputFrame, text='Change type', command=lambda: output())
        ok.grid(row=6, column=0)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: remake())
        cancel.grid(row=6, column=1)        

    #creates the delete class frame after click said button
    def makeDeleteClassFrame(self):
        inputlabel1 = tk.Label(self.inputFrame, text='Enter Class name to delete')
        inputlabel1.grid(row=0, columnspan=2) 
        e1 = tk.Entry(self.inputFrame, width=50)
        e1.grid(row=1, columnspan=2)
        def output():
            # Error check here????
            self.className = e1.get()
            print(self.className)
        ok = tk.Button(self.inputFrame, text='Delete Class', command=lambda: output())
        ok.grid(row=4, column=0)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: remake())
        cancel.grid(row=4, column=1)

    def makeRenameClassFrame(self):
        inputlabel1 = tk.Label(self.inputFrame, text='Enter Class name to rename:')
        inputlabel1.grid(row=0, columnspan=2) 
        e1 = tk.Entry(self.inputFrame, width=50)
        e1.grid(row=1, columnspan=2)
        inputlabel2 = tk.Label(self.inputFrame, text='Enter new name:')
        inputlabel2.grid(row=2, columnspan=2) 
        e2 = tk.Entry(self.inputFrame, width=50)
        e2.grid(row=3, columnspan=2)
        def output():
            # Error check here????
            self.className = e1.get()
            self.classNameNew = e2.get()
            print(self.className + " " + self.classNameNew)
        ok = tk.Button(self.inputFrame, text='Rename Class', command=lambda: output())
        ok.grid(row=4, column=0)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: remake())
        cancel.grid(row=4, column=1)   
       
    def makeAddRelationFrame(self):
        inputlabel1 = tk.Label(self.inputFrame, text='Enter source name:')
        inputlabel1.grid(row=0, columnspan=2) 
        e1 = tk.Entry(self.inputFrame, width=50)
        e1.grid(row=1, columnspan=2)
        inputlabel2 = tk.Label(self.inputFrame, text='Enter destination name:')
        inputlabel2.grid(row=2, columnspan=2) 
        e2 = tk.Entry(self.inputFrame, width=50)
        e2.grid(row=3, columnspan=2)
        inputlabel3 = tk.Label(self.inputFrame, text='Enter relationship type:')
        inputlabel3.grid(row=4, columnspan=2) 
        e3 = tk.Entry(self.inputFrame, width=50)
        e3.grid(row=5, columnspan=2)
        def output():
            # Error check here????
            self.source = e1.get()
            self.destination = e2.get()
            self.relationshipType = e3.get()
            print(self.source + " " + self.destination + " " + self.relationshipType)
        ok = tk.Button(self.inputFrame, text='Add Relationship', command=lambda: output())
        ok.grid(row=6, column=0)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: remake())
        cancel.grid(row=6, column=1)

    def makeDeleteRelationFrame(self):
        inputlabel1 = tk.Label(self.inputFrame, text='Enter source name to delete:')
        inputlabel1.grid(row=0, columnspan=2) 
        e1 = tk.Entry(self.inputFrame, width=50)
        e1.grid(row=1, columnspan=2)
        inputlabel2 = tk.Label(self.inputFrame, text='Enter destination name to delete:')
        inputlabel2.grid(row=2, columnspan=2) 
        e2 = tk.Entry(self.inputFrame, width=50)
        e2.grid(row=3, columnspan=2)
        def output():
            # Error check here????
            self.source = e1.get()
            self.destination = e2.get()
            print(self.source + " " + self.destination)
        ok = tk.Button(self.inputFrame, text='Delete relationship', command=lambda: output())
        ok.grid(row=4, column=0)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: remake())
        cancel.grid(row=4, column=1)
    
    def makeAddFieldFrame(self):
        inputlabel1 = tk.Label(self.inputFrame, text='Enter class name:')
        inputlabel1.grid(row=0, columnspan=2) 
        e1 = tk.Entry(self.inputFrame, width=50)
        e1.grid(row=1, columnspan=2)
        inputlabel2 = tk.Label(self.inputFrame, text='Enter field name:')
        inputlabel2.grid(row=2, columnspan=2) 
        e2 = tk.Entry(self.inputFrame, width=50)
        e2.grid(row=3, columnspan=2)
        inputlabel3 = tk.Label(self.inputFrame, text='Enter field type (leave empty if none):')
        inputlabel3.grid(row=4, columnspan=2) 
        e3 = tk.Entry(self.inputFrame, width=50)
        e3.grid(row=5, columnspan=2)
        def output():
            # Error check here????
            self.className = e1.get()
            self.field = e2.get()
            self.fieldType = e3.get()
            print(self.className + " " + self.field + " " + str(self.fieldType))
        ok = tk.Button(self.inputFrame, text='Add Field', command=lambda: output())
        ok.grid(row=6, column=0)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: remake())
        cancel.grid(row=6, column=1)

    def makeDeleteFieldFrame(self):
        inputlabel1 = tk.Label(self.inputFrame, text='Enter class name:')
        inputlabel1.grid(row=0, columnspan=2) 
        e1 = tk.Entry(self.inputFrame, width=50)
        e1.grid(row=1, columnspan=2)
        inputlabel2 = tk.Label(self.inputFrame, text='Enter field to delete:')
        inputlabel2.grid(row=2, columnspan=2) 
        e2 = tk.Entry(self.inputFrame, width=50)
        e2.grid(row=3, columnspan=2)
        def output():
            # Error check here????
            self.className = e1.get()
            self.field = e2.get()
            print(self.className + " " + self.field)
        ok = tk.Button(self.inputFrame, text='Delete field', command=lambda: output())
        ok.grid(row=4, column=0)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: remake())
        cancel.grid(row=4, column=1)

    def makeRenameFieldFrame(self):
        inputlabel1 = tk.Label(self.inputFrame, text='Enter class name:')
        inputlabel1.grid(row=0, columnspan=2) 
        e1 = tk.Entry(self.inputFrame, width=50)
        e1.grid(row=1, columnspan=2)
        inputlabel2 = tk.Label(self.inputFrame, text='Enter field name to rename:')
        inputlabel2.grid(row=2, columnspan=2) 
        e2 = tk.Entry(self.inputFrame, width=50)
        e2.grid(row=3, columnspan=2)
        inputlabel3 = tk.Label(self.inputFrame, text='Enter new field name:')
        inputlabel3.grid(row=4, columnspan=2) 
        e3 = tk.Entry(self.inputFrame, width=50)
        e3.grid(row=5, columnspan=2)
        def output():
            # Error check here????
            self.className = e1.get()
            self.field = e2.get()
            self.feildNew = e3.get()
            print(self.className + " " + self.field + " " + self.feildNew)
        ok = tk.Button(self.inputFrame, text='Rename Field', command=lambda: output())
        ok.grid(row=6, column=0)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: remake())
        cancel.grid(row=6, column=1)

    #creates the parameter frame for param input after clicking add params
    def makeParamInputFrame(self):
        inputlabel1 = tk.Label(self.inputFrame, text='Enter parameter name:')
        inputlabel1.grid(row=0, columnspan=2) 
        e1 = tk.Entry(self.inputFrame, width=50)
        e1.grid(row=1, columnspan=2)
        inputlabel2 = tk.Label(self.inputFrame, text='Enter parameter type:')
        inputlabel2.grid(row=2, columnspan=2) 
        e2 = tk.Entry(self.inputFrame, width=50)
        e2.grid(row=3, columnspan=2)
        def addParam():
            self.param = e1.get()
            self.paramType = e2.get()
            print(self.className + " " + self.method + " " + str(self.methodReturnType) + " " + self.param + " " + self.paramType)
            self.inputFrame.destroy()
            self.makeInputFrame()
            self.makeParamInputFrame()
        addParamButton = tk.Button(self.inputFrame, text='Add another parameter', command= lambda: addParam())
        addParamButton.grid(row=4, column=0)
        def output():
            # Error check here????
            self.param = e1.get()
            self.paramType = e2.get()
            print(self.className + " " + self.method + " " + str(self.methodReturnType) + " " + self.param + " " + self.paramType)
            remake()
        ok = tk.Button(self.inputFrame, text='Add and finish', command=lambda: output())
        ok.grid(row=4, column=1)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: remake())
        cancel.grid(row=4, column=2)

    def makeAddMethodFrame(self):
        inputlabel1 = tk.Label(self.inputFrame, text='Enter class name:')
        inputlabel1.grid(row=0, columnspan=2) 
        e1 = tk.Entry(self.inputFrame, width=50)
        e1.grid(row=1, columnspan=2)
        inputlabel2 = tk.Label(self.inputFrame, text='Enter method name:')
        inputlabel2.grid(row=2, columnspan=2) 
        e2 = tk.Entry(self.inputFrame, width=50)
        e2.grid(row=3, columnspan=2)
        inputlabel3 = tk.Label(self.inputFrame, text='Enter return type:')
        inputlabel3.grid(row=4, columnspan=2) 
        e3 = tk.Entry(self.inputFrame, width=50)
        e3.grid(row=5, columnspan=2)
        def addParam():
            self.className = e1.get()
            self.method = e2.get()
            self.methodReturnType = e3.get()
            self.inputFrame.destroy()
            self.makeInputFrame()
            self.makeParamInputFrame()
        
        addParamButton = tk.Button(self.inputFrame, text='Add method and parameter(s)', command= lambda : addParam())
        addParamButton.grid(row=6, column=0)
        
        def output():
            # Error check here????
            self.className = e1.get()
            self.method = e2.get()
            self.methodReturnType = e3.get()
            print(self.className + " " + self.method + " " + self.methodReturnType)
        ok = tk.Button(self.inputFrame, text='Add method no parameter(s)', command=lambda: output())
        ok.grid(row=6, column=1)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: remake())
        cancel.grid(row=6, column=2)

    def makeDeleteMethodFrame(self):
        inputlabel1 = tk.Label(self.inputFrame, text='Enter class name:')
        inputlabel1.grid(row=0, columnspan=2) 
        e1 = tk.Entry(self.inputFrame, width=50)
        e1.grid(row=1, columnspan=2)
        inputlabel2 = tk.Label(self.inputFrame, text='Enter method to delete:')
        inputlabel2.grid(row=2, columnspan=2) 
        e2 = tk.Entry(self.inputFrame, width=50)
        e2.grid(row=3, columnspan=2)
        def output():
            # Error check here????
            self.className = e1.get()
            self.method = e2.get()
            print(self.className + " " + self.method)
        ok = tk.Button(self.inputFrame, text='Delete method', command=lambda: output())
        ok.grid(row=4, column=0)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: remake())
        cancel.grid(row=4, column=1)

    def makeRenameMethodFrame(self):
        inputlabel1 = tk.Label(self.inputFrame, text='Enter class name:')
        inputlabel1.grid(row=0, columnspan=2) 
        e1 = tk.Entry(self.inputFrame, width=50)
        e1.grid(row=1, columnspan=2)
        inputlabel2 = tk.Label(self.inputFrame, text='Enter method to rename:')
        inputlabel2.grid(row=2, columnspan=2) 
        e2 = tk.Entry(self.inputFrame, width=50)
        e2.grid(row=3, columnspan=2)
        inputlabel3 = tk.Label(self.inputFrame, text='Enter new method name:')
        inputlabel3.grid(row=4, columnspan=2) 
        e3 = tk.Entry(self.inputFrame, width=50)
        e3.grid(row=5, columnspan=2)
        def output():
            # Error check here????
            self.className = e1.get()
            self.method = e2.get()
            self.methodNew = e3.get()
            print(self.className + " " + self.method + " " + self.methodNew)
        ok = tk.Button(self.inputFrame, text='Rename method', command=lambda: output())
        ok.grid(row=6, column=0)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: remake())
        cancel.grid(row=6, column=1)

    def makeAddParamFrame(self):        
        inputlabel1 = tk.Label(self.inputFrame, text='Enter class name:')
        inputlabel1.grid(row=0, columnspan=2) 
        e1 = tk.Entry(self.inputFrame, width=50)
        e1.grid(row=1, columnspan=2)
        inputlabel2 = tk.Label(self.inputFrame, text='Enter method name to add parameter(s):')
        inputlabel2.grid(row=2, columnspan=2) 
        e2 = tk.Entry(self.inputFrame, width=50)
        e2.grid(row=3, columnspan=2)
        def addParam():
            self.className = e1.get()
            self.method = e2.get()
            self.inputFrame.destroy()
            self.makeInputFrame()
            self.makeParamInputFrame()
        
        ok = tk.Button(self.inputFrame, text='Add parameter(s)', command=lambda: addParam())
        ok.grid(row=4, column=0)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: remake())
        cancel.grid(row=4, column=1)

    def makeParamDeleteInputFrame(self):
        inputlabel1 = tk.Label(self.inputFrame, text='Enter parameter name to delete:')
        inputlabel1.grid(row=0, columnspan=2) 
        e1 = tk.Entry(self.inputFrame, width=50)
        e1.grid(row=1, columnspan=2)
        def addParam():
            self.param = e1.get()
            print(self.className + " " + self.method + " " + self.param )
            self.inputFrame.destroy()
            self.makeInputFrame()
            self.makeParamDeleteInputFrame()
        addParamButton = tk.Button(self.inputFrame, text='Delete another parameter', command= lambda: addParam())
        addParamButton.grid(row=4, column=0)
        def output():
            # Error check here????
            self.param = e1.get()
            print(self.className + " " + self.method + " " + self.param )
            remake()
        ok = tk.Button(self.inputFrame, text='Delete and finish', command=lambda: output())
        ok.grid(row=4, column=1)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: remake())
        cancel.grid(row=4, column=2)

    def makeDeleteParamInputFrame(self):
        inputlabel1 = tk.Label(self.inputFrame, text='Enter parameter name:')
        inputlabel1.grid(row=0, columnspan=2) 
        e1 = tk.Entry(self.inputFrame, width=50)
        e1.grid(row=1, columnspan=2)
        def addParam():
            self.param = e1.get()
            print(self.className + " " + self.method + " " + self.param)
            self.inputFrame.destroy()
            self.makeInputFrame()
            self.makeParamDeleteInputFrame()
        addParamButton = tk.Button(self.inputFrame, text='Delete another parameter', command= lambda: addParam())
        addParamButton.grid(row=4, column=0)
        def output():
            # Error check here????
            self.param = e1.get()
            print(self.className + " " + self.method + " " + self.param )
            remake()
        ok = tk.Button(self.inputFrame, text='Delete and finish', command=lambda: output())
        ok.grid(row=4, column=1)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: remake())
        cancel.grid(row=4, column=2)

    def makeDeleteParamFrame(self):        
        inputlabel1 = tk.Label(self.inputFrame, text='Enter class name:')
        inputlabel1.grid(row=0, columnspan=2) 
        e1 = tk.Entry(self.inputFrame, width=50)
        e1.grid(row=1, columnspan=2)
        inputlabel2 = tk.Label(self.inputFrame, text='Enter method name to delete parameter(s):')
        inputlabel2.grid(row=2, columnspan=2) 
        e2 = tk.Entry(self.inputFrame, width=50)
        e2.grid(row=3, columnspan=2)
        def addParam():
            self.className = e1.get()
            self.method = e2.get()
            self.inputFrame.destroy()
            self.makeInputFrame()
            self.makeDeleteParamInputFrame()
        delete = tk.Button(self.inputFrame, text='Delete parameter(s)', command = lambda: addParam())
        delete.grid(row=4,column=0)
        def delAll():
            self.className = e1.get()
            self.method = e2.get()
            print("delete all: class " + self.className + " method " + self.method)
            remake()
        ok = tk.Button(self.inputFrame, text='Delete all parameters', command=lambda: delAll())
        ok.grid(row=4, column=1)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: remake())
        cancel.grid(row=4, column=2)
    
    def makeChangeParamInputFrame(self):
        inputlabel1 = tk.Label(self.inputFrame, text='Enter parameter name to change:')
        inputlabel1.grid(row=0, columnspan=2) 
        e1 = tk.Entry(self.inputFrame, width=50)
        e1.grid(row=1, columnspan=2)
        inputlabel2 = tk.Label(self.inputFrame, text='Enter new parameter name:')
        inputlabel2.grid(row=2, columnspan=2) 
        e2 = tk.Entry(self.inputFrame, width=50)
        e2.grid(row=3, columnspan=2)
        inputlabel3 = tk.Label(self.inputFrame, text='Enter new parameter type:')
        inputlabel3.grid(row=4, columnspan=2) 
        e3 = tk.Entry(self.inputFrame, width=50)
        e3.grid(row=5, columnspan=2)
        def addParam():
            self.param = e1.get()
            self.paramNew = e2.get()
            self.paramType = e3.get()
            print(self.className + " " + self.method + " " + self.param + " " + self.paramNew + " " + self.paramType)
            self.inputFrame.destroy()
            self.makeInputFrame()
            self.makeChangeParamInputFrame()
        addParamButton = tk.Button(self.inputFrame, text='Change another parameter', command= lambda: addParam())
        addParamButton.grid(row=6, column=0)
        def output():
            # Error check here????
            self.param = e1.get()
            self.paramNew = e2.get()
            self.paramType = e3.get()
            print(self.className + " " + self.method + " " + self.param + " " + self.paramNew + " " + self.paramType )
            remake()
        ok = tk.Button(self.inputFrame, text='Change and finish', command=lambda: output())
        ok.grid(row=6, column=1)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: remake())
        cancel.grid(row=6, column=2)
    
    def makeChangeParamFrame(self):
        inputlabel1 = tk.Label(self.inputFrame, text='Enter class name:')
        inputlabel1.grid(row=0, columnspan=2) 
        e1 = tk.Entry(self.inputFrame, width=50)
        e1.grid(row=1, columnspan=2)
        inputlabel2 = tk.Label(self.inputFrame, text='Enter method name to change parameter(s):')
        inputlabel2.grid(row=2, columnspan=2) 
        e2 = tk.Entry(self.inputFrame, width=50)
        e2.grid(row=3, columnspan=2)
        def addParam():
            self.className = e1.get()
            self.method = e2.get()
            self.inputFrame.destroy()
            self.makeInputFrame()
            self.makeChangeParamInputFrame()
        delete = tk.Button(self.inputFrame, text='Change parameter(s)', command = lambda: addParam())
        delete.grid(row=4,column=0)
        def delAll():
            self.className = e1.get()
            self.method = e2.get()
            print("delete all: class " + self.className + " method " + self.method)
            self.inputFrame.destroy()
            self.makeInputFrame()
            self.makeParamInputFrame()
        ok = tk.Button(self.inputFrame, text='Change all parameters', command=lambda: delAll())
        ok.grid(row=4, column=1)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: remake())
        cancel.grid(row=4, column=2)

    def makeListClassFrame(self):
        inputlabel1 = tk.Label(self.inputFrame, text='Enter Class name to list:')
        inputlabel1.grid(row=0, columnspan=2) 
        e1 = tk.Entry(self.inputFrame, width=50)
        e1.grid(row=1, columnspan=2)
        def output():
            # Error check here????
            self.className = e1.get()
            print(self.className)
        ok = tk.Button(self.inputFrame, text='List Class', command=lambda: output())
        ok.grid(row=4, column=0)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: remake())
        cancel.grid(row=4, column=1)            

def remake():
    view.inputFrame.destroy()
    view.makeInputFrame()

def wipe():
    view.inputFrame.destroy()
    view.makeInputFrame()

def updateRelationType():
    wipe()
    view.makeUpdateRelationType()

def addClassFrame():
    wipe()
    view.makeAddClassFrame()

def deleteClassFrame():
    wipe()
    view.makeDeleteClassFrame()

def renameClassFrame():
    wipe()
    view.makeRenameClassFrame()

def addRelationFrame():
    wipe()
    view.makeAddRelationFrame()

def deleteRelationFrame():
    wipe()
    view.makeDeleteRelationFrame()

def addFieldFrame():
    wipe()
    view.makeAddFieldFrame()

def deleteFieldFrame():
    wipe()
    view.makeDeleteFieldFrame()

def renameFieldFrame():
    wipe()
    view.makeRenameFieldFrame()

def addMethodFrame():
    wipe()
    view.makeAddMethodFrame()

def deleteMethodFrame():
    wipe()
    view.makeDeleteMethodFrame()

def renameMethodFrame():
    wipe()
    view.makeRenameMethodFrame()

def addParamFrame():
    wipe()
    view.makeAddParamFrame()

def deleteParamFrame():
    wipe()
    view.makeDeleteParamFrame()

def changeParamFrame():
    wipe()
    view.makeChangeParamFrame()

def listAllFrame():
    pass

def listClassFrame():
    wipe()
    view.makeListClassFrame()

def listRelationFrame():
    pass

def helpFrame():
    pass

view = View(None)
view.main()
