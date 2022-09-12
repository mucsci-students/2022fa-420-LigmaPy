


import pytest

from UMLClass import *
from relationship import *
@pytest.fixture
# runs through adding and deleting a realtionship
def newMyClass():
    x=relationship('type','source','destination')
    addClass('test1')
    addClass('test2')
    addClass('test3')
    x.Add_relationship('test1', 'test2', 'test3')
    print(x.type)
    z=x.Delete_relationship('test1', 'test2', 'test3')
    print(listofrelationships.__len__())
    assert len(listofrelationships)==0


    myClassInstance = relationship('1','2','3')
    return myClassInstance

def test_aMethod(newMyClass):
    typetest = newMyClass.type
    assert typetest
