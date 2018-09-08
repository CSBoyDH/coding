k = int(raw_input())
#print(k)
from itertools import permutations
def per(n,k):
    return len(list(permutations(range(n),k)))

all =per(5*k,5*k)
if k==1:
    print 120
else:
    print((all-(per(5,5)**k)*(per(k,k)))%1000000007)
