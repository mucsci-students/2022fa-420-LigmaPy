from tkinter import *

root = Tk()
root.geometry("800x600")
root.title("GUI")

def parameterInputWindow(label1, label2, paramList):
    top = Toplevel()
    inputlabel1 = Label(top, text=label1)
    inputlabel1.grid(row=0, columnspan=2) 
    e1 = Entry(top, width=50)
    e1.grid(row=1, columnspan=2)
    inputlabel2 = Label(top, text=label2)
    inputlabel2.grid(row=2, columnspan=2) 
    e2 = Entry(top, width=50)
    e2.grid(row=3, columnspan=2)
    def addParam():
        paramList.append((e1.get(),e2.get()))
        top.destroy()
        parameterInputWindow("Enter parameter name:", "Enter parameter type:", paramList)
    addParamButton = Button(top, text='Add another parameter', command=lambda: addParam())
    addParamButton.grid(row=4, column=0)
    def lastParam():
        paramList.append((e1.get(),e2.get()))
        top.destroy()
    finish = Button(top, text="Add and finish", command= lambda: lastParam())
    finish.grid(row=4, column=1)
    cancel = Button(top, text='Cancel', command=top.destroy)
    cancel.grid(row=4, column=2)
    top.transient(root)
    top.grab_set()
    top.wait_window()

def parameterDeleteWindow(label1, paramList):
    top = Toplevel()
    inputlabel1 = Label(top, text=label1)
    inputlabel1.grid(row=0, columnspan=2) 
    e1 = Entry(top, width=50)
    e1.grid(row=1, columnspan=2)
    def delParam():
        paramList.append(e1.get())
        top.destroy()
        parameterDeleteWindow("Enter parameter name:", paramList)
    delParamButton = Button(top, text='Delete another parameter', command=lambda: delParam())
    delParamButton.grid(row=2, column=0)
    def lastParam():
        paramList.append((e1.get()))
        top.destroy()
    finish = Button(top, text="Delete and finish", command= lambda: lastParam())
    finish.grid(row=2, column=1)
    cancel = Button(top, text='Cancel', command=top.destroy)
    cancel.grid(row=2, column=2)
    top.transient(root)
    top.grab_set()
    top.wait_window()

def changeWindow(label1, label2, label3, paramListDelete, paramListAdd):
    top = Toplevel()
    inputlabel1 = Label(top, text=label1)
    inputlabel1.grid(row=0, columnspan=2) 
    e1 = Entry(top, width=50)
    e1.grid(row=1, columnspan=2)
    inputlabel2 = Label(top, text=label2)
    inputlabel2.grid(row=2, columnspan=2) 
    e2 = Entry(top, width=50)
    e2.grid(row=3, columnspan=2)
    inputlabel3 = Label(top, text=label3)
    inputlabel3.grid(row=4, columnspan=2) 
    e3 = Entry(top, width=50)
    e3.grid(row=5, columnspan=2)
    def changeParam():
        paramListDelete.append(e1.get())
        paramListAdd.append((e2.get(),e3.get()))
        top.destroy()
        changeWindow("Enter parameter name to change:", "Enter new name:", "Enter new type:", paramListDelete, paramListAdd)
    changeParamButton = Button(top, text='Change another parameter', command=lambda: changeParam())
    changeParamButton.grid(row=6, column=0)
    def lastParam():
        paramListDelete.append((e1.get()))
        paramListAdd.append((e2.get(),e3.get()))
        top.destroy()
    finish = Button(top, text="Change and finish", command= lambda: lastParam())
    finish.grid(row=6, column=1)
    cancel = Button(top, text='Cancel', command=top.destroy)
    cancel.grid(row=6, column=2)
    top.transient(root)
    top.grab_set()
    top.wait_window()

def oneInputWindow(label1):
    top = Toplevel()
    inputlabel1 = Label(top, text=label1)
    inputlabel1.grid(row=0, columnspan=2) 
    e1 = Entry(top, width=50)
    e1.grid(row=1, columnspan=2)
    def output():
        print(e1.get())
        top.destroy()
    ok = Button(top, text='OK', command=lambda: output())
    ok.grid(row=4, column=0)
    cancel = Button(top, text='Cancel', command=top.destroy)
    cancel.grid(row=4, column=1)
    top.transient(root)
    top.grab_set()
    top.wait_window()

