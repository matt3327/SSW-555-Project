import unittest
from datetime import datetime
from parse_gedcom.parser import Individual, Family
from parse_gedcom.sprint1_user_stories import US01_check_date_before_today_error 

class Test(unittest.TestCase):

    def test_ValidBirthDate(self):
        indiv = Individual("I1")
        indiv.birthDateObject = datetime(1996, 9, 24)
        US01_check_date_before_today_error(indiv,"Birth")
        self.assertEqual(len(indiv.errors), 0)
        self.assertEqual(indiv.errors, [])

    def test_InvalidBirthDate(self):
        indiv = Individual("I1")
        indiv.birthDateObject = datetime(2030, 9, 24)
        US01_check_date_before_today_error(indiv,"Birth")
        self.assertEqual(len(indiv.errors), 1)
        self.assertEqual(indiv.errors[0], "Birth date is after current date")

    def test_ValidDeathDate(self):
        indiv = Individual("I1")
        indiv.deathDateObject = datetime(1996, 9, 24)
        US01_check_date_before_today_error(indiv,"Death")
        self.assertEqual(len(indiv.errors), 0)
        self.assertEqual(indiv.errors, [])

    def test_InvalidDeathDate(self):
        indiv = Individual("I1")
        indiv.deathDateObject = datetime(2030, 9, 24)
        US01_check_date_before_today_error(indiv,"Death")
        self.assertEqual(len(indiv.errors), 1)
        self.assertEqual(indiv.errors[0], "Death date is after current date")
    
    def test_ValidMarriage(self):
        fam = Family("F1")
        fam.marriageDateObject = datetime(1990, 10, 23)
        US01_check_date_before_today_error(fam,"Marriage")
        self.assertEqual(len(fam.errors), 0)
        self.assertEqual(fam.errors, [])

    def test_InvalidMarriage(self):
        fam = Family("F1")
        fam.marriageDateObject = datetime(2025, 10, 23)
        US01_check_date_before_today_error(fam,"Marriage")
        self.assertEqual(len(fam.errors), 1)
        self.assertEqual(fam.errors[0], "Marriage date is after current date")

    def test_ValidDivorce(self):
        fam = Family("F1")
        fam.divorceDateObject = datetime(1990, 10, 23)
        US01_check_date_before_today_error(fam,"Divorce")
        self.assertEqual(len(fam.errors), 0)
        self.assertEqual(fam.errors, [])

    def test_InvalidDivorce(self):
        fam = Family("F1")
        fam.divorceDateObject = datetime(2025, 10, 23)
        US01_check_date_before_today_error(fam,"Divorce")
        self.assertEqual(len(fam.errors), 1)
        self.assertEqual(fam.errors[0], "Divorce date is after current date")
    
if __name__ == "__main__":
    unittest.main()
 