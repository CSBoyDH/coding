N = int(input())
l = []
class Interval(object):
    def __init__(self,s =0,e = 0):
        self.start = s
        self.end = e
for i in range(N):
    x = list(map(int,input().split()))
    if x[1]<x[0]:
        x[0],x[1] = x[1],x[0]
    temp = Interval(x[0],x[1])
    l.append(temp)
l.sort(key= lambda x:x.end)
intervals = []
for i in l:
    intervals.append([i.start,i.end])
ans = 1
lastE = intervals[0][1]
for i in range(1,N):
    x = intervals[i][0]
    if intervals[i][0]>=lastE:
        ans+=1
        lastE = intervals[i][1]
print(ans)