def update_dictionary(dct, key, value):
    """
    - Updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Returns the updated dictionary.
    """
    if not isinstance(dct, dict):
        return -1  # Optional: handle non-dictionary inputs
    
    if key in dct:
        print(f"Original value for '{key}': {dct[key]}")
    
    dct[key] = value
    return dct


# Task 2 - Test cases
print(update_dictionary({}, "name", "Alice"))
print(update_dictionary({"age": 25}, "age", 26))