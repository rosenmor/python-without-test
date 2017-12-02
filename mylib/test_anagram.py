import unittest
import mylib.subs

class TestMy(unittest.TestCase):
        def test_anagram(self):
                    self.assertEqual(mylib.subs.is_anagram([1,2,3], [3,2,1]), 1)
