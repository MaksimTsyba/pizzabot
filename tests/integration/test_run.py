from bot.run import run
from unittest import mock
import pytest


@mock.patch('sys.argv', ['run.py', ''])
def test_get_input_with_empty_data():
    """ Test of function with empty data """
    with pytest.raises(Exception):
        run()


@mock.patch('sys.argv', ['run.py', '5x5 (1, 3) (4, 4)'])
def test_get_input_with_correct_data():
    """ Test of function with correct data """
    assert run() == 'ENNNDEEEND'


@mock.patch('sys.argv', '5x5 (1, 3) (4, 6)')
def test_get_input_with_incorrect_value():
    """ Test of function with incorrect value """
    with pytest.raises(Exception):
        run()


@mock.patch('sys.argv', '5x5 (1, ) (4, 6)')
def test_get_input_with_incorrect_input_data():
    """ Test of function with incorrect input data """
    with pytest.raises(Exception):
        run()

