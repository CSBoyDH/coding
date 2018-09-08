#s = input()
n = int(input())
l = []
for g  in range(n):
    l.append(input().split())
s = 'uuurrdddddl'
for i in range(0,len(l)):
    count = 0
    N = int(l[i][0])
    M = int(l[i][1])
    x = int(l[i][2])
    y = int(l[i][3])
    for j in s:
        if j == 'u':
            if x>1:
                count+=1
                x = x-1
            else:
                count+=1
                break
        if j == 'd':
            if x<N:
                count+=1
                x = x+1
            else:
                count += 1
                break
        if j == 'r':
            if y<M:
                count+=1
                y = y+1
            else:
                count += 1
                break
        if j == 'l':
            if y  > 1:
                count += 1
                y = y - 1
            else:
                count += 1
                break
    print(count)

