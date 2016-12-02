number = 23
running = True

while running:
    guess = int(raw_input('Please enter a integer : '))
    if guess == number:
        print 'Correct guess'
        running = False
    elif guess>number:
        print 'Enter a smaller number'
    else:
        print 'Enter a greater number'
else:
    print 'Exited from loop'
print 'Bye Bye...........'
