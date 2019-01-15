"""
Problem:
You need to check the start or end of a string for specific text patterns,
such as filename extension, URL schemes, and so on.

Solution:
A siimple way is to use the str.startswith() or str.endswith() methods.
"""
# Example 1:
filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file:'))

url = 'http://www.python.org'
print(url.startswith('http:'))

# Example 2: if you need to check against multiple choices, simply provide
# a tuple of possibilities to startswith() or endswith():
filenames = ['Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h']
c_files = [f for f in filenames if f.endswith(('c', '.h'))]
print(c_files)
print(any(name.endswith('.py') for name in filenames))

# Discussion:
# endswith() and startswith() are better to perform basic prefix and suffix
# checking. similar operations can be performed with slices or regular
# expression, but far less elegant.
