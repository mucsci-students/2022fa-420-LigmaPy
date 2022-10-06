# Class to test
import UMLClass

def test_add_class():
    UMLClass.addClass("Foo")
    assert UMLClass.findClass("Foo") != None

def test_add_existing_class_name():
    UMLClass.addClass("Foo")
    assert UMLClass.addClass("Foo") == -2

def test_empty_class_name():
    assert UMLClass.addClass("") == -1

def test_rename_class():
    UMLClass.addClass("Foo")
    UMLClass.renameClass("Foo", "Bar")
    assert UMLClass.findClass("Foo") == None and UMLClass.findClass != None

def test_rename_nonexisting_class():
    UMLClass.addClass("Foo")
    UMLClass.addClass("Bar")
    assert UMLClass.renameClass("Baz", "Far") == -2

def test_rename_existing_new_class():
    UMLClass.addClass("Foo")
    UMLClass.addClass("Bar")
    assert UMLClass.renameClass("Bar", "Foo") == -1

def test_delete_class():
    UMLClass.addClass("Foo")
    UMLClass.addClass("Bar")
    assert UMLClass.deleteClass("Foo") == 1

def test_delete_class_not_existing():
    UMLClass.addClass("Foo")
    UMLClass.addClass("Baz")
    assert UMLClass.deleteClass("Bar") == -1

