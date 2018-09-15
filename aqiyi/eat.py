N,M,P = list(map(int,input().split()))
ai = list(map(int,input().split()))
ops = []
for i in range(M):
    x,y = list(map(str,input().split()))
    y = int(y)
    ops.append([x,y])
for op in ops:
    if op[0]=='A':
        x= op[1]
        ai[x-1]+=1
    if op[0]=='B':
        x = op[1]
        ai[x -1] -= 1
target = ai[P-1]
temp = sorted(ai)[::-1]
for i in range(len(temp)):
    if target==temp[i] :
        print(i+1)
        break