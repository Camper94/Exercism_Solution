EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time) : 
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    remaining_bake_time = EXPECTED_BAKE_TIME-elapsed_bake_time
    return remaining_bake_time

 
def preparation_time_in_minutes(number_of_layers) : 
    """Implement the elapsed_time_in_minutes(number_of_layers, 
    elapsed_bake_time) function that has two parameters: 
    number_of_layers (the number of layers added to the lasagna) 
    and elapsed_bake_time (the number of minutes the lasagna has 
    been baking in the oven). This function should return the total 
    number of minutes you've been cooking, or the sum of your preparation 
    time and the time the lasagna has already spent baking in the oven."""
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time): 
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    return elapsed_bake_time + preparation_time_in_minutes(number_of_layers)