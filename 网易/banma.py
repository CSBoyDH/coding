#s = input()
s = 'wbwbbbbbwbwbwb'
def getlength(s):
    if len(s)<2:
        return len(s)
    length = 1
    maxlength =0
    start = 0
    end =1
    while start<len(s) and end<len(s):
        if s[end]!=s[start]:
            length+=1
            maxlength = max(length,maxlength)
            start+=1
            end+=1
        else:
            length=1
            start=end
            end = start+1

    return maxlength
print(getlength(s))
for i in range(1,len(s)-1):
    left = s[:i]
    


