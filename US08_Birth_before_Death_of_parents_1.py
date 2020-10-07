import unittest
import parser
from datetime import datetime
from parser import Individual
from parser import Family
from parser import US08_check_child_birth_before_parents_death_error

class Test(unittest.TestCase):
    def test_birthDate_before_parent_death(self):
        wife = Individual("I2")
        wife.deathDateObject = datetime(2005,3,4)
        fam = Family("F1")
        child1 = Individual("I3")
        child1.birthDateObject = datetime(2001,1,1)
        childrenObjects = []
        childrenObjects.append(child1)
        US08_check_child_birth_before_parents_death_error(fam,wife,child1)
        self.assertEqual(len(fam.errors), 1) 
        self.assertEqual(fam.errors, [])

    def test_birthDate_before_parent_death1(self):
        wife = Individual("I2")
        wife.deathDateObject = datetime(2000,3,4)
        fam = Family("F1")
        child1 = Individual("I3")
        child1.birthDateObject = datetime(2001,1,1)
        childrenObjects = []
        childrenObjects.append(child1)
        US08_check_child_birth_before_parents_death_error(fam, wife,child1)
        self.assertEqual(len(fam.errors), 1)
        self.assertEqual(fam.errors, [])
    
    def test_birthDate_before_parent_death2(self):
        wife = Individual("I2")
        wife.deathDateObject = datetime(2019,3,4)
        fam = Family("F1")
        child1 = Individual("I3")
        child1.birthDateObject = datetime(2001,1,1)
        childrenObjects = []
        childrenObjects.append(child1)
        US08_check_child_birth_before_parents_death_error(fam,wife,child1)
        self.assertEqual(len(fam.errors), 0)
        self.assertEqual(fam.errors, [])        

if __name__ == "__main__": 
    unittest.main()