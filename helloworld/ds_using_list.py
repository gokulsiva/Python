shopList = ['apple', 'mango', 'banana']
print 'I have to purchase {} items in shopping complex.'.format(len(shopList))
print 'The items are : '
for item in shopList:
    print item
print 'I missed rice in that list. Adding rice.'
shopList.append('rice')
print 'Now the list is : '
for item in shopList:
    print item
print 'Now I\'am sorting the list.'
shopList.sort()
print 'Now the list is : '
for item in shopList:
    print item
print 'I\'ve purchased {}.Now the list becomes '.format(shopList[0])
del shopList[0]
for item in shopList:
    print item

