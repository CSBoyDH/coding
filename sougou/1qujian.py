N = int(input())
l = []
for i in range(N):
    x = int(input())
    l.append(x)
#l = [1,1,3,4,6,6,5,1,3,3]

different = set(l)
different_length = len(different)
start = 0
temp_diff = different_length
end = temp_diff
min_length = 0xffffff
res = []
count =0
while res==[] :
    temp = l[start:end]
    if len(set(temp)) ==different_length:
        res.append([start+1,end])
        min_length = end-start
        break
    start+=1
    end+=1
    if end==len(l)+2:
        start=0
        temp_diff+=1
        end = temp_diff

start = res[0][0]-1
end = res[0][1]
out = []
while end<len(l):
    temp = l[start:end]
    if len(set(temp))==different_length:
         out.append([start+1,end])
    start+=1
    end+=1
print(str(min_length)+' '+str(len(out)))

s = ''
for i in out:

    s = s+'['+str(i[0])+','+str(i[1])+']'
    s = s+' '
print(s[:-1])
# for i in range(len(l)):
#     for j in range(len(l)+1):
#         if j>i:
#             temp = l[i:j]
#             if len(set(temp))==different_length:
#                 res.append([i+1,j])
#                 min_length = min(min_length,j-i)
#
# x = []
# for o in res:
#     if o[1]-o[0]+1==min_length:
#         x.append(o)
# print(str(min_length)+' '+str(len(x)))
# s = ''
# for i in x:
#
#     s = s+'['+str(i[0])+','+str(i[1])+']'
#     s = s+' '
# print(s[:-1])


# while end<len(l):
#     if len(set(l[start:end]))==different_length:
#         res.append([True_start+1,end])
#     True_start+=1
#     end+=1
# print(str(min_length)+' '+str(len(res)))
# s = ''
# for i in res:
#
#     s = s+'['+str(i[0])+','+str(i[1])+']'
#     s = s+' '
# print(s[:-1])



