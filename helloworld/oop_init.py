class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print 'Hello, {}'.format(self.name)

Person('Gokul').say_hi()
