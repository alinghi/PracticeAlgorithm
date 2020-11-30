l=[666]
N=int(input())
i=1665
while True:
    if "666" in str(i):
        l.append(i)
    if len(l)==N:
        break
    i+=1

print(l[N-1])