def twoInputWindow(label1, label2):
    top = Toplevel()
    inputlabel1 = Label(top, text=label1)
    inputlabel1.grid(row=0, columnspan=2) 
    e1 = Entry(top, width=50)
    e1.grid(row=1, columnspan=2)
    inputlabel2 = Label(top, text=label2)
    inputlabel2.grid(row=2, columnspan=2) 
    e2 = Entry(top, width=50)
    e2.grid(row=3, columnspan=2)
    def output():
        print(e1.get() + " " +  e2.get())
        top.destroy()
    ok = Button(top, text='OK', command=lambda: output())
    ok.grid(row=4, column=0)
    cancel = Button(top, text='Cancel', command=top.destroy)
    cancel.grid(row=4, column=1)
    top.transient(root)
    top.grab_set()
    top.wait_window()

def threeInputWindow(label1, label2, label3):
    top = Toplevel()
    top.geometry("300x200")
    inputlabel1 = Label(top, text=label1)
    inputlabel1.grid(row=0, columnspan=2) 
    e1 = Entry(top, width=50)
    e1.grid(row=1, columnspan=2)
    inputlabel2 = Label(top, text=label2)
    inputlabel2.grid(row=2, columnspan=2) 
    e2 = Entry(top, width=50)
    e2.grid(row=3, columnspan=2)
    inputlabel3 = Label(top, text=label3)
    inputlabel3.grid(row=4, columnspan=2) 
    e3 = Entry(top, width=50)
    e3.grid(row=5, columnspan=2)
    def output():
        print(e1.get() + " " +  e2.get() + " " + e3.get())
        top.destroy()
    ok = Button(top, text='OK', command= lambda : output())
    ok.grid(row=6, column=0)
    cancel = Button(top, text='Cancel', command=top.destroy)
    cancel.grid(row=6, column=1)
    top.transient(root)
    top.grab_set()
    top.wait_window()   

def threeInputParameterWindow(label1, label2, label3):
    top = Toplevel()
    top.geometry("400x300")
    inputlabel1 = Label(top, text=label1)
    inputlabel1.grid(row=0, columnspan=3) 
    e1 = Entry(top, width=50)
    e1.grid(row=1, columnspan=2)
    inputlabel2 = Label(top, text=label2)
    inputlabel2.grid(row=2, columnspan=3) 
    e2 = Entry(top, width=50)
    e2.grid(row=3, columnspan=2)
    inputlabel3 = Label(top, text=label3)
    inputlabel3.grid(row=4, columnspan=3) 
    e3 = Entry(top, width=50)
    e3.grid(row=5, columnspan=2)
    
    def addParam():
        print(e1.get() + ' ' + e2.get() + ' ' + e3.get())
        top.destroy()
        paramList = []
        parameterInputWindow("Enter parameter name:", "Enter parameter type:", paramList) 
        print(paramList)
        
    addParamButton = Button(top, text='Add parameter', command= lambda : addParam())
    addParamButton.grid(row=6, column=0)
    
    def output():
        print(e1.get() + ' ' + e2.get() + ' ' + e3.get())
        top.destroy()

    ok = Button(top, text='Add method without parameters', command = lambda : output())
    ok.grid(row=6, column=1)
    cancel = Button(top, text='Cancel', command=top.destroy)
    cancel.grid(row=6, column=2)
    top.transient(root)
    top.grab_set()
    top.wait_window()

