def swap_values(x, y):
    # Check if both x and y are numeric else it would return an error message
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        print("Only numeric is allowed for function")        
        return -1
    
    # Swap without using any extra variable
    x = x + y
    y = x - y
    x = x - y

    print("Swapped values:")
    print("x =", x)
    print("y =", y)


print(swap_values("apple", 10))
print(swap_values(9, 17))
