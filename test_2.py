import pytest
from UMLClass import *
from relationship import *
from saveload import *
from pathlib import Path

@pytest.fixture
def test_file():
    x=relationship("source",'destination')
    addClass('test1')
    addClass('test2')
    addClass('test3')
    x.Add_relationship( 'test2', 'test3')
    listofrelationships=Listofrelationships()
    classIndex=classIndexx()

    save(classIndex , listofrelationships, 'testfile')
    y=load('testfile.json')

    dir_path = os.path.dirname(os.path.realpath('testfile.json'))
    my_file = Path(dir_path)

    assert os.path.exists(my_file)
    assert y!=None
    assert type(y[0])==type(classIndex)
    assert type(y[1])==type(listofrelationships)
    assert y[0][1].name==classIndex[1].name
    assert y[0][0].name==classIndex[0].name

    assert list(listofrelationships[0])==list(y[1][0])
