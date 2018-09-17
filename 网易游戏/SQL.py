import math
N = int(input())
t1 =[]
for i in range(N):
    X = list(map(int,input().split()))
    t1.append(X)
t2 = t1.copy()
res = []
res_dict={}
for i in range(len(t1)):
    for j in range(len(t2)):
        if i!=j:
            id1 = t1[i][0]
            id2 = t2[j][0]
            if id1!=id2:
                sum2 = math.sqrt(pow(t1[i][1]-t2[j][1],2)+pow(t1[i][2]-t2[j][2],2)+pow(t1[i][3]-t2[j][3],2))

                if sum2<20:
                    if id1 not in res_dict :
                        res_dict[id1]=[id2,sum2]
                    elif res_dict[id1][0]==id2:
                        if sum2 <res_dict[id1][1]:
                            res_dict[id1] = [id2,sum2]


#print(res)

#print(res)
final = []
for k,v in res_dict.items():
    final.append([k,v[0],v[1]])

final.sort(key=lambda x:x[0])

for x in final:
    s=str(x[0])+' '+str(x[1])+' '
    print(s,end='')
    print('%.2f'%x[2])