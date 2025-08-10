def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    # Validate input types
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        raise TypeError("Both num and divisor must be numeric")
    
    # Prevent division by zero
    if divisor == 0:
        raise ValueError("Divisor cannot be zero")
    
    # Check divisibility using MOD/modulo funtion
    return num % divisor == 0


# Example usage
print(check_divisibility(10, 2))  # True
print(check_divisibility(10, 3))  # False