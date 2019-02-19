class Demo:
    def __init__(self, a, b):
        print('Class Demo is initialised.')
        self.a=a
        self.b=b
    def display(self):
        print(self.a, self.b)
obj= Demo(2,5)

obj.display()
