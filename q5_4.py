def add_numbers(*args):
    """
    Function Name: add_numbers
    Description: This function accepts a variable number of integer arguments 
                 and returns their sum.
    Parameters:
        *args : variable length argument list (integers)
    Returns:
        int : the sum of all integers passed as arguments
    Example:
        add_numbers(2, 3, 4) → 9
    """
    total = sum(args)
    return total


# Main Program
print("Sum of numbers:", add_numbers(10, 20, 30, 40))
print("Sum of numbers:", add_numbers(5, 15))
print("Sum of numbers:", add_numbers(1, 2, 3, 4, 5, 6))

# Displaying docstring
print("\nFunction Documentation:")
print(add_numbers.__doc__)
