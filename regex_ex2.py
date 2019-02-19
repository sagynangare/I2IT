import re
result = re.match(r'DA', 'DA Data Analytics DA')
result=re.findall(r'\b','DA is largest Analytics community of India')
print (". is : ", result)
'''
print(result.group())
print(help(result))

result = re.match(r'DA', 'DA Data Analytics DA')
print (result.start())
print (result.end())


#Search
result = re.search(r'Analytics', 'DA Data Analytics Data Analytics DA')
print (result.group())
print (result.start())
print (result.end())
print (result.span())


#Findall
result = re.findall(r'Analytics', 'DA Data Analytics Data Analytics DA')
print (result)

#Splits
result=re.split(r'y','Analytics')
print(result)

#Sub
result=re.sub(r'India','the World','DA is largest Analytics community of India India')
print(result)

#compile
pattern=re.compile('DA')
result=pattern.findall('DA Data Analytics DA')
print (result)
result2=pattern.findall('DA is largest analytics community of India')
print (result2)


#Return the first word of a given string
result=re.findall(r'.','DA is largest Analytics community of India')
print (". is : ", result)

result=re.findall(r'\w*','DA is largest Analytics community of India')
print (result)


#Extract each word (using “^“)
result=re.findall(r'^\w+','DA is largest Analytics community of India')
print ("The result of ^\w+ is ", result)


result=re.findall(r'\w+$','DA is largest Analytics community of India')
print (result)


#Return the first two character of each word
result=re.findall(r'\w\w','DA is largest Analytics community of India')
print ('Result of "\w\w"',result)
result=re.findall(r'\b\w.','DA is largest Analytics community of India')
print (result)
'''


#Return the domain type of given email-ids
result=re.findall(r'@\w+','abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz') 
print ("Domain name is ",result)
result=re.findall(r'@\w+.\w+','abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
print (result)
"""
#Extract only domain name using “( )”
result=re.findall(r'@\w+.(\w+)','abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
print (result)

#Return date from given string
result=re.findall(r'\d{2}-\d{2}-\d{4}','Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
print (result)

result=re.findall(r'\d{2}-\d{2}-(\d{4})','Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
print (result)

#Return all words of a string those starts with vowel
result=re.findall(r'\w+','DA is largest Analytics community of India')
print (result)
result=re.findall(r'[aeiouAEIOU]\w+','DA is largest Analytics community of India')
print (result)
result=re.findall(r'\b[aeiouAEIOU]\w+','DA is largest Analytics community of India')
print (result)

result=re.findall(r'\b[^aeiouAEIOU]\w+','DA is largest Analytics community of India')
print (result)

items = re.findall("[0-9]+", "Customer number: 232454, Date: February 12, 2011")
items1 = re.findall("([0-9]+).*: (.*)", "Customer number: 232454, Date: February 12, 2011")
print(items1, items[0])


#Validate a phone number (phone number must be of 10 digits and starts with 8 or 9)
li=['9999999999','999999-999','99999x9999']
for val in li:
 if re.match(r'[7-9]{1}[0-9]{9}',val) and len(val) == 10:
     print ('yes')
 else:
     print ('no')
#Split a string with multiple delimiters
line = 'asdf fjdk;afed,fjek,asdf,foo' # String has multiple delimiters (";",","," ").
result= re.split(r'[;,\s]', line)
print (result)
"""
