zoo = ('elephant','peacock','snake')
print 'Number of animals in zoo is',len(zoo)
new_zoo = ('lion','tiger',zoo)
print 'Number of cages in new zoo is',len(new_zoo)
print 'Animals in new zoo',new_zoo
print 'Animals from old zoo',zoo
print 'Total number of animals',len(new_zoo)-1+len(zoo)
