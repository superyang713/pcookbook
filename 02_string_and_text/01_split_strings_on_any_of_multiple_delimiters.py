"""
Problem:
You need to split a string into fields, but the delimiters (and spacing around
them) aren't consistent throughout the string.

Solution:
The split() method of string objects is really meant for very simple cases. In
case you need a bit more flexibility, use the re.split() method.
"""
import re

# Example 1:
line = 'asdf fjdk; afed, fjek,asfd,     foo'
words = re.split(r'[;,\s]\s*', line)
print(words)

# Example 2: when there is a capture group enclosed in parentheses, the matched
# text is also included.
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)

# Getting the split characters might be useful in certain contexts. For
# example, maybe you need the split characters later on to reform an output
# string:
values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)

# If you don't want the separator characters in the result, but still need to
# use parentheses to group parts of the regular expression pattern, make sure
# you use a noncapture group, specified as (?:...).
words = re.split(r'(?:,|;|\s)\s*', line)
print(words)
