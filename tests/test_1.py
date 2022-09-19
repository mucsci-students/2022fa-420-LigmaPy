from __future__ import print_function
from pytest import fixture
import pytest
import logging

from UMLClass import *
from relationship import *
from saveload import *
from pathlib import Path

@pytest.fixture
# runs through adding and deleting a realtionship
def newMyClass(caplog):

        x=UMLRelationship('source','destination')
        addClass('test1')
        addClass('test2')
        addClass('test3')
        addRelationship( 'test2', 'test3')
        deleteRelationship( 'test2', 'test3')
        print(relationIndex.__len__())
        return x

def test_aMethod(newMyClass,caplog):
        typetest = newMyClass.source
        typetest2= newMyClass.destination

