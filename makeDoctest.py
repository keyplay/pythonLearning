#! python2.7
# -*- coding: utf-8 -*-
# makeDoctest.py - test a function using doctest.

def fact(n):
    '''
    Iterative multiplication
    
    >>> fact(1)
    1
    >>> fact(3)
    6
    >>> fact(0)
    Traceback (most recent call last):
        ...
    ValueError
    >>> fact(-1)
    Traceback (most recent call last):
        ...
    ValueError
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    import doctest
    #print doctest.__file__ 
    doctest.testmod()
