"""
Filename    : singleton_test.py
Description : Makes sure that only one instance of the GUI view is allowed
"""

# Class to test
import view.View as v
import controller.GuiController as c


def test_make_two_singletons():
    # Make a controller and automatically make a view within it
    singleton = c.Controller().view

    # Try to make another view, should just return the view already created
    new_singleton = v.View("should not matter what is here")
 
    assert (singleton is new_singleton)