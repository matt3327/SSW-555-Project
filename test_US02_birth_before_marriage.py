import unittest
from datetime import datetime
from parser import Individual
from parser import Family
from parser import US02_birth_before_marriage_error

class Test(unittest.TestCase):


# def US02_birth_before_marriage_error(fam,husband,wife):
#   if fam.marriageDateObject < husband.birthDateObject or fam.marriageDateObject < wife.birthDateObject:
#     fam.errors.append("Marriage occured before birth date")

    def test_BirthBeforeMarriage(self):
        husband = Individual("I1")
        wife = Individual("I2")
        fam = Family("F1") 
        husband.birthDateObject = datetime(1977, 2, 1)
        wife.birthDateObject = datetime(1977, 2, 1)
        fam.husbandObject = husband
        fam.wifeObject = wife
        fam.marriageDateObject = datetime(2020, 12, 31)
        US02_birth_before_marriage_error(fam)
        self.assertEqual(len(fam.errors), 0)
        self.assertEqual(fam.errors, [])

    def test_BirthAfterMarriage(self):
        husband = Individual("I1")
        wife = Individual("I2")
        fam = Family("F1") 
        husband.birthDateObject = datetime(2020, 2, 1)
        wife.birthDateObject = datetime(2020, 5, 1)
        fam.husbandObject = husband
        fam.wifeObject = wife
        fam.marriageDateObject = datetime(1999, 12, 31)
        US02_birth_before_marriage_error(fam)
        self.assertEqual(len(fam.errors), 1)
        self.assertEqual(fam.errors[0], "Marriage occured before birth date") 

if __name__ == "__main__":
    unittest.main()