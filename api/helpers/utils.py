def check_if_input_is_number(input_value):
    """function to checks if input value is a number"""
    if isinstance(input_value, int) or isinstance(input_value, float):
        return True
    return False

def check_if_input_value_is_string(input_value):
    """function to checks if input value  is a string"""
    if (
        isinstance(input_value, str)
        and not str(input_value).isspace()
        and not input_value.isnumeric()
    ):
        return True
    return False

def check_if_input_contains_space(input_value):
    """function to checks if input value contains space"""
    if " " in input_value or len(str(input_value).split(" ")) > 1:
        return True
    return False
