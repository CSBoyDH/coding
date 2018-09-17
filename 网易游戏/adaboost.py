import math
M ,N,K=list(map(int,input().split()))
train_label = list(map(int,input().split()))
train_classifers_res = []
for i in range(M):
    x = list(map(int,input().split()))
    train_classifers_res.append(x)
test_classifers_res = []
for i in range(K):
    x = list(map(int,input().split()))
    test_classifers_res.append(x)
a_m = [1/M]*M
W_m_i = [1/N]*N
e_m = [0]*M

for i in range(M):

    for j in range(len(train_label)):
        if train_label[j]!= train_classifers_res[i][j]:
            Ix = 1
        else:
            Ix = 0
        x = W_m_i[j]*Ix
        e_m[i]+=x
    if e_m[i]==0:
        a_m[i] = 1
    elif e_m[i]==1:
        a_m[i]=0
    else:
        a_m[i]=(1/2)*math.log((1-e_m[i])/e_m[i])
    Z_m =0
    for j in range(len(train_label)):
       temp = W_m_i[j]*math.exp(-a_m[i]*train_label[j]*train_classifers_res[i][j])
       Z_m+=temp
    for o in range(len(W_m_i)):
        W_m_i[o] = (W_m_i[o]/Z_m)*math.exp(-a_m[i]*train_label[o]*train_classifers_res[i][o])
#print(W_m_i)
#print(sum(a_m))
for samples in test_classifers_res:
    y =0
    for  i in range(len(samples)):
        y_temp = a_m[i]*samples[i]
        y+=y_temp
    if y>=0:
        print(1)
    else:
        print(-1)