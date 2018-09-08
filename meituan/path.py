N = int(input())
l = [0]*10005
for i in range(N-1):
    s = list(map(int,input().split()))
    a = s[0]
    b  = s[1]
    l[b]=l[a]+1
depth =0
for i in range(1,N+1):
    depth = max(l[i],depth)
print(2*N-2-depth)
