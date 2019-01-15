"""
Problem:
You want to search for and replace a text pattern in a string.
"""
import re
# Example 1: for simple literal patterns, use the str.replace() method.
text = 'yeah, but no, but yeah, but no, but yeah'

text.replace('yeah', 'yep')
print(text)

# Example 2: for more complicated patterns, use the sub() functions/methods
# in the re module.
text = 'Today is 11/27/2012. PyCon starts 3/12/2013.'
text = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(text)
