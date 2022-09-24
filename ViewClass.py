import tkinter as tk

class View(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
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
        self.geometry("800x600")
        self.title("UML Editor")
        self.makeButtonFrame()
        self.makeInputFrame()
        self.makeButtons()
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
        filemenu.add_command(label="Load", command= lambda : print("Call load function"))
        filemenu.add_command(label="Save", command= lambda : print("Call save function"))
        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        self.config(menu=menubar)
    
    def makeButtonFrame(self):
        self.buttonFrame = tk.Frame(self)
        self.buttonFrame.grid( row=0, column=0)

    def makeInputFrame(self):
        self.inputFrame = tk.Frame(self)
        self.inputFrame.grid( row=0, column=0)

    
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
        addParamButton = tk.Button(self.inputFrame, text='Delete another parameter', command= lambda: addParam())
        addParamButton.grid(row=6, column=0)
        def output():
            # Error check here????
            self.param = e1.get()
            self.paramNew = e2.get()
            self.paramType = e3.get()
            print(self.className + " " + self.method + " " + self.param + " " + self.paramNew + " " + self.paramType )
            remake()
        ok = tk.Button(self.inputFrame, text='Delete and finish', command=lambda: output())
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
    
    def makeButtons(self):
        
        addClassButton = tk.Button(self.buttonFrame, width=25, text="Add Class", command=lambda : addClassFrame())
        addClassButton.grid(row=0, column=0)

        deleteClassButton = tk.Button(self.buttonFrame, width=25, text="Delete Class", command=lambda : deleteClassFrame())
        deleteClassButton.grid(row=1, column=0)
        
        renameClassButton = tk.Button(self.buttonFrame,width=25, text="Rename Class", command=lambda : renameClassFrame())
        renameClassButton.grid(row=2, column=0)
        
        addRelationButton = tk.Button(self.buttonFrame,width=25, text="Add Relationship", command=lambda : addRelationFrame())
        addRelationButton.grid(row=3, column=0)
        
        deleteRelationButton = tk.Button(self.buttonFrame,width=25, text="Delete Relationship", command=lambda : deleteRelationFrame())
        deleteRelationButton.grid(row=4, column=0)
        
        addFieldButton = tk.Button(self.buttonFrame,width=25, text="Add Field", command= lambda : addFieldFrame())
        addFieldButton.grid(row=5, column=0)
        
        deleteFieldButton = tk.Button(self.buttonFrame,width=25, text="Delete Field", command= lambda : deleteFieldFrame())
        deleteFieldButton.grid(row=6, column=0)

        renameFieldButton = tk.Button(self.buttonFrame,width=25, text="Rename Field", command= lambda : renameFieldFrame())
        renameFieldButton.grid(row=7, column=0)
        
        addMethodButton = tk.Button(self.buttonFrame, width=25, text="Add Method", command= lambda : addMethodFrame())
        addMethodButton.grid(row=8, column=0)
        
        deleteMethodButton = tk.Button(self.buttonFrame, width=25, text="Delete Method", command= lambda : deleteMethodFrame())
        deleteMethodButton.grid(row=9, column=0)
        
        renameMethodButton = tk.Button(self.buttonFrame, width=25, text="Rename Method", command= lambda : renameMethodFrame())
        renameMethodButton.grid(row=10, column=0)
        
        addParameterButton = tk.Button(self.buttonFrame, width=25, text="Add Parameter(s)", command= lambda : addParamFrame())
        addParameterButton.grid(row=11, column=0)
        
        deleteParameterButton = tk.Button(self.buttonFrame, width=25, text="Delete Paramater(s)", command= lambda : deleteParamFrame())
        deleteParameterButton.grid(row=12, column=0)
        
        changeParameterButton = tk.Button(self.buttonFrame, width=25, text="Change Parameter(s)", command= lambda : changeParamFrame())
        changeParameterButton.grid(row=13, column=0)
        
        listClassesButton = tk.Button(self.buttonFrame, width=25, text="List Classes", command= lambda : print("Print all classes to screen"))
        listClassesButton.grid(row=14, column=0)
        
        listClassButton = tk.Button(self.buttonFrame,width=25, text="List Class", command= lambda : listClassFrame())
        listClassButton.grid(row=15, column=0)
        
        listRelationButton = tk.Button(self.buttonFrame,width=25, text="List Relationships", command= lambda : print("Print relationships to screen"))
        listRelationButton.grid(row=16, column=0)
        
        helpButton = tk.Button(self.buttonFrame,width=25, text="Help", command= lambda : print("print help menu to screen"))
        helpButton.grid(row=17, column=0)


def remake():
    view.inputFrame.destroy()
    view.makeButtonFrame()
    view.makeButtons()

def wipe():
    view.buttonFrame.destroy()
    view.makeInputFrame()

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
