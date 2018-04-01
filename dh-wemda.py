class Solution(object):
    def f(self,string,n):
        l = []
        for i in range(0,len(string)):
            if len(set(string[i:i+n]))==1:
                l.append((i+1,i+n,string[i:i+n]))
        return l
a =Solution()
print(a.f('abbcccddeefffgggcc',2))
