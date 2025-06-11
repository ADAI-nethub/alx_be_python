# programming_paradigm/robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Performs division with robust error handling.

    Args:
        numerator: The number to be divided.
        denominator: The number to divide by.

    Returns:
        A string indicating the result or an error message.
    """
    try:
        # Attempt to convert to float
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        # Attempt to perform division
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."