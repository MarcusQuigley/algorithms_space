import unittest
from greedy.python import alg_toolbox_lectures

class Test_greedy_algorithms(unittest.TestCase):
    
    def test_largest_number(self):
        numbers = [3,9,5,9,7,1]
        expected = "997531"
        actual = alg_toolbox_lectures.largest_number(numbers)
        self.assertEqual(expected, actual)