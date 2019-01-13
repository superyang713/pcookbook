"""
Problem:
You have data inside of a sequence, and need to extract values or reduce the
sequence using some criteria.

Solution:
The easiest way to filter sequence data is often to use a list comprehension.
"""
from itertools import compress
# Example 1: list comprehension. Might be slow if the original input is large.
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
positive_list = [n for n in mylist if n > 0]
negative_list = [n for n in mylist if n < 0]
print(positive_list)
print(negative_list)

# Example 2: generator expression. It produces the filtered values iteratively.
pos = (n for n in mylist if n > 0)
for x in pos:
    print(x)

# Example 3: If filtering criteria is complicated, put the filtering code into
# its own its own function and use the built-in filter() function.
values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, values))
print(ivals)

# Example 4: another notable filtering tool is itertools.compress(). It is
# useful if you are trying to apply the results of filtering one sequence
# to another related sequence.
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

counts = [0, 3, 10, 4, 1, 7, 6, 1]
more5 = [n > 5 for n in counts]
result = list(compress(addresses, more5))
print(result)
