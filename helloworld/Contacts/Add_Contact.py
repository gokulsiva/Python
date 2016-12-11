import pickle
import os


def add_contact():
    f = None
    try:
        if os.path.exists('contacts.txt'):
            f = open('contacts.txt', 'a')
        else:
            f = open('contacts.txt', 'w')
        name = raw_input('Enter contact name : ')
        email = raw_input('Enter email id : ')
        phone = raw_input('Enter phone no : ')
        p = [name, email, phone]
        pickle.dump(p, f)
        print name, 'is successfully added to contacts.'
    except [IOError, EOFError]:
        print 'Error in opening file'
    finally:
        if f:
            f.close()

