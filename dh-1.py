def qsort(numlist,low ,high):
    if low<high:
        i,j = low ,high
        base = numlist[i]
        while i <j:
            while i<j and numlist[j]>=base:
                j = j-1
            numlist[i] = numlist[j]
            while i<j and numlist[i]<=base:
                i = i+1
            numlist[j] = numlist[i]
        numlist[i] = base
        qsort(numlist,low,i-1)
        qsort(numlist,j+1,high)
    return numlist
def merge(left,right):
    res = []
    i,j= 0,0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            res.append(left[i])
            i +=1
        else:
            res.append(right[j])
            j+=1
    res =res+ left[i:]
    res = res + right[j:]
    return res

def merge_sort(numlist):
    if len(numlist)<=1:
        return numlist
    middle = len(numlist)//2
    left = merge_sort(numlist[:middle])
    right = merge_sort(numlist[middle:])
    return merge(left,right)
myList = [49,38,65,97,76,13,27,49]

print(merge_sort(myList))
print(qsort(myList,0,len(myList)-1))
def binsearch(numlist,target):
    low  = 0
    high  = len(numlist)-1
    while low <high:
        mid = (low+high)//2
        if numlist[mid]==target:
            return mid
        elif numlist[mid]>target:
            low= mid+1
        else:
            high = mid-1
    return -1