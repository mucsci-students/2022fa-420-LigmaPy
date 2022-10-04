"""
Author(s)   : Trevor Bender and Aaron Heinbaugh
Filename    : View.py
Description : Constructs and displays the gui
"""

from cgitb import text
import tkinter as tk
#import UMLNotebook as notebook
from tkinter import RIGHT, VERTICAL, Y, OptionMenu, StringVar, ttk, filedialog


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
        self.fileName = None
        self.geometry("800x600")
        self.title("UML Editor")
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        # Sets the size of the window
        self.geometry(f"{screenWidth}x{screenHeight}")
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        self.makeOutputFrame()
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
        # File menu
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command= lambda : self.controller.clickLoadButton())
        filemenu.add_command(label="Save", command= lambda : self.controller.clickSaveButton())
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        # Help menu
        #helpmenu = tk.Menu(menubar, tearoff=0)
        #helpmenu.add_command(label="Commands", command=None)
        #menubar.add_cascade(label="Help", menu=helpmenu)
        # List menu
        listmenu = tk.Menu(menubar,tearoff=0)
        listmenu.add_command(label="List class", command = lambda : self.listClassFrame())
        listmenu.add_command(label="List all classes", command = lambda : self.controller.clickListAllClassesButton())
        listmenu.add_command(label="List Relationships", command= lambda : self.controller.clickListRelationsButton())
        listmenu.add_command(label="Clear", command= lambda : self.clearScreen())
        menubar.add_cascade(label="List", menu=listmenu)
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
                ttk.Button(frame, width=20, text="Add class", command=lambda : self.addClassFrame()).grid(row=0, column=0, pady=10, padx=5)
                ttk.Button(frame, width=20, text="Delete class", command= lambda : self.deleteClassFrame()).grid(row=0, column=1, pady=10)
                ttk.Button(frame, width=20, text="Rename class", command=lambda : self.renameClassFrame()).grid(row=0, column=2, pady=10, padx=5)
            
            classTabContents(classTab)
            # Relationship tab
            relationTab = tk.Frame(master=tabControl, bg='#bcade0')
            tabControl.add(relationTab, text=f'{"Relationship":^20s}')
            
            
            def relationTabContents(frame : ttk.Frame):
                """
                    Adds buttons for relationship commands to parent "frame"
                """
                ttk.Button(frame, width=20, text="Add relationship", command= lambda : self.addRelationFrame()).grid(row=0, column=0, pady=10, padx=5)
                ttk.Button(frame, width=20, text="Delete relationship", command= lambda : self.deleteRelationFrame()).grid(row=0, column=1, pady=10)
                ttk.Button(frame, width=20, text="Update type", command= lambda : self.updateRelationType()).grid(row=0, column=2, pady=10, padx=5)   
            
            relationTabContents(relationTab)
            # Field tab
            fieldTab = tk.Frame(master=tabControl, bg='#bcade0')
            tabControl.add(fieldTab, text=f'{"Field":^20s}')
            
            def fieldTabContent(frame : ttk.Frame):
                """
                    Adds buttons for field commands to parent "frame"
                """
                ttk.Button(frame, width=20, text="Add field", command= lambda : self.addFieldFrame()).grid(row=0, column=0, pady=10, padx=5)
                ttk.Button(frame, width=20, text="Delete field", command= lambda : self.deleteFieldFrame()).grid(row=0, column=1, pady=10)
                ttk.Button(frame, width=20, text="Rename field", command= lambda : self.renameFieldFrame()).grid(row=0, column=2, pady=10, padx=5)
            
            fieldTabContent(fieldTab)
            # Method tab
            methTab = tk.Frame(master=tabControl, bg='#bcade0')
            tabControl.add(methTab, text=f'{"Method":^20s}')
            
            def methodTabContent(frame : ttk.Frame):
                """
                    Adds buttons for method commands to parent "frame"
                """
                ttk.Button(frame, width=20, text="Add method", command= lambda : self.addMethodFrame()).grid(row=0, column=0, pady=10, padx=5)
                ttk.Button(frame, width=20, text="Delete method", command= lambda : self.deleteMethodFrame()).grid(row=0, column=1, pady=10)
                ttk.Button(frame, width=20, text="Update method", command= lambda : self.renameMethodFrame()).grid(row=0, column=2, pady=10, padx=5)
            
            methodTabContent(methTab)
            # Parameter tab
            paramTab = tk.Frame(master=tabControl, bg='#bcade0')
            tabControl.add(paramTab, text=f'{"Parameter":^20s}')
            
            def parameterTabContents(frame : ttk.Frame):
                """
                    Adds buttons for parameter commands to parent "frame"
                """
                ttk.Button(frame, width=20, text="Add parameter(s)", command= lambda : self.addParamFrame()).grid(row=0, column=0, pady=10, padx=5)
                ttk.Button(frame, width=20, text="Delete parameter(s)", command= lambda : self.deleteParamFrame()).grid(row=0, column=1, pady=10)
                ttk.Button(frame, width=20, text="Change parameter(s)", command= lambda : self.changeParamFrame()).grid(row=0, column=2, pady=10, padx=5) 
            
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
        self.canvas = tk.Canvas(self.outputFrame, bg='white')
        self.outputFrame.grid(row=0, column=1, sticky="nswe", rowspan=2)
        self.outputFrame.rowconfigure(0, weight=1)
        self.outputFrame.columnconfigure(1, weight=1)
        self.canvas.pack(fill=tk.BOTH, expand=1)
        self.canvas.grid(row=0, column=1, sticky="nswe", rowspan=2)
        self.makeScrollBar()

   #creates the output message label below the input
    def makeMessage(self, message):
        self.message = tk.Label(self.inputFrame, text = message)
        self.message.grid(row=8, column=0, columnspan=3)
    
    #creates the scrollbar
    def makeScrollBar(self):
        self.scrollbar = ttk.Scrollbar(self.outputFrame, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.grid(row=0, column=2, sticky="nswe")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion = self.canvas.bbox("all")))
        self.outputFrame2 = tk.Frame(self.canvas)
        self.canvas.create_window((0,0), window=self.outputFrame2, anchor="nw")        
   
   #refreshes canvas and prints the 'UMLclass' in a nice format to the canvas  
    def printClassToCanvas(self, UMLclass):
        self.canvas.destroy()
        self.scrollbar.destroy()
        self.canvas = tk.Canvas(self.outputFrame, bg='white')
        t = classToString(UMLclass)
        self.canvas.create_text(100, 100, text= t, fill="black", font=('Helvetica 10 bold'))
        self.canvas.grid(row=0, column=1, sticky="nswe", rowspan=2)    
        self.makeScrollBar()

    #clears canvas on right and input window on left
    def clearScreen(self):
        self.outputFrame.destroy()
        self.makeOutputFrame()
        self.remake()

    # refreshes the canvase and prints the list of class to the canvas 
    def printAllClassesToCanvas(self, list):
        self.canvas.destroy()
        self.scrollbar.destroy()
        self.canvas = tk.Canvas(self.outputFrame, bg='white')
        t = ''
        for c in list:
            t += classToString(c)
        self.canvas.create_text(100, 500, text= t, fill="black", font=('Helvetica 10 bold'))
        self.canvas.grid(row=0, column=1, sticky="nswe", rowspan=2)  
        self.makeScrollBar()

    #refreshs the canvas and prints the list of relationships to the canvas
    def printRelationsToCanvase(self, list):
        self.canvas.destroy()
        self.scrollbar.destroy()
        self.canvas = tk.Canvas(self.outputFrame, bg='white')
        t = ''
        for r in list:
            t += relationToString(r)
        self.canvas.create_text(100, 500, text= t, fill="black", font=('Helvetica 10 bold'))
        self.canvas.grid(row=0, column=1, sticky="nswe", rowspan=2)  
        self.makeScrollBar()
    
    def save(self):
        self.fileName = filedialog.asksaveasfilename(title="Open File", filetypes=[("JSON File", "*.json")])
        
    def load(self):
        self.fileName = filedialog.askopenfilename(title="Open File", filetypes=[("JSON File", "*.json")])
        
    """
    Instead of making comments for each and every input frame:
    See makeUpdateRelationType below and apply those comments to every other makeXXXXX(self) function
    The name of the function describes what frame will be made when called
    """
    
    #creates the frame to update relations after clicking said button
    def makeUpdateRelationType(self):
        #creates text above input entry
        inputlabel1 = tk.Label(self.inputFrame, text='Enter source name:')
        inputlabel1.grid(row=0, columnspan=2) 
        #creates the first input entry
        e1 = tk.Entry(self.inputFrame, width=50)
        e1.grid(row=1, columnspan=2)
        #creates text above 2nd entry 
        inputlabel2 = tk.Label(self.inputFrame, text='Enter destination name:')
        inputlabel2.grid(row=2, columnspan=2) 
        #creates 2nd input entry
        e2 = tk.Entry(self.inputFrame, width=50)
        e2.grid(row=3, columnspan=2)
        #creates text above 3rd entry
        inputlabel3 = tk.Label(self.inputFrame, text='Enter new relationship type:')
        inputlabel3.grid(row=4, columnspan=2) 
        #creates a variable for the drop down selector
        clicked = StringVar()
        clicked.set("Aggregation")
        #creates the drop down selector
        drop = OptionMenu(self.inputFrame, clicked, "Aggregation", "Composition", "Inheritance", "Realization") 
        drop.grid(row=5, columnspan=2)
        #function to output to the controller 
        def output():
            #gets e1, e2, and clicked variable from above and sets the appropriate class variable
            self.source = e1.get()
            self.destination = e2.get()
            self.relationshipTypeNew = clicked.get()
            self.controller.clickUpdateTypeButton()
        #creates first button and when clicked calls the output function above to set the class variables.
        ok = tk.Button(self.inputFrame, text='Change type', command=lambda: output())
        ok.grid(row=6, column=0)
        #creates 2nd button and when clicked calls remake to clear the screen and remake and empty input frame.
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
        cancel.grid(row=6, column=1)  


    #creates the add class frame upon clicking add class
    def makeAddClassFrame(self):
        inputlabel1 = tk.Label(self.inputFrame, text='Enter Class name to add')
        inputlabel1.grid(row=0, columnspan=2) 
        e1 = tk.Entry(self.inputFrame, width=50)
        e1.grid(row=1, columnspan=2)
        def output():
            self.className = e1.get()
            self.controller.clickAddClassButton()
        ok = tk.Button(self.inputFrame, text='Add Class', command=lambda: output())
        ok.grid(row=4, column=0)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
        cancel.grid(row=4, column=1)
       

    def makeDeleteClassFrame(self):
        inputlabel1 = tk.Label(self.inputFrame, text='Enter Class name to delete')
        inputlabel1.grid(row=0, columnspan=2) 
        e1 = tk.Entry(self.inputFrame, width=50)
        e1.grid(row=1, columnspan=2)
        def output():
            self.className = e1.get()
            self.controller.clickDeleteClassButton()
        ok = tk.Button(self.inputFrame, text='Delete Class', command=lambda: output())
        ok.grid(row=4, column=0)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
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
            self.className = e1.get()
            self.classNameNew = e2.get()
            self.controller.clickRenameClassButton()
        ok = tk.Button(self.inputFrame, text='Rename Class', command=lambda: output())
        ok.grid(row=4, column=0)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
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
        inputlabel3 = tk.Label(self.inputFrame, text='Select relationship type:')
        inputlabel3.grid(row=4, columnspan=2)
        clicked = StringVar()
        clicked.set("Aggregation")
        drop = OptionMenu(self.inputFrame, clicked, "Aggregation", "Composition", "Inheritance", "Realization") 
        drop.grid(row=5, columnspan=2)
        def output():
            self.source = e1.get()
            self.destination = e2.get()
            self.relationshipType = clicked.get()
            self.controller.clickAddRelationButton()
        ok = tk.Button(self.inputFrame, text='Add Relationship', command=lambda: output())
        ok.grid(row=6, column=0)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
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
            self.source = e1.get()
            self.destination = e2.get()
            self.controller.clickDeleteRelationButton()
        ok = tk.Button(self.inputFrame, text='Delete relationship', command=lambda: output())
        ok.grid(row=4, column=0)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
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
            self.className = e1.get()
            self.field = e2.get()
            self.fieldType = e3.get()
            self.controller.clickAddFieldButton()
        ok = tk.Button(self.inputFrame, text='Add Field', command=lambda: output())
        ok.grid(row=6, column=0)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
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
            self.className = e1.get()
            self.field = e2.get()
            self.controller.clickDeleteFieldButton()
        ok = tk.Button(self.inputFrame, text='Delete field', command=lambda: output())
        ok.grid(row=4, column=0)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
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
            self.className = e1.get()
            self.field = e2.get()
            self.feildNew = e3.get()
            self.controller.clickRenameFieldButton()
        ok = tk.Button(self.inputFrame, text='Rename Field', command=lambda: output())
        ok.grid(row=6, column=0)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
        cancel.grid(row=6, column=1)

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
            self.controller.clickAddParamButton()
        addParamButton = tk.Button(self.inputFrame, text='Add parameter', command= lambda: addParam())
        addParamButton.grid(row=4, column=0)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
        cancel.grid(row=4, column=1)

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
            self.controller.clickAddMethodAndParamsButton()
        addParamButton = tk.Button(self.inputFrame, text='Add method and parameter(s)', command= lambda : addParam())
        addParamButton.grid(row=6, column=0)
        
        def output():
            self.className = e1.get()
            self.method = e2.get()
            self.methodReturnType = e3.get()
            self.controller.clickAddMethodWithoutParamsButton()
        ok = tk.Button(self.inputFrame, text='Add method no parameter(s)', command=lambda: output())
        ok.grid(row=6, column=1)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
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
            self.className = e1.get()
            self.method = e2.get()
            self.controller.clickDeleteMethodButton()
        ok = tk.Button(self.inputFrame, text='Delete method', command=lambda: output())
        ok.grid(row=4, column=0)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
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
            self.className = e1.get()
            self.method = e2.get()
            self.methodNew = e3.get()
            self.controller.clickUpdateMethodButton()
        ok = tk.Button(self.inputFrame, text='Rename method', command=lambda: output())
        ok.grid(row=6, column=0)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
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
            self.controller.clickAddParamToMethodButton()        
        ok = tk.Button(self.inputFrame, text='Add parameter(s)', command=lambda: addParam())
        ok.grid(row=4, column=0)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
        cancel.grid(row=4, column=1)

    def makeParamDeleteInputFrame(self):
        inputlabel1 = tk.Label(self.inputFrame, text='Enter parameter name to delete:')
        inputlabel1.grid(row=0, columnspan=2) 
        e1 = tk.Entry(self.inputFrame, width=50)
        e1.grid(row=1, columnspan=2)
        def addParam():
            self.param = e1.get()
            self.inputFrame.destroy()
            self.makeInputFrame()
            self.makeParamDeleteInputFrame()
        addParamButton = tk.Button(self.inputFrame, text='Delete another parameter', command= lambda: addParam())
        addParamButton.grid(row=4, column=0)
        def output():
            self.param = e1.get()
            self.remake()
        ok = tk.Button(self.inputFrame, text='Delete and finish', command=lambda: output())
        ok.grid(row=4, column=1)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
        cancel.grid(row=4, column=2)

    def makeDeleteParamInputFrame(self):
        inputlabel1 = tk.Label(self.inputFrame, text='Enter parameter name:')
        inputlabel1.grid(row=0, columnspan=2) 
        e1 = tk.Entry(self.inputFrame, width=50)
        e1.grid(row=1, columnspan=2)
        def addParam():
            self.param = e1.get()
            self.controller.clickSecondDeleteParamButton()
        addParamButton = tk.Button(self.inputFrame, text='Delete parameter(s)', command= lambda: addParam())
        addParamButton.grid(row=4, column=0)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
        cancel.grid(row=4, column=1)

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
            self.controller.clickDeleteParamButton()
        delete = tk.Button(self.inputFrame, text='Delete parameter(s)', command = lambda: addParam())
        delete.grid(row=4,column=0)
        def delAll():
            self.className = e1.get()
            self.method = e2.get()
            self.controller.clickDeleteAllParamButton()
        ok = tk.Button(self.inputFrame, text='Delete all parameters', command=lambda: delAll())
        ok.grid(row=4, column=1)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
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
            self.paramTypeNew = e3.get()
            self.controller.clickChangeAnotherParamButton()
        addParamButton = tk.Button(self.inputFrame, text='Change parameter(s)', command= lambda: addParam())
        addParamButton.grid(row=6, column=0)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
        cancel.grid(row=6, column=1)
    
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
            self.controller.clickChangeParamButton()
        delete = tk.Button(self.inputFrame, text='Change parameter(s)', command = lambda: addParam())
        delete.grid(row=4,column=0)
        def delAll():
            self.className = e1.get()
            self.method = e2.get()
            self.controller.clickChangeAllParamButton()
        ok = tk.Button(self.inputFrame, text='Change all parameters', command=lambda: delAll())
        ok.grid(row=4, column=1)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
        cancel.grid(row=4, column=2)

    def makeListClassFrame(self):
        inputlabel1 = tk.Label(self.inputFrame, text='Enter Class name to list:')
        inputlabel1.grid(row=0, columnspan=2) 
        e1 = tk.Entry(self.inputFrame, width=50)
        e1.grid(row=1, columnspan=2)
        def output():
            self.className = e1.get()
            self.controller.clickListClassButton()
        ok = tk.Button(self.inputFrame, text='List Class', command=lambda: output())
        ok.grid(row=4, column=0)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
        cancel.grid(row=4, column=1)            

    def remake(self):
        self.inputFrame.destroy()
        self.makeInputFrame()

    def addClassFrame(self):
        self.wipe()
        self.makeAddClassFrame()

    def updateRelationType(self):
        self.wipe()
        self.makeUpdateRelationType()

    def deleteClassFrame(self):
        self.wipe()
        self.makeDeleteClassFrame()

    def renameClassFrame(self):
        self.wipe()
        self.makeRenameClassFrame()

    def addRelationFrame(self):
        self.wipe()
        self.makeAddRelationFrame()

    def deleteRelationFrame(self):
        self.wipe()
        self.makeDeleteRelationFrame()

    def addFieldFrame(self):
        self.wipe()
        self.makeAddFieldFrame()

    def deleteFieldFrame(self):
        self.wipe()
        self.makeDeleteFieldFrame()

    def renameFieldFrame(self):
        self.wipe()
        self.makeRenameFieldFrame()

    def addMethodFrame(self):
        self.wipe()
        self.makeAddMethodFrame()

    def deleteMethodFrame(self):
        self.wipe()
        self.makeDeleteMethodFrame()

    def renameMethodFrame(self):
        self.wipe()
        self.makeRenameMethodFrame()

    def addParamFrame(self):
        self.wipe()
        self.makeAddParamFrame()

    def deleteParamFrame(self):
        self.wipe()
        self.makeDeleteParamFrame()

    def changeParamFrame(self):
        self.wipe()
        self.makeChangeParamFrame()

    def listClassFrame(self):
        self.wipe()
        self.makeListClassFrame()

    def helpFrame(self):
        pass
    
    def wipe(self):
        self.inputFrame.destroy()
        self.makeInputFrame()

