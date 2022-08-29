import unittest
from utils_unibs.plots import set_size, CS, _update_dimension, plt


def reset_values():
    set_size("small", 10)
    set_size("medium", 15)
    set_size("big", 20)


class TestSetSize(unittest.TestCase):
    def test_unknown(self):
        self.assertFalse(set_size("sdadfgds", 100))
        self.assertFalse(set_size(4, 30))
        self.assertFalse(set_size("small", "s"))

    def test_small(self):
        self.assertTrue(set_size("smAll", 1))
        self.assertEqual(CS.small_size, 1)
        self.assertEqual(plt.rcParams["font.size"], 1)
        self.assertTrue(set_size(" SMALL  ", "4"))
        self.assertEqual(CS.small_size, 4)
        self.assertEqual(plt.rcParams["font.size"], 4)
        reset_values()
        self.assertFalse(set_size("small", 15))
        self.assertFalse(set_size("small", 0))

    def test_medium(self):
        self.assertTrue(set_size("MEDIUM", 12))
        self.assertEqual(CS.medium_size, 12)
        self.assertEqual(plt.rcParams["xtick.labelsize"], 12)
        self.assertTrue(set_size("  mEdium  ", "18"))
        self.assertEqual(CS.medium_size, 18)
        self.assertEqual(plt.rcParams["xtick.labelsize"], 18)
        reset_values()
        self.assertFalse(set_size("medium", 20))
        self.assertFalse(set_size("medium", 10))

    def test_big(self):
        self.assertTrue(set_size("BiG", 20))
        self.assertEqual(CS.big_size, 20)
        self.assertTrue(set_size(" biG  ", "50"))
        self.assertEqual(CS.big_size, 50)
        reset_values()
        self.assertFalse(set_size("big", 15))


class TestUpdateDimension(unittest.TestCase):
    def test_unknown(self):
        self.assertFalse(_update_dimension("fdsfds", "small"))
        self.assertFalse(_update_dimension("font", "dsadsad"))
        self.assertFalse(_update_dimension(1, 5))

    def test_font(self):
        self.assertTrue(_update_dimension(" FonT    ", "sMaLL"))
        self.assertEqual(plt.rcParams["font.size"], 10)
        self.assertTrue(_update_dimension("font", "medium"))
        self.assertEqual(plt.rcParams["font.size"], 15)
        self.assertTrue(_update_dimension("font", "  BIG  "))
        self.assertEqual(plt.rcParams["font.size"], 20)
        self.assertFalse(_update_dimension("font", " czfz"))

    def test_axes_title(self):
        self.assertTrue(_update_dimension(" axEs TITLe   ", "sMaLL"))
        self.assertEqual(plt.rcParams["axes.titlesize"], 10)
        self.assertTrue(_update_dimension("axes title", "medium"))
        self.assertEqual(plt.rcParams["axes.titlesize"], 15)
        self.assertTrue(_update_dimension("axes title", "  BIG  "))
        self.assertEqual(plt.rcParams["axes.titlesize"], 20)
        self.assertFalse(_update_dimension("axes title", " czfz"))
        self.assertFalse(_update_dimension("axes  title", "big"))

    def test_axes_label(self):
        self.assertTrue(_update_dimension(" axes LABEL    ", "sMaLL"))
        self.assertEqual(plt.rcParams["axes.labelsize"], 10)
        self.assertTrue(_update_dimension("axes label", "medium"))
        self.assertEqual(plt.rcParams["axes.labelsize"], 15)
        self.assertTrue(_update_dimension("axEs lABEL", "  BIG  "))
        self.assertEqual(plt.rcParams["axes.labelsize"], 20)
        self.assertFalse(_update_dimension("axes label", " czfz"))
        self.assertFalse(_update_dimension("axes  label", "big"))

    def test_xtick(self):
        self.assertTrue(_update_dimension(" xtick    ", "sMaLL"))
        self.assertEqual(plt.rcParams["xtick.labelsize"], 10)
        self.assertTrue(_update_dimension("XtiCk", "medium"))
        self.assertEqual(plt.rcParams["xtick.labelsize"], 15)
        self.assertTrue(_update_dimension("xtick", "  BIG  "))
        self.assertEqual(plt.rcParams["xtick.labelsize"], 20)
        self.assertFalse(_update_dimension("xtick", " czfz"))

    def test_ytick(self):
        self.assertTrue(_update_dimension(" ytick ", "sMaLL"))
        self.assertEqual(plt.rcParams["ytick.labelsize"], 10)
        self.assertTrue(_update_dimension("YtiCk", "medium"))
        self.assertEqual(plt.rcParams["ytick.labelsize"], 15)
        self.assertTrue(_update_dimension("ytick", "  BIG  "))
        self.assertEqual(plt.rcParams["ytick.labelsize"], 20)
        self.assertFalse(_update_dimension("ytick", " czfz"))

    def test_legend_title(self):
        self.assertTrue(_update_dimension(" LEGend TITLe  ", "sMaLL"))
        self.assertEqual(plt.rcParams["legend.title_fontsize"], 10)
        self.assertTrue(_update_dimension("legend title", "medium"))
        self.assertEqual(plt.rcParams["legend.title_fontsize"], 15)
        self.assertTrue(_update_dimension("legend title", "  BIG  "))
        self.assertEqual(plt.rcParams["legend.title_fontsize"], 20)
        self.assertFalse(_update_dimension("legend title", " czfz"))
        self.assertFalse(_update_dimension("legend  title", "big"))

    def test_legend_font(self):
        self.assertTrue(_update_dimension(" lEGEnd FONt    ", "sMaLL"))
        self.assertEqual(plt.rcParams["legend.fontsize"], 10)
        self.assertTrue(_update_dimension("legend font", "medium"))
        self.assertEqual(plt.rcParams["legend.fontsize"], 15)
        self.assertTrue(_update_dimension("LEgEND font", "  BIG  "))
        self.assertEqual(plt.rcParams["legend.fontsize"], 20)
        self.assertFalse(_update_dimension("legend font", " czfz"))
        self.assertFalse(_update_dimension("legend  font", "big"))

    def test_title(self):
        self.assertTrue(_update_dimension(" TiTLe    ", "sMaLL"))
        self.assertEqual(plt.rcParams["figure.titlesize"], 10)
        self.assertTrue(_update_dimension("TITLE", "medium"))
        self.assertEqual(plt.rcParams["figure.titlesize"], 15)
        self.assertTrue(_update_dimension("title", "  BIG  "))
        self.assertEqual(plt.rcParams["figure.titlesize"], 20)
        self.assertFalse(_update_dimension("title", " czfz"))

    def test_latex(self):
        self.assertTrue(_update_dimension(" LAtEx    ", "TrUe"))
        self.assertEqual(plt.rcParams["text.usetex"], True)
        self.assertTrue(_update_dimension("latex", "  FALSE  "))
        self.assertEqual(plt.rcParams["text.usetex"], False)
        self.assertFalse(_update_dimension("latex", "small"))
