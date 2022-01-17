import re


def validate_input_value(input_data: str) -> bool:
    """ Check if input value compare with correct pattern """
    len_input_data = len(input_data)
    match_result = re.match('\d+x\d+(\(\d+,\d+\))+', input_data)
    if match_result:
        if match_result.end() == len_input_data:
            return True
    raise Exception(f"""Error: You have specified incorrect argument. """
                    f""" Fix it and try again. Example correct argument "5x5 (1, 3) (4, 4)" """)

