import sys
s = list(map(int,input().split()))
x = s[0]
y = s[1]
z = s[2]
t = sum(s)
a = min(x,y,z)
c = max(x,y,z)
b = t-a-c
count = 0
for i in range(1, a+1):
    for j in range(1, b+1):
        r = i+j-1
        l = max(i,j)-min(i,j)+1
        if (c >= l and c <= r):
            count = (count+c-l+1)%1000000007
        elif (c > r):
            count = (count+r-l+1)%1000000007
print(count)