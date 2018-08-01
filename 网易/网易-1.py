n = int(input())
l = []
for i in range(n):
    l.append(input().split()[1:])
#print(l)
num_dict={}
for j in range(0,len(l)):
    a = set()
    for k in range(0,len(l)):
        if l[j][1]==l[k][1]:
            if l[j][0]!=l[k][0]:

                if l[j][0] not in num_dict:
                    a.add(l[k][1])
                    num_dict[l[j][0]]=len(a)
                else:
                    if l[k][1] not in a:
                        a.add(l[k][1])
                        num_dict[l[j][0]]=len(a)
res = []
for k,v in num_dict.items():
    res.append([k,v])
res.sort(key=lambda x:x[0])
for m in res:
    print(m[0],m[1])
