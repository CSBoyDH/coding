# 小易有一个长度为n的整数序列,a_1,...,a_n。然后考虑在一个空序列b上进行n次以下操作:
# 1、将a_i放入b序列的末尾
# 2、逆置b序列
# 小易需要你计算输出操作n次之后的b序列。
# 输入描述:
# 输入包括两行,第一行包括一个整数n(2 ≤ n ≤ 2*10^5),即序列的长度。
# 第二行包括n个整数a_i(1 ≤ a_i ≤ 10^9),即序列a中的每个整数,以空格分割。
#
#
# 输出描述:
# 在一行中输出操作n次之后的b序列,以空格分割,行末无空格。
# 示例1
# 输入
# 4
# 1 2 3 4
# 输出
# 4 2 1 3
n = int(input())
array = list(map(int,input().split()))
b = []
for i in array:
    b.append(i)
    b = b[::-1]
res = ''
for i in b:
    res = res + ' '+str(i)
print(res[1:])
# 分治思想，虽然我想的比较low，但是这样编写的时候速度快，分成左右两部分，
# 考虑奇偶情况，写出规律，是一个索引递减的情况,还有需要注意的是，
# 它数是一个个落下来的，不是全部落下来之后再挑选数字再逆序的，
# 所以自己走一下流程，就可以观察到索引的变化
n = int(input())
a = map(int,input().split())
b_left = []
b_right = []

# 这一段虽然可行，但是复杂度太高，AC 60%
#for i in a:
#    b.append(i)
#    b.reverse()
#print " ".join(map(str,b))

if len(a)%2 == 0:
    b_left = [a[k] for k in range(len(a)-1,0,-2)]
    b_right = [a[k] for k in range(0,len(a),2)]
else:
    b_left = [a[k] for k in range(len(a)-1,-1,-2)]
    b_right = [a[k] for k in range(1,len(a),2)]

print(" ".join(map(str,b_left+b_right)))