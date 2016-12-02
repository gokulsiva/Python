x = 50


def local(x):
    print 'x is', x
    x = 2
    print 'local x is changed to', x

local(x)
print 'Outer x value is',x
