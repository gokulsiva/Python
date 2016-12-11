import Add_Contact
import Browse_Contact
import Delete_Contact
import Modify_Contact
import Search_Contact

print 'Welcome to contact manager.\nPlease choose a option'
while True:
    print '1.Add Contact\n2.Browse all Contacts\n3.Search a Contact\n4.Modify a Contact\n5.Delete a Contact\nOther keys to exit'    
    choice = raw_input('Enter your choice : ')
    if choice == '1':
        Add_Contact.add_contact()
    elif choice == '2':
        Browse_Contact.browse_contact()
    elif choice == '3':
        Search_Contact.search_contact()
    elif choice == '4':
        Modify_Contact.modify_contact()
    elif choice == '5':
        Delete_Contact.delete_contact()
    else:
        print 'Thank you Bye.'
        break
