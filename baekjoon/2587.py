l=[]
for _ in range(5):
    l.append(int(input()))
    l.sort()
print(sum(l)//len(l))
print(l[2])