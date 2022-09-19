import unittest
import saveload as s
import UMLClass as u
import relationship as r
from io import StringIO

class SaveLoadTest(unittest.TestCase):
    
    def setUp(self):
        class1 = u.UMLClass("class1")
        class2 = u.UMLClass('class2') 
        class3 = u.UMLClass('class3')
        u.addClass(class1)
        u.addClass(class2)
        u.addClass(class3)
        class1.attributes.append('attr1')
        class1.attributes.append('attr2')
        class1.attributes.append('attr3')
        class2.attributes.append('attr1')
        class2.attributes.append('attr2')
        class2.attributes.append('attr3')
        class3.attributes.append('attr1')
        class3.attributes.append('attr2')
        class3.attributes.append('attr3')
        r.listofrelationships.append(('class1, class2'))
        r.listofrelationships.append(('class2, class3'))
        r.listofrelationships.append(('class3, class1'))

    def tearDown(self):
        r.listofrelationships = None
        u.classIndex = None

    def testSave(self):
        outfile = StringIO()
        s.save(outfile)
        outfile.seek(0)
        content = outfile.read()
        self.assertEqual(content, "Put stuff here")
    
    def testLoadEmpty(self):
        assert self.s.load('emptyfile') == ([],[])

    def testLoadBad(self):
        assert self.s.load('badfile') == (u.classIndex, r.listofrelationships)

    def testLoadNormal(self):
        assert self.s.load("testfile") == (u.classIndex, r.listofrelationships)

    def testLoadNoFile(self):
        assert self.s.load("doesntexist") == (u.classIndex, r.listofrelationships)
        
    if __name__ == "__main__":
        unittest.main() 