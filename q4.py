def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Convert the string to a list of characters
    char_list = list(s)
    
    # Reverse the list in place
    char_list.reverse()
    
    # Join the list back into a string
    return ''.join(char_list)


# Task 2
print(string_reverse("Hello World"))  # dlroW olleH
print(string_reverse("Python"))       # nohtyP