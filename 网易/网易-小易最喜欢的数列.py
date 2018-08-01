# 小易非常喜欢拥有以下性质的数列:
# 1、数列的长度为n
# 2、数列中的每个数都在1到k之间(包括1和k)
# 3、对于位置相邻的两个数A和B(A在B前),都满足(A <= B)或(A mod B != 0)(满足其一即可)
# 例如,当n = 4, k = 7
# 那么{1,7,7,2},它的长度是4,所有数字也在1到7范围内,并且满足第三条性质,所以小易是喜欢这个数列的
# 但是小易不喜欢{4,4,4,2}这个数列。小易给出n和k,希望你能帮他求出有多少个是他会喜欢的数列。
# 输入描述:
# 输入包括两个整数n和k(1 ≤ n ≤ 10, 1 ≤ k ≤ 10^5)
#
#
# 输出描述:
# 输出一个整数,即满足要求的数列个数,因为答案可能很大,输出对1,000,000,007取模的结果。
#
# 输入例子1:
# 2 2
#
# 输出例子1:
# 3
s = list(map(int,input().split()))
n = s[0]
k = s[1]
num = 1000000007
dp = [[0 for i in range(k+1)] for j in range(n+1)]
#print(dp)
dp[0][1] = 1
for i in range(1,n+1):
    sum =0
    for j in range(1,k+1):
        sum +=dp[i-1][j]
        sum %=num
    for x in range(1,k+1):
        sum2 = 0
        for y in range(x+x,k+1,x):
            sum2 +=dp[i-1][y]
            sum2%=num
        dp[i][x] = (sum-sum2+num)%num
result = 0
for i in range(1,k+1):
    result+=dp[n][i]
    result%=num
print(result)
