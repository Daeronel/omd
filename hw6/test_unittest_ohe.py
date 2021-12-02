import unittest
from one_hot_encoder import fit_transform


class TestFitTrancform(unittest.TestCase):
    def test_fit_transform(self):
        actual = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
        expected = [('Moscow', [0, 0, 1]),
                    ('New York', [0, 1, 0]),
                    ('Moscow', [0, 0, 1]),
                    ('London', [1, 0, 0])]
        self.assertEqual(actual, expected)

    def test_empty(self):
        actual = list(fit_transform([]))
        expected = []
        self.assertEqual(actual, expected)

    def test_one_word(self):
        actual = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
        expected = ('Moscow', [0, 0, 1])
        self.assertIn(expected, actual)

    def test_noargs(self):
        self.assertRaises(TypeError, fit_transform, )
