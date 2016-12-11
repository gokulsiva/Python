try:
    text = raw_input('Enter something : ')
except EOFError:
    print 'Why did you do a EOF to me ?'
except KeyboardInterrupt:
    print 'Why did you cancelled me ?'
else:
    print 'you entered', text
