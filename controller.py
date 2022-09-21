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
        try:
            result = self.model.Add_relationship(user_input)
        except ValueError:
            result = 'Failure'
        self.view.viewPanel.v_num.set(result)

    def actiontoremoveclass(self):
        # Pass data to view
        user_input = self.view.viewPanel.v_entry.get()
        try:
            result = self.model.Add_relationship(user_input)
        except ValueError:
            result = 'Failure'
        self.view.viewPanel.v_num.set(result)

    def actiontoremoverelationship(self):
        # Pass data to view
        user_input = self.view.viewPanel.v_entry.get()
        try:
            result = self.model.Remove_relationship(user_input)
        except ValueError:
            result = 'Failure'
        self.view.viewPanel.v_num.set(result)


Controller()

