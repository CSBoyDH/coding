s = int(input())
for i in range(s):
    t = list(map(int,input().split()))
    n = t[0]
    k = t[1]
    y = k
    no=n-k
    start = 1
    if no==0 or y<2:
        print('0 0')
        continue
    y =y-2
    no = no-1
    pre = 1
    pre =pre+min(y,no)
    temp = '0 '+str(pre)
    print(temp)