"""
Problem:
You need to search for and possibly replace text in a case-insensitive manner.

Solution:
YOu need to use the re module and supply the re.IGNORECASE flag to various
operations.
"""

import re

# Example 1:
text = "UPPER PYTHON, lower python, Mixed Python"
result = re.findall('python', text, flags=re.IGNORECASE)
print(result)
result = re.sub('python', 'snake', text, flags=re.IGNORECASE)
print(result)  # replacing text won't match the case of the matched text.


# Example 2: if you want to match the case of the matched text:
def match_case(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word

    return replace


result = re.sub('python', match_case('snake'), text, flags=re.IGNORECASE)
print(result)
