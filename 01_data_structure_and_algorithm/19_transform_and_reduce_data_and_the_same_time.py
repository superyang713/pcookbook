"""
Problem:
You need to execute a reduction function (e.g., sum(), min(), max()), but first
need to transform or filter the data.

Solution:
A very elegant way to combine a data reduction and transformation is to use a
generator-expression argument. You don't need repeated parentheses.
"""

import os

# Example 1: if you want to calculate the sum of squares, do the following:
nums = [1, 2, 3, 4, 5]
# The following two are the same.
s = sum(x * x for x in nums)
s = sum((x * x for x in nums))
print(s)

# Example 2:
files = os.listdir('01_data_structure_and_algorithm')
if any(name.endswith('py') for name in files):
    print('There are python!')
else:
    print('Sorry, no python')

# Example 3: output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# Example 4: Data reduction across fields of a data structure.
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65},
]

min_shares = min(s['shares'] for s in portfolio)
print(min_shares)
