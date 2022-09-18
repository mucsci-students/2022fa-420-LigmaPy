import pytest
import os,sys,json
from UMLClass import *
from relationship import *
from saveload import *
from attributes import *
from pathlib import Path

#@pytest.fixture
def test_file():

    x=UMLRelationship('source','destination')
    addClass('test4')
    addClass('test5')
    addAttribute('test4','test5')
    addRelationship( 'test2', 'test3')
    deleteRelationship( 'test2', 'test3')
    listofrelationships=relationIndex
    classIndexx=classIndex
    old_directory=os.getcwd()
    save(classIndexx , listofrelationships, 'testfile')
    os.chdir(old_directory+'/UMLsavefiles')
    y=load('testfile')

    f = open('testfile.json')
    realfile=json.load(f)

    os.chdir(old_directory)
    dir_path = os.path.dirname(os.path.realpath('testfile.json'))
    my_file = Path(dir_path)

    assert os.path.exists(my_file)
    assert y!=None
    assert type(y[0])==type(classIndexx)
    assert type(y[1])==type(listofrelationships)
    assert y[0][1].name==classIndexx[1].name
    assert y[0][0].name==classIndexx[0].name
    assert realfile[0][0]['name']=='test1'
    assert realfile[0][1]['name']=='test2'
    assert realfile[0][2]['name']=='test3'
    assert realfile[0][3]['name']=='test4'
    assert realfile[0][4]['attributes'][0]['name']== 'test4'
#    assert list(listofrelationships[0])==list(y[1][0])

