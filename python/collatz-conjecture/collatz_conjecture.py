def steps(number):
    if not isinstance(number, int) or number < 1:
        raise ValueError("Only positive integers are allowed")
    value = number
    counter = 0
    while value != 1:
        if value % 2 == 0:
            value //= 2
        else:
            value = value * 3 + 1
        counter += 1
    return counter