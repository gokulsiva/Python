number = 23
guess = int(raw_input('Enter an integer : '))
if number == guess:
    print 'Guess is correct'
elif guess < number:
    print 'A little greater number'
else:
    print 'A lower number'

