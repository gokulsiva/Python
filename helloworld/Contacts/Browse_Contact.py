import pickle


def browse_contact():
    f = None
    try:
        f = open('contacts.txt')
        i = 0
        while True:
            obj = pickle.load(f)
            if obj:
                i += 1
                print '{0: ^6}'.format(i),
                print '{0: ^20}'.format(obj[0]),
                print '{0: ^20}'.format(obj[1]),
                print '{0: ^20}'.format(obj[2])
            else:
                if i == 0:
                    print 'No contacts found'
                break
    except IOError:
        print 'No contacts found'
    except EOFError:
        print 'Loaded Contacts list'
    finally:
        if f:
            f.close()


