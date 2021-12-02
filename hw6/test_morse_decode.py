import pytest
from morse import decode


@pytest.mark.parametrize('morse, text',
                         [('... --- ...', 'SOS'),
                          ('-.-. .- - -..-. -.. --- --. ..--..', 'CAT/DOG?'),
                          ('..--- ----- ..--- .----', '2021')])

def test_decode(morse, text):
    assert decode(morse) == text
