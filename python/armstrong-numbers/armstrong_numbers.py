def is_armstrong_number(number):
    if number <= 0:
        return True
    digits = [int(d) for d in str(number)]
    n = len(digits)
    armstrong_sum = sum(d ** n for d in digits)
    return armstrong_sum == number
