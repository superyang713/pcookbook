"""
Problem:
You want to combine many small strings together into a larger string.

Solution:
If the strings to combine are found in a sequence or iterable, the fastest way
to combine them is to use the join() method.
"""

# Example 1: use join() method
parts = ['Is', 'Chicago', 'Not', 'Chicago']
joined = ' '.join(parts)
print(joined)

joined = ','.join(parts)
print(joined)

# Example 2: + operator is inefficient due to the memory copies and garbage
# collection. The fastest way to combine is to use generator together with
# join() method, as discussed in recipe 1.19
data = ['ACME', 50, 91.1]
result = ','.join(str(d) for d in data)
print(result)

# Example 3: Be on the lookout for unnecessary string concatenations.
print(a + ':' + b + ':' + c)  # Ugly
print(':'.join([a, b, c]))    # Still ugly
print(a, b, c, sep=':')       # Better
