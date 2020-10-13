import unittest
from datetime import datetime
from parser import Individual
from parser import Family
from parser import US08_check_child_birth_before_mother_death_error

class Test(unittest.TestCase):
    def test_birthDate_before_mother_death(self):
        wife = Individual("I2")
        wife.alive = False
        wife.deathDateObject = datetime(2005,3,4)
        fam = Family("F1")
        fam.wifeObject = wife
        child1 = Individual("I3")
        child1.birthDateObject = datetime(2001,1,1)
        fam.childrenObjects.append(child1)
        US08_check_child_birth_before_mother_death_error(fam)
        self.assertEqual(len(fam.errors), 0) 
        self.assertEqual(fam.errors, [])

    def test_birthDate_after_mother_death(self):
        wife = Individual("I2")
        wife.alive = False
        wife.deathDateObject = datetime(2000,3,4)
        fam = Family("F1")
        fam.wifeObject = wife
        child1 = Individual("I3")
        child1.birthDateObject = datetime(2001,1,1)
        fam.childrenObjects.append(child1)
        US08_check_child_birth_before_mother_death_error(fam)
        self.assertEqual(len(fam.errors), 1)
        self.assertEqual(fam.errors, ["Child born after death of mother"])
    
    def test_1_birthDate_before_mother_death_1_after(self):
        wife = Individual("I2")
        wife.alive = False
        wife.deathDateObject = datetime(2019,3,4)
        fam = Family("F1")
        fam.wifeObject = wife
        child1 = Individual("I3")
        child1.birthDateObject = datetime(2001,1,1)
        fam.childrenObjects.append(child1)
        child2 = Individual("I4")
        child2.birthDateObject = datetime(2020,1,1)
        fam.childrenObjects.append(child2)
        US08_check_child_birth_before_mother_death_error(fam)
        self.assertEqual(len(fam.errors), 1)
        self.assertEqual(fam.errors, ["Child born after death of mother"])        
   

    def test_2_birthDate_before_mother_death(self):
        wife = Individual("I2")
        wife.alive = False
        wife.deathDateObject = datetime(2019,3,4)
        fam = Family("F1")
        fam.wifeObject = wife
        child1 = Individual("I3")
        child1.birthDateObject = datetime(2020,1,1)
        fam.childrenObjects.append(child1)
        child2 = Individual("I4")
        child2.birthDateObject = datetime(2020,2,1)
        fam.childrenObjects.append(child2)
        US08_check_child_birth_before_mother_death_error(fam)
        self.assertEqual(len(fam.errors), 2)
        self.assertEqual(fam.errors, ["Child born after death of mother", "Child born after death of mother"])  


    def test_mother_alive(self):
        wife = Individual("I2")
        fam = Family("F1")
        fam.wifeObject = wife
        child1 = Individual("I3")
        child1.birthDateObject = datetime(2001,1,1)
        fam.childrenObjects.append(child1)
        US08_check_child_birth_before_mother_death_error(fam)
        self.assertEqual(len(fam.errors), 0)
        self.assertEqual(fam.errors, []) 

if __name__ == "__main__": 
    unittest.main()