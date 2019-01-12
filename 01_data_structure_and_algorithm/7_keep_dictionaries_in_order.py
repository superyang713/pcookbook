"""
Problem:
You want to create a dictionary, and  you also want to control the order of
items when iterating or serializing.

Solution:
To control the order of items in a dictionary, you can use OrderedDict from
the collections module. It exactly preserves the original insertion order
of data when iterating.
"""

from collections import OrderedDict
import json

# Example 1:
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])

# Example 2: precisely control the order of fields appearing in a JSON encoding

result = json.dumps(d)
print(result)
