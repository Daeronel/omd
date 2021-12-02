import pytest
from one_hot_encoder import fit_transform


@pytest.mark.parametrize('input, expected',
                         [(['Moscow', 'New York', 'Moscow', 'London'], [('Moscow', [0, 0, 1]),
                                                                        ('New York', [0, 1, 0]),
                                                                        ('Moscow', [0, 0, 1]),
                                                                        ('London', [1, 0, 0])]),
                          (['Moscow'], [('Moscow', [1])]),
                          ([], []),
                          ('', [('', [1])])])
def test_ft(input, expected):
    assert fit_transform(input) == expected


def test_exception():
    with pytest.raises(TypeError):
        fit_transform()
