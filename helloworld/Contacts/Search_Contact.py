import pickle


def search_contact():
    f = None
    search = raw_input('Enter a search word : ')
    try:
        f = open('contacts.txt')
        i = 0
        while True:
            obj = pickle.load(f)
            if obj:
                if search in obj[0]:
                    i += 1
                    print '{0: ^6}'.format(i),
                    print '{0: ^20}'.format(obj[0]),
                    print '{0: ^20}'.format(obj[1]),
                    print '{0: ^20}'.format(obj[2])
            else:
                if i == 0:
                    print 'No such contacts found'
                break
    except [IOError]:
        print 'No such contacts found'
    except EOFError:
        pass
    finally:
        if f:
            f.close()


