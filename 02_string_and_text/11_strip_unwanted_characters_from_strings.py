"""
Problem:
You want to strip unwanted characters, such as whitespace, from the beginning,
end, or middle of a text string.

Solution:
The strip() method can be used to strip characters from the beginning or end of
a string.
"""

import re

# Example 1:

s = '   hello world    \n'
print(s.lstrip())
print(s.rstrip())
print(s.strip())

t = '---------hello=============='
print(t.lstrip('-'))
print(t.rstrip('='))
print(t.strip('-='))

# Example 2: To do something to the inner space, you would need to use
# replace() method or a regular expression substitution.
print(s.replace(' ', ''))
print(re.sub(r'\s+', ' ', s.strip()))

# Example 3: it is useful to combine string stripping operations with some
# other kind of iterative processing, such as reading lines of data from a
# file. If so, this is one area where a generator expression can be useful.
with open('05_search_and_replace_text.py') as fin:
    lines = (line.strip() for line in fin)
    for line in lines:
        print(line)
