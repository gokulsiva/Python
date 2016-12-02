dict = {'gokul':'gsgokul305@gmail.com',
        'gokul1':'gokul1@gmail.com',
        'miaw':'miaw@gmail.com'}
print dict
print 'Gokul\'s address is',dict['gokul']
del dict['gokul1']
for key,val in dict.items():
    print key,':',val
print 'Adding gokul1'
dict['gokul1'] = 'gokul1@gmail.com'
print dict
if 'gokul' in dict:
    print 'Gokul is present'
