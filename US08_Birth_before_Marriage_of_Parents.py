import unittest
import parser
from datetime import datetime
from parser import Individual
from parser import Family
from parser import US08_check_child_birth_before_marriage_anomaly

class Test(unittest.TestCase):

    def test_BirthAfterMarriage(self):
        fam = Family("F1")
        fam.marriageDateObject = datetime(2000,9,13)
        child1 = Individual("I1")
        child1.birthDateObject = datetime(2001,1,1)
        childrenObjects = []
        childrenObjects.append(child1)
        US08_check_child_birth_before_marriage_anomaly(fam,childrenObjects)
        self.assertEqual(len(fam.errors), 0)
        self.assertEqual(fam.errors, [])

    def test_OneBirthBeforeMarriage(self):
        fam = Family("F1")
        fam.marriageDateObject = datetime(2000,9,13)
        child1 = Individual("I1")
        child1.birthDateObject = datetime(1999,1,1)
        childrenObjects = []
        childrenObjects.append(child1)
        US08_check_child_birth_before_marriage_anomaly(fam,childrenObjects)
        self.assertEqual(len(fam.errors),1)
        self.assertEqual(fam.errors[0], "Child born before marriage of parents")
    
    def test_OneBirthBeforeMarriage_OneBirthAfterMarriage(self):
        fam = Family("F1")
        fam.marriageDateObject = datetime(2000,9,13)
        child1 = Individual("I1")
        child2 = Individual("I2")
        child1.birthDateObject = datetime(1999,1,1)
        child2.birthDateObject = datetime(2009,10,1)
        childrenObjects = []
        childrenObjects.append(child1)
        childrenObjects.append(child2)
        US08_check_child_birth_before_marriage_anomaly(fam,childrenObjects)
        self.assertEqual(len(fam.errors),1)
        self.assertEqual(fam.errors[0], "Child born before marriage of parents")

    def test_TwoBirthsBeforeMarriage(self):
        fam = Family("F1")
        fam.marriageDateObject = datetime(2000,9,13)
        child1 = Individual("I1")
        child2 = Individual("I2")
        child1.birthDateObject = datetime(1999,1,1)
        child2.birthDateObject = datetime(2000,8,1)
        childrenObjects = []
        childrenObjects.append(child1)
        childrenObjects.append(child2)
        US08_check_child_birth_before_marriage_anomaly(fam,childrenObjects)
        self.assertEqual(len(fam.errors),2)
        self.assertEqual(fam.errors[0], "Child born before marriage of parents")
       
if __name__ == "__main__": 
    unittest.main()
