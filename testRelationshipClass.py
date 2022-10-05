import unittest
import relationship as r
import UMLClass as u

class relationshipTestCase(unittest.TestCase):


    def setUp(self):
        abcdef = ['a','b','c','d','e','f']
        for each in abcdef:
            u.addClass(each)
        for n in range(len(u.classIndex) - 1):
            r.addRelationship(u.classIndex[n].name, u.classIndex[n+1].name, "Aggregation")


    def tearDown(self):
        u.classIndex = []
        r.relationIndex = []

    def addEmpty(self):
        num = r.addRelationship("","","")
        assert num == -1

    def addEmptyS(self):
        num = r.addRelationship("","a","Aggregation")
        assert num == -1

    def addEmptyD(self):
        num = r.addRelationship("a","","Aggregation")
        assert num == -1

    def addSame(self):
        num = r.addRelationship("a","a","Aggregation")
        assert num == -2

    def addNonExistantSource(self):
        num = r.addRelationship("z","a","Aggregation")
        assert num == -3

    def addNonExistantDest(self):
        num = r.addRelationship("a","z","Aggregation")
        assert num == -3

    def addNonExistantBoth(self):
        num = r.addRelationship("z","y","Aggregation")
        assert num == -3



unittest.main() 