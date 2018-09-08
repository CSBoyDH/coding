n= int(input())
l = []
for i in range(n):
    l.append(input().split())
#print(l)
for row in l:
    k = int(row[0])
    mink = []
    for x in range(k):
        mink.append([1,int(row[len(row)-x-1]),1/int(row[len(row)-x-1])])
    for leftnum in range(2,len(row)):
        for rightnum in range(len(row)-1,-1,-1):
            if int(row[leftnum])<int(row[rightnum]):
                if int(row[leftnum])/int(row[rightnum])<mink[-1][2]:
                    mink.pop()
                    mink.append([int(row[leftnum]),int(row[rightnum]),int(row[leftnum])/int(row[rightnum])])

                    mink.sort(key=lambda x:x[2])
            else:
                break
    print(mink[-1][0],mink[-1][1])