def twoInputParameterWindow(label1, label2):
    top = Toplevel()
    top.geometry("400x300")
    inputlabel1 = Label(top, text=label1)
    inputlabel1.grid(row=0, columnspan=3) 
    e1 = Entry(top, width=50)
    e1.grid(row=1, columnspan=2)
    inputlabel2 = Label(top, text=label2)
    inputlabel2.grid(row=2, columnspan=3) 
    e2 = Entry(top, width=50)
    e2.grid(row=3, columnspan=2)
    
    def addParam():
        print(e1.get() + ' ' + e2.get())
        top.destroy()
        paramList = []
        parameterInputWindow("Enter parameter name:", "Enter parameter type:", paramList) 
        print(paramList)
        
    addParamButton = Button(top, text='Add parameter', command= lambda : addParam())
    addParamButton.grid(row=6, column=0)
    cancel = Button(top, text='Cancel', command=top.destroy)
    cancel.grid(row=6, column=1)
    top.transient(root)
    top.grab_set()
    top.wait_window()  

def deleteParameterWindow(label1, label2):
    top = Toplevel()
    top.geometry("400x300")
    inputlabel1 = Label(top, text=label1)
    inputlabel1.grid(row=0, columnspan=3) 
    e1 = Entry(top, width=50)
    e1.grid(row=1, columnspan=2)
    inputlabel2 = Label(top, text=label2)
    inputlabel2.grid(row=2, columnspan=3) 
    e2 = Entry(top, width=50)
    e2.grid(row=3, columnspan=2)
    
    def delParam():
        print(e1.get() + ' ' + e2.get())
        top.destroy()
        paramList = []
        parameterDeleteWindow("Enter parameter name:", paramList) 
        print(paramList)
        
    deleteParamButton = Button(top, text='Delete parameter', command= lambda : delParam())
    deleteParamButton.grid(row=6, column=0)
    
    def delAllParam():
        print("Delete all parameters for: " + e1.get() + ' ' + e2.get())
        top.destroy()

    deleteAllButton = Button(top, text='Delete every parameter', command= lambda : delAllParam())
    deleteAllButton.grid(row=6, column=1)
    cancel = Button(top, text='Cancel', command=top.destroy)
    cancel.grid(row=6, column=2)
    top.transient(root)
    top.grab_set()
    top.wait_window()

def changeParameterWindow(label1, label2):
    top = Toplevel()
    top.geometry("400x300")
    inputlabel1 = Label(top, text=label1)
    inputlabel1.grid(row=0, columnspan=3) 
    e1 = Entry(top, width=50)
    e1.grid(row=1, columnspan=2)
    inputlabel2 = Label(top, text=label2)
    inputlabel2.grid(row=2, columnspan=3) 
    e2 = Entry(top, width=50)
    e2.grid(row=3, columnspan=2)
    
    def changeParam():
        print(e1.get() + ' ' + e2.get())
        top.destroy()
        paramListDelete = []
        paramListAdd = []
        changeWindow("Enter parameter name to change:", "Enter new name:", "Enter new type:", paramListDelete, paramListAdd) 
        print("Delete:")
        print(paramListDelete)
        print("Add:")
        print(paramListAdd)

        
    changeParamButton = Button(top, text='Change parameter', command= lambda : changeParam())
    changeParamButton.grid(row=6, column=0)
    
    def changeAllParam():
        print("Delete all parameters for: " + e1.get() + ' ' + e2.get())
        top.destroy()
        paramList = []
        parameterInputWindow("Enter parameter name:", "Enter parameter type:", paramList) 
        print("add the following params:")
        print(paramList)

    deleteAllButton = Button(top, text='Change every parameter', command= lambda : changeAllParam())
    deleteAllButton.grid(row=6, column=1)
    cancel = Button(top, text='Cancel', command=top.destroy)
    cancel.grid(row=6, column=2)
    top.transient(root)
    top.grab_set()
    top.wait_window()           

