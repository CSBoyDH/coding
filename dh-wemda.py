class Solution(object):
    def f(self,string,n):
        l = []
        for i in range(0,len(string)):
            if len(set(string[i:i+n]))==1 and i+n<=len(string):
                if i>0 and i+n<len(string):
                    if string[i-1]!=string[i] and string[i+n]!=string[i]:
                        l.append((i+1,i+n,string[i:i+n]))
                elif i==0 and i+n<len(string):
                    if string[i+n]!=string[i]:
                        l.append((i+1,i+n,string[i:i+n]))
                elif i>0 and i+n==len(string):
                    if string[i-1]!=string[i]:
                        l.append((i+1,i+n,string[i:i+n]))
                else:
                    l.append((i + 1, i + n, string[i:i + n]))

        return l
a =Solution()
print(a.f('abbssgggeeeeffcc',2))
