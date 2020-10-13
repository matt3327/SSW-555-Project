import unittest
from datetime import datetime
from parser import Family
from parser import Individual
from parser import US09_check_child_birth_before_marriage_anomaly

class Test(unittest.TestCase):

    def testBornBeforeMarriage(self):
        testFam1 = Family("F1")
        testIndiv1= Individual("I1")
        testFam1.marriageDateObject = datetime(2019, 5, 3)
        testIndiv1.birthDateObject = datetime(2018, 5, 3)
        US09_check_child_birth_before_marriage_anomaly(testFam1, testIndiv1)
        self.assertEqual(len(testFam1.anomalies), 1)
        self.assertEqual(testFam1.anomalies[0], "I1 born before parents married")
    
    def testBornAfterMarriage(self):
        testFam2 = Family("F1")
        testIndiv2 = Individual("I2")
        testFam2.marriageDateObject = datetime(2018, 5, 3)
        testIndiv2.birthDateObject = datetime(2019, 5, 3)
        US09_check_child_birth_before_marriage_anomaly(testFam2, testIndiv2)
        self.assertEqual(len(testFam2.anomalies), 0)
        self.assertEqual(testFam2.anomalies, [])

    def testBornOnMarriage(self):
        testFam3 = Family("F3")
        testIndiv3 = Individual("I3")
        testFam3.marriageDateObject = datetime(2018, 5, 3)
        testIndiv3.birthDateObject = datetime(2018, 5, 3)
        US09_check_child_birth_before_marriage_anomaly(testFam3, testIndiv3)
        self.assertEqual(len(testFam3.anomalies), 0)
        self.assertEqual(testFam3.anomalies, [])


if __name__ == "__main__":
    unittest.main()