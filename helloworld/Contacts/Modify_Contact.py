import pickle


def modify_contact():
    search_name = raw_input('Enter the contact name to modify : ')
    f = None
    array = []
    try:
        f = open('contacts.txt')
        i = 0
        while True:
            obj = pickle.load(f)
            if obj:
                i += 1
                if obj[0] == search_name:
                    print "Leave a field blank by pressing enter to retain old value"
                    name = raw_input('New name of the contact : ')
                    if name != '':
                        obj[0] = name
                    email = raw_input('New email of the contact : ')
                    if email != '':
                        obj[1] = email
                    phone = raw_input('New phone number of the contact : ')
                    if phone != '':
                        obj[2] = phone
                    array.append(obj)
                    print 'Contact modified Successfully'
                else:
                    array.append(obj)
            else:
                if i == 0:
                    print 'No contacts found'
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

