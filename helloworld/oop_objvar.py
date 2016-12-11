class Robot:

    population = 0

    def __init__(self, name):
        self.name = name
        print "Initializing {}".format(self.name)
        Robot.population += 1

    def die(self):
        print "{} is being destroyed.".format(self.name)
        Robot.population -= 1
        if Robot.population == 0:
            print "{} is the last one.".format(self.name)
        else:
            print 'There are still {} robots working'.format(Robot.population)

    def say_hi(self):
        print "Greetings, my masters call me {}.".format(self.name)

    @classmethod
    def how_many(cls):
        print 'We have {} robots.'.format(cls.population)


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("R2-D3")
droid2.say_hi()
Robot.how_many()

print 'Robots are doing their work.....................'

print 'Robots finished their work let\'s destroy them.'

droid1.die()
droid2.die()
Robot.how_many()
