def reverseList(phead):
    if phead==None:
        return None
    head = phead
    phead = phead.next
    head.next = None
    while phead!=None:
        next = phead.next
        phead.next = head
        head = phead
        phead = next
    return head
def qsort(numList,low,high):
    if low<high:
        i,j = low,high
        base = numList[i]
        while i<j:
            while i<j and numList[j]>=base:
                j=j-1
            numList[i] = numList[j]
            while i<j and numList[i]<=base:
                i+=1
            numList[j] = numList[i]
        numList[i] = base
        qsort(numList,low,i-1)
        qsort(numList,j+1,high)
    return numList
def bubble(numlist):
    for i in range(0,len(numlist)):
        for j in range(i+1,len(numlist)):
            if numlist[i]>numlist[j]:
                numlist[i],numlist[j] = numlist[j],numlist[i]
    return numlist
def merge(left,right):
    result = []
    i,j = 0,0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+= left[i:]
    result+=right[j:]
    return result
def merge_sort(numList):
    if len(numList)<=1:
        return numList
    mid = len(numList)//2
    left = merge_sort(numList[:mid])
    right= merge_sort(numList[mid:])
    return merge(left,right)