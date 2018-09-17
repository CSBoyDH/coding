N,M =list(map(int,input().split()))
P = list(map(int,input().split()))

class A(object):

    res = []
    def __init__(self,N,M,P):
        self.res =[]
        self.M=M
        self.N = N
        self.P = P

    def dfs(self,P,N,M,path):
        if M == 0:
            path = sorted(path)
            if path not in self.res:
                self.res.append(path)


        elif M<0:
            return
        else:
            for i in range(len(P)):
                if M -self.P[i]>=0:

                    self.dfs(self.P,self.N,M-self.P[i],path+[i+1])
                else:
                    continue
a =A(N,M,P)
a.dfs(P,N,M,[])

#print(a.res)
print(len(a.res))

N,M =list(map(int,input().split()))
P = list(map(int,input().split()))

h=[0]*1000
h[0]=1

for i in range(N):
    for j in range(P[i],M+1):
        h[j]+=h[j-P[i]]
print(h[M])