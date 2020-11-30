import collections
N=int(input())
l=[int(input()) for _ in range(N)]
print(round(sum(l)/len(l)))
l.sort()
print(l[len(l)//2])
d={}
for i in l:
    d[i]=0
for i in l:
    d[i]=d[i]+1
z=sorted(d.items(),key=lambda x:(-x[1],x[0]))
if len(z)>1:
    if z[0][1]==z[1][1]:
        print(z[1][0])
    else:
        print(z[0][0])
else:
    print(z[0][0])
print(l[-1]-l[0])