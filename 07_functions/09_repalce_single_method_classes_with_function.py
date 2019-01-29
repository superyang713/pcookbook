"""
Problem:
You have a class that only defines a single method besides __init__(). However,
to simply your code, you would much rather just have a simple function.

Solution:
In many cases, single-method classes can be turned into functions using
closures.
"""

from urllib.request import urlopen


class UrlTemplate:
    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))


# Example use. Download stock data from yahoo
yahoo = UrlTemplate(
    "https://finance.yahoo.com/d/quotes.csv?s={names}$f={fields}")
for line in yahoo.open(names="IBM,AAPL,FB", fields="sl1c1v"):
    print(line.decode("utf-8"))


# This class could be replaced with a much simpler function:
def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))

    return opener


yahoo = UrlTemplate(
    "https://finance.yahoo.com/d/quotes.csv?s={names}$f={fields}")
for line in yahoo(names="IBM,AAPL,FB", fields="sl1c1v"):
    print(line.decode("utf-8"))


# Whenever you're writing code and you enounter the problem of attaching
# additonal state to a function, think closures.
