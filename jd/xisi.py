s = input()
t = input()


def isIsomorphic(temp, t):

    a =set(temp)
    b = set(t)
    if len(a)!=len(b) or len(temp)!=len(t):
        return False
    pos1,pos2 = [-1]*256,[-1]*256
    for i in range(len(temp)):
        if pos1[ord(temp[i])]!= pos2[ord(t[i])]:
            return False
        pos1[ord(temp[i])] = pos2[ord(t[i])]=i
    return True

def solve(s,t):
    start = 0
    end = len(t)
    count = 0
    while end<=len(s):

        temp = s[start:end]
        if isIsomorphic(temp,t):
            count+=1
        start+=1
        end+=1
    return count
print(solve(s,t))