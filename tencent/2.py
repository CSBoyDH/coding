S=list(map(int,input().split()))
x = S[0]
y = S[1]

lun=0
import math
t=1
s=0
lun = (-1+math.sqrt(1+8*(x+y)))/2
# print(c)
# count =0
# if c>=x:
#     print(1)
# else:
#     while x>=0:

nx=x
ny=y
count=0
i = lun
while i>0:
    if i<=nx:
        nx-=i
        count+=1
    else:
        ny-=i
    i-=1
if nx==0 and ny==0:
    print(count)
else:
    print(-1)

# rx=x
# ry=y
# count=0
# for i in range(lun,0,-1):
#     if i<=rx:
#         rx-=i
#         count+=1
#     else:
#         ry-=i
#
# if rx==0 and ry==0:
#     print(count)
# else:
#     print(-1)