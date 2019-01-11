"""
Problem:
You want to make a dictonary that maps keys to more than one value (a so-called
'multidict').

Solution:
You need to store the multiple values in another container such as a list or
set.
"""

# Example 1:
d = {
    'a': [1, 2, 3],
    'b': [4, 5],
}

e = {
    'a': {1, 2, 3},
    'b': {4, 5},
}

# Example 2: To easily construct such dictionary, you can use defaultdict in
# the collections module. A feature of defaultdict is that it automatically
# initialize the first value so you can simply focus on adding items.
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(d)

# Discussion: In principle, constructing a multivalued dictionary is simple,
# however, initialization of the first value can be messy if you do it
# youself, for example, the following code looks messay:
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)

# Using the defaultdict simply leads to much cleaner code
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
