import unittest
from utils_unibs.tables import get_idxs


class TestGetID(unittest.TestCase):
    def test_correct(self):
        self.assertEqual(get_idxs(1, 0, 3, [8, 5]), (0, 3))
        self.assertEqual(get_idxs(5, 1, 3, [8, 5]), (3, 6))
        self.assertEqual(get_idxs(1, 1, -1, [5, 3]), (0, 3))
        self.assertEqual(get_idxs(1, 0, -1, [5, 3]), (0, 5))

    def test_unknown(self):
        self.assertEqual(get_idxs(1, 0, 0, [8, 5]), (0, 8))
        self.assertEqual(get_idxs(4, 0, 20, [10, 4]), (0, 20))
