##def add(a, b):
##    c=a+b
##    print("addition ", c)
##add(3, 5)
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n* fact(n-1)
print(fact(5))

