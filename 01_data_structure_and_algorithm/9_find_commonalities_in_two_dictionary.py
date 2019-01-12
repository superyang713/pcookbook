"""
Problem:
You have two dictionaries and want to find out what they might have in common
(same keys, same values, etc.).

Solution:
Perform common set operations using the keys() or items() methods.
"""
a = {
    'x': 1,
    'y': 2,
    'z': 3,
}

b = {
    'w': 10,
    'x': 11,
    'y': 2,
}

# Find keys in common
result = a.keys() & b.keys()
print(result)

# Find keys in a that are not in b
result = a.keys() - b.keys()
print(result)

# Find (key, value) pairs in common
result = a.items() & b.items()
print(result)

# These kinds of operation can also be used to alter or filter dictionary
# contents. For example, suppose you want to make a new dict with selected keys
# removed.
result = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(result)
