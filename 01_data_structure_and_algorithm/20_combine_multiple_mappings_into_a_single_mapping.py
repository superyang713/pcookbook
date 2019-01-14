"""
Problem:
You have multiple dictionaries or mappings that you want to logically combine
into a single mapping to perform certain operations, such as looking up values
or checking for the existence of keys.

Solution:
Use collections.ChainMap
"""

from collections import ChainMap

# Example 1: Suppose you want to perform lookups where you have to check both
# dictionaries. If there is duplicates, the values from the first mapping get
# used.

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)
print(c['x'])
print(c['y'])
print(c['z'])
print(list(c.keys()))
print(len(c))

# Explanation: operations that mutate the mapping always affect the first
# mapping listed. For example:
c['z'] = 10
c['w'] = 40
del c['x']
print(a)
# The following expression will lead to a traceback: del c['y']

# Example 3: A ChainMap is particularly useful when working with scoped
# values such as variables (i.e., globals, locals, etc.).
values = ChainMap()
values['x'] = 1
# Add a new mapping
values = values.new_child()
values['x'] = 2
# Add a new mapping
values = values.new_child()
values['x'] = 3

print(values)
print(values['x'])

# Discard last mapping
values = values.parents
print(values['x'])

# Discard last mapping
values = values.parents
print(values['x'])
