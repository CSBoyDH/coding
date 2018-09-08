#!/usr/bin/env python  
# coding=utf-8


string = list(map(int,input().split()))


N =string[0]
K = string[1]


a = []
s = input()


if s != "":
    for x in s.split():
        a.append(int(x))

pos0=[]
pos1=[]
for i in range(N):
    if a[i]==0:
        pos0.append(i)
    else:
        pos1.append(i)


maxl=0
for index in range(len(pos0)):
    start=pos0[index]
    if index+K-1>=len(pos0):
        end=pos0[-1]
    else:
        end=pos0[index+K-1]

    l=end-start+1

    for j in range(start-1,-1,-1):
        if a[j]==1:
            l+=1
        else:
            break
    for j in range(end+1,N):
        if a[j]==1:
            l+=1
        else:
            break
    maxl=max(l,maxl)

print(maxl)