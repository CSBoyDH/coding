#a = input()
a = '12A+BB4=239'
res= a.split('=')[1]
preequal = a.split('=')[0]
print(res)
first=''
second=''
signal = True
if '+' in preequal:
    first,second =preequal.split('+')[0] ,preequal.split('+')[1]
    signal = True
if '-' in preequal:
    first, second = preequal.split('-')[0], preequal.split('-')[1]
    signal = False
print(first,second,res)
alphanum=[]
for i in first+second+res:
    if i.isalpha() and i not in alphanum:
        alphanum.append(i)
alphanum = sorted(alphanum)
def findalpha(string):
    alpha_dict={}
    for i in range(0,len(string)):
        if string[i].isalpha() and string[i] not in alpha_dict:
            alpha_dict[string[i]]=[i]
        elif string[i].isalpha() and string[i]  in alpha_dict:
            alpha_dict[string[i]].append(i)
    return alpha_dict
first_dict = findalpha(first)
second_dict = findalpha(second)
res_dict = findalpha(res)
print(first_dict,second_dict,res_dict)

def f(first,second,res,alphanum,first_dict,second_dict,res_dict):
    for i in range(0,10):
        if alphanum[0] in first_dict:
            first_indexs=first_dict[alphanum[0]]
            for first_index in first_indexs:
                first = first.replace(first[first_index], str(i))
        if alphanum[0] in second_dict:
            second_indexs = second_dict[alphanum[0]]
            for second_index in second_indexs:
                second = second.replace(second[second_index], str(i))
        if alphanum[0] in res_dict:
            res_indexs = res_dict[alphanum[0]]
            for res_index in res_indexs:
                res = res.replace(second[res_index], str(i))

        if first.isdigit() and second.isdigit() and res.isdigit():
            if signal==True:
                if int(first)+int(second)==int(res):
                    return first,second,res
        elif len(alphanum[1:])!=0:
            f(first, second, res, alphanum[1:],first_dict,second_dict,res_dict)
    return
print(f(first,second,res,alphanum,first_dict,second_dict,res_dict))

