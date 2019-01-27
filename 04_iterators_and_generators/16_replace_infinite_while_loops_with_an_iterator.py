"""
Problem:
you have code that uses a while loop to iteratively process data because it
involves a function or some kind of unusual test condition that doesn't fall
into the usual iteration pattern.

Solution:
Use built-in iter() function. 
"""
CHUNKSIZE = 8192

def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        process_data(data)

# The code above can be replaced using iter()
def reader(s):
    for data in iter(lambda: s.recv(CHUNKSIZE), b''):
        process_data(data)


# A little-known feature of the built-in iter() function is that it optionally
# accepts a zero-argument callable and sentinel (terminating) value as inputs.
# When used in this way, it creates an iterator that repeatedly calls the
# supplied callable over and over again until it return the value given as a
# sentinel.

# The following is a simple example of an infinite loop using for loop.
for x in iter(int, 1):
    pass
