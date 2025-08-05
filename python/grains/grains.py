def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")    
    grains = 2**(number-1)       
    
    return grains 


def total():
    try:
        result = int(2*(square(64)))-1
        return result
    except Exception as exc:
        raise ValueError(str(exc))
    
