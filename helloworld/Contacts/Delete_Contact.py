import pickle

boo = True


def delete_contact():
    search_name = raw_input('Enter the contact name to delete : ')
    f = None
    array = []
    try:
        f = open('contacts.txt')
        while True:
            obj = pickle.load(f)
            if obj:
                if obj[0] == search_name:
                    global boo
                    boo = False
                    print 'Contact deleted Successfully'
                else:
                    array.append(obj)
            else:
                break
    except IOError:
        print 'No contacts found'
    except EOFError:
        pass
    finally:
        if f:
            f.close()
        if len(array) > 0:
            with open('contacts.txt', 'w') as fi:
                for i in array:
                    pickle.dump(i, fi)

    if boo:
        print 'No such contacts found'

