import unittest
from datetime import datetime
from parser import Individual
from parser import Family
from parser import US03_check_birth_before_death_error

class Test(unittest.TestCase):
    
    def test_BirthBeforeDeath(self):
        indiv = Individual("I1")
        indiv.alive = False
        indiv.birthDateObject = datetime(1999, 12, 31)
        indiv.deathDateObject = datetime(2000, 1, 1)
        US03_check_birth_before_death_error(indiv)
        self.assertEqual(len(indiv.errors), 0)
        self.assertEqual(indiv.errors, [])

    def test_BirthAfterDeath(self):
        indiv = Individual("I1")
        indiv.alive = False
        indiv.birthDateObject = datetime(2000, 1, 1)
        indiv.deathDateObject = datetime(1999, 12, 31)
        US03_check_birth_before_death_error(indiv)
        self.assertEqual(len(indiv.errors), 1)
        self.assertEqual(indiv.errors[0], "Death date is before birth date")

    def test_Alive(self):
        indiv = Individual("I1")
        indiv.alive = True
        US03_check_birth_before_death_error(indiv)
        self.assertEqual(len(indiv.errors), 0)
        self.assertEqual(indiv.errors, [])

if __name__ == "__main__":
    unittest.main()
