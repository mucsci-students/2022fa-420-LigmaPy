import unittest 
import controller
import tkinter as tkinter 
from tkinter import _tkinter 
from view import View
from model import Model
class TKinterTestCase(unittest.TestCase):
    """These methods are going to be the same for every GUI test,
    so refactored them into a separate class
    """
    def setUp(self):
        self.root=controller.Controller()
        self.pump_events()

    def tearDown(self):
        if self.root:
            self.root.destroy()
            self.pump_events()

    def pump_events(self):
        while self.root.update(_tkinter.ALL_EVENTS | _tkinter.DONT_WAIT):
            pass
    

class TestViewAskText(TKinterTestCase):
    def test_enter(self):
        v = controller.Controller()
        self.pump_events()
        v.e.focus_set()
        v.e.insert(tkinter.END,'stuff')
        v.e.event_generate('<Return>')
        self.pump_events()

        self.assertRaises(tkinter.TclError, lambda: v.top.winfo_viewable())
        self.assertEqual(v.value,u'йцукен')