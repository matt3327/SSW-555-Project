import unittest
from datetime import datetime
from parse_gedcom.parser import Individual, Family
from parse_gedcom.sprint1_user_stories import US06_check_divorce_before_spouse_death_error

class Test(unittest.TestCase):
    
    def test_DeadHusband_ValidDate(self):
        husband = Individual("I1")
        wife = Individual("I2")
        testFam = Family("F1")
        testFam.divorced = True
        testFam.husbandId = husband.Id
        testFam.husbandObject = husband
        testFam.wifeId = wife.Id
        testFam.wifeObject =wife
        husband.alive = False
        husband.deathDateObject = datetime(2000, 1, 1)
        testFam.divorceDateObject = datetime(1999, 12, 31)
        US06_check_divorce_before_spouse_death_error(testFam)
        self.assertEqual(len(testFam.errors), 0)
        self.assertEqual(testFam.errors, [])

    def test_DeadHusband_InvalidDate(self):
        husband = Individual("I3")
        wife = Individual("I4")
        testFam = Family("F2")
        testFam.divorced = True
        testFam.husbandId = husband.Id
        testFam.husbandObject = husband
        testFam.wifeId = wife.Id
        testFam.wifeObject =  wife
        husband.alive = False
        husband.deathDateObject = datetime(1999, 12, 31)
        testFam.divorceDateObject = datetime(2000, 1, 1)
        US06_check_divorce_before_spouse_death_error(testFam)
        self.assertEqual(len(testFam.errors), 1)
        self.assertEqual(testFam.errors[0], "Divorce date is after husband death date")

    def test_DeadWife_ValidDate(self):
        husband = Individual("I5")
        wife = Individual("I6")
        testFam = Family("F3")
        testFam.divorced = True
        testFam.husbandId = husband.Id
        testFam.husbandObject = husband
        testFam.wifeId = wife.Id
        testFam.wifeObject = wife
        wife.alive = False
        wife.deathDateObject = datetime(2000, 1, 1)
        testFam.divorceDateObject = datetime(1999, 12, 31)
        US06_check_divorce_before_spouse_death_error(testFam)
        self.assertEqual(len(testFam.errors), 0)
        self.assertEqual(testFam.errors, [])

    def test_DeadWife_InvalidDate(self):
        husband = Individual("I7")
        wife = Individual("I8")
        testFam = Family("F4")
        testFam.divorced = True
        testFam.husbandId = husband.Id
        testFam.husbandObject = husband
        testFam.wifeId = wife.Id
        testFam.wifeObject  = wife
        wife.alive = False
        wife.deathDateObject = datetime(1999, 12, 31)
        testFam.divorceDateObject = datetime(2000, 1, 1)
        US06_check_divorce_before_spouse_death_error(testFam)
        self.assertEqual(len(testFam.errors), 1)
        self.assertEqual(testFam.errors[0], "Divorce date is after wife death date")
    
    def test_BothAlive(self):
        husband = Individual("I9")
        wife = Individual("I10")
        testFam = Family("F5")
        testFam.divorced = True
        testFam.husbandId = husband.Id
        testFam.husbandObject = husband
        testFam.wifeId = wife.Id
        testFam.wifeObject = wife
        testFam.divorceDateObject = datetime(2000, 1, 1)
        US06_check_divorce_before_spouse_death_error(testFam)
        self.assertEqual(len(testFam.errors), 0)
        self.assertEqual(testFam.errors, [])

    def test_BothDead_ValidDate(self):
        husband = Individual("I11")
        wife = Individual("I12")
        testFam = Family("F6")
        testFam.divorced = True
        testFam.husbandId = husband.Id
        testFam.husbandObject  = husband
        testFam.wifeId = wife.Id
        testFam.wifeObject = wife
        husband.alive = False
        husband.deathDateObject = datetime(2000, 1, 1)
        wife.alive = False
        wife.deathDateObject = datetime(2000, 1, 2)
        testFam.divorceDateObject = datetime(1999, 12, 31)
        US06_check_divorce_before_spouse_death_error(testFam)
        self.assertEqual(len(testFam.errors), 0)
        self.assertEqual(testFam.errors, [])

    def test_BothDead_InvalidHusbandDeathDate(self):
        husband = Individual("I13")
        wife = Individual("I14")
        testFam = Family("F7")
        testFam.divorced = True
        testFam.husbandId = husband.Id
        testFam.husbandObject = husband
        testFam.wifeId = wife.Id
        testFam.wifeObject  = wife
        husband.alive = False
        husband.deathDateObject = datetime(1999, 12, 30)
        wife.alive = False
        wife.deathDateObject = datetime(2000, 1, 1)
        testFam.divorceDateObject = datetime(1999, 12, 31)
        US06_check_divorce_before_spouse_death_error(testFam)
        self.assertEqual(len(testFam.errors), 1)
        self.assertEqual(testFam.errors[0], "Divorce date is after husband death date")

    def test_BothDead_InvalidWifeDeathDate(self):
        husband = Individual("I15")
        wife = Individual("I16")
        testFam = Family("F8")
        testFam.divorced = True
        testFam.husbandId = husband.Id
        testFam.husbandObject = husband
        testFam.wifeId = wife.Id
        testFam.wifeObject = wife
        husband.alive = False
        husband.deathDateObject = datetime(2000, 1, 1)
        wife.alive = False
        wife.deathDateObject = datetime(1999, 12, 30)
        testFam.divorceDateObject = datetime(1999, 12, 31)
        US06_check_divorce_before_spouse_death_error(testFam)
        self.assertEqual(len(testFam.errors), 1)
        self.assertEqual(testFam.errors[0], "Divorce date is after wife death date")

    def test_BothDead_InvalidHusbandDeathDate_InvalidWifeDeathDate(self):
        husband = Individual("I17")
        wife = Individual("I18")
        testFam = Family("F9")
        testFam.divorced = True
        testFam.husbandId = husband.Id
        testFam.husbandObject = husband
        testFam.wifeId = wife.Id
        testFam.wifeObject = wife
        husband.alive = False
        husband.deathDateObject = datetime(1999, 12, 30)
        wife.alive = False
        wife.deathDateObject = datetime(1999, 12, 31)
        testFam.divorceDateObject = datetime(2000, 1, 1)
        US06_check_divorce_before_spouse_death_error(testFam)
        self.assertEqual(len(testFam.errors), 2)
        self.assertEqual(testFam.errors[0], "Divorce date is after husband death date")
        self.assertEqual(testFam.errors[1], "Divorce date is after wife death date")

if __name__ == "__main__":
    unittest.main()
