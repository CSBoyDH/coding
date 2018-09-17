k=int(input())
A = input()
B = input()

start = 0
end=start+k
import itertools

A_zichuan=[]
for x in itertools.permutations(A,k):
    if x in A:
        A_zichuan.append(x)

count = 0

import re
for zichuan in A_zichuan:
    rule1 = re.compile(r'(?='+zichuan+')')
    count+=len(rule1.findall(B))
print(count)