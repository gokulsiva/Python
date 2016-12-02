import sys
import os
from math import sqrt #This is use sqrt(x) instead of math.sqrt(x)
print 'The command line arguments are : '
for i in sys.argv:
    print i
print '\n\nPython path is',sys.path
print os.getcwd()
print sqrt(4)
