def find_and_replace(lst, find_val, replace_val):
    """
    - Searches for all occurrences of find_val in lst
      and replaces them with replace_val.
    - lst must be a list.
    - Returns the modified list.
    """
    if not isinstance(lst, list):
        print("Error item is not found within the listing")
        return -1  # or raise an error if preferred
    
    # Replace all matching values
    new_list = []
    for item in lst:
        if item == find_val:
            new_list.append(replace_val)
        else:
            new_list.append(item)
    return new_list

# Example usage:
print(find_and_replace([1, 2, 3, 2, 4], 2, 99))   # [1, 99, 3, 99, 4]
print(find_and_replace("not a list", 2, 99))      # -1
