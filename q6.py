def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")

    i = 0
    # Traversing using the WHILE loop based upon the length of the input string."i" is used as a counter to mark the position.
    while i < len(lst):
        if isinstance(lst[i], (int, float)) and lst[i] < 0:
            return lst[i]
        i += 1
    
    return "No negatives"


# Example usage
print(find_first_negative([3, 5, -2, 7, -9]))  # -2
print(find_first_negative([1, 2, 3]))          # No negatives