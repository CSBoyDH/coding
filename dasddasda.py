# coding=utf-8
import sys

for line in sys.stdin:
    a = line.split()
    s = []
    s0 = ""
    s1 = 0
    for i in range(1,int(a[0]) + 1):
        s0+=str(i)
    s.append(s0)
    for i in range(int(a[0]) + 1, int(a[1]) + 1):
        s0 += str(i)
        s.append(s0)
    for i in s:
        if int(i) % 3 == 0:
            s1 =s1+1

    print(s1)