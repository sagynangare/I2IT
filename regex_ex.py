import re
ex_str="Jessica is 15 years old, and Daniel is 27 years old.\
    Edward is 97 years old, and his grandfather, Oscar, is 102."
age = re.findall(r'\d[0-9]*',ex_str)
name = re.findall(r'[A-Z][a-z]*',ex_str)


#print(dir(re))
print("Ages are: ", age)
print("Names: ",name)

regex = re.compile(r"(\w+) World")
result = regex.search("Hello World is the easiest")
if result:
    print(result.start(), result.end())
for result in regex.findall("Hello World, Python World"):
    print(result)

print(regex.sub(r"\1 Earth", "Hello World"))

s="rabcdeefgyYhFjkloomnpOeorteeeeet"
#s="aaaarrtuieieieifgjfkeiiwiiaajieooeeaeiouaeiouaeioumckcmo"
p=re.compile(r'[aeiouAEIOU]+')
m=p.finditer(s)
for i in m:
    print(i.group(0))
