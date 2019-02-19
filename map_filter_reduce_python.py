s1='Python'
s2="Programming"
'''
z=zip(s1, s2)
print(list(z))
z1=list(zip(s1))
print(z1)

s3=''
z2=list(zip(s3))
print(z2)


L=[10, 20,30,40]
L1=[11,12,13,14,15]
m1=list(map(lambda x,y:x+y, L,L1))
print(m1)

p=['spring', 'django', 'hibernet','hadoop']
q=list(map(len, p))
print(q)

def demo(seq):
    if seq%2==0 and seq>0:
        return seq,
    

print(list(filter(demo, range(-9, 32))))
print(list(filter(lambda x:x>0, range(-9, 32))))

print([[1 if i==j else 0 for j in range(3)] for i in range(3)])
'''

print(list(filter(lambda x: x>0 and x%2==0, range(-9, 32))))

import functools as f
print(f.reduce(lambda x,y: x+y, list('Python'), 't'))
print('Empty Iterable', f.reduce(lambda x,y:x+y, '', "Empty"))






































