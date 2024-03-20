def factorial(n):
    """Calculate the factorial of a non-negative integer."""
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


def sine_taylor_series(x, terms=10):
    """
    Calculate the sine of an angle 'x' (in radians) using the Taylor series expansion.

    Parameters:
        x (float): The angle in radians for which to calculate the sine.
        terms (int): The number of terms to use in the Taylor series expansion. Default is 10.

    Returns:
        float: The approximate value of sine of 'x'.
    """
    sine = 0.0
    for n in range(terms):
        coefficient = (-1) ** n
        term = coefficient * (x ** (2 * n + 1)) / factorial(2 * n + 1)
        sine += term
    return sine


# Test the function
angle_degrees = 30
angle_radians = angle_degrees * (3.14159 / 180)  # Convert degrees to radians
print("Approximate sine of", angle_degrees, "degrees:", sine_taylor_series(angle_radians))
