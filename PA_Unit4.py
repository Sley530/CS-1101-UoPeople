def is_divisible(x, y):     # This is the is_divisible function from the textbook
    return x % y == 0

def is_power(a, b):         # This is the is_power function that takes two arguments
    if not is_divisible(a, b):   # This is the function is_power that calls the function is_divisible.
        return False
    if b == a:      # This is the code for the base case of the two arguments being equal
        return True
    elif b == 1:    # This is the code for the base case of the second argument being 1
        return False
    return is_power(int(a/b), b)    # This is the function is_power that calls itself recursively.

print('is_power(10, 2) returns:', is_power(10, 2))
print('is_power(27, 3) returns:', is_power(27, 3))
print('is_power(1, 1) returns:', is_power(1, 1))
print('is_power(10, 1) returns:', is_power(10, 1))
print('is_power(3, 3) returns:', is_power(3, 3))
