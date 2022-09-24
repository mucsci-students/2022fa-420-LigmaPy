import pytest
import model as model
import relationship as relationships
import UMLClass as UMLClass

def test_model():
    test_model= model.Model()

    save=test_model.Load_data()
    test1=relationships.relationIndex  
    print(test1)
    assert  type(save[0][0])==(UMLClass.UMLClass)
    assert  save[0][0].name=='test1'
    assert test1[0].source=='test1'
    assert test1[0].destination=='test2'

