import unittest
from greedy.python import leetcode_medium

class Test_greedy_leetcode_medium(unittest.TestCase):
    def test_peoplegrouper(self):
        group = [3,3,3,3,3,1,3]
        expected = [[5],[0,1,2],[3,4,6]]
        actual = leetcode_medium.peoplegrouper(group)
        self.assertEqual(expected, actual)

    def test_peoplegrouper2(self):
        group = [2,1,3,3,3,2]
        expected = [[1],[0,5],[2,3,4]]
        actual = leetcode_medium.peoplegrouper(group)
        self.assertEqual(expected, actual)

    def test_peoplegrouper3(self):
        group = [1]
        expected = [[0]]
        actual = leetcode_medium.peoplegrouper(group)
        self.assertEqual(expected, actual)

    def test_brackets(self):
        str = "())"
        expected = 1
        actual = leetcode_medium.brackets(str)
        self.assertEqual(expected, actual)

    def test_brackets1(self):
        str = "()"
        expected = 0
        actual = leetcode_medium.brackets(str)
        self.assertEqual(expected, actual)

    def test_brackets2(self):
        str = "((("
        expected = 3
        actual = leetcode_medium.brackets(str)
        self.assertEqual(expected, actual)

    def test_brackets3(self):
        str = "()))(("
        expected = 4
        actual = leetcode_medium.brackets(str)
        self.assertEqual(expected, actual)
    
    def test_brackets4(self):
        str = "((())"
        expected = 1
        actual = leetcode_medium.brackets(str)
        self.assertEqual(expected, actual)
     
    
    

        