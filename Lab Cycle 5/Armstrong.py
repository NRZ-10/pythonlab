# Armstrong.py

def is_armstrong(number):
    """
    Check whether a number is an Armstrong number.
    An Armstrong number is a number that is equal to the sum of its digits
    raised to the power of the number of digits.
    """
    num_str = str(number)
    num_digits = len(num_str)
    total = sum(int(digit) ** num_digits for digit in num_str)
    return total == number
