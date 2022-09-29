''' import tkinter
from tkinter import messagebox
import unittest
import controller
import View

class MyGUI(tkinter.Frame):
    def __init__(self, master, **kw):
        tkinter.Frame.__init__(self, master, **kw)
        self.info_button = tkinter.Button(self, command=self.info_cmd, text='Info')
        self.info_button.pack()
        self.quit_button = tkinter.Button(self, command=self.quit_cmd, text='Quit')
        self.quit_button.pack()

    def info_cmd(self):
        messagebox.showinfo('Info', master=self)

    def quit_cmd(self):
        confirm = messagebox.askokcancel('Quit?', master=self)
        if confirm:
            self.destroy()


class TKinterTestCase(unittest.TestCase):
    def setUp(self):
        self.root = View.View(controller=controller.Controller(), title='Test')
        self.root.bind('<Key>', lambda e: print(self.root, e.keysym))

    def tearDown(self):
        if self.root:
            self.root.destroy()

    def test_enter(self):
        v = View.View(self.root, title='Test')
        v.pack()
        self.root.update_idletasks()

        # info
        v.after(100, lambda: self.root.event_generate('<Return>'))
        v.info_button.invoke()

        # quit
        def cancel():
            self.root.event_generate('<Tab>')
            self.root.event_generate('<Return>')

        v.after(100, cancel)
        v.quit_button.invoke()
        self.assertTrue(v.winfo_ismapped())    
        v.after(100, lambda: self.root.event_generate('<Return>'))
        v.quit_button.invoke()
        with self.assertRaises(tkinter.TclError):
            v.winfo_ismapped()


if __name__ == "__main__":
    unittest.main() '''