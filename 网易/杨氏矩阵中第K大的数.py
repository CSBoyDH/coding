# 杨氏矩阵行列均递增
def getorder(matrix,mid):
    #从右上角搜索，得到mid是矩阵中第几大的元素
    row = 0
    col = len(matrix[0])-1
    order = 0
    while row<len(matrix) and col>=0:
        if matrix[row][col]<mid:
            order=order+col+1
            row+=1
        else:
            col-=1
    return order
def findKthNum(matrix,k):
    if matrix==None or k<0 or k>len(matrix)*len(matrix[0]):
        return False
    low = matrix[0][0]
    high = matrix[len(matrix)-1][len(matrix[0])-1]
    mid = 0
    order=0
    while True:
        mid = (low+high)//2 #mid不一定在矩阵中
        order = getorder(matrix,mid)
        if order<k:
            low = mid+1
        elif order>k:
            high = mid-1
        else:
            break
    #此时得到mid为矩阵中第order+1名
    row = 0
    col = len(matrix[0])-1
    ret = mid
    while row<len(matrix) and col>=0:
        if matrix[row][col]<mid:#找出比mid小的最大数
            if matrix[row][col]>ret:
                ret = matrix[row][col]
            row+=1
        else:
            col-=1
    return ret

matrix= [[1,3,5],[2,4,8],[6,9,10]]
k = 6
kmax = len(matrix)*len(matrix[0])-k+1
print(findKthNum(matrix,kmax))