import unittest
from one_hot_encoder import fit_transform


class TestFitTrancform(unittest.TestCase):
    def fit_transform(self):
        result = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
        expected = [('Moscow', [0, 0, 1]),
                    ('New York', [0, 1, 0]),
                    ('Moscow', [0, 0, 1]),
                    ('London', [1, 0, 0])]
        self.assertEqual(result, expected)

