import sys
import time


f = None
try:
    f = open("poem.txt","r")
    while True:
        line = f.readline()
        if line == '':
            break
        print line
        sys.stdout.flush()
        print "Ctrl+c to exit"
        time.sleep(2)
except IOError:
    print 'Could not find the file'
except KeyboardInterrupt:
    print 'You cancelled the operation'
finally:
    if f:
        f.close()
        print 'Filed Closed'
