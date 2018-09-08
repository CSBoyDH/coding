import numpy as np
num = (input().split())
sec = input().split()
x= int(sec[0])
k = int(sec[1])
abs_dict={}
l = []
for i in range(0,len(num)):
    distance = abs(int(num[i])-x)
    l.append((int(num[i]),distance))
l.sort(key=lambda x:x[2])
#print(l)
res = []
for i in range(0,k):
    res.append(l[i][0])
res =sorted(res)
string = ''
for i in range(0,len(res)):
    if i != len(res)-1:
        string = string+str(res[i])+' '
    else:
        string = string+str(res[i])
print(string)

