def factorial(n):
    """Calculate the factorial of a given number."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Test the function
number = 5
print("The factorial of", number, "is:", factorial(number))  # Output: The factorial of 5 is: 120
