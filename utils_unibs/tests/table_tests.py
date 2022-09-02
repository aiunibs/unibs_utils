import unittest
from utils_unibs.tables import get_idxs, print_latex_table


class TestGetID(unittest.TestCase):
    def test_correct(self):
        self.assertEqual(get_idxs(1, 3), (0, 3))
        self.assertEqual(get_idxs(5, 3), (3, 6))
        self.assertEqual(get_idxs(1, 3), (0, 3))
        self.assertEqual(get_idxs(1, 5), (0, 5))

    def test_unknown(self):
        self.assertEqual(get_idxs(1,8), (0, 8))
        self.assertEqual(get_idxs(4, 20), (0, 20))


class TestPrintLatexTable(unittest.TestCase):

    x = [[1,2,3], [1,2,3]]

    def test_correct(self):
        sol = ' & 1 & 2 & 3 \\\\\\hline\n & 1 & 2 & 3 \\\\\\hline\n'
        self.assertEqual(print_latex_table(dataset=self.x, precision=0, hline=1), sol)
        sol = ' & 1 & 2 & 3 \\\\\n & 1 & 2 & 3 \\\\\n'
        self.assertEqual(print_latex_table(dataset=self.x, precision=0, hline=0), sol)
        self.assertEqual(print_latex_table(dataset=self.x, precision=0, hline=-1), sol)
        self.assertEqual(print_latex_table(dataset=self.x, precision=0, hline=5), sol)
        sol = ' & 1 & 2 & 3 \\\\\n & 1 & 2 & 3 \\\\\\hline\n'
        self.assertEqual(print_latex_table(dataset=self.x, precision=0, hline=2), sol)
