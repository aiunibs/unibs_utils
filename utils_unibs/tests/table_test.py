import unittest
from utils_unibs.tables import get_idxs, print_latex_table, transpose_latex_table
from utils_unibs.constants import C


class TestGetID(unittest.TestCase):
    def test_correct(self):
        self.assertEqual(get_idxs(1, 3), (0, 3))
        self.assertEqual(get_idxs(5, 3), (3, 6))
        self.assertEqual(get_idxs(1, 3), (0, 3))
        self.assertEqual(get_idxs(1, 5), (0, 5))

    def test_unknown(self):
        self.assertEqual(get_idxs(1, 8), (0, 8))
        self.assertEqual(get_idxs(4, 20), (0, 20))


class TestPrintLatexTable(unittest.TestCase):

    x = [[1, 2, 3], [1, 2, 3]]
    x_string = [[1, 2, "c"], ["1%", "b", 4]]
    labels = ["a", "b"]
    labels_special = ["a>b", "a & b ~ c"]

    def test_correct(self):
        sol = " & 1 & 2 & 3 \\\\\\hline\n & 1 & 2 & 3 \\\\\\hline\n"
        self.assertEqual(print_latex_table(dataset=self.x, precision=0, hline=1), sol)
        sol = " & 1 & 2 & 3 \\\\\n & 1 & 2 & 3 \\\\\n"
        self.assertEqual(print_latex_table(dataset=self.x, precision=0, hline=0), sol)
        self.assertEqual(print_latex_table(dataset=self.x, precision=0, hline=-1), sol)
        self.assertEqual(print_latex_table(dataset=self.x, precision=0, hline=5), sol)
        sol = " & 1 & 2 & 3 \\\\\n & 1 & 2 & 3 \\\\\\hline\n"
        self.assertEqual(print_latex_table(dataset=self.x, precision=0, hline=2), sol)
        sol = " & 1.000 & 2.000 & 3.000 \\\\\n & 1.000 & 2.000 & 3.000 \\\\\n"
        self.assertEqual(print_latex_table(dataset=self.x, precision=3, hline=0), sol)
        sol = " & 1 & \\bf{2} & \\bf{3} \\\\\n & 1 & \\bf{2} & \\bf{3} \\\\\n"
        self.assertEqual(
            print_latex_table(
                dataset=self.x, best=0, axis=1, count_vals=2, precision=0
            ),
            sol,
        )
        sol = (
            " & \\bf{1} & \\bf{2} & \\bf{3} \\\\\n & \\bf{1} & \\bf{2} & \\bf{3} \\\\\n"
        )
        self.assertEqual(
            print_latex_table(dataset=self.x, best=1, axis=0, precision=0), sol
        )
        self.assertEqual(
            print_latex_table(dataset=self.x, best=0, axis=0, precision=0), sol
        )
        self.assertEqual(
            print_latex_table(
                dataset=self.x, precision=0, best=0, axis=0, count_vals=-1
            ),
            sol,
        )
        self.assertEqual(
            print_latex_table(
                dataset=self.x, precision=0, best=0, axis=0, count_vals=0
            ),
            sol,
        )
        sol = "a & 1 & 2 & 3 \\\\\nb & 1 & 2 & 3 \\\\\n"
        self.assertEqual(
            print_latex_table(dataset=self.x, precision=0, hline=0, labels=self.labels),
            sol,
        )
        sol = " & 1 & 2 & c \\\\\n & 1\\% & b & 4 \\\\\n"
        self.assertEqual(print_latex_table(dataset=self.x_string, precision=0), sol)
        self.assertEqual(
            print_latex_table(
                dataset=self.x_string, precision=0, best=0, axis=0, count_vals=0
            ),
            sol,
        )
        self.assertEqual(
            print_latex_table(
                dataset=self.x_string, precision=0, best=1, axis=C.ROW, count_vals=2
            ),
            sol,
        )
        sol = "a\\textgreater{}b & 1 & 2 & c \\\\\na \\& b \\textasciitilde{} c & 1\\% & b & 4 \\\\\n"
        self.assertEqual(
            print_latex_table(
                dataset=self.x_string, precision=0, labels=self.labels_special
            ),
            sol,
        )


class TestTranspose(unittest.TestCase):
    s = r'''
    \toprule
    A & B & C \\
    \midrule
    1 & 2 & 3 \\
    4 & 5 & 6 \\
    \bottomrule
    '''

    s1 = r'''
    1 & 2 & 3 \\
    4 & 5 & 6 \\
    \bottomrule
    '''
    def test_correct(self):
        s_transpose = '''\\toprule\nA & 1 & 4 \\\\ \n\midrule\nB & 2 & 5 \\\\ \nC & 3 & 6 \\\\ \n\\bottomrule'''
        self.assertEqual(transpose_latex_table(self.s), s_transpose)
        s_transpose = '''\\toprule\n1 & 4 \\\\ \n\midrule\n2 & 5 \\\\ \n3 & 6 \\\\ \n\\bottomrule'''
        self.assertEqual(transpose_latex_table(self.s1), s_transpose)
