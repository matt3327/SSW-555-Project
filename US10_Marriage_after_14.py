import unittest
import parser
from datetime import datetime
from parser import Individual
from parser import Family
from parser import US10_check_marriage_after_14_anomaly

class Test(unittest.TestCase):
    def test_wifeYoungerThan14(self):
        wife = Individual("I1")
        husband = Individual("I2")
        fam = Family("F1")
        wife.birthDateObject = datetime(2000, 9,14)
        husband.birthDateObject = datetime(1996,9,14)
        fam.marriageDateObject = datetime(2013, 9 ,14)
        US10_check_marriage_after_14_anomaly(fam,wife,husband)
        self.assertEqual(len(fam.errors), 1)
        self.assertEqual(fam.errors, [])  

    def test_husbandYoungerThan14(self):
        wife = Individual("I1")
        husband = Individual("I2")
        fam = Family("F1")
        wife.birthDateObject = datetime(1992, 9,14)
        husband.birthDateObject = datetime(2003,9,14)
        fam.marriageDateObject = datetime(2013, 9 ,14)
        US10_check_marriage_after_14_anomaly(fam,wife,husband)
        self.assertEqual(len(fam.errors), 1)
        self.assertEqual(fam.errors, []) 

    def test_bothOlderThan14(self):   
        wife = Individual("I1")
        husband = Individual("I2")
        fam = Family("F1")
        wife.birthDateObject = datetime(1992, 9,14)
        husband.birthDateObject = datetime(1995,9,14)
        fam.marriageDateObject = datetime(2013, 9 ,14)
        US10_check_marriage_after_14_anomaly(fam,wife,husband)
        self.assertEqual(len(fam.errors), 0)
        self.assertEqual(fam.errors, [])  

if __name__ == "__main__": 
    unittest.main()