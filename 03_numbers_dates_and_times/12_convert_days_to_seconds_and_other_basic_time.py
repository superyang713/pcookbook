"""
Problem:
You have code that needs to perform simple time conversions, liek days to
seconds, hours to minutes, and so on.

Solution:
Use datatime module.
"""

from datetime import timedelta
from datetime import datetime


# Example 1: perform conversions and arithmetic involving different units of
# time, use the datetiem module.
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days)
print(c.seconds)
print(c.total_seconds() / 3600)

# Example 2: represent specific dates and times, create datetime instances
# and use the standard mathematical operations to manipulate them.
a = datetime(2012, 9, 23)
print(a + timedelta(days=10))

b = datetime(2012, 12, 21)
d = b - a
print(d.days)

now = datetime.today()
print(now.date())
print(now + timedelta(minutes=10))
