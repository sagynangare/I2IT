def gen(n):
    yield n
    yield n+n
    yield n*8
    
g=gen(7)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
