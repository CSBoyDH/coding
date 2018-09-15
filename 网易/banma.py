s = input()
#s = 'wbwbbbbbwbwbwb'
def getlength(s):
    if len(s)<2:
        return len(s)
    length = 1
    maxlength =0
    maxstart=0
    maxend = 0
    start = 0
    end =1
    while start<len(s) and end<len(s):
        if s[end]!=s[start]:
            length+=1
            maxlength = max(length,maxlength)
            maxstart=end-maxlength+1
            maxend = end
            start+=1
            end+=1
        else:
            length=1
            start=end
            end = start+1

    return maxlength,maxstart,maxend
maxlength ,maxstart,maxend=getlength(s)
left = s[:maxstart]
mid = s[maxstart:maxend+1]
right = s[maxend+1:]
left =left[::-1]
mid = mid[::-1]
right = right[::-1]
temp1 = left+mid
temp2 = mid+right
x1 = getlength(temp1)[0]
x2 = getlength(temp2)[0]
maxlength = max(x1,x2,maxlength)
print(maxlength)

