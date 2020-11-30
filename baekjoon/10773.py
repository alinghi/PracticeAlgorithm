N=int(input())
l=[]
for _ in range(N):
    x=int(input())
    if x:
        l.append(x)
    else:
        l.pop()
print(sum(l))
