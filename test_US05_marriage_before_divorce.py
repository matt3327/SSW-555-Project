import unittest
from datetime import datetime
from parse_gedcom.parser import Individual, Family
from parse_gedcom.sprint1_user_stories import US05_check_marriage_before_divorce_error

class Test(unittest.TestCase):
    # make a family
    # run the error test
    # test to error value on family
    def testErrorDivorce(self):
        testFam1 = Family("F1")
        testFam1.divorced = True
        testFam1.marriageDateObject = datetime(2019, 5, 3)
        testFam1.divorceDateObject = datetime(2018, 5, 3)
        US05_check_marriage_before_divorce_error(testFam1)
        self.assertEqual(len(testFam1.errors), 1)
        self.assertEqual(testFam1.errors[0], "Divorce date is before marriage date")
    
    def testValidDivorce(self):
        testFam2 = Family("F2")
        testFam2.divorced = True
        testFam2.marriageDateObject = datetime(2018, 5, 3)
        testFam2.divorceDateObject = datetime(2019, 5, 3)
        US05_check_marriage_before_divorce_error(testFam2)
        self.assertEqual(len(testFam2.errors), 0)
        self.assertEqual(testFam2.errors, [])

    def testMarriageNoDivorce(self):
        testFam3 = Family("F3")
        testFam3.divorced = False
        testFam3.marriageDateObject = datetime(2018, 5, 3)
        US05_check_marriage_before_divorce_error(testFam3)
        self.assertEqual(len(testFam3.errors), 0)
        self.assertEqual(testFam3.errors, [])


if __name__ == "__main__":
    unittest.main()