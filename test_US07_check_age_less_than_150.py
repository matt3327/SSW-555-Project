import unittest
from parser import Individual
from parser import US07_check_age_less_than_150_error


class Test(unittest.TestCase):
    def testOlderThan150(self):
        testIndiv1 = Individual("I1")
        testIndiv1.age = "160"
        US07_check_age_less_than_150_error(testIndiv1)
        self.assertEqual(len(testIndiv1.errors), 1)
        self.assertEqual(testIndiv1.errors[0], "Individual age greater than 150")
    
    def testYoungerThan150(self):
        testIndiv2 = Individual("I2")
        testIndiv2.age = "70"
        US07_check_age_less_than_150_error(testIndiv2)
        self.assertEqual(len(testIndiv2.errors), 0)
        self.assertEqual(testIndiv2.errors, [])
        
    def testExactly150(self):
        testIndiv3 = Individual("I3")
        testIndiv3.age = "150"
        US07_check_age_less_than_150_error(testIndiv3)
        self.assertEqual(len(testIndiv3.errors), 0)
        self.assertEqual(testIndiv3.errors, [])



if __name__ == "__main__":
    unittest.main()