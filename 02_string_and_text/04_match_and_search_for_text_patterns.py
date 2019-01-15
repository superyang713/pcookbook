"""
Problem:
You want to match or search text for a specific pattern.

Solution:
Regular expression
"""
import re

# Example 1:
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')

# Example 2: if you are going to perform a lot of matchs using the same
# pattern, if usually pays to precompile the regular expression pattern
# into a pattern object first:
datepat = re.compile(r'\d+/\d+/\d+')

if datepat.match(text1):
    print('yes')
else:
    print('no')

if datepat.match(text2):
    print('yes')
else:
    print('no')

# Example 3: if you want to search text for all occurrences of a pattern,
# use the findall() method instead.
text = 'Today is 11/27/2012. PyCon starts 3/12/2013.'
result = datepat.findall(text)
print(result)


# Example 4: Capture groups often simplify subsequent processing of the
# matched text because the contents of each group can be extracted individually
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())

# Find all matches (notice splitting into tuples)
result = datepat.findall(text)
print(result)
for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))
