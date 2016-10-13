#! python2.7
# ListComrehensions.py - generate a list which only contains lower case strings.

L = ['Hello', 'World', 18, 'Apple', None]
print [s.lower() for s in L if isinstance(s, str)]
