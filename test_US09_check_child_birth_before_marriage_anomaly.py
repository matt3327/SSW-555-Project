import unittest
from datetime import datetime
from parse_gedcom.parser import Individual, Family
from parse_gedcom.sprint1_user_stories import US09_check_child_birth_before_marriage_anomaly

class Test(unittest.TestCase):

    def setUp(self):
        self.testChild1 = Individual("I1") #child
        self.testFam = Family("F1") #test family
        self.testFam.marriageDateObject = datetime(2019, 5, 3) #marriage date
        self.testFam.childrenObjects.append(self.testChild1) #added child
        
    def testBornBeforeMarriage(self):
        testFam = self.testFam
        testChild1 = self.testChild1
        testChild1.birthDateObject = datetime(2018, 5, 3)
        US09_check_child_birth_before_marriage_anomaly(testFam)
        self.assertEqual(len(testFam.anomalies), 1)
        self.assertEqual(testFam.anomalies[0], "I1 born before parents married")
    
    def testBornAfterMarriage(self):
        testFam = self.testFam
        testChild1 = self.testChild1
        testChild1.birthDateObject = datetime(2020, 5, 3)
        testFam.childrenObjects.append(testChild1)
        US09_check_child_birth_before_marriage_anomaly(testFam)
        self.assertEqual(len(testFam.anomalies), 0)
        self.assertEqual(testFam.anomalies, [])

    def testBornOnMarriage(self):
        testFam = self.testFam
        testChild1 = self.testChild1
        testChild1.birthDateObject = datetime(2019, 5, 3)
        US09_check_child_birth_before_marriage_anomaly(testFam)
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
        US09_check_child_birth_before_marriage_anomaly(testFam)
        self.assertEqual(len(testFam.anomalies), 1)
        self.assertEqual(testFam.anomalies[0], "I1 born before parents married")

if __name__ == "__main__":
    unittest.main()