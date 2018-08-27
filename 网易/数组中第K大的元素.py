def sort(nums,low,high):
    base = nums[low]
    if low<high:
        while low<high and nums[high]>=base:
            high = high-1
        nums[low] = nums[high]
        while low<high and nums[low]<=base:
            low+=1
        nums[high] = nums[low]
    nums[low] = base
    return low
def qsort_k(nums,low,high,k):
    if low>=high:
        return nums[low]
    else:
        mid  = sort(nums,low,high)
        if mid==k:
            return nums[mid]
        elif mid>k:
            return qsort_k(nums,low,mid-1,k)
        else:
            return qsort_k(nums,mid+1,high,k)

nums = [4,2,31,1]
k = 1
print(qsort_k(nums,0,3,len(nums)-k))
