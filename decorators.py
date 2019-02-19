def outer(a):
    def inner(b):
        return a*b
    return inner
d=outer(9)
print(d(3))
#ax^2+bx+c
def outer(x):
    def inner(a,b,c):
        return a*x**2+b*x+c
    return inner
p=outer(3)
print(p(2,-3,6))
