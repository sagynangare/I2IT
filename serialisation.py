import pickle
f=open('serial.txt','rb')
d={'a':12, 'b':90, 'c':67}
#pickle.dump(d, f)
#f.close()
sd=pickle.load(f)
print(sd)
s=pickle.dumps(d)
print(s)
p=pickle.loads(s)
print(p)
