import UMLClass

def test_add_class():
    UMLClass.addClass("Foo")
    assert UMLClass.findClass("Foo") is not None


def test_rename_class():
    UMLClass.renameClass("Foo", "Bar")
    assert UMLClass.findClass("Foo") is None and UMLClass.findClass("Bar") is not None

def test_delete_class():
    UMLClass.deleteClass("Bar")
    assert UMLClass.findClass("Bar") is None

