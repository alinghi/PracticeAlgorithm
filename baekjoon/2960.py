N,M=map(int,input().split())
l=[i for i in range(2,N+1)]
z=[]
while len(z)<M:
    P=l[0]
    z.append(P)
    l.pop(0)
    z1=[x for x in l if x%P==0]
    z2 = [x for x in l if x % P >0]
    z=z+z1
    l=z2

print(z[M-1])