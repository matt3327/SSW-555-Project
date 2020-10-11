import unittest
import parser
from datetime import datetime
from parser import Individual
from parser import Family
from parser import US04_check_marriage_before_spouse_death_error

class Test(unittest.TestCase):
    
    def test_DeadHusband_ValidDate(self):
        husband = Individual("I1")
        wife = Individual("I2")
        testFam = Family("F1")
        testFam.husbandObject = husband
        testFam.wifeObject = wife
        husband.alive = False
        husband.deathDateObject = datetime(2000, 1, 1)
        testFam.marriageDateObject = datetime(1999, 12, 31)
        US04_check_marriage_before_spouse_death_error(testFam)
        self.assertEqual(len(testFam.errors), 0)
        self.assertEqual(testFam.errors, [])

    def test_DeadHusband_InvalidDate(self):
        husband = Individual("I1")
        wife = Individual("I2")
        testFam = Family("F1")
        testFam.husbandObject = husband
        testFam.wifeObject = wife
        husband.alive = False
        husband.deathDateObject = datetime(1999, 12, 31)
        testFam.marriageDateObject = datetime(2000, 1, 1)
        US04_check_marriage_before_spouse_death_error(testFam)
        self.assertEqual(len(testFam.errors), 1)
        self.assertEqual(testFam.errors[0], "Marriage date is after husband death date")

    def test_DeadWife_ValidDate(self):
        husband = Individual("I1")
        wife = Individual("I2")
        testFam = Family("F1")
        testFam.husbandObject = husband
        testFam.wifeObject = wife
        wife.alive = False
        wife.deathDateObject = datetime(2000, 1, 1)
        testFam.marriageDateObject = datetime(1999, 12, 31)
        US04_check_marriage_before_spouse_death_error(testFam)
        self.assertEqual(len(testFam.errors), 0)
        self.assertEqual(testFam.errors, [])

    def test_DeadWife_InvalidDate(self):
        husband = Individual("I1")
        wife = Individual("I2")
        testFam = Family("F1")
        testFam.husbandObject = husband
        testFam.wifeObject = wife
        wife.alive = False
        wife.deathDateObject = datetime(1999, 12, 31)
        testFam.marriageDateObject = datetime(2000, 1, 1)
        US04_check_marriage_before_spouse_death_error(testFam)
        self.assertEqual(len(testFam.errors), 1)
        self.assertEqual(testFam.errors[0], "Marriage date is after wife death date")
    
    def test_BothAlive(self):
        husband = Individual("I1")
        wife = Individual("I2")
        testFam = Family("F1")
        testFam.husbandObject = husband
        testFam.wifeObject = wife
        testFam.marriageDateObject = datetime(2000, 1, 1)
        US04_check_marriage_before_spouse_death_error(testFam)
        self.assertEqual(len(testFam.errors), 0)
        self.assertEqual(testFam.errors, [])

    def test_BothDead_ValidDate(self):
        husband = Individual("I1")
        wife = Individual("I2")
        testFam = Family("F1")
        testFam.husbandObject = husband
        testFam.wifeObject = wife
        husband.alive = False
        husband.deathDateObject = datetime(2000, 1, 1)
        wife.alive = False
        wife.deathDateObject = datetime(2000, 1, 2)
        testFam.marriageDateObject = datetime(1999, 12, 31)
        US04_check_marriage_before_spouse_death_error(testFam)
        self.assertEqual(len(testFam.errors), 0)
        self.assertEqual(testFam.errors, [])

    def test_BothDead_InvalidHusbandDeathDate(self):
        husband = Individual("I1")
        wife = Individual("I2")
        testFam = Family("F1")
        testFam.husbandObject = husband
        testFam.wifeObject = wife
        husband.alive = False
        husband.deathDateObject = datetime(1999, 12, 30)
        wife.alive = False
        wife.deathDateObject = datetime(2000, 1, 1)
        testFam.marriageDateObject = datetime(1999, 12, 31)
        US04_check_marriage_before_spouse_death_error(testFam)
        self.assertEqual(len(testFam.errors), 1)
        self.assertEqual(testFam.errors[0], "Marriage date is after husband death date")

    def test_BothDead_InvalidWifeDeathDate(self):
        husband = Individual("I1")
        wife = Individual("I2")
        testFam = Family("F1")
        testFam.husbandObject = husband
        testFam.wifeObject = wife
        husband.alive = False
        husband.deathDateObject = datetime(2000, 1, 1)
        wife.alive = False
        wife.deathDateObject = datetime(1999, 12, 30)
        testFam.marriageDateObject = datetime(1999, 12, 31)
        US04_check_marriage_before_spouse_death_error(testFam)
        self.assertEqual(len(testFam.errors), 1)
        self.assertEqual(testFam.errors[0], "Marriage date is after wife death date")

    def test_BothDead_InvalidHusbandDeathDate_InvalidWifeDeathDate(self):
        husband = Individual("I1")
        wife = Individual("I2")
        testFam = Family("F1")
        testFam.husbandObject = husband
        testFam.wifeObject = wife
        husband.alive = False
        husband.deathDateObject = datetime(1999, 12, 30)
        wife.alive = False
        wife.deathDateObject = datetime(1999, 12, 31)
        testFam.marriageDateObject = datetime(2000, 1, 1)
        US04_check_marriage_before_spouse_death_error(testFam)
        self.assertEqual(len(testFam.errors), 2)
        self.assertEqual(testFam.errors[0], "Marriage date is after husband death date")
        self.assertEqual(testFam.errors[1], "Marriage date is after wife death date")

if __name__ == "__main__":
    unittest.main()
