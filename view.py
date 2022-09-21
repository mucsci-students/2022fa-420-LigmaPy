import tkinter as Tk


class View():
    def __init__(self, title, controller):
        self.controller = controller
        self.frame = Tk.Frame(title)
        self.frame.pack()
        self.viewPanel = ViewPanel(title, controller)


class ViewPanel():
    def __init__(self, root, controller):
        self.controller = controller

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
        self.btn.pack(side='left')
        # Event handlers passes events to controller
        self.btn.bind("<Button>", controller.addclass)

        self.btn2 = Tk.Button(self.framePanel2, text="Add Relationship")
        self.btn2.pack(side='right')
        # Event handlers passes events to controller
        self.btn2.bind("<Button>", controller.addclass)

        self.btn3 = Tk.Button(self.framePanel2, text="DELETE Class")
        self.btn3.pack(side='right')
        # Event handlers passes events to controller
        self.btn3.bind("<Button>", controller.addclass)

        self.btn4 = Tk.Button(self.framePanel2, text="DELETE Relationship")
        self.btn4.pack(side='right')
        # Event handlers passes events to controller
        self.btn4.bind("<Button>", controller.deleterelationship)