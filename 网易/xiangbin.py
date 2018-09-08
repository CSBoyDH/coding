s= list(map(int,input().split()))
n = s[0]
m = s[1]
a = list(map(int,input().split()))
l = []
for i in range(m):
    x = list(map(int,input().split()))
    l.append(x)
v_dict={}
v_cur = {}
v_over={}
for i in range(len(a)):
    v_dict[i+1] = a[i]
    v_cur[i+1]=0
    v_over[i+1]=0
def isfull(v_cur,v_dict):
    flag=True
    for k,v in v_dict.items():
        if v_dict[k]!=v_cur[k]:
            flag = False
            break
    return flag
def dfs(v_cur,v,x):
    if x>=1:
        if v_cur[x]+v>v_dict[x]:
            next = v_cur[x] + v - v_dict[x]
            v_cur[x] = v_dict[x]
            if x-1<1 and isfull(v_cur,v_dict)==False:
                dfs(v_cur,next,n)
            else:
                dfs(v_cur,next,x-1)
        else:
            v_cur[x]+=v
for sample in l:
    if sample[0]==2:
        x = sample[1]
        v = sample[2]
        dfs(v_cur,v,x)
        # if v_over[x+1]:
        #     v_cur[x] = v_cur[x]+v+v_over[x+1]
        # else:
        #     v_cur[x] = v_cur[x] + v
        # if v_cur[x]>v_dict[x]:
        #     v_over[x] +=v_cur[x]-v_dict[x]
        #     v_cur[x] = v_dict[x]
    if sample[0]==1:
        k = sample[1]

        print(v_cur[k])



