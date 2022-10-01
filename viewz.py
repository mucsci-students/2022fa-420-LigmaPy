
import tkinter as Tk
from tkinter import  Canvas, Frame, BOTH
import os, json
import saveload as sl
import UMLClass as uml
import relationship as rel
class View():
    def __init__(self, title, controller):
        self.controller = controller
        self.frame = Tk.Frame(title)
        self.frame.pack()
        self.viewPanel = ViewPanel(title, controller)
        #self.viewPanel.Draw()


class ViewPanel():
    def __init__(self, root, controller):
        self.controller = controller
        self.master = root
        self.canvas = Canvas(root, width=800, height=800)
        self.canvas.place(x=50, y=50)

        # frame 1
        self.framePanel = Tk.Frame(root)
        self.framePanel.pack()
        self.label = Tk.Label(self.framePanel, text="UMLCLASS EDITOR")
        self.label.pack()

        self.v_num = Tk.StringVar()
        self.num = Tk.Label(self.framePanel, textvariable=self.v_num)
        self.num.pack()

        self.v_entry = Tk.StringVar()
        self.entry = Tk.Entry(self.framePanel, textvariable=self.v_entry)
        self.entry.pack()

        # frame 2
        self.framePanel2 = Tk.Frame(root)
        self.framePanel2.pack()

        self.btn = Tk.Button(self.framePanel2, text="Add Class")
        self.btn.pack(side='right')
        # Event handlers passes events to controller
        self.btn.bind("<Button>", controller.addclass)

        self.btn2 = Tk.Button(self.framePanel2, text="Add Rel.")
        self.btn2.pack(side='right')
        # Event handlers passes events to controller
        self.btn2.bind("<Button>", controller.addrelationship)

        self.btn3 = Tk.Button(self.framePanel2, text="DELETE Class")
        self.btn3.pack(side='right')
        # Event handlers passes events to controller
        self.btn3.bind("<Button>", controller.deleteclass)

        self.btn4 = Tk.Button(self.framePanel2, text="DELETE Rel.")
        self.btn4.pack(side='right')
        # Event handlers passes events to controller
        self.btn4.bind("<Button>", controller.deleterelationship)
        
        self.btn5 = Tk.Button(self.framePanel2, text="Load")
        self.btn5.pack(side='right')
        # Event handlers passes events to controller
        self.btn5.bind("<Button>", controller.load)
        
        self.btn6 = Tk.Button(self.framePanel2, text="Save")
        self.btn6.pack(side='right')
        # Event handlers passes events to controller
        self.btn6.bind("<Button>", controller.save)
        
        self.btn7 = Tk.Button(self.framePanel2, text="Get Rel.")
        self.btn7.pack(side='right')
        # Event handlers passes events to controller
        self.btn7.bind("<Button>", controller.getrelationship)
        
        self.btn8 = Tk.Button(self.framePanel2, text="Get Class.")
        self.btn8.pack(side='right')
        # Event handlers passes events to controller
        self.btn8.bind("<Button>", controller.getclass)
        
        self.btn9 = Tk.Button(self.framePanel2, text="List Class.")
        self.btn9.pack(side='right')
        # Event handlers passes events to controller
        self.btn9.bind("<Button>", controller.getlistofclasses)
        
        self.btn10 = Tk.Button(self.framePanel2, text="List Relationships.")
        self.btn10.pack(side='right')
        # Event handlers passes events to controller
        self.btn10.bind("<Button>", controller.getlistofrelationships)
        
        self.framePanel3 = Tk.Frame(root)
        self.framePanel3.pack()
        
        self.btn11 = Tk.Button(self.framePanel2, text="DRAW!.")
        self.btn11.pack(side='right')
        # Event handlers passes events to controller
        self.btn11.bind("<Button>", controller.Draw)#(self.framePanel3))
        
        #self.btn8.grid(row=4, column=0)
    def Draw(self, filename=''):
        if filename=='':
            sl.save(uml.UMLClass,rel.Relationship,'draw-checkpoint.json')
            # try:
            path_to_json = 'UMLsavefiles/'
            json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
            print(json_files)  # this is the most recent json file in the directory
            filepath='UMLsavefiles/'+'draw-checkpoint.json'
            f = open(filepath)
            data=json.load(f)
            x0=0
            x1=0
            y0=0
            y1=0
            classlocation=[]
            canvas = self.canvas
            for items in data['classes']:
                print(items['name'])
                classid=canvas.create_rectangle(x0+10, x1+10, y0+10, y1+10, outline="#f11",
                fill="#1f1", width=10)
                x0=x0+20
                x1=x1+10
                y0=y0+20
                y1=y1+10
                # we need to store the instances to access the location later
                classlocation.append((canvas.coords(classid),items['name']))
            
            for items in data['relationships']:
                for names in data['classes']:
                    if names['name']==items['source']:
                        canvas.create_line(classlocation[0][0], classlocation[1][0])
                        
            canvas.place(x=50, y=50)
            # except:
                # print("No file to load")
        else:
            filename=filename+'.json'
            filepath='UMLsavefiles/'+filename
            f = open(filepath)
            data=json.load(f)
            x0=0
            x1=0
            y0=0
            y1=0
            classlocation=[]
            canvas = self.canvas
            for items in data['classes']:
                print(items['name'])
                classid=canvas.create_rectangle(x0+10, x1+10, y0+10, y1+10, outline="#f11",
                fill="#1f1", width=10)
                x0=x0+20
                x1=x1+10
                y0=y0+20
                y1=y1+10
                # we need to store the instances to access the location later
                classlocation.append((canvas.coords(classid),items['name']))
            
            for items in data['relationships']:
                for names in data['classes']:
                    if names['name']==items['source']:
                        canvas.create_line(classlocation[0][0], classlocation[1][0])
                        
            self.canvas.place(x=110, y=110)
            self.canvas.update_idletasks()
            
            