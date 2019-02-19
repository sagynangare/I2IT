"""
int add(int a, int b){
    c=a+b;
    printf('Addition: ',c);
    }
add(3,5);
"""
def add(a,b):
    c=a+b
    print('Addition is ', c)
#add(3,5)

#recursive
##5!=5*4*3*2*1
##n!=n*(n-1)*(n-2)*1
'''
n=1 =>1
n=2 =>2*1
n=3
f(n)=> n*f(n-1)
5*fact(4)=>
    4*fact(3)=>
        3*fact(2)=>
            2*fact(1)=>
                1
'''

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))
    














