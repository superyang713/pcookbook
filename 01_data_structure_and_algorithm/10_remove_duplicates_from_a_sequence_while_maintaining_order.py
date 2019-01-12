"""
Problem:
You want to eliminate the duplicates values in a sequence, but preserve the
order of the remaining items.
"""


# Solution 1: if the values in the sequence are hashable, the problem can be
# easily solved using a set and a generator.
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
remove_duplicate = list(dedupe(a))
print(remove_duplicate)


# Solution 2: if the sequence is not hashable (such as dicts):
# For example, the following method can also be applied for reading a file,
# eliminating duplicate lines.
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
remove_duplicate = list(dedupe(a, key=lambda d: (d['x'], d['y'])))
print(remove_duplicate)

remove_duplicate = list(dedupe(a, key=lambda d: d['x']))
print(remove_duplicate)
