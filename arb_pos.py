def foo(*a):
    for i in a:
        print(i)
#foo(*(12, 23,32))
def demo(**kwagrs):
    for k, v in kwagrs.items():
        print(k, v)
d={'a':10, 'b':20, 'c':34}


#demo(**d)

d3={'a': 10, 'b': 20, 'c': 34, 1: 56}
print(d3)
it=iter(d3)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))





















