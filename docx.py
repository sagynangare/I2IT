"""
'ab*'=>'a','ab','abb'
'ab+'=>'ab', 'abbbbb'
'a{3,5}b'
'[0-5][0-9]'=>00,59
'python\\nexe'

'A|B'
'([A-Z][a-z]+){2}'
'\A'
'\Z'
'\d'='[0-9]'
'\w'=>'[A-Za-z0-9_]'
'\b'=>''
"""







import re
#re.compile(pattern)
com=re.compile(r'cats')
#re.match(pattern, string, flags=0)
s='cats are smarter than dogs'
m=re.match(r'cats', s, re.I)
#print(m)
#print(m.group())
m1=com.match(s)
#print(m1.group())


#re.search(pattern, string, flags=0)
sr=re.search(r'dogs', s)
#print(sr)
#print(sr.group())
st='aaabccsssaaaaeeeiouooottouioiuuio'
f=re.findall(r'[aeiou]+', st)
#print(f)
f1=re.finditer(r'[aeiou]+', st)
#print(next(f1))
#re.split(pattern, string, maxsplit=0, flags=0)
t='abc!def#ghi@stu=gds xyz'
sp=re.split(r'[!@#=\s]', t)
#print(sp)
#re.sub(pattern, repl, string, count=0)
a='string is important so focus'
d=re.sub(r's', '#', a)
#print(d)
#re.subn(pattern, repl, string, count=0)
#(new string, count)
d1=re.subn(r's', '#', a)
#print(d1)

s='''
    Name: Python Language
    Contact num: 999 888 7777
'''