def fourInputWindow(label1, label2, label3, label4):
    top = Toplevel()
    top.geometry("300x300")
    inputlabel1 = Label(top, text=label1)
    inputlabel1.grid(row=0, columnspan=2) 
    e1 = Entry(top, width=50)
    e1.grid(row=1, columnspan=2)
    inputlabel2 = Label(top, text=label2)
    inputlabel2.grid(row=2, columnspan=2) 
    e2 = Entry(top, width=50)
    e2.grid(row=3, columnspan=2)
    inputlabel3 = Label(top, text=label3)
    inputlabel3.grid(row=4, columnspan=2) 
    e3 = Entry(top, width=50)
    e3.grid(row=5, columnspan=2)
    inputlabel4 = Label(top, text=label4)
    inputlabel4.grid(row=6, columnspan=2) 
    e4 = Entry(top, width=50)
    e4.grid(row=7, columnspan=2)
    def output():
        print(e1.get() + " " +  e2.get() + " " + e3.get() + " " + e4.get())
        top.destroy()
    ok = Button(top, text='OK', command= lambda : output())
    ok.grid(row=8, column=0)
    cancel = Button(top, text='Cancel', command=top.destroy)
    cancel.grid(row=8, column=1)
    top.transient(root)
    top.grab_set()
    top.wait_window()   

#creating buttons
addClassButton = Button(root, width=25, text="Add Class", command=lambda : oneInputWindow("Enter class to add:")).grid(row=0, column=0)
deleteClassButton = Button(root, width=25, text="Delete Class", command=lambda : oneInputWindow("Enter class to delete:")).grid(row=1, column=0)
renameClassButton = Button(root,width=25, text="Rename Class", command=lambda : twoInputWindow("Enter class to rename", "Enter new name:")).grid(row=2, column=0)
addRelationButton = Button(root,width=25, text="Add Relationship", command=lambda : threeInputWindow("Enter source class:", "Enter destination class:", "Enter type:")).grid(row=3, column=0)
deleteRelationButton = Button(root,width=25, text="Delete Relationship", command=lambda : twoInputWindow("Enter source class:", "Enter destination class:")).grid(row=4, column=0)
addFieldButton = Button(root,width=25, text="Add Field", command= lambda : threeInputWindow("Enter class name:", "Enter field name:", "Enter field type: (Leave empty if none)")).grid(row=5, column=0)
deleteFieldButton = Button(root,width=25, text="Delete Field", command= lambda : twoInputWindow("Enter class name:", "Enter field name:")).grid(row=6, column=0)
renameFieldButton = Button(root,width=25, text="Rename Field", command= lambda : threeInputWindow("Enter class name:", "Enter field name to rename:", "Enter new field name:")).grid(row=7, column=0)
addMethodButton = Button(root, width=25, text="Add Method", command= lambda : threeInputParameterWindow("Enter class name:", "Enter method name", "Enter return type")).grid(row=8, column=0)
deleteMethodButton = Button(root, width=25, text="Delete Method", command= lambda : twoInputWindow("Enter class name:", "Enter method to delete:")).grid(row=9, column=0)
renameMethodButton = Button(root, width=25, text="Rename Method", command= lambda : threeInputWindow("Enter class name:", "Enter method to rename:", "Enter new name:")).grid(row=10, column=0)
addParameterButton = Button(root, width=25, text="Add Parameter(s)", command= lambda : twoInputParameterWindow("Enter class name:", "Enter method name:")).grid(row=11, column=0)
deleteParameterButton = Button(root, width=25, text="Delete Paramater(s)", command= lambda : deleteParameterWindow("Enter class name:", "Enter method name:")).grid(row=12, column=0)
changeParameterButton = Button(root, width=25, text="Change Parameter(s)", command= lambda : changeParameterWindow("Enter class name:", "Enter method name:")).grid(row=13, column=0)
listClassesButton = Button(root,width=25, text="List Classes", command= lambda : print("Print all classes to screen")).grid(row=14, column=0)
listClassButton = Button(root,width=25, text="List Class", command= lambda : oneInputWindow("Enter class to print:")).grid(row=15, column=0)
listRelationButton = Button(root,width=25, text="List Relationships", command= lambda : print("Print relationships to screen")).grid(row=16, column=0)
helpButton = Button(root,width=25, text="Help", command= lambda : print("print help menu to screen")).grid(row=17, column=0)

#menu
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Load", command= lambda : print("Call load function"))
filemenu.add_command(label="Save", command= lambda : print("Call save function"))
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)

root.mainloop()