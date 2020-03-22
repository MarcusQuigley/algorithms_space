import unittest
from greedy.python import leetcode_easy

class Test_greedy_leetcode_easy(unittest.TestCase):
    def test_balancedStringSplit(self):
        stringvalue = "RLRRLLRLRL"
        expected = 4
        actual = leetcode_easy.balancedStringSplit(stringvalue)
        self.assertEqual(expected, actual)
    
    def test_balancedStringSplit2(self):
        stringvalue = "RLRRRLLRLL"
        expected = 2
        actual = leetcode_easy.balancedStringSplit(stringvalue)
        self.assertEqual(expected, actual)

    def test_balancedStringSplit3(self):
        stringvalue = "RLLLLRRRLR"
        expected = 3
        actual = leetcode_easy.balancedStringSplit(stringvalue)
        self.assertEqual(expected, actual)

    def test_balancedStringSplit4(self):
        stringvalue = "LLLLRRRR"
        expected = 1
        actual = leetcode_easy.balancedStringSplit(stringvalue)
        self.assertEqual(expected, actual)
    
    

        