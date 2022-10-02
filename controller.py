
from itertools import count
import tkinter as Tk
from tkinter import Canvas, Frame, BOTH
from model import Model
from viewz import View
import json,os
f = open('UMLsavefiles/testfile.json')
json.load(f)
# to-do trim user input 
class Controller():
    def __init__(self):
        self.root = Tk.Tk()
        self.model = Model()
        self.view = View(self.root, self)

        self.root.title("MVC example")
        self.root.geometry('800x800')
        # VM teminal issues >:()
        #self.root.geometry(os.system('xterm -into %d -geometry 40x20 -sb &' % wid))

        self.root.mainloop()

    def addclass(self, event):
        self.actiontoaddclass()

    def addrelationship(self, event):
        self.actiontoaddrelationship()

    def deleteclass(self, event):
        self.actiontoremoveclass()

    def deleterelationship(self, event):
        self.actiontoremoverelationship()

    def getclass(self,event):
        self.actiontoregetclass()

    def renameclass(self,event):
        self.actiontorenameclass()

    def getrelationship(self,event):
        self.actiontogetrelationship()
        
    def getclass(self,event):
        self.actiontogetclass()
    
    def save(self,event):
        self.action_to_save()
        
    def load(self,event ):
        self.action_to_load()
        
    def Draw(self, event):
        self.action_to_draw()
        
    def getlistofclasses(self,event):
        self.action_list_classes()

    def getlistofrelationships(self,event):
        self.action_list_relationships()
        

    def action_list_relationships(self):
        rellist=[]

        result = self.model.List_relationships( )
        for item in result:
            rellist.append(item.__repr__())
        self.view.viewPanel.v_num.set(rellist)
                
    
    def action_list_classes(self):
        classlist=[]
        count=0
        result= self.model.List_classes()
        
        for items in result:
            if isinstance(items, list):
                for item in items:
                    classlist.append(item.name)
            else:
                classlist.append(items.name)
            count=0+1
        self.view.viewPanel.v_num.set(classlist)


    def actiontogetrelationship(self):
        user_input = self.view.viewPanel.v_entry.get()
        clean_input=user_input.split(' ')
        try:
            result = self.model.Get_relationship(clean_input[0],clean_input[1] )
        except ValueError:
            result = 'Failure'
        self.view.viewPanel.v_num.set(result)



    def actiontorenameclass(self):
        user_input = self.view.viewPanel.v_entry.get()
        try:
            result = self.model.Rename_class(user_input)
        except ValueError:
            result = 'Failure'
        self.view.viewPanel.v_num.set(result)
        

    def actiontogetclass(self):
        user_input = self.view.viewPanel.v_entry.get()
        try:
            result = self.model.Find_class(user_input)
        except ValueError:
            result = 'Failure'
        self.view.viewPanel.v_num.set(result)


    def actiontoaddclass(self):
        # Pass data to view
        user_input = self.view.viewPanel.v_entry.get()
        try:
            result = self.model.Add_class(user_input)
        except ValueError:
            result = 'Failure'
        self.view.viewPanel.v_num.set(result)

    def actiontoaddrelationship(self):
        # Pass data to view
        user_input = self.view.viewPanel.v_entry.get()
        clean_input=user_input.split(' ')
        try:
            result = self.model.Add_relationship(clean_input[0],clean_input[1],clean_input[2])
        except ValueError:
            result = 'Failure'
        self.view.viewPanel.v_num.set(result)

    def actiontoremoveclass(self):
        # Pass data to view
        user_input = self.view.viewPanel.v_entry.get()
        try:
            result = self.model.Remove_class(user_input)
        except ValueError:
            result = 'Failure'
        self.view.viewPanel.v_num.set(result)

    def actiontoremoverelationship(self):
        # Pass data to view
        user_input = self.view.viewPanel.v_entry.get()
        clean_input=user_input.split(' ')
        try:
            result = self.model.Remove_relationship(clean_input[0],clean_input[1])
        except ValueError:
            result = 'Failure'
        self.view.viewPanel.v_num.set(result)

    def action_to_save(self):
        # Pass data to view
        user_input = self.view.viewPanel.v_entry.get()
        try:
            result = self.model.Save_data(user_input)
        except ValueError:
            result = 'Failure'
        self.view.viewPanel.v_num.set(result)
        
    def action_to_load(self):
        user_input = self.view.viewPanel.v_entry.get()
        try:
            result = self.model.Load_data(user_input)
        except ValueError:
            result = 'Failure'
        self.view.viewPanel.v_num.set(result)
        
    def action_to_draw(self):
        user_input = self.view.viewPanel.v_entry.get()
        try:
            result = self.view.viewPanel.Draw(user_input)
        except ValueError:
            result = 'Failure'
        self.view.viewPanel.v_num.set(result)