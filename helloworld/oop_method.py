class Person:
    def say_hi(self):
        print 'Hello, How are you ?'

p = Person()
p.say_hi()
# Both are same
Person().say_hi()
