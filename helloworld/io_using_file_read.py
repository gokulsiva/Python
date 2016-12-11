f = open("poem.txt")
while True:
    t = f.readline()
    if t != '':
        print t
    else:
        break
f.close()
