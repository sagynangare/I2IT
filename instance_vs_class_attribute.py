class Demo:
    name="Python"
    def __init__(self, name):
        self.name= name
    def display(self):
        print('Name: ', self.name)
d=Demo('DON')
#print(d.name)
#print(Demo.name)

class Foo:
    name='Python'
    def __init__(self, a, b):
        self.a = a
        self.b = b
f=Foo(12,21)
print('Class variable')
print('obj: ', f.name)
print('class: ', Foo.name)
print('\n\n Instance variables')
print('obj: ', f.a, f.b)
print('class: ', Foo.a, Foo.b)
f1=Foo(1,2)














