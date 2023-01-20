# Part 1
def my_sqrt(a):
    x = 24.5
    while True:
        y = (x + a / x) / 2.0
        if y == x:
            break
        x = y
    return y


print(my_sqrt(25))


# Part 2
def test_sqrt():
    import math
    a = 1
    while a <= 25:
        diff = my_sqrt(a) - math.sqrt(a)
        print('a =', a, '|my_sqrt(a) =', my_sqrt(a), '|math.sqrt(a) =', math.sqrt(a), '| diff =', abs(diff))
        a += 1


test_sqrt()
