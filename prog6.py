alphabet = "abcdefghijklmnopqrstuvwxyz"

test_dups = ["zzz", "dog", "bookkeeper", "subdermatoglyphic", "subdermatoglyphics"]

test_miss = ["zzz", "subdermatoglyphic", "the quick brown fox jumps over the lazy dog"]


# The histogram function
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


# The has_duplicates function
def has_duplicates(a):
    g = histogram(a)
    for x, y in g.items():
        if y > 1:
            return True
            break
    return False


# Looping through the strings in the list test_dups
for b in test_dups:
    if has_duplicates(b):
        print(b, 'has duplicates')
    else:
        print(b, 'has no duplicates')


# Part 2
# The function missing_letters
def missing_letters(c):
    h = histogram(c)
    e = []
    for d in alphabet:
        if d not in h:
            e.append(d)
    return ''.join(e)


# Looping through the strings
for j in test_miss:
    n = missing_letters(j)
    if len(n):
        print(j, 'is missing letters', n)
    else:
        print(j, 'uses all the letters')
