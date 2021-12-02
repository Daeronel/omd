from what_is_year_now import what_is_year_now
from unittest.mock import patch, MagicMock
import json
import pytest

TEST_RESPONSE_1 = {'$id': '1',
                   'currentDateTime': '02.12.2021T18:33Z',
                   'currentFileTime': 132829435921950587,
                   'dayOfTheWeek': 'Thursday',
                   'isDayLightSavingsTime': False,
                   'ordinalDate': '2021-336',
                   'serviceResponse': None,
                   'timeZoneName': 'UTC',
                   'utcOffset': '00:00:00'}

TEST_RESPONSE_2 = {'$id': '1',
                   'currentDateTime': '2021/12/02',
                   'currentFileTime': 132829435921950587,
                   'dayOfTheWeek': 'Thursday',
                   'isDayLightSavingsTime': False,
                   'ordinalDate': '2021-336',
                   'serviceResponse': None,
                   'timeZoneName': 'UTC',
                   'utcOffset': '00:00:00'}


def test_result():
    actual = what_is_year_now()
    expected = 2021
    assert actual == expected


def test_valid():
    with patch.object(json, "load", return_value=TEST_RESPONSE_1):
        actual = what_is_year_now()
    expected = 2021
    assert actual == expected


def test_invalid():
    with patch.object(json, "load", return_value=TEST_RESPONSE_2):
        with pytest.raises(ValueError):
            what_is_year_now()