#returns a class 'c' in a string format for output
def classToString(c):
    string = ''
    string += "Class: " + c.name + "\n"
    string += "\n    Fields:\n"
    for each in c.fields:
        string += "        " + str(each.type) + " " + each.name + "\n"
    string += "\n    Methods:\n"
    for each in c.methods:
        parameters = ""
        if len(each.params) > 0:  
            for param in each.params:
                parameters += str(param.type) + " " + param.name + ", "
        parameters = parameters[:-2] 
        string += "        " + str(each.return_type) + " " + each.name + "(" + parameters + ")\n"
    string += "\n"
    return string

# returns a relationship 'r' in a string format for output
def relationToString(r):
    string = ""
    string += "Relationship:\n"
    string += "    Source: " + r.source + "\n"
    string += "    Destination: " + r.destination + "\n"
    string += "    Type: " + r.type + "\n\n"
    return string

"""
#for testing
def printClass (c):
    print(f"Class:  {c.name}\n")
    print(f"Fields:")
    for each in c.fields:
        print(f"{each.type} {each.name}")
    print()
    print("Methods:")
    for each in c.methods:
        parameters = ""
        if len(each.params) > 0:  
            for param in each.params:
                parameters += param.type + " " + param.name + ", "
        parameters = parameters[:-2] 
        print(f"{each.return_type} {each.name}({parameters})")
    print()
"""
