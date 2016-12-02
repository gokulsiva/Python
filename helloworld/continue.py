while True:
    s = raw_input("Enter something : ")
    x = len(s)
    if s == 'quit':
        break
    elif x < 4:
        print "Too small"
        continue
    else:
        break
print "Input is sufficient length"
