import functools
s=input().split("-")
l=[]
for i in s:
    l.append(sum(map(int,i.split("+"))) if "+" in i else int(i))
print(functools.reduce(lambda x,y:x-y, l))