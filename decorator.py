#! python2.7
# decorator.py - log some strings before and after the function running.

def log(func):
    def wrapper(*args, **kw):
        print 'begin call'
        out = func(*args, **kw)
        print 'end call'
        return out
    return wrapper

@log
def f():
    print 'function'

f()
