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
        fam.wifeObject = wife
        fam.husbandObject = husband
        fam.wifeObject.birthDateObject = datetime(2000,9,14)
        fam.husbandObject.birthDateObject = datetime(1996,9,14)
        fam.marriageDateObject = datetime(2013, 9 ,14)
        US10_check_marriage_after_14_anomaly(fam)
        self.assertEqual(len(fam.anomalies), 1)
        self.assertEqual(fam.anomalies, ["Wife married before 14 anomaly"])  

    def test_husbandYoungerThan14(self):
        wife = Individual("I1")
        husband = Individual("I2")
        fam = Family("F1")
        fam.wifeObject = wife
        fam.husbandObject = husband
        fam.wifeObject.birthDateObject = datetime(1992,9,14)
        fam.husbandObject.birthDateObject = datetime(2003,9,14)
        fam.marriageDateObject = datetime(2013, 9 ,14)
        US10_check_marriage_after_14_anomaly(fam)
        self.assertEqual(len(fam.anomalies), 1)
        self.assertEqual(fam.anomalies, ["Husband married before 14 anomaly"]) 

    def test_bothOlderThan14(self):   
        wife = Individual("I1")
        husband = Individual("I2")
        fam = Family("F1")
        fam.wifeObject = wife
        fam.husbandObject = husband
        fam.wifeObject.birthDateObject = datetime(1992,9,14)
        fam.husbandObject.birthDateObject = datetime(1995,9,14)
        fam.marriageDateObject = datetime(2013, 9 ,14)
        US10_check_marriage_after_14_anomaly(fam)
        self.assertEqual(len(fam.anomalies), 0)
        self.assertEqual(fam.anomalies, [])  
   
    def test_bothYoungerThan14(self):   
        wife = Individual("I1")
        husband = Individual("I2")
        fam = Family("F1")
        fam.wifeObject = wife
        fam.husbandObject = husband
        fam.wifeObject.birthDateObject = datetime(2000,9,14)
        fam.husbandObject.birthDateObject = datetime(2000,9,14)
        fam.marriageDateObject = datetime(2013,9,14)
        US10_check_marriage_after_14_anomaly(fam)
        self.assertEqual(len(fam.anomalies), 2)
        self.assertEqual(fam.anomalies, ["Wife married before 14 anomaly", "Husband married before 14 anomaly"])  
    
if __name__ == "__main__": 
    unittest.main()