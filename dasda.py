one = input()
one = one.split()
N = int(one[0])
M = int(one[1])
tasks = []
for i in range(N):
    task = input()
    task = task.split()
    tasks.append(task)

power = input()
power = power.split()

print(N,M)
print(tasks)
print(power)
for j in range(0,len(power)):
    k = int(power[j])
    maxreward = 0
    for m in range(0,len(tasks)):
        hard = int(tasks[m][0])
        reward = int(tasks[m][1])
        print(hard,reward)
        if k>=hard and reward>maxreward:
            maxreward = reward
    print(maxreward)

