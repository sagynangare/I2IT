''' forward loop '''
'''
range(start, stop-1, step)
'''
##
##for i in range(0,100,2):
##    print(i)

##for i in range(10, 0, -1):
##    print(i)
'''
for i in range(1, 51):
    if (i%3==0) and (i%5==0):
        print(i, ' is divisible by both 3&5')
    elif i%3==0:
        print(i, ' is divisible by 3')
    elif i%5==0:
        print(i, ' is divisible by 5')
    else:
        print('num is: ', i)


py2:                |py3
str: raw_input(msg) |str => input(msg)
int;= input(msg)    |int=> int(input(msg))
'''

total=0
count=0
while True:
    num= input(' Enter num or done to break')
    if num=='done':
        break
    else:
        total = total+int(num)
        count+=1
print('AVerage is ', total/count)


















        
    
        















