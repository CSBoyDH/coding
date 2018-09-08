
n = int(raw_input())
for i in range(n):
    x = (raw_input())
    length = len(x)
    count = 0
    for j in range(1,length):
        count = count+ int(('9'+'0'*(j-1)))*j
    s = '1'+'0'*(length-1)
    num = int(x)-int(s)+1
    count = count+ num*length

    print(count)
