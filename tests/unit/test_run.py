from bot.run import get_input_data
from unittest import mock
import pytest


@mock.patch('sys.argv', ['run.py', ''])
def test_get_input_with_empty_data():
    """ Test of function with empty data """
    with pytest.raises(Exception):
        get_input_data()


@mock.patch('sys.argv', ['run.py'])
def test_get_input_without_data():
    """ Test of function without data """
    with pytest.raises(Exception):
        get_input_data()


@mock.patch('sys.argv', ['run.py', '5x5 (1, 3) (4, 4)'])
def test_get_input_with_correct_data():
    """ Test of function with correct data """
    assert get_input_data() == '5x5 (1, 3) (4, 4)'.replace(' ', '')
