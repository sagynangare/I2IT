class ClgMember:
    def __init__(self, Id, name, age):
        self.Id=Id
        self.name=name
        self.age=age
    def display(self):
        print('ID: ', self.Id,'\n', 'Name: ',
              self.name, 'Age: ', self.age)
class Teacher(ClgMember):
    def __init__(self, Id, name, age, salary):
        ClgMember.__init__(self, Id, name, age)
        self.salary=salary
    def display(self):
        ClgMember.display(self)
        print('\n', 'Salary: ', self.salary)
class Student(ClgMember):
    def __init__(self, Id, name, age, Marks):
        ClgMember.__init__(self, Id, name, age)
        self.Marks=Marks
    def display(self):
        ClgMember.display(self)
        print('\n', 'Marks: ', self.Marks)
st=Student(12, 'Prasad', 20, 89)
st.display()
t=Teacher(1, 'Python', 25, 50000)
t.display()











    
        
