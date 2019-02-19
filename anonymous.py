'''
def <fname>(para's):
            body
            '''
'''
lambda (paras): expression
'''
#print((lambda a,b: a+b)(5, 4))
l=[]
for i in range(1,21):
    if i%2==0:
        l.append(i)
#print(l)
'''
[expression loop condition]
'''
p=[i for i in range(1,21) if i%2==0]
g=(i for i in range(1,21) if i%2==0)
#print(g)
#print(p)

#1)enumerate(iterable, start=0)
#op=[(index, value)]
l=list(range(11,21))
#print(list(enumerate(list(range(11,21)), 1)))
#2)zip(*iterables)
p=list(range(1,7))
q=list(range(4,8))
#print(list(zip(p, q)))
#print(list(zip('python', 'abc')))
#print(list(zip('')))

p=list(range(1,7))
q=list(range(4,8))
#map(function, iterables)
#print(list(map(lambda a, b:a+b, p,q)))
#n=int(input("enter num: "))#3
s='abc'
#print(list(map(lambda a, b: a+str(b), s, range(n))))
r=range(-10, 10)
#filter(function, iterable)
#print(list(filter(lambda s: s>0 and s%2==0, r)))

#import functools
#functools.reduce(function, iterable, intializer)
#print(functools.reduce(lambda a, b:a+b, range(1,11)))
def demo():
    L=['a', 0, 0.7, 3]
    for i in L:    
        try:
            c=1/int(i)

        except ValueError as e:
            print('Opps ', e, " occured")
        except ZeroDivisionError as e:
            print('Opps ', e, " occured")

        else:
            print("this is else block")
            print("result is: ", c)

        finally:
            print('this is finnaly block')
            return "hi"
print(demo())



































