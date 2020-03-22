import unittest
from greedy.python import alg_toolbox_lectures

class Test_greedy_algorithms(unittest.TestCase):
    def test_fractional_knapsack(self):
        weights = [20,18,14]
        values = [4,3,2]
        capacity = 7
        expected = 7
        actual = alg_toolbox_lectures.fractional_knapsack(capacity, weights, values)
        self.assertEqual(expected, actual)
    
    def test_largest_number(self):
        numbers = [3,9,5,9,7,1]
        expected = "997531"
        actual = alg_toolbox_lectures.largest_number(numbers)
        self.assertEqual(expected, actual)

    def test_fractional_knapsack2(self):
        weights = [20,18,14]
        values = [4,3,2]
        capacity = 7
        expected = 7
        actual = alg_toolbox_lectures.fractional_knapsack_take2(capacity, weights, values)
        self.assertEqual(expected, actual)

        