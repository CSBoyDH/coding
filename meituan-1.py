
def f(x,y):
    return x%y
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,f(a,b))

while True:
    res = 0
    intp  = raw_input().split()
    N = int(intp[0])
    n = int(intp[1])
    m = int(intp[2])
    p = int(intp[3])
    gcd_dict ={}
    max_index = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            x = gcd(i,j)
            if x>max_index:
                max_index = x
            if x not in gcd_dict:
                gcd_dict[x] = 1
            else:
                gcd_dict[x] += 1

    cur = p
    count =1
    for i in range(1,max_index+1):
        if i==1:
            if i in gcd_dict:
                res = res+cur*gcd_dict[1]
        else:
            if i in gcd_dict:
                cur = (cur+153)%p
                res+=cur*gcd_dict[i]

    print(res)
# while True:
#     res = 0
#     intp  = raw_input().split()
#     N = int(intp[0])
#     n = int(intp[1])
#     m = int(intp[2])
#     p = int(intp[3])
#     l = [0]*(N+1)
#     l[1]=p
#     for i in range(2,N):
#         l[i] = (l[i-1]+153)%p
#
#     for i in range(1,n+1):
#         for j in range(1,m+1):
#             x = gcd(i,j)
#             res =res+l[x]
#     print(res)
