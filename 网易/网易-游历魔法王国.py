# 魔法王国一共有n个城市,编号为0~n-1号,n个城市之间的道路连接起来恰好构成一棵树。
# 小易现在在0号城市,每次行动小易会从当前所在的城市走到与其相邻的一个城市,小易最多能行动L次。
# 如果小易到达过某个城市就视为小易游历过这个城市了,小易现在要制定好的旅游计划使他能游历最多的城市,请你帮他计算一下他最多能游历过多少个城市(注意0号城市已经游历了,游历过的城市不重复计算)。
# 输入描述:
# 输入包括两行,第一行包括两个正整数n(2 ≤ n ≤ 50)和L(1 ≤ L ≤ 100),表示城市个数和小易能行动的次数。
# 第二行包括n-1个整数parent[i](0 ≤ parent[i] ≤ i), 对于每个合法的i(0 ≤ i ≤ n - 2),在(i+1)号城市和parent[i]间有一条道路连接。
#
#
# 输出描述:
# 输出一个整数,表示小易最多能游历的城市数量。
#
# 输入例子1:
# 5 2
# 0 1 2 3
#
# 输出例子1:
# 3
# 前面不知道算不算提示，城市间连接成一棵树。那么我们首先想到的是深度遍历这棵树，找到最大深度max_depth，然后与L比较。
# 如果最大深度max_depth-1>L，则可直接打印L+1，这里为什么要减1比较，后面又要加1呢。因为一开始，我们假设小易在0城市，0城市的深度为1，那么当达到最大深度时
# ，我们只用了max_depth-1步，当其大于（可以等于）L时，那么L步都可以顺着这条路径走，走L步加上原来0城市，就经历了L+1个城市。当max_depth-1小于L时，意味着我们可以用剩下的步数去走其他城市。
# 我们从输入的信息“第i个输入的城市号与编号为i+1的城市有一条相通的道路”可以知道，编号为i+1的城市都至少与前面的0到i号中的任意一个城市有一条连接。
# 对于在最大深度路径结点上分叉的路径，我们每走一个分叉路径上的结点，若要返回到原来最大深度路径上的结点，总共需要耗费2步，
# 简单来说，若假设走的分叉结点个数为 k ，我们要花费 k 步原路返回，总共花费就是 2k 了。那么我们继续选择最大深度的路径，
# 走分叉的路径需要两步，那我们将剩下步数除以2取整就可以得到我们能走的分叉城市个数了。
# 当然这里还要判断走完分叉城市个数加上最大深度路径的城市个数是否大于总城市个数，牛客上没有这个边界，顾不讨论。
n,L=map(int,input().split(' '))
parent_node=[int(x) for x in input().split(' ')]

#每个节点的最大深度列表，引索对应的是城市编号，0初始化为1
node_depth=[0]*n
node_depth[0]=1
for i in range(n-1):
    #当前城市的下一个连接城市的最大深度等于当前城市的最大深度+1
    node_depth[i+1]=node_depth[parent_node[i]]+1
#取出最大深度比较
max_depth=max(node_depth)
if max_depth-1>L:
    print(L+1)
else:
    #剩下能走的步数
    leftover_steps=L-max_depth+1
    #用剩下步数走其他城市的个数
    other_cities=int(leftover_steps/2)
    print(max_depth+other_cities)