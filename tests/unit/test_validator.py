from bot.validator import validate_input_value
import pytest


def test_validate_input_value_with_correct_data():
    """ Test of input validator with correct data """
    input_data = "5x5 (1, 3) (4, 4)".replace(' ', '')
    assert validate_input_value(input_data)


def test_validate_input_value_with_incorrect_grid_points():
    """ Test of input validator with incorrect grid_points """
    input_data = "5x5 (1, 3, 6) (4, 4)".replace(' ', '')
    with pytest.raises(Exception):
        validate_input_value(input_data)


def test_validate_input_value_without_grid_size():
    """ Test of input validator without grid size """
    input_data = "(1, 3) (4, 4)".replace(' ', '')
    with pytest.raises(Exception):
        validate_input_value(input_data)


def test_validate_input_value_without_grid_points():
    """ Test of input validator without grid points """
    input_data = "5x5"
    with pytest.raises(Exception):
        validate_input_value(input_data)


def test_validate_input_value_with_empty_value():
    """ Test of input validator with empty data """
    input_data = ""
    with pytest.raises(Exception):
        validate_input_value(input_data)
