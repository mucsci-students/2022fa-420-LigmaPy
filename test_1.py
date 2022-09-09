import pytest

from UMLClass import *
from relationship import *
@pytest.fixture
# runs through adding and deleting a realtionship
def newMyClass():
    x=relationship('source','destination')
    addClass('test1')
    addClass('test2')
    addClass('test3')
    x.Add_relationship( 'test2', 'test3')
    x.Delete_relationship( 'test2', 'test3')
    print(listofrelationships.__len__())
    assert len(listofrelationships)==0
    myClassInstance = relationship('test3','test4')
    return myClassInstance

def test_types(newMyClass):
    testsource = newMyClass.source
    testdestination=newMyClass.destination
    print(testsource)
    assert testsource=='test3'
    assert testdestination=='test4'

def test_edit():
    addClass('source')
    addClass('destination')
    addClass('newsource')
    addClass('newdestination')
    x=relationship('source','destination')
    x.Add_relationship('source','destination')
    y=x.Edit_relationship('source', 'destination',"newsource",'newdestination')
    testlist=Listofrelationships()

    listofdestinationclasses =(list(list(zip(*testlist))[1]))
    assert listofdestinationclasses[0]=='newdestination'
    listofsourceclasses =(list(list(zip(*testlist))[0]))
    assert listofsourceclasses[0]=='newsource'
    x.Delete_relationship('newsource', 'newdestination')
    assert len(listofrelationships)==0

    