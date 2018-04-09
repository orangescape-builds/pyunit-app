import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "./"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))

import xmlrunner
import unittest
from calc import operation

class TestOperation(unittest.TestCase):

    def setUp(self):
        self.operation = operation.Operation()

    def tearDown(self):
        pass

    def testPlusSuccess(self):
        self.assertEqual(self.operation.Plus(1,2),3)

    def testMinusFail(self):
        self.assertEqual(self.operation.Minus(2, 1), 3)

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="./python_unittests_xml"))