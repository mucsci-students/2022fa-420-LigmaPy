import pytest
import model as model
import relationship as relationships
import UMLClass as UMLClass

def test_model():
    test_model= model.Model()

    save=test_model.Load_data('testfile')
    test1=relationships.relationIndex  
    print(save)
    assert  type(save[0][0])==(str)
    # assert  save[0][0].name=='test1'
    # assert test1[0].source=='test1'
    # assert test1[0].destination=='test2'

