# X = input()
# Y  = input()
X = 'abcd1elfl'
Y = 'bcd2e2f2'


def dp(S1, S2):
    m = len(S1)
    n = len(S2)
    if m < 0 or n < 0:
        return 0
    memo = [[0] * (n + 1) for j in range(m + 1)]
    # 初始状态 第0行 第0列 都是0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S1[i - 1] == S2[j - 1]:  # S1中的第i个字符 S2中的第j个字符
                memo[i][j] = 1 + memo[i - 1][j - 1]
            else:
                memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])
    return memo[m][n]
print(dp(X,Y))

# def lcs(a,b):
#     lena=len(a)
#     lenb=len(b)
#     c=[[0 for i in range(lenb+1)] for j in range(lena+1)]
#     flag=[[0 for i in range(lenb+1)] for j in range(lena+1)]
#     for i in range(lena):
#         for j in range(lenb):
#             if a[i]==b[j]:
#                 c[i+1][j+1]=c[i][j]+1
#                 flag[i+1][j+1]='ok'
#             elif c[i+1][j]>c[i][j+1]:
#                 c[i+1][j+1]=c[i+1][j]
#                 flag[i+1][j+1]='left'
#             else:
#                 c[i+1][j+1]=c[i][j+1]
#                 flag[i+1][j+1]='up'
#     return c,flag
# def printLcs(flag,a,i,j):
#     if i==0 or j==0:
#         return
#     if flag[i][j]=='ok':
#         printLcs(flag,a,i-1,j-1)
#
#         print(a[i-1],end='')
#     elif flag[i][j]=='left':
#         printLcs(flag,a,i,j-1)
#     else:
#         printLcs(flag,a,i-1,j)
# c,flag=lcs(X,Y)
# printLcs(flag,X,len(X),len(Y))
