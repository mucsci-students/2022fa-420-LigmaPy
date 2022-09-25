import tkinter as Tk
from model import Model
from view import View

class Controller():
    def __init__(self):
        self.root = Tk.Tk()
        self.model = Model()
        self.view = View(self.root, self)
        self.root.title("MVC example")
        self.root.geometry('300x200')
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

    def actiontogetrelationship():
        user_input = self.view.viewPanel.v_entry.get()
        try:
            result = self.model.Get_relationship(user_input)
        except ValueError:
            result = 'Failure'
        self.view.viewPanel.v_num.set(result)


    def actiontorenameclass():
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
            result = self.model.Add_relationship(clean_input[0],clean_input[1])
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

    def save(self):
        self.model.Save()
        
    def load(self):
        self.model.Load()