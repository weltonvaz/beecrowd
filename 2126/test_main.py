import unittest
from main import find_subsequences

class TestSubsequences(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(find_subsequences(78954, 7895478954789547895447895478954), (6, 27))
        
    def test_example_2(self):
        self.assertEqual(find_subsequences(464133, 1331646546874694), (0, -1))
        
    def test_example_3(self):
        self.assertEqual(find_subsequences(12, 1231321455123214565423112), (3, 24))
        
    def test_no_subsequence(self):
        self.assertEqual(find_subsequences(123, 456789), (0, -1))
        
    def test_single_subsequence(self):
        self.assertEqual(find_subsequences(123, 123456), (1, 1))

if __name__ == '__main__':
    unittest.main()
