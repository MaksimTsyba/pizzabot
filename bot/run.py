from bot.pizzabot import Pizzabot
from bot.validator import validate_input_value
import sys
sys.tracebacklimit = 0


def get_input_data() -> str:
    """ Get input data """
    arguments = sys.argv
    if len(arguments) > 1:
        if arguments[1]:
            argument = sys.argv[1].replace(' ', '')
            return argument
    raise Exception("""Error: You need to specify argument. Example argument "5x5 (1, 3) (4, 4)" """)


def run() -> str:
    """ Run Pizzabot """
    input_data = get_input_data()
    validate_input_value(input_data)
    instruction = Pizzabot(input_data).generate_instruction()
    return instruction


if __name__ == "__main__":
    result = run()
    sys.stdout.write(f"Instruction for Pizzabot: {result} \n")