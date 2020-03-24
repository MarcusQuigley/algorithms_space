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

    def test_minDeletionSize(self):
        list = ["cba","daf","ghi"]
        expected = 1
        actual = leetcode_easy.minDeletionSize(list)
        self.assertEqual(expected, actual)

    def test_minDeletionSize1(self):
        list = ["a","b"]
        expected = 0
        actual = leetcode_easy.minDeletionSize(list)
        self.assertEqual(expected, actual)

    def test_minDeletionSize2(self):
        list = ["zyx","wvu","tsr"]
        expected = 3
        actual = leetcode_easy.minDeletionSize(list)
        self.assertEqual(expected, actual)

    def test_laststoneweight(self):
        stones = [2,7,4,1,8,1]
        expected = 1
        actual = leetcode_easy.laststoneweight(stones)
        self.assertEqual(expected, actual)
    
    def test_laststoneweight2(self):
        stones = [2,2,1,1]
        expected = 0
        actual = leetcode_easy.laststoneweight(stones)
        self.assertEqual(expected, actual)
