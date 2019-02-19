'''p=[]
s=[10]
s1=[10, 7.7 ,'python']
#print(s1[2])
#print(s1[2][::-1])#'nohtyp'
s1[1]="Hello"
#print(s1)
L=[1,2,3]
#print(L*3)
L.append(4)
#print(L)
#L.append('Python')
L.extend('Python')
#print(L)
t=(10,)
t1=10,
#print(type(t1))
t2=(10, [10,20], 'Python')
t2[1].append(30)
print(t2)
'''
s='Python programming world and welcome'
s1=s.split()
#print(s1)
s1[-2]='&'
#print(s1)
s2= ' '.join(s1)
#print(s2)

s1='hahahahahahahahahahahhhhhaaaaaaPython'
a=s1.lstrip('ha')
#print(a)
s2='Python wawawawawawawawawahawaha'
b=s2.rstrip('wah')
#print(b)
s3='############ Welcome to Python wawawawawa@'
#print(s3.strip('#wah@'))
s4='welcOme TO pyTHON'
#print(s4.istitle())
#print(s4.title())

#s='abc@der#ghi^zde!'
#s1='welcome to python world'

#Empty set
s=set()
s1={10, 'Python', (10,20)}
s2='programmingworld'
s3=set(s2)#{'i', 'l', 'n', 'a', 'o', 'd', 'p', 'g', 'r',
#    'm', 'w'}
#print(s3)
s4=set('programisdifficult')
#print(s4)
#{'c', 'r', 's', 'u', 'm', 'f', 'd', 'l', 't', 'a', 'i',
#    'p', 'o', 'g'}
##print('intersection: ', s3&s4)
##print('Union: ', s3|s4)
##print('difference: ', s3-s4)
##print('symmetric difference: ', s3^s4)
##
##s3.update(s4)
##print('New s3: ', s3)
##
##s5=frozenset({12,23,23,34,54,34})

#Dictionary:
# d={key:value}
#Empty dict

#update
###d[key]=value
##d[1]=10
##print(d)

d={}
for i in range(1,21):
    d[i]=i*i
#print(d)
#keys()


d={'a': 10, 'b':20, 'c':30}
#print(d.keys())
#print(d.values())
#print(d.items())
#print(d.get(101, 'Key is Not present'))
##print(d)
##print(d.setdefault('d'))
##print(d)

d1={'a':45, 'd':33, 'e':78}
d.update(d1)
###print(d)
##print(d['a'])
d={'id':[], 'name':[], 'age':[]}
for j in range(3):
    for i in d:#i ='id', 'name', 'age'
        print(i)
        if i=='id' or i=='age':
            d[i].append(int(input('Enter '+i)))
        else:
            d[i].append(input('Enter '+i))
print(d)



























































































































































s



















