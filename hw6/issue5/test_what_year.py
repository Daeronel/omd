import urllib
from what_is_year_now import what_is_year_now
from unittest.mock import patch
from io import StringIO
import pytest

TEST_RESPONSE_1 = '{"currentDateTime": "02.12.2021T18:33Z"}'

TEST_RESPONSE_2 = '{"currentDateTime": "2021/12/02"}'


def test_result():
    actual = what_is_year_now()
    expected = 2021
    assert actual == expected


def test_valid():
    with patch.object(urllib.request, 'urlopen', return_value=StringIO(TEST_RESPONSE_1)):
        actual = what_is_year_now()
    expected = 2021
    assert actual == expected


def test_invalid():
    with patch.object(urllib.request, 'urlopen', return_value=StringIO(TEST_RESPONSE_2)):
        with pytest.raises(ValueError):
            what_is_year_now()
