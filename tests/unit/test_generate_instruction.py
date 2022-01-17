from bot.pizzabot import Pizzabot
import pytest


class TestPizzabot:
    """ Test Pizzabot class """

    def test_generate_instruction_with_correct_value(self):
        """ Test of generator instruction with correct value """
        input_data = "5x5 (1, 3) (4, 4)".replace(' ', '')
        get_instruction = Pizzabot(input_data).generate_instruction()
        assert get_instruction == 'ENNNDEEEND'

    def test_generate_instruction_with_incorrect_value(self):
        """ Test of generator instruction with value that don't fit to grid sizes  """
        input_data = "5x5 (1, 3) (6, 7)".replace(' ', '')

        with pytest.raises(Exception):
            Pizzabot(input_data).generate_instruction()
