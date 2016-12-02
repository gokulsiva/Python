x = 50


def func():
    global x
    print 'x is',x
    x = 2
    print 'now x is',x


func()
print 'outer x is',x
