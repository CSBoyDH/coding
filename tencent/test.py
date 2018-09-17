import re
reg=re.compile("(?=aba)")
length=len(reg.findall(s))
print(length)