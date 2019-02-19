class CollegeMember:
    def __init__(self, name, age):
        self.name = name
        self.age= age
    def display(self):
        print('Name: ', self.name, ' age: ', self.age)

class Teacher(CollegeMember):
    def __init__(self, name, age, salary):
        CollegeMember.__init__(self, name, age)
        self.salary= salary
    def display(self):
        CollegeMember.display(self)
        print('Salary: ', self.salary)

class Student(CollegeMember):
    def __init__(self, name, age, marks):
        CollegeMember.__init__(self, name, age)
        self.marks= marks
    def display(self):
        CollegeMember.display(self)
        print('Marks: ', self.marks)
t=Teacher('A', 25, 500000)
t.display()#
s = Student('STD', 12, 96)
s.display()




        
