import unittest
import parser
from datetime import datetime
from parser import Individual
from parser import Family
from parser import US14_Parents_not_too_old 

class Test(unittest.TestCase):
    def test_motherIsOlderthan60(self):
        wife = Individual("I1")  
        husband = Individual("I2")
        child = Individual("I3")
        fam = Family("F1")
        fam.wifeObject = wife
        fam.husbandObject = husband
        fam.childObject = child
        fam.wifeObject.birthDateObject = datetime(1900,9,14)
        fam.husbandObject.birthDateObject = datetime(1996,9,14)
        child.birthDateObject = datetime(2013, 9 ,14)
        US14_Parents_not_too_old(fam,child)
        self.assertEqual(len(fam.anomalies), 1)
        self.assertEqual(fam.anomalies, ["Mother is 60 years older than child/ren"])  

    def test_husbandIsOlderthan80(self):
        wife = Individual("I1")
        husband = Individual("I2")
        child = Individual("I3")
        fam = Family("F1")
        fam.wifeObject = wife
        fam.husbandObject = husband
        fam.childObject = child
        fam.wifeObject.birthDateObject = datetime(1992,9,14)
        fam.husbandObject.birthDateObject = datetime(1900,9,14)
        child.birthDateObject = datetime(2013, 9 ,14)
        US14_Parents_not_too_old(fam,child)
        self.assertEqual(len(fam.anomalies), 1)
        self.assertEqual(fam.anomalies, ["Father is 80 years older than child/ren"]) 

    def test_bothWifeIs60AndHusbandis80(self):   
        wife = Individual("I1")
        husband = Individual("I2")
        fam = Family("F1")
        child = Individual("I3")
        fam.wifeObject = wife
        fam.husbandObject = husband
        fam.childObject = child
        fam.wifeObject.birthDateObject = datetime(1900,9,14)
        fam.husbandObject.birthDateObject = datetime(1900,9,14)
        child.birthDateObject = datetime(2013, 9 ,14)
        US14_Parents_not_too_old(fam,child)
        self.assertEqual(len(fam.anomalies), 2)
        self.assertEqual(fam.anomalies, ["Mother is 60 years older than child/ren", "Father is 80 years older than child/ren"])  
    
if __name__ == "__main__": 
    unittest.main()