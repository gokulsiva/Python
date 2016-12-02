def func(a,b=10,c=15):
    print 'a is {} b is {} and c is {}'.format(a,b,c)

func(25)
func(a=35)
func(c=50,a=35)
func(25,c=32,b=78)

