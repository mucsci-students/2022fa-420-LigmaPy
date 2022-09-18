import pytest
import os,sys,json
from UMLClass import *
from relationship import *
from saveload import *  
from attributes import *
from pathlib import Path

def test_attributes():
    x=findAttribute('test4','test5')
    attributes=classIndex[4].attributes
    print(attributes)
    assert x!=None
    assert attributes[0].name == 'test4'
    deleteAttribute('test4','test5')
    findAttribute('test4','test5')
    final=classIndex[4].attributes
    assert final==[]
