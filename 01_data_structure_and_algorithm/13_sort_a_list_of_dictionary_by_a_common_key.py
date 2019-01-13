"""
Problem:
You have a list of dictionaries and you would like to sort the entries according
to one or more of the dictionary values.

Solution:
Sorting this type of structure is easy using the operator module's itemgetter
function. 
"""
from operator import itemgetter
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'Jone', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
]

# It is fairly easy to output these rows ordered by any of the fields common to
# all of the dictionaries. For example:
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
rows_by_lname = sorted(rows, key=lambda x: x['lname'])
print(rows_by_fname)
print(rows_by_uid)
print(rows_by_lname)

# The itemgetter() function can also accept multiple keys. For example:
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)

# itemgetter() is sometimes replaced by lambda exprerssion, and it works fine,
# but the solution involving itemgetter() typically runs a bit faster. And both
# can be applied to functions such as min() and max().
print(min(rows, key=itemgetter('uid')))
