l=[0,1,1]
N=int(input())
for i in range(3,N+1):
    l.append(l[i-1]+l[i-2])
print(l[N])