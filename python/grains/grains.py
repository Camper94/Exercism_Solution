def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    grains = 2**(number-1)       
    return grains 


def total():
    try:
        result = 0
        for i in range(1, 65):
            result += square(i)
        return result
    except Exception as exc:
        raise ValueError(str(exc))
    
