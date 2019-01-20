"""
Problem:
Your applicatio receives temporal data in string format, but you want to
convert those strings into datetime objects in order to perform nonstring
operations on them.

Solution:
datetime.strptime will work.
"""

from datetime import datetime

# Example 1: 
text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
diff = z - y
print(diff)

# Example 2: these format placeholders also work in reverse, in case you
# need to represent a datetime object in string output and make it nice.
nice_z = datetime.strftime(z, '%A %B %d, %Y')
print(nice_z)

# Example 3: strptime() is often low performance. If you need to deal with
# a lot of dates and you know the precise format, you should use a custom
# solution instead. For example, if the format is like "YYYY-MM-DD"
def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))
