class SchoolMember:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print "Initializing SchoolMember :",self.name

    def tell(self):
        print "Name : '{}' \nAge : '{}'".format(self.name, self.age)


class Teacher(SchoolMember):

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print "Initialized Teacher :", self.name

    def tell(self):
        SchoolMember.tell(self)
        print "Salary :", self.salary


class Student(SchoolMember):

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print "Initialized Student :",self.name

    def tell(self):
        SchoolMember.tell(self)
        print "Marks :", self.marks


t = Teacher("Ramesh", 35, 30000)
s = Student("Gokul", 21, 1082)

lst = [t, s]

for i in lst:
    i.tell()


