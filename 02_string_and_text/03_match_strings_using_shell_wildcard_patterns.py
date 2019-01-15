"""
Problem:
You want to match text using the same wildcard patterns as are commonly used
when working in Unix shells (e.g., *.py, Dat[0-9]*.csv, etc)

Solution:
The fnmatch module provides two functions--fnmatch() and fnmatchcase()--that
can be used to perform such matching.
"""

from fnmatch import fnmatch
# Example 1:
print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))

names = ['Dat1.csv', 'Dat2.csv', 'config.inif', 'foo.py']
dat_files = [name for name in names if fnmatch(name, 'Dat*.csv')]
print(dat_files)
