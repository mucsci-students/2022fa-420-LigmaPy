"""
Author(s)   : Trevor Bender and Aaron Heinbaugh
Filename    : View.py
Description : Constructs and displays the gui
"""



import tkinter as tk
#import UMLNotebook as notebook
from tkinter import LEFT, RIGHT, VERTICAL, Y, Canvas, OptionMenu, StringVar, ttk, filedialog

import model.UMLClass as u
import model.relationship as r
import model.attributes as a
import math



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
        self.canvasSizeX = 2000
        self.canvasSizeY = 2000
        self.title("UML Editor")
        #screenWidth = self.winfo_screenwidth() - 100
        #screenHeight = self.winfo_screenheight() - 100
        # Sets the size of the window
        self.state('zoomed')
        #self.geometry(f"{screenWidth}x{screenHeight}")
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        self.makeOutputFrame()
        self.makeButtonFrame()
        self.makeInputFrame()
        #self.makeButtons()
        self.makeMenu()
        
    #resets all the class variables
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
    
    #creates the file and list menus
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
        #listmenu = tk.Menu(menubar,tearoff=0)
        #listmenu.add_command(label="List class", command = lambda : self.listClassFrame())
        #listmenu.add_command(label="List all classes", command = lambda : self.controller.clickListAllClassesButton())
        #listmenu.add_command(label="List Relationships", command= lambda : self.controller.clickListRelationsButton())
        #listmenu.add_command(label="Clear", command= lambda : self.clearScreen())
        #menubar.add_cascade(label="List", menu=listmenu)
        self.config(menu=menubar)

    #creates all the button in the top left
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
        #self.buttonFrame.pack(side = LEFT, fill=Y)
    #creates input frame on bottom right to put in input fields 
    def makeInputFrame(self):
        #self.inputFrame = tk.Frame(self)
        #self.inputFrame.grid(row = 1, column=0)
        self.inputFrame = tk.Frame(self.buttonFrame)
        self.inputFrame.grid(row = 0, column=0)

    #creates canvas for output on right side
    def makeOutputFrame(self):
        self.outputFrame = tk.Frame(self)
        self.outputFrame.grid(row=0, column=1, sticky="nswe", rowspan=2)
        self.outputFrame.rowconfigure(0, weight=1)
        self.outputFrame.columnconfigure(1, weight=1)
        self.canvas = tk.Canvas(self.outputFrame, bg='white', scrollregion=(0, 0, self.canvasSizeX, self.canvasSizeY))
        #self.outputFrame.pack(side = RIGHT, fill=Y)
        self.makeScrollBar()
        self.canvas.pack(fill=tk.BOTH, expand=tk.YES)
        #self.canvas.grid(row=0, column=1, sticky="nswe", rowspan=2)
       

   #creates the output message label below the input
    def makeMessage(self, message):
        self.message = tk.Label(self.inputFrame, text = message)
        self.message.grid(row=8, column=0, columnspan=3)
    
    #creates the scrollbar
    def makeScrollBar(self):
        self.canvas_frame = tk.Frame(self.canvas)
        self.scrollbar = tk.Scrollbar(self.outputFrame, orient=tk.VERTICAL, command=self.canvas.yview)
        #self.scrollbar.grid(row=0, column=2, sticky="nswe")
        self.scrollbar.pack(fill = tk.Y, side = tk.RIGHT)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion = self.canvas.bbox("all")))
        #self.outputFrame2 = tk.Frame(self.canvas)
        #self.canvas.create_window((0,0), window=self.outputFrame2, anchor="nw")        
        #self.canvas.create_window((0, 0), window=self.canvas_frame, anchor='nw')
        #self.canvas_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion = self.canvas.bbox("all"),width=self.canvasSizeX,height=self.canvasSizeY))

    #prints the 'UMLclass' in a nice box to the canvas
    def printClassToCanvas(self, UMLClass):
        #gets the text, width and heigth as tuple(t,w,h)
        t = classToString(UMLClass)
        
        lowercaseName = UMLClass.name.lower()

        #holders to recreate lines
        sourceList = []
        destList = []
        
        #checks if a box / relation exists and deletes the line and box so they can be remade
        if lowercaseName in UMLBoxes:
            for each in list(UMLLines):
                if UMLBoxes[lowercaseName] in each:
                    if each.index(UMLBoxes[lowercaseName]) == 0:
                        destList.append(each[1])
                        self.deleteLine(each[0].winfo_name(), each[1].winfo_name())
                    else:
                        sourceList.append(each[0])
                        self.deleteLine(each[0].winfo_name(), each[1].winfo_name())
            self.removeClassFromCanvas(lowercaseName)
        
        #makes/remakes boxes using tuple above
        UMLBoxes[lowercaseName] = tk.Label(self.canvas, text=t[0], height=t[1], width=t[2], borderwidth=1, relief="solid", justify=LEFT, name = lowercaseName)
        #UMLBoxes[lowercaseName].place(x=UMLClass.location['x'], y=UMLClass.location['y'])
        #binds boxes to drag and drop event
        UMLBoxes[lowercaseName].bind("<Button-1>", self.dragStart)
        UMLBoxes[lowercaseName].bind("<B1-Motion>", self.dragMove)
        
        self.canvas.create_window((UMLClass.location['x'],UMLClass.location['y']), window=UMLBoxes[lowercaseName])
        #remakes the line with the new label if a relationship existed
        for each in sourceList:
            self.makeLine(each.winfo_name(), UMLBoxes[lowercaseName].winfo_name())
        for each in destList:
            self.makeLine(UMLBoxes[lowercaseName].winfo_name(), each.winfo_name())

        

    def printRenamedClassToCanvas(self, UMLclass, UMLold):
        #gets the text, width and heigth as tuple(t,w,h)
        new = classToString(UMLclass)
        #holders to recreate lines
        lowercaseName = UMLclass.name.lower()
        
        sourceList = []
        destList = []
        
        #checks if a box / relation exists and deletes the line and box so they can be remade
        if UMLold.lower() in UMLBoxes:
            for each in list(UMLLines):
                if UMLBoxes[UMLold.lower()] in each:
                    if each.index(UMLBoxes[UMLold.lower()]) == 0:
                        destList.append(each[1])
                        self.deleteLine(each[0].winfo_name(), each[1].winfo_name())
                    else:
                        sourceList.append(each[0])
                        self.deleteLine(each[0].winfo_name(), each[1].winfo_name())
            self.removeClassFromCanvas(UMLold.lower())
        
        #makes/remakes boxes using tuple above
        UMLBoxes[lowercaseName] = tk.Label(self.canvas, text=new[0], height=new[1], width=new[2], borderwidth=1, relief="solid", justify=LEFT, name = lowercaseName)
        #UMLBoxes[lowercaseName].place(x=UMLclass.location['x'], y=UMLclass.location['y'])
        self.canvas.create_window((UMLclass.location['x'],UMLclass.location['y']), window=UMLBoxes[lowercaseName])
        #binds boxes to drag and drop event
        UMLBoxes[lowercaseName].bind("<Button-1>", self.dragStart)
        UMLBoxes[lowercaseName].bind("<B1-Motion>", self.dragMove)
        
        #remakes the line with the new label if a relationship existed
        for each in sourceList:
            self.makeLine(each.winfo_name(), UMLBoxes[lowercaseName].winfo_name())
        for each in destList:
            self.makeLine(UMLBoxes[lowercaseName].winfo_name(), each.winfo_name())


        
    #delete class box from canvas and any relationship lines dependant on the box    
    def removeClassFromCanvas(self, UMLclass):
        #deletes and relation lines linked to box
        if UMLclass.lower() in UMLBoxes:
            for each in list(UMLLines):
                if UMLBoxes[UMLclass.lower()] in each:
                    self.deleteLine(each[0].winfo_name(), each[1].winfo_name())
        #deletes the box and removes it from the dict
        UMLBoxes[UMLclass.lower()].destroy()
        del UMLBoxes[UMLclass.lower()]    

    #makes the relationship lines and adds them to a dictionary
    def makeLine(self, s, d):
        #updates the canvas to make the winfo calls accurate
        self.canvas.update()
        #gets the boxes
        source = UMLBoxes[s.lower()]
        dest = UMLBoxes[d.lower()]
        #gets x and y coords for source box (top left corner)
        sXCoord = source.winfo_x()
        sYCoord = source.winfo_y()
        #gets x and y coords for dest box (top left corner)
        dXCoord = dest.winfo_x()
        dYCoord = dest.winfo_y()
        #gets the width and heigth of the source box
        sWidth = source.winfo_reqwidth()
        sHeight = source.winfo_reqheight()
        #gets the width and heigth of the dest box
        dWidth = dest.winfo_reqwidth()
        dHeight = dest.winfo_reqheight()

        # finds the type of the relationship
        index = r.findRelationship(s, d)
        print(index)
        type = r.relationIndex[index].type

        #gets the center coord of the source where the line starts
        sCenterCoord = (sXCoord + sWidth//2, sYCoord + sHeight //2)
        #gets the topmid, leftmid, rightmid, and bottommid coord of dest (we can change these if needed)
        #one of these (the closest to the center above) is where the line will end
        dTopCoord = (dXCoord + dWidth//2, dYCoord)
        dLeftCoord = (dXCoord, dYCoord + dHeight//2)
        dRightCoord = (dXCoord + dWidth, dYCoord + dHeight//2)
        dBottomCoord = (dXCoord + dWidth//2, dYCoord + dHeight)
        dTopRight = (dXCoord, dYCoord)
        dTopLeft = (dXCoord + dWidth, dYCoord)
        dBottomRight = (dXCoord, dYCoord + dHeight )
        dBottomLeft = (dXCoord + dWidth, dYCoord + dHeight)


        #determines the closest coord from above
        closest = []
        closest.append(math.dist(sCenterCoord,dTopCoord))
        closest.append(math.dist(sCenterCoord,dLeftCoord))
        closest.append(math.dist(sCenterCoord,dRightCoord))
        closest.append(math.dist(sCenterCoord,dBottomCoord))

        closest.append(math.dist(sCenterCoord,dTopRight))
        closest.append(math.dist(sCenterCoord,dTopLeft))
        closest.append(math.dist(sCenterCoord,dBottomRight))
        closest.append(math.dist(sCenterCoord,dBottomLeft))

        # determines color of arrow from relationship type
        if type == "Aggregation":
            color = "red"
        elif type == "Composition":
            color = "blue"
        elif type == "Inheritance":
            color = "green"
        else: 
            color = "purple"

        #creates the line to closest point and add it to the list
        minpos = closest.index(min(closest))
        if minpos == 0:
            UMLLines[(source, dest)] = self.canvas.create_line(sCenterCoord[0],sCenterCoord[1],dTopCoord[0],dTopCoord[1], width=3, arrow=tk.LAST, fill=color)
        if minpos == 1:
            UMLLines[(source, dest)] = self.canvas.create_line(sCenterCoord[0],sCenterCoord[1],dLeftCoord[0],dLeftCoord[1], width=3, arrow=tk.LAST, fill=color)
        if minpos == 2:
            UMLLines[(source, dest)] = self.canvas.create_line(sCenterCoord[0],sCenterCoord[1],dRightCoord[0],dRightCoord[1], width=3, arrow=tk.LAST, fill=color)
        if minpos == 3:
            UMLLines[(source, dest)] = self.canvas.create_line(sCenterCoord[0],sCenterCoord[1],dBottomCoord[0],dBottomCoord[1], width=3, arrow=tk.LAST, fill=color)
        if minpos == 4:
            UMLLines[(source, dest)] = self.canvas.create_line(sCenterCoord[0],sCenterCoord[1],dTopRight[0],dTopRight[1], width=3, arrow=tk.LAST, fill=color)
        if minpos == 5:
            UMLLines[(source, dest)] = self.canvas.create_line(sCenterCoord[0],sCenterCoord[1],dTopLeft[0],dTopLeft[1], width=3, arrow=tk.LAST, fill=color)            
        if minpos == 6:
            UMLLines[(source, dest)] = self.canvas.create_line(sCenterCoord[0],sCenterCoord[1],dBottomRight[0],dBottomRight[1], width=3, arrow=tk.LAST, fill=color)    
        if minpos == 7:
            UMLLines[(source, dest)] = self.canvas.create_line(sCenterCoord[0],sCenterCoord[1],dBottomLeft[0],dBottomLeft[1], width=3, arrow=tk.LAST, fill=color)
    

    #delete a line and removes it from the list
    def deleteLine(self, s, d):
        source = UMLBoxes[s.lower()]
        dest = UMLBoxes[d.lower()]
        self.canvas.delete(UMLLines[(source, dest)])
        del UMLLines[(source, dest)]

    #clears canvas on right and input window on left
    def clearScreen(self):
        self.outputFrame.destroy()
        self.makeOutputFrame()
        self.remake()

    # refreshes the canvas and prints the list of class to the canvas 
    def printAllClassesToCanvas(self, list):
        self.canvas.destroy()
        self.scrollbar.destroy()
        self.canvas = tk.Canvas(self.outputFrame, bg='white')
        t = ''
        for c in list:
            t += classToString(c)[0]
        self.canvas.create_text(100, 500, text= t, fill="black", font=('Helvetica 10 bold'))
        self.makeScrollBar()
        self.canvas.grid(row=0, column=1, sticky="nswe", rowspan=2)  
        

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
        self.fileName = filedialog.asksaveasfilename(title="Open File", initialdir="UMLsavefiles",  filetypes=[("JSON File", "*.json")])
 
    def load(self):
        self.fileName = filedialog.askopenfilename(title="Open File", initialdir="UMLsavefiles", filetypes=[("JSON File", "*.json")])
        
    """
    Instead of making comments for each and every input frame (bottom left box in GUI):
    See makeUpdateRelationType and makeDeleteFieldFrame below and apply their comments to every other makeXXXXX(self) function
    The name of the function describes what frame will be made when called
    """
    
    #creates the frame to update relations after clicking said button
    def makeUpdateRelationType(self):
        #checks if any relationships exist and alerts user if no
        if len(r.relationIndex) == 0:
            #creates alert message
            inputlabel1 = tk.Label(self.inputFrame, text='Not enough relationships exist', width=30)
            inputlabel1.grid(row=0)
            #button to close alert message above
            cancel = tk.Button(self.inputFrame, text='Close', command=lambda: self.remake())
            cancel.grid(row=1)
        else:
            #adds each relationship to a list in the form of : "sourceName -> destName"
            relList  = [ each.source + " -> " + each.destination for each in r.relationIndex]
            #creates label to give user insturctions
            inputlabel1 = tk.Label(self.inputFrame, text='Select relationship to update type:', width=40)
            inputlabel1.grid(row=0, columnspan=2) 
            #variable for drop down menu output
            clicked1 = StringVar()
            #creates drop down menu using list above as items and variable above as output
            drop = OptionMenu(self.inputFrame, clicked1, *relList) 
            drop.grid(row=1, columnspan=2)
            inputlabel3 = tk.Label(self.inputFrame, text='Select new relationship type:')
            inputlabel3.grid(row=2, columnspan=2) 
            #creates a variable for the drop down selector
            clicked = StringVar()
            clicked.set("Aggregation")
            #creates the drop down selector
            drop = OptionMenu(self.inputFrame, clicked, "Aggregation", "Composition", "Inheritance", "Realization") 
            drop.grid(row=3, columnspan=2)
            #function to output to the controller 
            def output(event):
                #splits the input into 2 source/dest
                parsed = clicked1.get().split(" -> ")
                #sets each output variable
                self.source = parsed[0]
                self.destination = parsed[1]
                self.relationshipTypeNew = clicked.get()
                #calls controller function to do stuff with output variables above
                self.controller.clickUpdateTypeButton()
            def output1():
                #splits the input into 2 source/dest
                parsed = clicked1.get().split(" -> ")
                #sets each output variable
                self.source = parsed[0]
                self.destination = parsed[1]
                self.relationshipTypeNew = clicked.get()
                #calls controller function to do stuff with output variables above
                self.controller.clickUpdateTypeButton()
            #creates first button and when clicked calls the output function above to set the class variables.
            ok = tk.Button(self.inputFrame, text='Change type', command=lambda: output1())
            ok.grid(row=6, column=0)
            #creates 2nd button and when clicked calls remake to clear the screen and remake and empty input frame.
            cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
            cancel.grid(row=6, column=1)
            self.bind('<Return>', output)  

    #creates the bottom left frame for deleting fields when the 'delete field' button is clicked
    def makeDeleteFieldFrame(self):
        #fills a dictionary {className: fields[], className: fields, ... } given the class has fields
        classDict = {c.name : c.fields for c in u.classIndex if len(c.fields) > 0}
        #checks if any classes have fields from the dict above and alerts user if not
        if len(classDict) == 0:
            inputlabel1 = tk.Label(self.inputFrame, text='No classes exist with fields', width=30)
            inputlabel1.grid(row=0)
            cancel = tk.Button(self.inputFrame, text='Close', command=lambda: self.remake())
            cancel.grid(row=1)
        else:
            #updates the 2nd drop down box based on the selection of the 1st drop down box
            def update2ndDrop(*args):
                #gets the fields for whatever class was first selected
                feilds = [each.name for each in classDict[clicked.get()]]
                deleteF.set(feilds[0])
                #gets 2nd dropmenu and delete it
                menu = drop2['menu']
                menu.delete(0, 'end')
                #fills 2nd dropmenu with each field from above
                for f in feilds:
                    menu.add_command(label=f, command=lambda classN=f: deleteF.set(classN))
            #fills variables based on drop down menu selection
            clicked = StringVar()
            deleteF = StringVar()
            #writes 2nd dropdown menu using method above
            clicked.trace('w', update2ndDrop)
            #creates both dropmenus
            drop = OptionMenu(self.inputFrame, clicked, *classDict.keys()) 
            drop2 = OptionMenu(self.inputFrame, deleteF,'')
            #creates label with instructions for user
            inputlabel1 = tk.Label(self.inputFrame, text='Select class to delete field:' , width=40)
            inputlabel1.grid(row=0, columnspan=2)
            #places dropdown menu in specified area in frame box
            drop.grid(row=1, columnspan=2)
            drop2.grid(row=3, columnspan=2)
            #creates another label for user instructions
            inputlabel2 = tk.Label(self.inputFrame, text='Select field to delete:')
            inputlabel2.grid(row=2, columnspan=2) 
            #output function to set variables and call to controller function to do stuff
            def output(event):
                self.className = clicked.get().strip()
                self.field = deleteF.get().strip()
                self.controller.clickDeleteFieldButton()
            def output1():
                self.className = clicked.get().strip()
                self.field = deleteF.get().strip()
                self.controller.clickDeleteFieldButton()
            #creates the two buttons, one for sending input, the other to cancel and clear input frame box    
            ok = tk.Button(self.inputFrame, text='Delete field', command=lambda: output1())
            ok.grid(row=4, column=0)
            cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
            cancel.grid(row=4, column=1)
            self.bind('<Return>', output)


    #creates the add class frame upon clicking add class
    def makeAddClassFrame(self):
        inputlabel1 = tk.Label(self.inputFrame, text='Enter Class name to add')
        inputlabel1.grid(row=0, columnspan=2) 
        e1 = tk.Entry(self.inputFrame, width=50)
        e1.grid(row=1, columnspan=2)
        e1.focus_set()
        def output(event):
            self.className = e1.get()
            self.controller.clickAddClassButton()
        def output1():
            self.className = e1.get()
            self.controller.clickAddClassButton()
        ok = tk.Button(self.inputFrame, text='Add Class', command=lambda: output1())
        ok.grid(row=4, column=0)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
        cancel.grid(row=4, column=1)
        self.bind('<Return>', output)
        
       

    def makeDeleteClassFrame(self):
        classList = [c.name for c in u.classIndex]
        if len(classList) == 0:
            inputlabel1 = tk.Label(self.inputFrame, text='No classes exist', width=30)
            inputlabel1.grid(row=0)
            cancel = tk.Button(self.inputFrame, text='Close', command=lambda: self.remake())
            cancel.grid(row=1) 
        else:
            clicked = StringVar()
            drop = OptionMenu(self.inputFrame, clicked, *classList) 
            drop.grid(row=1, columnspan=2)
            inputlabel1 = tk.Label(self.inputFrame, text='Select name to delete', width=40)
            inputlabel1.grid(row=0, columnspan=2) 
            def output(event):
                self.className = clicked.get()
                self.controller.clickDeleteClassButton()
            def output1():
                self.className = clicked.get()
                self.controller.clickDeleteClassButton()
            ok = tk.Button(self.inputFrame, text='Delete Class', command=lambda: output1())
            ok.grid(row=4, column=0)
            cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
            cancel.grid(row=4, column=1)
            self.bind('<Return>', output)

    def makeRenameClassFrame(self):
        classList = [c.name for c in u.classIndex]
        if len(classList) == 0:
            inputlabel1 = tk.Label(self.inputFrame, text='No classes exist', width=30)
            inputlabel1.grid(row=0)
            cancel = tk.Button(self.inputFrame, text='Close', command=lambda: self.remake())
            cancel.grid(row=1)
        else: 
            clicked = StringVar()
            drop = OptionMenu(self.inputFrame, clicked, *classList) 
            drop.grid(row=1, columnspan=2)
            inputlabel1 = tk.Label(self.inputFrame, text='Select name to rename:')
            inputlabel1.grid(row=0, columnspan=2) 
            inputlabel2 = tk.Label(self.inputFrame, text='Enter new name:')
            inputlabel2.grid(row=2, columnspan=2) 
            e2 = tk.Entry(self.inputFrame, width=50)
            e2.grid(row=3, columnspan=2)
            e2.focus_set()
            def output(event):
                self.className = clicked.get()
                self.classNameNew = e2.get()
                self.controller.clickRenameClassButton()
            def output1():
                self.className = clicked.get()
                self.classNameNew = e2.get()
                self.controller.clickRenameClassButton()
            ok = tk.Button(self.inputFrame, text='Rename Class', command=lambda: output1())
            ok.grid(row=4, column=0)
            cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
            cancel.grid(row=4, column=1)
            self.bind('<Return>', output)   
       
    def makeAddRelationFrame(self):
        if len(u.classIndex) < 2:
            inputlabel1 = tk.Label(self.inputFrame, text='Not enough classes exist', width=30)
            inputlabel1.grid(row=0)
            cancel = tk.Button(self.inputFrame, text='Close', command=lambda: self.remake())
            cancel.grid(row=1)
        else:
            classList = [c.name for c in u.classIndex]
            sor = StringVar()
            des = StringVar()
            drop1 = OptionMenu(self.inputFrame, sor, *classList) 
            drop1.grid(row=1, columnspan=2)
            inputlabel1 = tk.Label(self.inputFrame, text='Select source name:', width= 40)
            inputlabel1.grid(row=0, columnspan=2) 
            inputlabel2 = tk.Label(self.inputFrame, text='Select destination name:')
            inputlabel2.grid(row=2, columnspan=2) 
            drop2 = OptionMenu(self.inputFrame, des, *classList) 
            drop2.grid(row=3, columnspan=2)
            inputlabel3 = tk.Label(self.inputFrame, text='Select relationship type:')
            inputlabel3.grid(row=4, columnspan=2)
            clicked = StringVar()
            clicked.set("Aggregation")
            drop = OptionMenu(self.inputFrame, clicked, "Aggregation", "Composition", "Inheritance", "Realization") 
            drop.grid(row=5, columnspan=2)
            def output(event):
                self.source = sor.get()
                self.destination = des.get()
                self.relationshipType = clicked.get()
                self.controller.clickAddRelationButton()
            def output1():
                self.source = sor.get()
                self.destination = des.get()
                self.relationshipType = clicked.get()
                self.controller.clickAddRelationButton()
            ok = tk.Button(self.inputFrame, text='Add Relationship', command=lambda: output1())
            ok.grid(row=6, column=0)
            cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
            cancel.grid(row=6, column=1)
            self.bind('<Return>', output) 

    def makeDeleteRelationFrame(self):
        if len(r.relationIndex) == 0:
            inputlabel1 = tk.Label(self.inputFrame, text='Not enough relationships exist', width=30)
            inputlabel1.grid(row=0)
            cancel = tk.Button(self.inputFrame, text='Close', command=lambda: self.remake())
            cancel.grid(row=1)
        else:
            relList  = [ each.source + " -> " + each.destination for each in r.relationIndex]
            inputlabel1 = tk.Label(self.inputFrame, text='Select relationship to delete:', width=40)
            inputlabel1.grid(row=0, columnspan=2) 
            clicked = StringVar()
            drop = OptionMenu(self.inputFrame, clicked, *relList) 
            drop.grid(row=1, columnspan=2)
            def output(event):
                parsed = clicked.get().split(" -> ")
                self.source = parsed[0]
                self.destination = parsed[1]
                self.controller.clickDeleteRelationButton()
            def output1():
                parsed = clicked.get().split(" -> ")
                self.source = parsed[0]
                self.destination = parsed[1]
                self.controller.clickDeleteRelationButton()
            ok = tk.Button(self.inputFrame, text='Delete relationship', command=lambda: output1())
            ok.grid(row=4, column=0)
            cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
            cancel.grid(row=4, column=1)
            self.bind('<Return>', output)
    
    def makeAddFieldFrame(self):
        classList = [c.name for c in u.classIndex]
        if len(classList) == 0:
            inputlabel1 = tk.Label(self.inputFrame, text='No classes exist', width=30)
            inputlabel1.grid(row=0)
            cancel = tk.Button(self.inputFrame, text='Close', command=lambda: self.remake())
            cancel.grid(row=1)
        else: 
            clicked = StringVar()
            drop = OptionMenu(self.inputFrame, clicked, *classList) 
            drop.grid(row=1, columnspan=2)
            inputlabel1 = tk.Label(self.inputFrame, text='Select class to add field:')
            inputlabel1.grid(row=0, columnspan=2) 
            inputlabel2 = tk.Label(self.inputFrame, text='Enter field name:')
            inputlabel2.grid(row=2, columnspan=2) 
            e2 = tk.Entry(self.inputFrame, width=50)
            e2.grid(row=3, columnspan=2)
            e2.focus_set()
            inputlabel3 = tk.Label(self.inputFrame, text='Enter field type (leave empty if none):')
            inputlabel3.grid(row=4, columnspan=2) 
            e3 = tk.Entry(self.inputFrame, width=50)
            e3.grid(row=5, columnspan=2)
            def output(event):
                self.className = clicked.get()
                self.field = e2.get()
                self.fieldType = e3.get()
                self.controller.clickAddFieldButton()
            def output1():
                self.className = clicked.get()
                self.field = e2.get()
                self.fieldType = e3.get()
                self.controller.clickAddFieldButton()
            ok = tk.Button(self.inputFrame, text='Add Field', command=lambda: output1())
            ok.grid(row=6, column=0)
            cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
            cancel.grid(row=6, column=1)
            self.bind('<Return>', output)



    def makeRenameFieldFrame(self):
        classDict = {c.name : c.fields for c in u.classIndex if len(c.fields) > 0}
        if len(classDict) == 0:
            inputlabel1 = tk.Label(self.inputFrame, text='No classes exist with fields', width=30)
            inputlabel1.grid(row=0)
            cancel = tk.Button(self.inputFrame, text='Close', command=lambda: self.remake())
            cancel.grid(row=1)
        else:
            def update2ndDrop(*args):
                feilds = [each.name for each in classDict[clicked.get()]]
                deleteF.set(feilds[0])
                menu = drop2['menu']
                menu.delete(0, 'end')
                for f in feilds:
                    menu.add_command(label=f, command=lambda classN=f: deleteF.set(classN))

            clicked = StringVar()
            deleteF = StringVar()
            clicked.trace('w', update2ndDrop)
            drop = OptionMenu(self.inputFrame, clicked, *classDict.keys()) 
            drop2 = OptionMenu(self.inputFrame, deleteF,'')
            inputlabel1 = tk.Label(self.inputFrame, text='Select class to rename field:' , width=40)
            inputlabel1.grid(row=0, columnspan=2)
            drop.grid(row=1, columnspan=2)
            drop2.grid(row=3, columnspan=2)
            inputlabel2 = tk.Label(self.inputFrame, text='Select field to rename:')
            inputlabel2.grid(row=2, columnspan=2) 
            inputlabel3 = tk.Label(self.inputFrame, text='Enter new field name:')
            inputlabel3.grid(row=4, columnspan=2) 
            e3 = tk.Entry(self.inputFrame, width=50)
            e3.grid(row=5, columnspan=2)
            e3.focus_set()
            def output(event):
                self.className = clicked.get().strip()
                self.field = deleteF.get().strip()
                self.feildNew = e3.get()
                self.controller.clickRenameFieldButton()
            def output1():
                self.className = clicked.get().strip()
                self.field = deleteF.get().strip()
                self.feildNew = e3.get()
                self.controller.clickRenameFieldButton()
            ok = tk.Button(self.inputFrame, text='Rename Field', command=lambda: output1())
            ok.grid(row=6, column=0)
            cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
            cancel.grid(row=6, column=1)
            self.bind('<Return>', output)

    def makeParamInputFrame(self):
        inputlabel1 = tk.Label(self.inputFrame, text='Enter parameter name:')
        inputlabel1.grid(row=0, columnspan=2) 
        e1 = tk.Entry(self.inputFrame, width=50)
        e1.grid(row=1, columnspan=2)
        e1.focus_set()
        inputlabel2 = tk.Label(self.inputFrame, text='Enter parameter type:')
        inputlabel2.grid(row=2, columnspan=2) 
        e2 = tk.Entry(self.inputFrame, width=50)
        e2.grid(row=3, columnspan=2)
        def addParam(event):
            self.param = e1.get()
            self.paramType = e2.get()
            self.controller.clickAddParamButton()
        def addParam1():
            self.param = e1.get()
            self.paramType = e2.get()
            self.controller.clickAddParamButton()
        addParamButton = tk.Button(self.inputFrame, text='Add parameter', command= lambda: addParam1())
        addParamButton.grid(row=4, column=0)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
        cancel.grid(row=4, column=1)
        self.bind('<Return>', addParam)
    
    def makeAddMethodFrame(self):
        classList = [c.name for c in u.classIndex]
        if len(classList) == 0:
            inputlabel1 = tk.Label(self.inputFrame, text='No classes exist', width=30)
            inputlabel1.grid(row=0)
            cancel = tk.Button(self.inputFrame, text='Close', command=lambda: self.remake())
            cancel.grid(row=1)
        else: 
            clicked = StringVar()
            drop = OptionMenu(self.inputFrame, clicked, *classList) 
            drop.grid(row=1, columnspan=2)
            inputlabel1 = tk.Label(self.inputFrame, text='Select class to add method:')
            inputlabel1.grid(row=0, columnspan=2)         
            inputlabel2 = tk.Label(self.inputFrame, text='Enter method name:')
            inputlabel2.grid(row=2, columnspan=2) 
            e2 = tk.Entry(self.inputFrame, width=50)
            e2.grid(row=3, columnspan=2)
            e2.focus_set()
            inputlabel3 = tk.Label(self.inputFrame, text='Enter return type:')
            inputlabel3.grid(row=4, columnspan=2) 
            e3 = tk.Entry(self.inputFrame, width=50)
            e3.grid(row=5, columnspan=2)
            def addParam():
                self.className = clicked.get()
                self.method = e2.get()
                self.methodReturnType = e3.get()
                self.controller.clickAddMethodAndParamsButton()
            addParamButton = tk.Button(self.inputFrame, text='Add method and parameter(s)', command= lambda : addParam())
            addParamButton.grid(row=6, column=0)
            
            def output(event):
                self.className = clicked.get()
                self.method = e2.get()
                self.methodReturnType = e3.get()
                self.controller.clickAddMethodWithoutParamsButton()
            def output1():
                self.className = clicked.get()
                self.method = e2.get()
                self.methodReturnType = e3.get()
                self.controller.clickAddMethodWithoutParamsButton()
            ok = tk.Button(self.inputFrame, text='Add method no parameter(s)', command=lambda: output1())
            ok.grid(row=6, column=1)
            cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
            cancel.grid(row=6, column=2)
            self.bind('<Return>', output)

    def makeDeleteMethodFrame(self):
        classDict = {c.name : c.methods for c in u.classIndex if len(c.methods) > 0}
        if len(classDict) == 0:
            inputlabel1 = tk.Label(self.inputFrame, text='No classes exist with methods', width=30)
            inputlabel1.grid(row=0)
            cancel = tk.Button(self.inputFrame, text='Close', command=lambda: self.remake())
            cancel.grid(row=1)
        else:
            def update2ndDrop(*args):
                feilds = [each.name for each in classDict[clicked.get()]]
                deleteF.set(feilds[0])
                menu = drop2['menu']
                menu.delete(0, 'end')
                for f in feilds:
                    menu.add_command(label=f, command=lambda classN=f: deleteF.set(classN))

            clicked = StringVar()
            deleteF = StringVar()
            clicked.trace('w', update2ndDrop)
            drop = OptionMenu(self.inputFrame, clicked, *classDict.keys()) 
            drop2 = OptionMenu(self.inputFrame, deleteF,'')
            inputlabel1 = tk.Label(self.inputFrame, text='Select class to delete method:' , width=40)
            inputlabel1.grid(row=0, columnspan=2)
            drop.grid(row=1, columnspan=2)
            drop2.grid(row=3, columnspan=2)
            inputlabel2 = tk.Label(self.inputFrame, text='Select method to delete:')
            inputlabel2.grid(row=2, columnspan=2) 
            def output(event):
                self.className = clicked.get().strip()
                self.method = deleteF.get().strip()
                self.controller.clickDeleteMethodButton()
            def output1():
                self.className = clicked.get().strip()
                self.method = deleteF.get().strip()
                self.controller.clickDeleteMethodButton()
            ok = tk.Button(self.inputFrame, text='Delete method', command=lambda: output1())
            ok.grid(row=4, column=0)
            cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
            cancel.grid(row=4, column=1)
            self.bind('<Return>', output)

    def makeRenameMethodFrame(self):
        classDict = {c.name : c.methods for c in u.classIndex if len(c.methods) > 0}
        if len(classDict) == 0:
            inputlabel1 = tk.Label(self.inputFrame, text='No classes exist with methods', width=30)
            inputlabel1.grid(row=0)
            cancel = tk.Button(self.inputFrame, text='Close', command=lambda: self.remake())
            cancel.grid(row=1)
        else:
            def update2ndDrop(*args):
                feilds = [each.name for each in classDict[clicked.get()]]
                deleteF.set(feilds[0])
                menu = drop2['menu']
                menu.delete(0, 'end')
                for f in feilds:
                    menu.add_command(label=f, command=lambda classN=f: deleteF.set(classN))

            clicked = StringVar()
            deleteF = StringVar()
            clicked.trace('w', update2ndDrop)
            drop = OptionMenu(self.inputFrame, clicked, *classDict.keys()) 
            drop2 = OptionMenu(self.inputFrame, deleteF,'')
            inputlabel1 = tk.Label(self.inputFrame, text='Select class to rename method:' , width=40)
            inputlabel1.grid(row=0, columnspan=2)
            drop.grid(row=1, columnspan=2)
            drop2.grid(row=3, columnspan=2)
            inputlabel2 = tk.Label(self.inputFrame, text='Select method to rename:')
            inputlabel2.grid(row=2, columnspan=2) 
            inputlabel3 = tk.Label(self.inputFrame, text='Enter new method name:')
            inputlabel3.grid(row=4, columnspan=2) 
            e3 = tk.Entry(self.inputFrame, width=50)
            e3.grid(row=5, columnspan=2)
            e3.focus_set()
            def output(event):
                self.className = clicked.get().strip()
                self.method = deleteF.get().strip()
                self.methodNew = e3.get()
                self.controller.clickUpdateMethodButton()
            def output1():
                self.className = clicked.get().strip()
                self.method = deleteF.get().strip()
                self.methodNew = e3.get()
                self.controller.clickUpdateMethodButton()
            ok = tk.Button(self.inputFrame, text='Rename method', command=lambda: output1())
            ok.grid(row=6, column=0)
            cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
            cancel.grid(row=6, column=1)
            self.bind('<Return>', output)


    def makeAddParamFrame(self):        
        classDict = {c.name : c.methods for c in u.classIndex if len(c.methods) > 0}
        if len(classDict) == 0:
            inputlabel1 = tk.Label(self.inputFrame, text='No classes exist with methods', width=30)
            inputlabel1.grid(row=0)
            cancel = tk.Button(self.inputFrame, text='Close', command=lambda: self.remake())
            cancel.grid(row=1)
        else:
            def update2ndDrop(*args):
                feilds = [each.name for each in classDict[clicked.get()]]
                deleteF.set(feilds[0])
                menu = drop2['menu']
                menu.delete(0, 'end')
                for f in feilds:
                    menu.add_command(label=f, command=lambda classN=f: deleteF.set(classN))

            clicked = StringVar()
            deleteF = StringVar()
            clicked.trace('w', update2ndDrop)
            drop = OptionMenu(self.inputFrame, clicked, *classDict.keys()) 
            drop2 = OptionMenu(self.inputFrame, deleteF,'')
            inputlabel1 = tk.Label(self.inputFrame, text='Select class to add parameter:' , width=40)
            inputlabel1.grid(row=0, columnspan=2)
            drop.grid(row=1, columnspan=2)
            drop2.grid(row=3, columnspan=2)
            inputlabel2 = tk.Label(self.inputFrame, text='Select method to add parameter:')
            inputlabel2.grid(row=2, columnspan=2) 
            def addParam(event):
                self.className = clicked.get().strip()
                self.method = deleteF.get().strip()
                self.controller.clickAddParamToMethodButton()
            def addParam1():
                self.className = clicked.get().strip()
                self.method = deleteF.get().strip()
                self.controller.clickAddParamToMethodButton()         
            ok = tk.Button(self.inputFrame, text='Add parameter(s)', command=lambda: addParam1())
            ok.grid(row=4, column=0)
            cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
            cancel.grid(row=4, column=1)
            self.bind('<Return>', addParam)


    def makeParamDeleteInputFrame(self):
        
        inputlabel1 = tk.Label(self.inputFrame, text='Enter parameter name to delete:')
        inputlabel1.grid(row=0, columnspan=2) 
        e1 = tk.Entry(self.inputFrame, width=50)
        e1.grid(row=1, columnspan=2)
        e1.focus_set()
        def addParam(event):
            self.param = e1.get()
            self.inputFrame.destroy()
            self.makeInputFrame()
            self.makeParamDeleteInputFrame()
        def addParam1():
            self.param = e1.get()
            self.inputFrame.destroy()
            self.makeInputFrame()
            self.makeParamDeleteInputFrame()
        addParamButton = tk.Button(self.inputFrame, text='Delete another parameter', command= lambda: addParam1())
        addParamButton.grid(row=4, column=0)
        def output():
            self.param = e1.get()
            self.remake()
        ok = tk.Button(self.inputFrame, text='Delete and finish', command=lambda: output())
        ok.grid(row=4, column=1)
        cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
        cancel.grid(row=4, column=2)
        self.bind('<Return>', addParam)

    def makeDeleteParamInputFrame(self):
        paramList = u.classIndex[u.findClass(self.className)].methods[a.findMethod(self.method, self.className)].params
        if len(paramList) == 0:
            inputlabel1 = tk.Label(self.inputFrame, text='No parameters left in method', width=30)
            inputlabel1.grid(row=0)
            cancel = tk.Button(self.inputFrame, text='Close', command=lambda: self.remake())
            cancel.grid(row=1) 
        else:
            justParams = [each.name for each in paramList] 
            clicked = StringVar()
            drop = OptionMenu(self.inputFrame, clicked, *justParams) 
            drop.grid(row=1, columnspan=2)
            inputlabel1 = tk.Label(self.inputFrame, text='Select parameter to delete', width=40)
            inputlabel1.grid(row=0, columnspan=2) 
            def addParam(event):
                self.param = clicked.get()
                self.controller.clickSecondDeleteParamButton()
            def addParam1():
                self.param = clicked.get()
                self.controller.clickSecondDeleteParamButton()
            addParamButton = tk.Button(self.inputFrame, text='Delete parameter(s)', command= lambda: addParam1())
            addParamButton.grid(row=4, column=0)
            cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
            cancel.grid(row=4, column=1)
            self.bind('<Return>', addParam)


    def makeDeleteParamFrame(self):        
        classDict = {c.name : c.methods for c in u.classIndex for each in c.methods if len(each.params) > 0  }
        if len(classDict) == 0:
            inputlabel1 = tk.Label(self.inputFrame, text='No classes exist that have methods with parameters', width=60)
            inputlabel1.grid(row=0)
            cancel = tk.Button(self.inputFrame, text='Close', command=lambda: self.remake())
            cancel.grid(row=1)
        else:
            def update2ndDrop(*args):
                feilds = [each.name for each in classDict[clicked.get()] if len(each.params) > 0]
                deleteF.set(feilds[0])
                menu = drop2['menu']
                menu.delete(0, 'end')
                for f in feilds:
                    menu.add_command(label=f, command=lambda classN=f: deleteF.set(classN))

            clicked = StringVar()
            deleteF = StringVar()
            clicked.trace('w', update2ndDrop)
            drop = OptionMenu(self.inputFrame, clicked, *classDict.keys()) 
            drop2 = OptionMenu(self.inputFrame, deleteF,'')
            inputlabel1 = tk.Label(self.inputFrame, text='Select class to delete parameter:' , width=40)
            inputlabel1.grid(row=0, columnspan=2)
            drop.grid(row=1, columnspan=2)
            drop2.grid(row=3, columnspan=2)
            inputlabel2 = tk.Label(self.inputFrame, text='Select method to delete parameter:')
            inputlabel2.grid(row=2, columnspan=2) 
            def addParam(event):
                self.className = clicked.get().strip()
                self.method = deleteF.get().strip()
                self.controller.clickDeleteParamButton()
            def addParam1():
                self.className = clicked.get().strip()
                self.method = deleteF.get().strip()
                self.controller.clickDeleteParamButton()
            delete = tk.Button(self.inputFrame, text='Delete parameter(s)', command = lambda: addParam1())
            delete.grid(row=4,column=0)
            def delAll():
                self.className = clicked.get().strip()
                self.method = deleteF.get().strip()
                self.controller.clickDeleteAllParamButton()
            ok = tk.Button(self.inputFrame, text='Delete all parameters', command=lambda: delAll())
            ok.grid(row=4, column=1)
            cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
            cancel.grid(row=4, column=2)
            self.bind('<Return>', addParam)
    
    def makeChangeParamInputFrame(self):
        paramList = u.classIndex[u.findClass(self.className)].methods[a.findMethod(self.method, self.className)].params
        if len(paramList) == 0:
            inputlabel1 = tk.Label(self.inputFrame, text='No parameters left in method', width=30)
            inputlabel1.grid(row=0)
            cancel = tk.Button(self.inputFrame, text='Close', command=lambda: self.remake())
            cancel.grid(row=1) 
        else:
            justParams = [each.name for each in paramList] 
            clicked = StringVar()
            drop = OptionMenu(self.inputFrame, clicked, *justParams) 
            drop.grid(row=1, columnspan=2)
            inputlabel1 = tk.Label(self.inputFrame, text='Select parameter to change', width=40)
            inputlabel1.grid(row=0, columnspan=2) 
            inputlabel2 = tk.Label(self.inputFrame, text='Enter new parameter name:')
            inputlabel2.grid(row=2, columnspan=2) 
            e2 = tk.Entry(self.inputFrame, width=50)
            e2.grid(row=3, columnspan=2)
            e2.focus_set()
            inputlabel3 = tk.Label(self.inputFrame, text='Enter new parameter type:')
            inputlabel3.grid(row=4, columnspan=2) 
            e3 = tk.Entry(self.inputFrame, width=50)
            e3.grid(row=5, columnspan=2)
            def addParam(event):
                self.param = clicked.get().strip()
                self.paramNew = e2.get()
                self.paramTypeNew = e3.get()
                self.controller.clickChangeAnotherParamButton()
            def addParam1():
                self.param = clicked.get().strip()
                self.paramNew = e2.get()
                self.paramTypeNew = e3.get()
                self.controller.clickChangeAnotherParamButton()
            addParamButton = tk.Button(self.inputFrame, text='Change parameter(s)', command= lambda: addParam1())
            addParamButton.grid(row=6, column=0)
            cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
            cancel.grid(row=6, column=1)
            self.bind('<Return>', addParam)

    
    def makeChangeParamFrame(self):
        classDict = {c.name : c.methods for c in u.classIndex for each in c.methods if len(each.params) > 0  }
        if len(classDict) == 0:
            inputlabel1 = tk.Label(self.inputFrame, text='No classes exist that have methods with parameters', width=60)
            inputlabel1.grid(row=0)
            cancel = tk.Button(self.inputFrame, text='Close', command=lambda: self.remake())
            cancel.grid(row=1)
        else:
            def update2ndDrop(*args):
                feilds = [each.name for each in classDict[clicked.get()] if len(each.params) > 0]
                deleteF.set(feilds[0])
                menu = drop2['menu']
                menu.delete(0, 'end')
                for f in feilds:
                    menu.add_command(label=f, command=lambda classN=f: deleteF.set(classN))

            clicked = StringVar()
            deleteF = StringVar()
            clicked.trace('w', update2ndDrop)
            drop = OptionMenu(self.inputFrame, clicked, *classDict.keys()) 
            drop2 = OptionMenu(self.inputFrame, deleteF,'')
            inputlabel1 = tk.Label(self.inputFrame, text='Select class to change parameter:' , width=40)
            inputlabel1.grid(row=0, columnspan=2)
            drop.grid(row=1, columnspan=2)
            drop2.grid(row=3, columnspan=2)
            inputlabel2 = tk.Label(self.inputFrame, text='Select method to change parameter:')
            inputlabel2.grid(row=2, columnspan=2) 
            def addParam(event):
                self.className = clicked.get().strip()
                self.method = deleteF.get().strip()
                self.controller.clickChangeParamButton()
            def addParam1():
                self.className = clicked.get().strip()
                self.method = deleteF.get().strip()
                self.controller.clickChangeParamButton()
            delete = tk.Button(self.inputFrame, text='Change parameter(s)', command = lambda: addParam1())
            delete.grid(row=4,column=0)
            def delAll():
                self.className = clicked.get().strip()
                self.method = deleteF.get().strip()
                self.controller.clickChangeAllParamButton()
            ok = tk.Button(self.inputFrame, text='Change all parameters', command=lambda: delAll())
            ok.grid(row=4, column=1)
            cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
            cancel.grid(row=4, column=2)
            self.bind('<Return>', addParam)


    def makeListClassFrame(self):
        classList = [c.name for c in u.classIndex]
        if len(classList) == 0:
            inputlabel1 = tk.Label(self.inputFrame, text='No classes exist', width=30)
            inputlabel1.grid(row=0)
            cancel = tk.Button(self.inputFrame, text='Close', command=lambda: self.remake())
            cancel.grid(row=1) 
        else:
            clicked = StringVar()
            drop = OptionMenu(self.inputFrame, clicked, *classList) 
            drop.grid(row=1, columnspan=2)
            inputlabel1 = tk.Label(self.inputFrame, text='Select class name to list', width=40)
            inputlabel1.grid(row=0, columnspan=2) 
            def output(event):
                self.className = clicked.get()
                self.controller.clickListClassButton()
            def output1():
                self.className = clicked.get()
                self.controller.clickListClassButton()
            ok = tk.Button(self.inputFrame, text='List Class', command=lambda: output1())
            ok.grid(row=4, column=0)
            cancel = tk.Button(self.inputFrame, text='Cancel', command=lambda: self.remake())
            cancel.grid(row=4, column=1)
            self.bind('<Return>', output)
            

    #remakes the input frame in the bottom left corner
    def remake(self):
        self.inputFrame.destroy()
        self.makeInputFrame()

    #the following clear the bottom left frame and make a new inputframe decribed by self.make<this frame>()  
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
    
    #clears bottom left input frames and remakes base frame
    def wipe(self):
        self.inputFrame.destroy()
        self.makeInputFrame()

    def dragStart(self, event):
        widget = event.widget
        widget.startX = event.x
        widget.startY = event.y

    def dragMove(self, event):

        widget = event.widget

        x = widget.winfo_x() - widget.startX + event.x
        y = widget.winfo_y() - widget.startY + event.y

        
        cx = self.canvas.canvasx(event.x)
        cy = self.canvas.canvasy(event.y)
        # top left corner of widget relative to window - place where we
        #click in the label itself + where be begin draging the widget to
        if (x > 0 and y > 0):
            self.canvas.create_window((x + widget.winfo_width()//2, y + widget.winfo_height()//2), window=widget)
            for each in u.classIndex:
                if each.name.lower() == widget.winfo_name():
                    each.location['x'] = x + widget.winfo_width()//2
                    each.location['y'] = y + widget.winfo_height()//2
        elif y > 0:
            self.canvas.create_window((widget.winfo_width()//2, y + widget.winfo_height()//2), window=widget)
            for each in u.classIndex:
                if each.name.lower() == widget.winfo_name():
                    each.location['x'] = widget.winfo_width()//2
                    each.location['y'] = y + widget.winfo_height()//2

        elif x > 0:
            self.canvas.create_window((x + widget.winfo_width()//2, widget.winfo_height()//2), window=widget)
            for each in u.classIndex:
                if each.name.lower() == widget.winfo_name():
                    each.location['x'] = x + widget.winfo_width()//2
                    each.location['y'] = widget.winfo_height()//2
        
        else:
            self.canvas.create_window((widget.winfo_width()//2, widget.winfo_height()//2), window=widget)
            for each in u.classIndex:
                if each.name.lower() == widget.winfo_name():
                    each.location['x'] = widget.winfo_width()//2 
                    each.location['y'] = widget.winfo_height()//2


        

        #set the widget at the location
        #widget.place(x=x, y=y)
        
            

        #sets the UMLClass object's x and y values


        #name = u.classIndex[u.findClass(widget.winfo_name())]
        #name.location['x'] = x
        #name.location['y'] = y

        #updates the relationship lines (deletes then remakes)
        for each in list(UMLLines):
            if widget in each:
                if each.index(widget) == 0:
                    self.deleteLine(each[0].winfo_name(), each[1].winfo_name())
                    self.makeLine( widget.winfo_name(), each[1].winfo_name())
                else:
                    self.deleteLine(each[0].winfo_name(), each[1].winfo_name())
                    self.makeLine(each[0].winfo_name(), widget.winfo_name())

#returns a class 'c' in a string format, plus its heigth and width
def classToString(c):
    classLen = 7
    fieldLen = 10
    methLen = 12
    height = 8
    string = ''
    string += "Class: " + c.name + "\n"
    classLen += len(c.name)
    string += "\n    Fields:\n"
    for each in c.fields:
        string += "        " + str(each.type) + " " + each.name + "\n"
        fLen = 9 + len(each.type) + len(each.name)
        if fLen > fieldLen:
            fieldLen = fLen
        height += 1 
    string += "\n    Methods:\n"
    for each in c.methods:
        parameters = ""
        if len(each.params) > 0:  
            for param in each.params:
                parameters += str(param.type) + " " + param.name + ", "
        parameters = parameters[:-2] 
        string += "        " + str(each.return_type) + " " + each.name + "(" + parameters + ")\n"
        mLen = 11 + len(each.return_type) + len(each.name) + len(parameters)
        if mLen > methLen:
            methLen = mLen
        height += 1
    string += "\n"
    width = max(classLen, methLen, fieldLen)
    return (string, height, width)

# returns a relationship 'r' in a string format for output
def relationToString(r):
    string = ""
    string += "Relationship:\n"
    string += "    Source: " + r.source + "\n"
    string += "    Destination: " + r.destination + "\n"
    string += "    Type: " + r.type + "\n\n"
    return string
"""
def dragStart(event):
    widget = event.widget
    #print(widget.name)
    widget.startX = event.x
    widget.startY = event.y

def dragMove(event):
# top left corner of widget relative to window - place where we
#click in the label itself + where be begin draging the widget to
    widget = event.widget
    print(widget.winfo_name())
    print(widget.winfo_id())
    
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)
    name = u.classIndex[u.findClass(widget.winfo_name())]
    name.location['x'] = x
    name.location['y'] = y
    print(str(name.location['x']) + " : " + str(name.location['x']))
    for each in UMLLines:
        if widget in each:
            if each.index(widget) == 0:
                View.deleteLine(tk.Tk, each[0].winfo_name(), each[1].winfo_name())
                View.makeLine(tk.Tk, widget.winfo_name(), each[1].winfo_name())
            else:
                View.deleteLine(tk.Tk ,each[0].winfo_name(), each[1].winfo_name())
                View.makeLine(tk.Tk ,each[0].winfo_name(), widget.winfo_name())
"""
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
UMLBoxes = {}
UMLLines = {}