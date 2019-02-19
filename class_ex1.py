class Demo:
    def __init__(self, a, b):
        print('Demo is initialized.......')
        self.a = a
        self.b = b
    def display(self):
        print('A: ', self.a, '\n', 'B: ', self.b)
        
obj= Demo(5, 8)
obj.display()
