import unittest
from datetime import datetime
from parse_gedcom.parser import Individual, Family
from parse_gedcom.sprint2_user_stories import US12_check_child_birth_after_divorce_anomaly

class Test(unittest.TestCase):

    def setUp(self):
        self.testChild1 = Individual("I1") #child
        self.testFam = Family("F1") #test family
        self.testFam.divorceDateObject = datetime(2019, 5, 3) #divorce date
        self.testFam.childrenObjects.append(self.testChild1) #added child
        
    def testBornAfterDivorce(self):
        testFam = self.testFam
        testChild1 = self.testChild1
        testChild1.birthDateObject = datetime(2020, 5, 3)
        US12_check_child_birth_after_divorce_anomaly(testFam)
        self.assertEqual(len(testFam.anomalies), 1)
        self.assertEqual(testFam.anomalies[0], "I1 born after parents divorced")
    
    def testBornBeforeDivorce(self):
        testFam = self.testFam
        testChild1 = self.testChild1
        testChild1.birthDateObject = datetime(2018, 5, 3)
        testFam.childrenObjects.append(testChild1)
        US12_check_child_birth_after_divorce_anomaly(testFam)
        self.assertEqual(len(testFam.anomalies), 0)
        self.assertEqual(testFam.anomalies, [])

    def testBornOnDivorce(self):
        testFam = self.testFam
        testChild1 = self.testChild1
        testChild1.birthDateObject = datetime(2019, 5, 3)
        US12_check_child_birth_after_divorce_anomaly(testFam)
        testFam.childrenObjects.append(testChild1)
        self.assertEqual(len(testFam.anomalies), 0)
        self.assertEqual(testFam.anomalies, [])

    def testBornBeforeAndAfter(self):
        testFam = self.testFam
        testChild1 = self.testChild1
        testChild2 = Individual("I2")
        testFam.childrenObjects.append(testChild2)
        testChild1.birthDateObject = datetime(2018, 5, 3)
        testChild2.birthDateObject = datetime(2020, 5, 3)
        US12_check_child_birth_after_divorce_anomaly(testFam)
        self.assertEqual(len(testFam.anomalies), 1)
        self.assertEqual(testFam.anomalies[0], "I2 born after parents divorced")

if __name__ == "__main__":
    unittest.main()