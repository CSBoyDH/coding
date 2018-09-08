inx =raw_input().split()
#print inx
n = int(inx[0])
m = int(inx[1])
ins = raw_input().split()
sx = int(ins[0])-1
sy = int(ins[1])-1
#print(n,m,sx,sy)
l = []
for o in range(n):
    l.append(raw_input().split())
class a(object):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    maxhigh = 0
    def go(self,l,sx,sy):
        curhigh = int(l[sx][sy])
        if curhigh>self.maxhigh:
            self.maxhigh = curhigh
        for x,y in zip(self.dx,self.dy):
            if sx+x>=0 and sx+x<m and sy+y>=0 and sy+y<n:
                nextx ,nexty = sx+x,sy+y
                if int(l[nextx][nexty])>curhigh:
                    sx ,sy= nextx,nexty
                    self.go(l,sx,sy)
                else:
                    continue
            else:
                continue
        return self.maxhigh
b = a()
print b.go(l,sx,sy)



